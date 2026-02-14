"""
GitHub repository search functionality.
Searches for relevant repositories based on topics and filters.
"""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from github import Github, Auth


def search_github_repos(
    github_token: Optional[str],
    github_topics: List[str],
    days_back: int = 7,
    max_results_per_topic: int = 10
) -> List[Dict[str, Any]]:
    """Search GitHub for relevant repositories.
    
    Args:
        github_token: GitHub personal access token
        github_topics: List of topics to search for
        days_back: Number of days to look back for updates
        max_results_per_topic: Maximum results per topic
        
    Returns:
        List of repository dictionaries with metadata
    """
    logging.info("Searching GitHub repositories...")
    results = []
    
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
                    if any(kw in description for kw in ["ai", "llm", "ml", "machine learning", "automation", "automated", "gpt"]):
                        results.append({
                            "title": repo.full_name,
                            "url": repo.html_url,
                            "description": repo.description,
                            "stars": repo.stargazers_count,
                            "updated": repo.updated_at.isoformat(),
                            "source": "github",
                            "topic": topic
                        })
            except Exception as topic_error:
                logging.error(f"Error searching topic '{topic}': {str(topic_error)[:100]}")
                continue
        
        logging.info(f"Found {len(results)} relevant GitHub repositories")
    except Exception as e:
        logging.error(f"Error initializing GitHub search: {str(e)[:100]}")
    
    return results
