#!/usr/bin/env python3
"""
Unit tests for Newsbot dataclass models.
Tests the dataclass models defined in models.py.
"""

import pytest
import sys
import os

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

from models import SearchResult, GitHubResult, RSSResult, WebSearchResult


class TestSearchResult:
    """Test SearchResult base dataclass."""
    
    def test_create_search_result(self):
        """Test creating a basic SearchResult."""
        result = SearchResult(
            title="Test Article",
            url="https://example.com/test",
            description="Test description",
            source="test_source"
        )
        
        assert result.title == "Test Article"
        assert result.url == "https://example.com/test"
        assert result.description == "Test description"
        assert result.source == "test_source"
        assert result.credibility is None
    
    def test_search_result_with_credibility(self):
        """Test SearchResult with credibility."""
        result = SearchResult(
            title="Test Article",
            url="https://example.com/test",
            description="Test description",
            source="test_source",
            credibility="high"
        )
        
        assert result.credibility == "high"
    
    def test_to_dict(self):
        """Test converting SearchResult to dictionary."""
        result = SearchResult(
            title="Test Article",
            url="https://example.com/test",
            description="Test description",
            source="test_source",
            credibility="medium"
        )
        
        result_dict = result.to_dict()
        
        assert isinstance(result_dict, dict)
        assert result_dict["title"] == "Test Article"
        assert result_dict["url"] == "https://example.com/test"
        assert result_dict["description"] == "Test description"
        assert result_dict["source"] == "test_source"
        assert result_dict["credibility"] == "medium"


class TestGitHubResult:
    """Test GitHubResult dataclass."""
    
    def test_create_github_result(self):
        """Test creating a GitHubResult."""
        result = GitHubResult(
            title="test/repo",
            url="https://github.com/test/repo",
            description="AI security tool",
            source="github",
            stars=100,
            updated="2024-01-01T00:00:00",
            topic="security"
        )
        
        assert result.title == "test/repo"
        assert result.url == "https://github.com/test/repo"
        assert result.description == "AI security tool"
        assert result.source == "github"
        assert result.stars == 100
        assert result.updated == "2024-01-01T00:00:00"
        assert result.topic == "security"
    
    def test_github_result_post_init(self):
        """Test that source is automatically set to 'github'."""
        result = GitHubResult(
            title="test/repo",
            url="https://github.com/test/repo",
            description="Test repo",
            source="wrong"  # Should be overridden
        )
        
        assert result.source == "github"
    
    def test_github_result_to_dict(self):
        """Test converting GitHubResult to dictionary."""
        result = GitHubResult(
            title="test/repo",
            url="https://github.com/test/repo",
            description="AI security tool",
            source="github",
            stars=100,
            updated="2024-01-01T00:00:00",
            topic="security"
        )
        
        result_dict = result.to_dict()
        
        assert result_dict["source"] == "github"
        assert result_dict["stars"] == 100
        assert result_dict["updated"] == "2024-01-01T00:00:00"
        assert result_dict["topic"] == "security"


class TestRSSResult:
    """Test RSSResult dataclass."""
    
    def test_create_rss_result(self):
        """Test creating an RSSResult."""
        result = RSSResult(
            title="Security Article",
            url="https://example.com/article",
            description="Article about security",
            source="rss",
            feed_name="Security Blog",
            feed_category="research",
            priority="high",
            keyword_matches=3
        )
        
        assert result.title == "Security Article"
        assert result.url == "https://example.com/article"
        assert result.description == "Article about security"
        assert result.source == "rss"
        assert result.feed_name == "Security Blog"
        assert result.feed_category == "research"
        assert result.priority == "high"
        assert result.keyword_matches == 3
    
    def test_rss_result_post_init(self):
        """Test that source is automatically set to 'rss'."""
        result = RSSResult(
            title="Article",
            url="https://example.com/article",
            description="Description",
            source="wrong"  # Should be overridden
        )
        
        assert result.source == "rss"
    
    def test_rss_result_default_values(self):
        """Test RSSResult with default values."""
        result = RSSResult(
            title="Article",
            url="https://example.com/article",
            description="Description",
            source="rss"
        )
        
        assert result.priority == "medium"
        assert result.keyword_matches == 0
        assert result.tags == []
        assert result.author is None
    
    def test_rss_result_with_tags(self):
        """Test RSSResult with tags."""
        result = RSSResult(
            title="Article",
            url="https://example.com/article",
            description="Description",
            source="rss",
            tags=["ai", "security", "automation"]
        )
        
        assert len(result.tags) == 3
        assert "ai" in result.tags


class TestWebSearchResult:
    """Test WebSearchResult dataclass."""
    
    def test_create_web_search_result(self):
        """Test creating a WebSearchResult."""
        result = WebSearchResult(
            title="AI Security News",
            url="https://example.com/news",
            description="Latest developments in AI security",
            source="web_search_llm",
            search_topic="AI security",
            key_points=["Point 1", "Point 2"],
            date="2024-01-01"
        )
        
        assert result.title == "AI Security News"
        assert result.url == "https://example.com/news"
        assert result.description == "Latest developments in AI security"
        assert result.source == "web_search_llm"
        assert result.search_topic == "AI security"
        assert len(result.key_points) == 2
        assert result.date == "2024-01-01"
    
    def test_web_search_result_optional_fields(self):
        """Test WebSearchResult with optional fields."""
        result = WebSearchResult(
            title="Summary",
            url="",
            description="Summary text",
            source="web_search_summary"
        )
        
        assert result.search_topic is None
        assert result.key_points is None
        assert result.date is None
        assert result.credible_sources_found is None
    
    def test_web_search_result_with_credible_sources(self):
        """Test WebSearchResult with credible_sources_found."""
        result = WebSearchResult(
            title="Summary: AI Security",
            url="",
            description="Summary of findings",
            source="web_search_summary",
            search_topic="AI security",
            credible_sources_found=5
        )
        
        assert result.credible_sources_found == 5
    
    def test_web_search_result_to_dict(self):
        """Test converting WebSearchResult to dictionary."""
        result = WebSearchResult(
            title="AI Security News",
            url="https://example.com/news",
            description="Latest developments",
            source="web_search_llm",
            credibility="high",
            search_topic="AI security",
            key_points=["Point 1", "Point 2"],
            date="2024-01-01"
        )
        
        result_dict = result.to_dict()
        
        assert isinstance(result_dict, dict)
        assert result_dict["source"] == "web_search_llm"
        assert result_dict["credibility"] == "high"
        assert result_dict["search_topic"] == "AI security"
        assert len(result_dict["key_points"]) == 2
        assert result_dict["date"] == "2024-01-01"


class TestDataclassCompatibility:
    """Test dataclass compatibility with existing code."""
    
    def test_github_result_dict_compatibility(self):
        """Test that GitHubResult dict output matches old format."""
        result = GitHubResult(
            title="test/repo",
            url="https://github.com/test/repo",
            description="AI tool",
            source="github",
            stars=100,
            updated="2024-01-01T00:00:00",
            topic="security"
        )
        
        result_dict = result.to_dict()
        
        # Check all expected fields are present
        expected_fields = ["title", "url", "description", "source", "stars", "updated", "topic"]
        for field in expected_fields:
            assert field in result_dict
    
    def test_rss_result_dict_compatibility(self):
        """Test that RSSResult dict output matches old format."""
        result = RSSResult(
            title="Article",
            url="https://example.com/article",
            description="Description",
            source="rss",
            published="2024-01-01",
            feed_name="Blog",
            feed_category="research",
            priority="high",
            keyword_matches=2,
            author="John Doe",
            tags=["ai", "security"]
        )
        
        result_dict = result.to_dict()
        
        # Check all expected fields are present
        expected_fields = [
            "title", "url", "description", "source", "published",
            "feed_name", "feed_category", "priority", "keyword_matches",
            "author", "tags"
        ]
        for field in expected_fields:
            assert field in result_dict
    
    def test_web_search_result_dict_compatibility(self):
        """Test that WebSearchResult dict output matches old format."""
        result = WebSearchResult(
            title="News",
            url="https://example.com",
            description="Description",
            source="web_search_llm",
            credibility="high",
            search_topic="topic",
            key_points=["point"],
            date="2024-01-01"
        )
        
        result_dict = result.to_dict()
        
        # Check all expected fields are present
        expected_fields = [
            "title", "url", "description", "source", "credibility",
            "search_topic", "key_points", "date"
        ]
        for field in expected_fields:
            assert field in result_dict
