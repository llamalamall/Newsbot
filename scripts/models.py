"""
Data models for Newsbot results.
Defines dataclasses for different types of search results to improve type safety.
"""

from dataclasses import dataclass, asdict, field
from typing import Optional, List, Any, Dict


@dataclass
class SearchResult:
    """Base class for all search results.
    
    Attributes:
        title: Title of the result
        url: URL link to the source
        description: Description or summary of the content
        source: Source type identifier (e.g., 'github', 'rss', 'web_search_llm')
        credibility: Optional credibility rating ('high', 'medium', 'low')
    """
    title: str
    url: str
    description: str
    source: str
    credibility: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the dataclass to a dictionary.
        
        Returns:
            Dictionary representation of the result
        """
        return asdict(self)


@dataclass
class GitHubResult(SearchResult):
    """GitHub repository search result.
    
    Attributes:
        stars: Number of GitHub stars
        updated: Last update timestamp (ISO format string)
        topic: GitHub topic that matched the search
    """
    stars: Optional[int] = None
    updated: Optional[str] = None
    topic: Optional[str] = None
    
    def __post_init__(self):
        """Ensure source is set to 'github'."""
        self.source = "github"


@dataclass
class RSSResult(SearchResult):
    """RSS feed search result.
    
    Attributes:
        published: Publication date/time
        feed_name: Name of the RSS feed
        feed_category: Category of the feed (e.g., 'research', 'news', 'ai')
        priority: Priority level ('high', 'medium', 'low')
        keyword_matches: Number of keyword matches found
        author: Article author if available
        tags: List of tags associated with the article
    """
    published: Optional[str] = None
    feed_name: Optional[str] = None
    feed_category: Optional[str] = None
    priority: str = "medium"
    keyword_matches: int = 0
    author: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Ensure source is set to 'rss'."""
        self.source = "rss"


@dataclass
class WebSearchResult(SearchResult):
    """Web search result with LLM processing.
    
    Attributes:
        search_topic: The search topic/query used
        key_points: List of key takeaways from the content
        date: Publication date if available
        credible_sources_found: Number of credible sources found (for summaries)
    """
    search_topic: Optional[str] = None
    key_points: Optional[List[str]] = None
    date: Optional[str] = None
    credible_sources_found: Optional[int] = None
