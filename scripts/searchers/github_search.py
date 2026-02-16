"""
GitHub repository search functionality.
Searches for relevant repositories based on topics and filters.
"""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Set
from github import Github, Auth

# Import dataclass models
try:
    from ..models import GitHubResult
    from ..utils.llm_assessment import (
        assess_repositories_batch,
        get_llm_call_count,
        reset_llm_call_count
    )
    from ..utils.article_cache import generate_article_id
except ImportError:
    # Fallback for direct execution
    import sys
    import os
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    from models import GitHubResult
    from utils.llm_assessment import (
        assess_repositories_batch,
        get_llm_call_count,
        reset_llm_call_count
    )
    from utils.article_cache import generate_article_id


AI_KEYWORDS = [
    "ai",
    "llm",
    "ml",
    "machine learning",
    "automation",
    "automated",
    "gpt"
]


def search_github_repos(
    github_token: Optional[str],
    github_topics: List[str],
    days_back: int = 7,
    max_results_per_topic: int = 10,
    rejected_results: Optional[List[Dict[str, Any]]] = None,
    openai_client=None,
    config: Optional[Dict[str, Any]] = None,
    keywords: Optional[List[str]] = None,
    analyzed_ids: Optional[Set[str]] = None
) -> List[Dict[str, Any]]:
    """Search GitHub for relevant repositories.
    
    Args:
        github_token: GitHub personal access token
        github_topics: List of topics to search for
        days_back: Number of days to look back for updates
        max_results_per_topic: Maximum results per topic
        rejected_results: Optional list to append filtered-out repositories
        openai_client: Optional OpenAI client for LLM assessment
        config: Optional configuration dictionary containing llm_assessment settings
        keywords: Optional list of keywords for LLM assessment
        analyzed_ids: Optional set of previously analyzed repository IDs to skip
        
    Returns:
        List of repository dictionaries with metadata
    """
    logging.info("Searching GitHub repositories...")
    results: List[Dict[str, Any]] = []
    
    if not github_token:
        logging.warning("GITHUB_TOKEN not set, skipping GitHub search")
        return results
    
    # Reset LLM call counter for this search
    reset_llm_call_count()
    
    # Get LLM assessment settings
    llm_settings = config.get('llm_assessment', {}) if config else {}
    llm_enabled = llm_settings.get('enabled', False)
    llm_model = llm_settings.get('model', 'gpt-4o')
    applicability_threshold = llm_settings.get('applicability_threshold', 0.6)
    credibility_threshold = llm_settings.get('credibility_threshold', 0.5)
    filter_inapplicable = llm_settings.get('filter_inapplicable', True)
    filter_not_credible = llm_settings.get('filter_not_credible', True)
    batch_size = llm_settings.get('batch_size', 5)
    
    if llm_enabled and openai_client and not llm_model:
        logging.error("LLM model not configured; disable LLM assessment or set llm_assessment.model")
        llm_enabled = False
    
    if llm_enabled and not openai_client:
        logging.warning("LLM assessment enabled but no OpenAI client available")
        llm_enabled = False
    
    try:
        auth = Auth.Token(github_token)
        g = Github(auth=auth)
        since_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
        
        # Search for repositories with relevant topics
        for topic in github_topics:
            try:
                query = f"topic:{topic} pushed:>={since_date}"
                repos = g.search_repositories(query=query, sort="updated", order="desc")
                
                for repo in repos[:max_results_per_topic]:
                    # Get repository topics
                    try:
                        repo_topics = repo.get_topics()
                    except Exception:
                        repo_topics = []
                    
                    # Check if repo description contains AI/automation keywords (basic filter)
                    description = (repo.description or "").lower()
                    if any(kw in description for kw in AI_KEYWORDS):
                        result_dict = GitHubResult(
                            title=repo.full_name,
                            url=repo.html_url,
                            description=repo.description or "",
                            source="github",
                            stars=repo.stargazers_count,
                            updated=repo.updated_at.isoformat(),
                            topic=topic
                        ).to_dict()
                        # Add topics for LLM assessment
                        result_dict["topics"] = repo_topics
                        results.append(result_dict)
                    elif rejected_results is not None:
                        rejected = GitHubResult(
                            title=repo.full_name,
                            url=repo.html_url,
                            description=repo.description or "",
                            source="github",
                            stars=repo.stargazers_count,
                            updated=repo.updated_at.isoformat(),
                            topic=topic
                        ).to_dict()
                        rejected["rejection_type"] = "relevance"
                        rejected["rejection_reason"] = "missing_ai_keywords"
                        rejected_results.append(rejected)
            except Exception as topic_error:
                logging.error(f"Error searching topic '{topic}': {str(topic_error)[:100]}")
                continue
        
        logging.info(f"Found {len(results)} repositories matching AI/automation keywords")
        
        # Skip repositories already analyzed (reduces unnecessary LLM calls)
        if analyzed_ids:
            filtered_results = []
            skipped_count = 0
            for repo in results:
                repo_id = generate_article_id(repo)
                if repo_id and repo_id in analyzed_ids:
                    skipped_count += 1
                    logging.debug(f"Skipping already analyzed repository: {repo.get('title', 'Untitled')}")
                else:
                    filtered_results.append(repo)
            
            if skipped_count > 0:
                logging.info(f"Skipped {skipped_count} previously analyzed repository/repositories before LLM assessment")
            results = filtered_results
        
        # Apply LLM assessment if enabled
        if llm_enabled and results and openai_client:
            num_batches = (len(results) + batch_size - 1) // batch_size
            logging.info(f"Running batch LLM assessment for {len(results)} repositories in {num_batches} batch(es) (batch_size={batch_size})...")
            
            # Batch assess repositories
            assessment_keywords = keywords if keywords else []
            assessments = assess_repositories_batch(
                openai_client=openai_client,
                repositories=results,
                keywords=assessment_keywords,
                model=llm_model,
                batch_size=batch_size
            )
            
            # Apply assessment results and filter
            filtered_results = []
            for repo, assessment in zip(results, assessments):
                # Add LLM assessment fields to repository
                repo["llm_applicable"] = assessment["applicable"]
                repo["llm_applicability_score"] = assessment["applicability_score"]
                repo["llm_applicability_reason"] = assessment["applicability_reason"]
                repo["llm_matched_keywords"] = assessment["matched_keywords"]
                repo["llm_credible"] = assessment["credible"]
                repo["llm_credibility_score"] = assessment["credibility_score"]
                repo["llm_credibility_reason"] = assessment["credibility_reason"]
                repo["llm_credibility_flags"] = assessment["flags"]
                
                # Filter based on applicability
                if filter_inapplicable and not assessment["applicable"]:
                    if assessment["applicability_score"] < applicability_threshold:
                        if rejected_results is not None:
                            repo["rejection_type"] = "applicability"
                            repo["rejection_reason"] = assessment["applicability_reason"]
                            rejected_results.append(repo)
                        continue
                
                # Filter based on credibility
                if filter_not_credible and not assessment["credible"]:
                    if assessment["credibility_score"] < credibility_threshold:
                        if rejected_results is not None:
                            repo["rejection_type"] = "credibility"
                            repo["rejection_reason"] = assessment["credibility_reason"]
                            rejected_results.append(repo)
                        continue
                
                filtered_results.append(repo)
            
            results = filtered_results
            llm_calls = get_llm_call_count()
            logging.info(f"LLM assessment complete. {len(results)} repositories passed filters. Total LLM calls: {llm_calls}")
        
        logging.info(f"Returning {len(results)} GitHub repositories")
    except Exception as e:
        logging.error(f"Error initializing GitHub search: {str(e)[:100]}")
    
    return results
