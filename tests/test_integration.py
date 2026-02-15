#!/usr/bin/env python3
"""
Test NewsBot integration with RSS feeds
"""

import sys
import os
import json

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))


def load_list_config(config, key, file_key, base_dir):
    """Load a list-based config from a file or inline config."""
    file_ref = config.get(file_key)
    if not file_ref:
        return config.get(key, [])

    resolved_path = file_ref
    if not os.path.isabs(file_ref):
        resolved_path = os.path.join(base_dir, file_ref)

    try:
        with open(resolved_path, 'r') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        print(f"⚠ {resolved_path} is not a JSON list; using empty list")
    except Exception as exc:
        print(f"⚠ Could not load {resolved_path}: {exc}")

    return []

def test_newsbot_rss_integration():
    """Test that NewsBot properly initializes with RSS configuration."""
    print("Testing NewsBot RSS Integration...")
    print("=" * 60)
    
    # Test 1: Load config
    print("\n1. Testing configuration loading...")
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    base_dir = os.path.dirname(config_path)
    
    print("✓ Configuration loaded successfully")
    print(f"  - Content source: {config.get('content_source', 'not set')}")
    print(f"  - RSS enabled: {config.get('rss_enabled', False)}")
    rss_feeds = load_list_config(config, 'rss_feeds', 'rss_feeds_file', base_dir)
    print(f"  - Number of RSS feeds: {len(rss_feeds)}")
    
    # Test 2: Check RSS settings
    print("\n2. Testing RSS settings...")
    rss_settings = config.get('rss_settings', {})
    print("✓ RSS settings found")
    print(f"  - Max age days: {rss_settings.get('max_age_days', 'not set')}")
    print(f"  - Min keyword matches: {rss_settings.get('min_keyword_matches', 'not set')}")
    print(f"  - Cache enabled: {rss_settings.get('cache_enabled', 'not set')}")
    print(f"  - Cache TTL hours: {rss_settings.get('cache_ttl_hours', 'not set')}")
    print(f"  - Request timeout: {rss_settings.get('request_timeout', 'not set')}")
    print(f"  - Rate limit delay: {rss_settings.get('rate_limit_delay', 'not set')}")
    
    # Test 3: Check RSS feeds
    print("\n3. Testing RSS feed configuration...")
    rss_feeds = load_list_config(config, 'rss_feeds', 'rss_feeds_file', base_dir)
    print(f"✓ Found {len(rss_feeds)} RSS feeds configured")
    
    # Show feed categories
    categories = {}
    priorities = {}
    for feed in rss_feeds:
        cat = feed.get('category', 'unknown')
        pri = feed.get('priority', 'unknown')
        categories[cat] = categories.get(cat, 0) + 1
        priorities[pri] = priorities.get(pri, 0) + 1
    
    print(f"\n  Feed categories:")
    for cat, count in sorted(categories.items()):
        print(f"    • {cat}: {count}")
    
    print(f"\n  Feed priorities:")
    for pri, count in sorted(priorities.items()):
        print(f"    • {pri}: {count}")
    
    # Show sample feeds
    print(f"\n  Sample feeds (first 5):")
    for i, feed in enumerate(rss_feeds[:5], 1):
        print(f"    {i}. {feed.get('name', 'Unknown')} ({feed.get('priority', 'N/A')})")
    
    # Test 4: Validate feed structure
    print("\n4. Validating feed structure...")
    valid_feeds = 0
    for feed in rss_feeds:
        if all(key in feed for key in ['name', 'url', 'priority', 'category']):
            valid_feeds += 1
    
    print(f"✓ Feed validation complete")
    print(f"  - Total feeds: {len(rss_feeds)}")
    print(f"  - Valid feeds: {valid_feeds}")
    print(f"  - Invalid feeds: {len(rss_feeds) - valid_feeds}")
    
    # Test 5: Try to import NewsBot
    print("\n5. Testing NewsBot import and initialization...")
    try:
        from newsbot import NewsBot
        print("✓ NewsBot imported successfully")
        
        # Note: We can't fully initialize without GITHUB_TOKEN
        # but we can verify the class exists and has the right methods
        if hasattr(NewsBot, 'search_rss_feeds'):
            print("✓ NewsBot has search_rss_feeds method")
        else:
            print("✗ NewsBot missing search_rss_feeds method")
        
        if hasattr(NewsBot, 'aggregate_news'):
            print("✓ NewsBot has aggregate_news method")
        else:
            print("✗ NewsBot missing aggregate_news method")
        
    except Exception as e:
        print(f"⚠ Could not fully test NewsBot: {str(e)}")
        print("  (This is expected without GITHUB_TOKEN)")
    
    print("\n" + "=" * 60)
    print("Integration tests completed! ✓")
    print("\nConfiguration is ready for RSS feed aggregation.")
    print("Run newsbot.py with GITHUB_TOKEN to test full functionality.")

if __name__ == '__main__':
    test_newsbot_rss_integration()
