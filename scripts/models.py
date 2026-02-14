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
        source: Source type identifier (e.g., 'github', 'rss')
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
        llm_applicable: Optional boolean indicating LLM applicability assessment
        llm_applicability_score: Optional float (0.0-1.0) for applicability confidence
        llm_applicability_reason: Optional explanation for applicability decision
        llm_matched_keywords: List of keywords matched by LLM assessment
        llm_credible: Optional boolean indicating LLM credibility assessment
        llm_credibility_score: Optional float (0.0-1.0) for credibility confidence
        llm_credibility_reason: Optional explanation for credibility decision
        llm_credibility_flags: List of credibility concerns identified by LLM
    """
    published: Optional[str] = None
    feed_name: Optional[str] = None
    feed_category: Optional[str] = None
    priority: str = "medium"
    keyword_matches: int = 0
    author: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    # LLM assessment fields
    llm_applicable: Optional[bool] = None
    llm_applicability_score: Optional[float] = None
    llm_applicability_reason: Optional[str] = None
    llm_matched_keywords: List[str] = field(default_factory=list)
    llm_credible: Optional[bool] = None
    llm_credibility_score: Optional[float] = None
    llm_credibility_reason: Optional[str] = None
    llm_credibility_flags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Ensure source is set to 'rss'."""
        self.source = "rss"
