"""
Searcher modules for NewsBot.
"""

from .github_search import search_github_repos
from .web_search import search_with_llm, perform_web_search, search_with_web_context
from .rss_search import search_rss_feeds

__all__ = [
    'search_github_repos',
    'search_with_llm',
    'perform_web_search',
    'search_with_web_context',
    'search_rss_feeds'
]
