"""
Tests for article cache functionality.
"""

import json
import pytest
from pathlib import Path

# Import the module to test
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from utils.article_cache import (
    generate_article_id,
    load_analyzed_articles,
    filter_analyzed_articles
)


class TestGenerateArticleId:
    """Test generate_article_id function."""
    
    def test_generate_id_from_url(self):
        """Test that article ID is generated from URL."""
        article = {
            'title': 'Test Article',
            'url': 'https://example.com/article1'
        }
        article_id = generate_article_id(article)
        assert article_id == 'https://example.com/article1'
    
    def test_generate_id_with_whitespace(self):
        """Test that whitespace in URL is stripped."""
        article = {
            'title': 'Test Article',
            'url': '  https://example.com/article1  '
        }
        article_id = generate_article_id(article)
        assert article_id == 'https://example.com/article1'
    
    def test_generate_id_fallback_to_title(self):
        """Test fallback to title when URL is missing."""
        article = {
            'title': 'Test Article Title',
            'url': ''
        }
        article_id = generate_article_id(article)
        assert article_id == 'test article title'
    
    def test_generate_id_empty_article(self):
        """Test handling of article with no url or title."""
        article = {}
        article_id = generate_article_id(article)
        assert article_id == ''


class TestLoadAnalyzedArticles:
    """Test load_analyzed_articles function."""
    
    def test_load_from_nonexistent_directory(self):
        """Test loading from a directory that doesn't exist."""
        analyzed_ids = load_analyzed_articles('/nonexistent/path')
        assert analyzed_ids == set()
    
    def test_load_from_empty_directory(self, tmp_path):
        """Test loading from an empty directory."""
        analyzed_ids = load_analyzed_articles(str(tmp_path))
        assert analyzed_ids == set()
    
    def test_load_from_single_file(self, tmp_path):
        """Test loading articles from a single JSON file."""
        # Create a results file
        results = [
            {'title': 'Article 1', 'url': 'https://example.com/1'},
            {'title': 'Article 2', 'url': 'https://example.com/2'},
            {'title': 'Article 3', 'url': 'https://example.com/3'}
        ]
        
        results_file = tmp_path / 'results_20240101_120000.json'
        with open(results_file, 'w') as f:
            json.dump(results, f)
        
        analyzed_ids = load_analyzed_articles(str(tmp_path))
        
        assert len(analyzed_ids) == 3
        assert 'https://example.com/1' in analyzed_ids
        assert 'https://example.com/2' in analyzed_ids
        assert 'https://example.com/3' in analyzed_ids
    
    def test_load_from_multiple_files(self, tmp_path):
        """Test loading articles from multiple JSON files."""
        # Create first results file
        results1 = [
            {'title': 'Article 1', 'url': 'https://example.com/1'},
            {'title': 'Article 2', 'url': 'https://example.com/2'}
        ]
        results_file1 = tmp_path / 'results_20240101_120000.json'
        with open(results_file1, 'w') as f:
            json.dump(results1, f)
        
        # Create second results file
        results2 = [
            {'title': 'Article 3', 'url': 'https://example.com/3'},
            {'title': 'Article 4', 'url': 'https://example.com/4'}
        ]
        results_file2 = tmp_path / 'results_20240102_120000.json'
        with open(results_file2, 'w') as f:
            json.dump(results2, f)
        
        analyzed_ids = load_analyzed_articles(str(tmp_path))
        
        assert len(analyzed_ids) == 4
        assert 'https://example.com/1' in analyzed_ids
        assert 'https://example.com/2' in analyzed_ids
        assert 'https://example.com/3' in analyzed_ids
        assert 'https://example.com/4' in analyzed_ids
    
    def test_load_deduplicates_across_files(self, tmp_path):
        """Test that duplicate URLs across files are deduplicated."""
        # Create first results file
        results1 = [
            {'title': 'Article 1', 'url': 'https://example.com/1'},
            {'title': 'Article 2', 'url': 'https://example.com/2'}
        ]
        results_file1 = tmp_path / 'results_20240101_120000.json'
        with open(results_file1, 'w') as f:
            json.dump(results1, f)
        
        # Create second results file with one duplicate
        results2 = [
            {'title': 'Article 2', 'url': 'https://example.com/2'},  # Duplicate
            {'title': 'Article 3', 'url': 'https://example.com/3'}
        ]
        results_file2 = tmp_path / 'results_20240102_120000.json'
        with open(results_file2, 'w') as f:
            json.dump(results2, f)
        
        analyzed_ids = load_analyzed_articles(str(tmp_path))
        
        # Should only have 3 unique URLs
        assert len(analyzed_ids) == 3
        assert 'https://example.com/1' in analyzed_ids
        assert 'https://example.com/2' in analyzed_ids
        assert 'https://example.com/3' in analyzed_ids
    
    def test_load_ignores_non_results_files(self, tmp_path):
        """Test that non-results JSON files are ignored."""
        # Create a results file
        results = [
            {'title': 'Article 1', 'url': 'https://example.com/1'}
        ]
        results_file = tmp_path / 'results_20240101_120000.json'
        with open(results_file, 'w') as f:
            json.dump(results, f)
        
        # Create other JSON files that shouldn't be loaded
        other_file = tmp_path / 'config.json'
        with open(other_file, 'w') as f:
            json.dump({'key': 'value'}, f)
        
        analyzed_ids = load_analyzed_articles(str(tmp_path))
        
        # Should only load from results file
        assert len(analyzed_ids) == 1
        assert 'https://example.com/1' in analyzed_ids
    
    def test_load_handles_invalid_json(self, tmp_path):
        """Test that invalid JSON files are skipped gracefully."""
        # Create a valid results file
        results = [
            {'title': 'Article 1', 'url': 'https://example.com/1'}
        ]
        results_file1 = tmp_path / 'results_20240101_120000.json'
        with open(results_file1, 'w') as f:
            json.dump(results, f)
        
        # Create an invalid JSON file
        invalid_file = tmp_path / 'results_20240102_120000.json'
        with open(invalid_file, 'w') as f:
            f.write('invalid json {')
        
        analyzed_ids = load_analyzed_articles(str(tmp_path))
        
        # Should only load from valid file
        assert len(analyzed_ids) == 1
        assert 'https://example.com/1' in analyzed_ids
    
    def test_load_handles_non_list_format(self, tmp_path):
        """Test that files with non-list format are skipped."""
        # Create a file with object instead of list
        invalid_format = tmp_path / 'results_20240101_120000.json'
        with open(invalid_format, 'w') as f:
            json.dump({'articles': []}, f)
        
        analyzed_ids = load_analyzed_articles(str(tmp_path))
        
        # Should return empty set
        assert len(analyzed_ids) == 0


class TestFilterAnalyzedArticles:
    """Test filter_analyzed_articles function."""
    
    def test_filter_with_empty_analyzed_set(self):
        """Test filtering when no articles have been analyzed."""
        articles = [
            {'title': 'Article 1', 'url': 'https://example.com/1'},
            {'title': 'Article 2', 'url': 'https://example.com/2'}
        ]
        
        filtered, skipped = filter_analyzed_articles(articles, set())
        
        assert len(filtered) == 2
        assert skipped == 0
        assert filtered == articles
    
    def test_filter_all_new_articles(self):
        """Test filtering when all articles are new."""
        articles = [
            {'title': 'Article 1', 'url': 'https://example.com/1'},
            {'title': 'Article 2', 'url': 'https://example.com/2'}
        ]
        
        analyzed_ids = {'https://example.com/99', 'https://example.com/100'}
        
        filtered, skipped = filter_analyzed_articles(articles, analyzed_ids)
        
        assert len(filtered) == 2
        assert skipped == 0
        assert filtered == articles
    
    def test_filter_some_analyzed_articles(self):
        """Test filtering when some articles have been analyzed."""
        articles = [
            {'title': 'Article 1', 'url': 'https://example.com/1'},
            {'title': 'Article 2', 'url': 'https://example.com/2'},
            {'title': 'Article 3', 'url': 'https://example.com/3'}
        ]
        
        analyzed_ids = {'https://example.com/2'}
        
        filtered, skipped = filter_analyzed_articles(articles, analyzed_ids)
        
        assert len(filtered) == 2
        assert skipped == 1
        assert filtered[0]['url'] == 'https://example.com/1'
        assert filtered[1]['url'] == 'https://example.com/3'
    
    def test_filter_all_analyzed_articles(self):
        """Test filtering when all articles have been analyzed."""
        articles = [
            {'title': 'Article 1', 'url': 'https://example.com/1'},
            {'title': 'Article 2', 'url': 'https://example.com/2'}
        ]
        
        analyzed_ids = {
            'https://example.com/1',
            'https://example.com/2'
        }
        
        filtered, skipped = filter_analyzed_articles(articles, analyzed_ids)
        
        assert len(filtered) == 0
        assert skipped == 2
    
    def test_filter_empty_article_list(self):
        """Test filtering with empty article list."""
        articles = []
        analyzed_ids = {'https://example.com/1'}
        
        filtered, skipped = filter_analyzed_articles(articles, analyzed_ids)
        
        assert len(filtered) == 0
        assert skipped == 0
    
    def test_filter_handles_articles_without_url(self):
        """Test filtering articles that have no URL."""
        articles = [
            {'title': 'Article 1', 'url': 'https://example.com/1'},
            {'title': 'Article 2', 'url': ''},  # No URL
            {'title': 'Article 3', 'url': 'https://example.com/3'}
        ]
        
        analyzed_ids = {'https://example.com/1'}
        
        filtered, skipped = filter_analyzed_articles(articles, analyzed_ids)
        
        # Article 1 should be skipped (analyzed), Article 2 and 3 should remain
        assert len(filtered) == 2
        assert skipped == 1
        assert filtered[0]['title'] == 'Article 2'
        assert filtered[1]['url'] == 'https://example.com/3'
