#!/usr/bin/env python3
"""
Test script to verify deduplication functionality.
"""

import os
import sys
import shutil
import tempfile
from datetime import datetime

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from rss_feed_manager import RSSFeedManager


def test_deduplication():
    """Test that seen articles are properly deduplicated."""
    
    # Create a temporary cache directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        print("Testing Deduplication Functionality")
        print("=" * 60)
        
        # Create manager with cache enabled
        manager = RSSFeedManager(
            cache_enabled=True,
            cache_dir=temp_dir
        )
        
        # Create test entries
        test_entries = [
            {
                'title': 'Article 1',
                'link': 'https://example.com/article1',
                'description': 'Test article 1',
                'published': datetime.now().isoformat()
            },
            {
                'title': 'Article 2',
                'link': 'https://example.com/article2',
                'description': 'Test article 2',
                'published': datetime.now().isoformat()
            }
        ]
        
        print("\n1. Initial state - no seen articles")
        print(f"   Seen articles count: {len(manager._seen_articles)}")
        
        print("\n2. Mark articles as seen")
        for entry in test_entries:
            manager._mark_article_as_seen(entry['link'])
        print(f"   Seen articles count: {len(manager._seen_articles)}")
        
        print("\n3. Save seen articles to disk")
        manager._save_seen_articles()
        cache_file = os.path.join(temp_dir, 'seen_articles.json')
        print(f"   Cache file exists: {os.path.exists(cache_file)}")
        
        print("\n4. Create new manager instance (simulates new run)")
        manager2 = RSSFeedManager(
            cache_enabled=True,
            cache_dir=temp_dir
        )
        print(f"   Loaded seen articles: {len(manager2._seen_articles)}")
        
        print("\n5. Check if articles are marked as seen")
        for entry in test_entries:
            is_seen = manager2._is_article_seen(entry['link'])
            print(f"   {entry['link']}: {'SEEN' if is_seen else 'NEW'}")
        
        print("\n6. Verify new article is not seen")
        new_url = 'https://example.com/article3'
        is_seen = manager2._is_article_seen(new_url)
        print(f"   {new_url}: {'SEEN (ERROR!)' if is_seen else 'NEW (CORRECT)'}")
        
        # Verify results
        all_seen = all(manager2._is_article_seen(e['link']) for e in test_entries)
        new_not_seen = not manager2._is_article_seen(new_url)
        
        print("\n" + "=" * 60)
        if all_seen and new_not_seen:
            print("✓ DEDUPLICATION TEST PASSED")
            print("  - Previously seen articles are correctly identified")
            print("  - New articles are correctly identified as new")
            print("  - Persistent cache works across manager instances")
            return True
        else:
            print("✗ DEDUPLICATION TEST FAILED")
            if not all_seen:
                print("  - ERROR: Previously seen articles not detected")
            if not new_not_seen:
                print("  - ERROR: New article incorrectly marked as seen")
            return False
            
    finally:
        # Cleanup
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == '__main__':
    success = test_deduplication()
    sys.exit(0 if success else 1)
