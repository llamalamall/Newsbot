"""
GitHub repository search functionality.
Searches for relevant repositories based on topics and filters.
"""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from github import Github, Auth

# Import dataclass models
try:
    from ..models import GitHubResult
except ImportError:
    # Fallback for direct execution
    import sys
    import os
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    from models import GitHubResult


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
    rejected_results: Optional[List[Dict[str, Any]]] = None
) -> List[Dict[str, Any]]:
    """Search GitHub for relevant repositories.
    
    Args:
        github_token: GitHub personal access token
        github_topics: List of topics to search for
        days_back: Number of days to look back for updates
        max_results_per_topic: Maximum results per topic
        rejected_results: Optional list to append filtered-out repositories
        
    Returns:
        List of repository dictionaries with metadata
    """
    logging.info("Searching GitHub repositories...")
    results: List[Dict[str, Any]] = []
    
    if not github_token:
        logging.warning("GITHUB_TOKEN not set, skipping GitHub search")
        return results
    
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
                    # Check if repo description contains AI/automation keywords
                    description = (repo.description or "").lower()
                    if any(kw in description for kw in AI_KEYWORDS):
                        result = GitHubResult(
                            title=repo.full_name,
                            url=repo.html_url,
                            description=repo.description or "",
                            source="github",
                            stars=repo.stargazers_count,
                            updated=repo.updated_at.isoformat(),
                            topic=topic
                        )
                        results.append(result.to_dict())
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
        
        logging.info(f"Found {len(results)} relevant GitHub repositories")
    except Exception as e:
        logging.error(f"Error initializing GitHub search: {str(e)[:100]}")
    
    return results
