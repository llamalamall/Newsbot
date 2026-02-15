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
    initialize_docs_directory,
    load_rejected_articles,
    generate_rejected_articles_page,
    publish_rejected_articles_page
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
            assert "2 articles total" in content
            
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


class TestRejectedArticles:
    """Tests for rejected articles functionality."""
    
    def test_load_rejected_articles_empty_directory(self):
        """Test loading rejected articles from empty directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            rejected = load_rejected_articles(tmpdir)
            assert rejected == []
    
    def test_load_rejected_articles_no_files(self):
        """Test loading when directory exists but has no rejected JSON files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create some other files
            with open(os.path.join(tmpdir, "results.json"), 'w') as f:
                json.dump([], f)
            
            rejected = load_rejected_articles(tmpdir)
            assert rejected == []
    
    def test_load_rejected_articles_single_file(self):
        """Test loading rejected articles from a single file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a rejected articles file
            rejected_data = [
                {
                    "title": "Test Article 1",
                    "url": "https://example.com/1",
                    "topic": "security",
                    "rejection_type": "relevance",
                    "rejection_reason": "missing_ai_keywords"
                },
                {
                    "title": "Test Article 2",
                    "url": "https://example.com/2",
                    "topic": "malware",
                    "rejection_type": "credibility",
                    "rejection_reason": "llm_credibility_below_threshold",
                    "rejection_threshold": 0.6
                }
            ]
            
            with open(os.path.join(tmpdir, "rejected_20260215_120000.json"), 'w') as f:
                json.dump(rejected_data, f)
            
            rejected = load_rejected_articles(tmpdir)
            assert len(rejected) == 2
            assert rejected[0]["title"] == "Test Article 1"
            assert rejected[1]["rejection_type"] == "credibility"
    
    def test_load_rejected_articles_multiple_files(self):
        """Test loading rejected articles from multiple files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create multiple rejected articles files
            for i in range(3):
                rejected_data = [
                    {
                        "title": f"Article {i}",
                        "url": f"https://example.com/{i}",
                        "topic": "security",
                        "rejection_type": "relevance",
                        "rejection_reason": "missing_ai_keywords"
                    }
                ]
                
                with open(os.path.join(tmpdir, f"rejected_2026021{i}_120000.json"), 'w') as f:
                    json.dump(rejected_data, f)
            
            rejected = load_rejected_articles(tmpdir)
            assert len(rejected) == 3
    
    def test_generate_rejected_articles_page(self):
        """Test generating rejected articles page content."""
        rejected_data = [
            {
                "title": "Test Article",
                "url": "https://example.com/test",
                "topic": "security",
                "rejection_type": "relevance",
                "rejection_reason": "missing_ai_keywords"
            },
            {
                "title": "Another Article",
                "url": "https://example.com/another",
                "topic": "malware",
                "rejection_type": "credibility",
                "rejection_reason": "llm_credibility_below_threshold",
                "rejection_threshold": 0.6
            }
        ]
        
        content = generate_rejected_articles_page(rejected_data)
        
        # Check for expected sections
        assert "# Rejected Articles" in content
        assert "## What Constitutes a \"Rejected\" Article?" in content
        assert "## Rejected Articles Table" in content
        
        # Check table header
        assert "| Title | Topic | Rejection Type | Rejection Reason |" in content
        
        # Check table content
        assert "[Test Article](https://example.com/test)" in content
        assert "missing_ai_keywords" in content
        assert "llm_credibility_below_threshold (threshold: 0.6)" in content
        
        # Check total count
        assert "Total rejected articles: **2**" in content
        
        # Check navigation
        assert "[← Back to Index](index.md)" in content
    
    def test_generate_rejected_articles_page_no_url(self):
        """Test generating page with articles without URLs."""
        rejected_data = [
            {
                "title": "Test Article",
                "topic": "security",
                "rejection_type": "relevance",
                "rejection_reason": "missing_ai_keywords"
            }
        ]
        
        content = generate_rejected_articles_page(rejected_data)
        
        # Title should not be a link if URL is missing
        assert "Test Article" in content
        assert "[Test Article]" not in content
    
    def test_publish_rejected_articles_page(self):
        """Test publishing rejected articles page."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            output_dir = os.path.join(tmpdir, "outputs")
            os.makedirs(output_dir, exist_ok=True)
            os.makedirs(docs_dir, exist_ok=True)
            
            # Create rejected articles data
            rejected_data = [
                {
                    "title": "Test Article",
                    "url": "https://example.com/test",
                    "topic": "security",
                    "rejection_type": "relevance",
                    "rejection_reason": "missing_ai_keywords"
                }
            ]
            
            with open(os.path.join(output_dir, "rejected_20260215_120000.json"), 'w') as f:
                json.dump(rejected_data, f)
            
            # Publish the page
            result = publish_rejected_articles_page(output_dir, docs_dir)
            
            assert result is not None
            assert os.path.exists(result)
            assert result.endswith("rejected.md")
            
            # Verify content
            with open(result, 'r') as f:
                content = f.read()
            
            assert "layout: default" in content
            assert "title: Rejected Articles" in content
            assert "[Test Article](https://example.com/test)" in content
    
    def test_publish_rejected_articles_page_no_data(self):
        """Test publishing when no rejected articles exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            output_dir = os.path.join(tmpdir, "outputs")
            os.makedirs(output_dir, exist_ok=True)
            
            # No rejected articles files
            result = publish_rejected_articles_page(output_dir, docs_dir)
            
            # Should return None when no data exists
            assert result is None
    
    def test_publish_structured_docs_includes_rejected(self):
        """Test that publish_structured_docs includes rejected articles page."""
        from reporters.docs_publisher import publish_structured_docs
        
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            output_dir = os.path.join(tmpdir, "outputs")
            os.makedirs(output_dir, exist_ok=True)
            
            # Create rejected articles data
            rejected_data = [
                {
                    "title": "Rejected Article",
                    "url": "https://example.com/rejected",
                    "topic": "security",
                    "rejection_type": "relevance",
                    "rejection_reason": "missing_ai_keywords"
                }
            ]
            
            with open(os.path.join(output_dir, "rejected_20260215_120000.json"), 'w') as f:
                json.dump(rejected_data, f)
            
            # Create test results
            results = [
                {
                    "source": "github",
                    "title": "test-repo",
                    "url": "https://github.com/user/test-repo",
                    "description": "Test repository",
                    "stars": 100,
                    "updated": "2026-02-15T10:00:00Z",
                    "topic": "security"
                }
            ]
            
            timestamp = "20260215_120000"
            published = publish_structured_docs(results, timestamp, docs_dir, output_dir)
            
            # Check that rejected page was created
            assert "rejected" in published
            assert published["rejected"] is not None
            assert os.path.exists(published["rejected"])
            
            # Verify content
            with open(published["rejected"], 'r') as f:
                content = f.read()
            
            assert "[Rejected Article](https://example.com/rejected)" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
