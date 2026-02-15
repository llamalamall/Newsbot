#!/usr/bin/env python3
"""
Tests for article deduplication functionality across runs.
"""

import os
import sys
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scripts'))

from rss_feed_manager import RSSFeedManager


class TestDeduplication(unittest.TestCase):
    """Test cases for article deduplication."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_seen_articles_persist_across_instances(self):
        """Test that seen articles persist when creating new manager instances."""
        # Create first manager and mark articles as seen
        manager1 = RSSFeedManager(
            cache_enabled=True,
            cache_dir=self.temp_dir
        )
        
        test_urls = [
            'https://example.com/article1',
            'https://example.com/article2',
            'https://example.com/article3'
        ]
        
        # Mark articles as seen
        for url in test_urls:
            manager1._mark_article_as_seen(url)
        
        # Save to disk
        manager1._save_seen_articles()
        
        # Create second manager (simulates new run)
        manager2 = RSSFeedManager(
            cache_enabled=True,
            cache_dir=self.temp_dir
        )
        
        # Verify all articles are marked as seen
        for url in test_urls:
            self.assertTrue(
                manager2._is_article_seen(url),
                f"Article {url} should be marked as seen"
            )
        
        # Verify new article is not seen
        new_url = 'https://example.com/article4'
        self.assertFalse(
            manager2._is_article_seen(new_url),
            f"New article {new_url} should not be marked as seen"
        )
    
    def test_deduplication_filters_seen_entries(self):
        """Test that fetch_feed filters out previously seen articles."""
        manager = RSSFeedManager(
            cache_enabled=True,
            cache_dir=self.temp_dir
        )
        
        # Pre-mark some URLs as seen
        seen_urls = [
            'https://example.com/old1',
            'https://example.com/old2'
        ]
        for url in seen_urls:
            manager._mark_article_as_seen(url)
        
        # Verify seen URLs are marked
        for url in seen_urls:
            self.assertTrue(manager._is_article_seen(url))
        
        # Verify new URL is not marked
        new_url = 'https://example.com/new'
        self.assertFalse(manager._is_article_seen(new_url))
    
    def test_cache_file_created(self):
        """Test that cache file is created when saving seen articles."""
        manager = RSSFeedManager(
            cache_enabled=True,
            cache_dir=self.temp_dir
        )
        
        # Mark an article as seen
        manager._mark_article_as_seen('https://example.com/test')
        
        # Save seen articles
        manager._save_seen_articles()
        
        # Verify file exists
        cache_file = os.path.join(self.temp_dir, 'seen_articles.json')
        self.assertTrue(
            os.path.exists(cache_file),
            f"Cache file should be created at {cache_file}"
        )
    
    def test_clear_cache_with_seen_articles(self):
        """Test that clear_cache can optionally clear seen articles."""
        manager = RSSFeedManager(
            cache_enabled=True,
            cache_dir=self.temp_dir
        )
        
        # Mark articles as seen and save
        manager._mark_article_as_seen('https://example.com/test')
        manager._save_seen_articles()
        
        # Verify cache file exists
        cache_file = os.path.join(self.temp_dir, 'seen_articles.json')
        self.assertTrue(os.path.exists(cache_file))
        
        # Clear cache including seen articles
        manager.clear_cache(clear_seen_articles=True)
        
        # Verify cache file is removed
        self.assertFalse(
            os.path.exists(cache_file),
            "Cache file should be removed after clear_cache(clear_seen_articles=True)"
        )
        
        # Verify set is cleared
        self.assertEqual(len(manager._seen_articles), 0)
    
    def test_old_articles_filtered_from_cache(self):
        """Test that old seen articles are filtered out when loading cache."""
        manager1 = RSSFeedManager(
            cache_enabled=True,
            cache_ttl_hours=24,
            cache_dir=self.temp_dir
        )
        
        # Manually create cache file with old articles
        cache_file = os.path.join(self.temp_dir, 'seen_articles.json')
        
        # Create entries: one recent, one old (60 days ago)
        recent_date = datetime.now()
        old_date = datetime.now() - timedelta(days=60)
        
        import json
        cache_data = [
            {'url': 'https://example.com/recent', 'seen_at': recent_date.isoformat()},
            {'url': 'https://example.com/old', 'seen_at': old_date.isoformat()}
        ]
        
        with open(cache_file, 'w') as f:
            json.dump(cache_data, f)
        
        # Create new manager to load cache
        manager2 = RSSFeedManager(
            cache_enabled=True,
            cache_ttl_hours=24,
            cache_dir=self.temp_dir
        )
        
        # Recent article should be loaded
        self.assertTrue(
            manager2._is_article_seen('https://example.com/recent'),
            "Recent article should be in cache"
        )
        
        # Old article should be filtered out
        self.assertFalse(
            manager2._is_article_seen('https://example.com/old'),
            "Old article should be filtered from cache"
        )
    
    def test_cache_disabled_does_not_save(self):
        """Test that deduplication is skipped when cache is disabled."""
        manager = RSSFeedManager(
            cache_enabled=False,
            cache_dir=self.temp_dir
        )
        
        # Mark article as seen
        manager._mark_article_as_seen('https://example.com/test')
        
        # Save (should not create file when disabled)
        manager._save_seen_articles()
        
        # Verify no cache file created
        cache_file = os.path.join(self.temp_dir, 'seen_articles.json')
        self.assertFalse(
            os.path.exists(cache_file),
            "Cache file should not be created when cache is disabled"
        )


if __name__ == '__main__':
    unittest.main()
