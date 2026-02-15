"""
Tests for the docs_publisher module.
"""

import os
import tempfile
import shutil
import json
from datetime import datetime
import pytest

# Import the module to test
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from reporters.docs_publisher import (
    initialize_docs_directory
)


class TestInitializeDocsDirectory:
    """Tests for initialize_docs_directory function."""
    
    def test_initialize_creates_directory(self):
        """Test that initialization creates the docs directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            initialize_docs_directory(docs_dir)
            
            assert os.path.exists(docs_dir)
            assert os.path.isdir(docs_dir)
    
    def test_initialize_creates_index(self):
        """Test that index.md is created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            initialize_docs_directory(docs_dir)
            
            index_path = os.path.join(docs_dir, "index.md")
            assert os.path.exists(index_path)
            
            with open(index_path, 'r') as f:
                content = f.read()
            
            assert "# Newsbot - Security News Aggregator" in content
            assert "## About Newsbot" in content
            assert "## Latest Reports" in content
    
    def test_initialize_creates_readme(self):
        """Test that README.md is created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            initialize_docs_directory(docs_dir)
            
            readme_path = os.path.join(docs_dir, "README.md")
            assert os.path.exists(readme_path)
            
            with open(readme_path, 'r') as f:
                content = f.read()
            
            assert "# Newsbot Documentation" in content
            assert "Setup GitHub Pages" in content
    
    def test_initialize_idempotent(self):
        """Test that initialization is idempotent (can be run multiple times)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            # Initialize twice
            initialize_docs_directory(docs_dir)
            initialize_docs_directory(docs_dir)
            
            # All files should still exist
            assert os.path.exists(os.path.join(docs_dir, "index.md"))
            assert os.path.exists(os.path.join(docs_dir, "README.md"))


class TestStructuredPublishing:
    """Tests for structured documentation publishing."""
    
    def test_publish_repositories_page(self):
        """Test publishing repositories page with table format."""
        from reporters.docs_publisher import publish_repositories_page
        
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = tmpdir
            
            # Create test GitHub items
            github_items = [
                {
                    "source": "github",
                    "title": "test-repo-1",
                    "url": "https://github.com/user/test-repo-1",
                    "description": "First test repository",
                    "stars": 100,
                    "updated": "2026-02-15T10:00:00Z",
                    "topic": "security"
                },
                {
                    "source": "github",
                    "title": "test-repo-2",
                    "url": "https://github.com/user/test-repo-2",
                    "description": "Second test repository",
                    "stars": 50,
                    "updated": "2026-02-14T10:00:00Z",
                    "topic": "automation"
                }
            ]
            
            result = publish_repositories_page(github_items, docs_dir)
            
            assert result is not None
            assert os.path.exists(result)
            
            # Check content
            with open(result, 'r') as f:
                content = f.read()
            
            assert "# GitHub Repositories" in content
            assert "| Repository | Description | Stars | Last Updated | Topics |" in content
            assert "[test-repo-1]" in content
            assert "[test-repo-2]" in content
            assert "First test repository" in content
            # Higher stars should come first
            assert content.index("test-repo-1") < content.index("test-repo-2")
    
    def test_publish_rss_article_pages(self):
        """Test publishing individual RSS article pages."""
        from reporters.docs_publisher import publish_rss_article_pages
        
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = tmpdir
            
            # Create test RSS items
            rss_items = [
                {
                    "source": "rss",
                    "title": "Test Article 1",
                    "url": "https://example.com/article1",
                    "description": "This is test article 1",
                    "feed_name": "Test Feed",
                    "published": "2026-02-15T10:00:00Z",
                    "priority": "high"
                },
                {
                    "source": "rss",
                    "title": "Test Article 2",
                    "url": "https://example.com/article2",
                    "description": "This is test article 2",
                    "feed_name": "Test Feed",
                    "published": "2026-02-14T10:00:00Z",
                    "priority": "low",
                    "keyword_matches": 5
                }
            ]
            
            timestamp = "20260215_120000"
            result = publish_rss_article_pages(rss_items, timestamp, docs_dir)
            
            assert len(result) == 2
            
            # Check that articles directory was created
            articles_dir = os.path.join(docs_dir, "articles")
            assert os.path.exists(articles_dir)
            
            # Check first article file
            article1_path = os.path.join(articles_dir, "article_20260215_120000_001.md")
            assert os.path.exists(article1_path)
            
            with open(article1_path, 'r') as f:
                content = f.read()
            
            assert "# Test Article 1" in content
            assert "This is test article 1" in content
            assert "[← Back to Index](../index.md)" in content
            # First article should have next but no previous
            assert "[Next Article →]" in content
            assert "[← Previous Article]" not in content
    
    def test_update_index_with_structured_content(self):
        """Test updating index with structured content links."""
        from reporters.docs_publisher import update_index_with_structured_content
        
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = tmpdir
            
            # Create initial index
            index_path = os.path.join(docs_dir, "index.md")
            
            article_entries = [
                {
                    "filename": "article_20260215_120000_001.md",
                    "title": "Test Article 1",
                    "url": "https://example.com/article1",
                    "published": "2026-02-15T10:00:00Z",
                    "llm_applicability_score": 0.85,
                    "llm_credibility_score": 0.75
                },
                {
                    "filename": "article_20260215_120000_002.md",
                    "title": "Test Article 2",
                    "url": "https://test.org/article2",
                    "published": "2026-02-15T09:00:00Z",
                    "llm_applicability_score": 0.90,
                    "llm_credibility_score": 0.80
                }
            ]
            
            update_index_with_structured_content(
                docs_dir, "20260215_120000", 5, 2, article_entries
            )
            
            assert os.path.exists(index_path)
            
            with open(index_path, 'r') as f:
                content = f.read()
            
            # Check for repositories link
            assert "[GitHub Repositories](repositories.md)" in content
            
            # Check for articles section
            assert "## Latest Articles" in content
            assert "February 15, 2026" in content
            assert "2 articles published" in content
            
            # Check for table format
            assert "| Source | Updated | Applicability | Credibility | Title |" in content
            assert "|--------|---------|--------------|-------------|-------|" in content
            
            # Check for article entries in table
            assert "example.com" in content
            assert "test.org" in content
            assert "0.85" in content
            assert "0.90" in content
            assert "0.75" in content
            assert "0.80" in content
            assert "[Test Article 1](articles/article_20260215_120000_001.md)" in content
            assert "[Test Article 2](articles/article_20260215_120000_002.md)" in content
    
    def test_publish_structured_docs(self):
        """Test complete structured documentation publishing."""
        from reporters.docs_publisher import publish_structured_docs
        
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = tmpdir
            
            # Create test results with both GitHub repos and RSS articles
            results = [
                {
                    "source": "github",
                    "title": "test-repo",
                    "url": "https://github.com/user/test-repo",
                    "description": "Test repository",
                    "stars": 100,
                    "updated": "2026-02-15T10:00:00Z",
                    "topic": "security"
                },
                {
                    "source": "rss",
                    "title": "Test Article",
                    "url": "https://example.com/article",
                    "description": "Test article content",
                    "feed_name": "Test Feed",
                    "published": "2026-02-15T10:00:00Z"
                }
            ]
            
            timestamp = "20260215_120000"
            published = publish_structured_docs(results, timestamp, docs_dir)
            
            # Check that all expected files were created
            assert published["repositories"] is not None
            assert os.path.exists(published["repositories"])
            
            assert len(published["articles"]) == 1
            assert os.path.exists(published["articles"][0])
            
            assert os.path.exists(published["index"])
            
            # Verify index content
            with open(published["index"], 'r') as f:
                content = f.read()
            
            assert "[GitHub Repositories](repositories.md)" in content
            assert "## Latest Articles" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
