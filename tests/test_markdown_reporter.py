"""
Tests for the markdown_reporter module.
"""

import os
import sys
import pytest

# Import the module to test
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from reporters.markdown_reporter import (
    generate_repositories_page,
    generate_rss_article_page
)


class TestGenerateRepositoriesPage:
    """Tests for generate_repositories_page function."""
    
    def test_empty_repositories(self):
        """Test generating page with no repositories."""
        result = generate_repositories_page([])
        
        assert "# GitHub Repositories" in result
        assert "*No repositories found.*" in result
    
    def test_single_repository(self):
        """Test generating page with one repository."""
        repos = [
            {
                "title": "test-repo",
                "url": "https://github.com/user/test-repo",
                "description": "A test repository",
                "stars": 42,
                "updated": "2026-02-15T10:00:00Z",
                "topic": "security"
            }
        ]
        
        result = generate_repositories_page(repos)
        
        assert "# GitHub Repositories" in result
        assert "1 repositories found" in result
        assert "| Repository | Description | Stars | Last Updated | Topics |" in result
        assert "[test-repo]" in result
        assert "A test repository" in result
        assert "42" in result
        assert "security" in result
    
    def test_multiple_repositories_sorted_by_stars(self):
        """Test that repositories are sorted by stars (descending)."""
        repos = [
            {
                "title": "repo-low",
                "url": "https://github.com/user/repo-low",
                "description": "Low stars",
                "stars": 10,
                "updated": "2026-02-15T10:00:00Z",
                "topic": "security"
            },
            {
                "title": "repo-high",
                "url": "https://github.com/user/repo-high",
                "description": "High stars",
                "stars": 100,
                "updated": "2026-02-15T10:00:00Z",
                "topic": "automation"
            }
        ]
        
        result = generate_repositories_page(repos)
        
        # High stars should come before low stars
        assert result.index("repo-high") < result.index("repo-low")
    
    def test_long_description_truncated(self):
        """Test that long descriptions are truncated."""
        repos = [
            {
                "title": "test-repo",
                "url": "https://github.com/user/test-repo",
                "description": "A" * 150,  # Very long description
                "stars": 42,
                "updated": "2026-02-15T10:00:00Z",
                "topic": "security"
            }
        ]
        
        result = generate_repositories_page(repos)
        
        # Should be truncated
        assert "..." in result
        # Description in table should not exceed 103 characters (100 + "...")
        lines = result.split('\n')
        for line in lines:
            if '|' in line and 'AAAA' in line:  # Find the repo line
                # Extract description column (second column)
                parts = line.split('|')
                if len(parts) >= 3:
                    desc = parts[2].strip()
                    assert len(desc) <= 103
    
    def test_pipe_character_escaping(self):
        """Test that pipe characters in description are escaped."""
        repos = [
            {
                "title": "test-repo",
                "url": "https://github.com/user/test-repo",
                "description": "Description with | pipe character",
                "stars": 42,
                "updated": "2026-02-15T10:00:00Z",
                "topic": "security"
            }
        ]
        
        result = generate_repositories_page(repos)
        
        # Pipe should be escaped
        assert "\\|" in result


class TestGenerateRssArticlePage:
    """Tests for generate_rss_article_page function."""
    
    def test_basic_article(self):
        """Test generating page for basic article."""
        article = {
            "title": "Test Article",
            "description": "This is a test article description.",
            "url": "https://example.com/article",
            "published": "2026-02-15T10:00:00Z",
            "feed_name": "Test Feed"
        }
        
        result = generate_rss_article_page(article)
        
        assert "# Test Article" in result
        assert "This is a test article description" in result
        assert "https://example.com/article" in result
        assert "**Feed:** Test Feed" in result
    
    def test_article_with_llm_assessment(self):
        """Test article with LLM applicability and credibility assessment."""
        article = {
            "title": "Test Article",
            "description": "Test description",
            "url": "https://example.com/article",
            "llm_applicable": True,
            "llm_applicability_score": 0.85,
            "llm_matched_keywords": ["AI", "security"],
            "llm_applicability_reason": "Relevant to AI security",
            "llm_credible": True,
            "llm_credibility_score": 0.90,
            "llm_credibility_flags": ["credible source"],
            "llm_credibility_reason": "Published by reputable source"
        }
        
        result = generate_rss_article_page(article)
        
        assert "## Relevance Assessment" in result
        assert "✓ Relevant" in result
        assert "0.85" in result
        assert "AI, security" in result
        assert "Relevant to AI security" in result
        
        assert "## Credibility Assessment" in result
        assert "✓ Credible" in result
        assert "0.90" in result
        assert "credible source" in result
        assert "Published by reputable source" in result
    
    def test_article_with_html_description(self):
        """Test that HTML in description is cleaned."""
        # Note: This test requires BeautifulSoup to be available
        try:
            from bs4 import BeautifulSoup
            
            article = {
                "title": "Test Article",
                "description": "<p>This is <strong>HTML</strong> content</p>",
                "url": "https://example.com/article"
            }
            
            result = generate_rss_article_page(article)
            
            # HTML tags should be removed
            assert "<p>" not in result or "This is HTML content" in result
        except ImportError:
            # Skip if BeautifulSoup is not available
            pytest.skip("BeautifulSoup not available")
    
    def test_article_with_feed_category(self):
        """Test article with feed category."""
        article = {
            "title": "Test Article",
            "description": "Test description",
            "feed_name": "Security Blog",
            "feed_category": "research"
        }
        
        result = generate_rss_article_page(article)
        
        assert "Security Blog (research)" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
