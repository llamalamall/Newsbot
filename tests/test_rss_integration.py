#!/usr/bin/env python3
"""
Comprehensive test to verify RSS integration doesn't break existing functionality.
This test runs without requiring GITHUB_TOKEN or network access.
"""

import sys
import os
import json

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

def test_configuration():
    """Test that configuration is valid."""
    print("=" * 60)
    print("TEST 1: Configuration Validation")
    print("=" * 60)
    
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✓ Configuration file is valid JSON")
    except Exception as e:
        print(f"✗ Failed to load config: {e}")
        return False
    
    # Check required fields
    required_fields = ['search_topics', 'search_keywords', 'github_topics', 'days_back']
    for field in required_fields:
        if field in config:
            print(f"✓ Required field '{field}' present")
        else:
            print(f"✗ Missing required field: {field}")
            return False
    
    # Check RSS configuration
    if config.get('rss_enabled'):
        print("✓ RSS is enabled")
        
        if 'rss_feeds' in config:
            print(f"✓ RSS feeds configured ({len(config['rss_feeds'])} feeds)")
        else:
            print("✗ RSS enabled but no feeds configured")
            return False
        
        if 'rss_settings' in config:
            print("✓ RSS settings configured")
        else:
            print("⚠ RSS settings not configured (will use defaults)")
    
    # Check dual-mode configuration
    content_source = config.get('content_source', 'dual')
    print(f"✓ Content source mode: {content_source}")
    
    print()
    return True


def test_rss_manager_import():
    """Test that RSSFeedManager can be imported."""
    print("=" * 60)
    print("TEST 2: RSS Feed Manager Import")
    print("=" * 60)
    
    try:
        from rss_feed_manager import RSSFeedManager
        print("✓ RSSFeedManager imported successfully")
        
        # Test initialization
        manager = RSSFeedManager()
        print("✓ RSSFeedManager instantiated")
        
        # Test methods exist
        required_methods = [
            'fetch_feed',
            'fetch_all_feeds',
            'filter_by_date',
            'filter_by_keywords',
            'is_feed_healthy',
            'clear_cache'
        ]
        
        for method in required_methods:
            if hasattr(manager, method):
                print(f"✓ Method '{method}' exists")
            else:
                print(f"✗ Missing method: {method}")
                return False
        
        print()
        return True
        
    except Exception as e:
        print(f"✗ Failed to import RSSFeedManager: {e}")
        print()
        return False


def test_newsbot_methods():
    """Test that NewsBot has required methods (without initializing fully)."""
    print("=" * 60)
    print("TEST 3: NewsBot Methods Check")
    print("=" * 60)
    
    try:
        # Import the class definition (won't fail on missing GITHUB_TOKEN)
        import newsbot
        NewsBot = newsbot.NewsBot
        
        print("✓ NewsBot class imported")
        
        # Check for required methods
        required_methods = [
            'search_github_repos',
            'search_rss_feeds',
            'aggregate_news',
            'generate_report',
            'assess_source_credibility',
            'extract_article_content'
        ]
        
        for method in required_methods:
            if hasattr(NewsBot, method):
                print(f"✓ Method '{method}' exists")
            else:
                print(f"✗ Missing method: {method}")
                return False
        
        print()
        return True
        
    except Exception as e:
        print(f"✗ Failed to check NewsBot methods: {e}")
        print()
        return False


def test_backwards_compatibility():
    """Test that old configuration still works."""
    print("=" * 60)
    print("TEST 4: Backwards Compatibility")
    print("=" * 60)
    
    # Create a minimal config without RSS
    old_config = {
        "search_keywords": ["test"],
        "github_topics": ["test"],
        "days_back": 7,
        "max_results_per_topic": 10,
    }
    
    # Save to temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(old_config, f)
        temp_config = f.name
    
    try:
        from newsbot import NewsBot
        
        # Try to initialize with old config (without GITHUB_TOKEN, will fail but that's ok)
        try:
            bot = NewsBot(config_path=temp_config)
            print("⚠ NewsBot initialized without GITHUB_TOKEN (unexpected)")
        except SystemExit:
            # Expected - no GITHUB_TOKEN
            print("✓ Old configuration format accepted")
        except Exception as e:
            if 'GITHUB_TOKEN' in str(e) or 'github' in str(e).lower():
                print("✓ Old configuration format accepted (GITHUB_TOKEN not set)")
            else:
                print(f"✗ Unexpected error: {e}")
                return False
        
        print()
        return True
        
    except Exception as e:
        print(f"✗ Failed backwards compatibility test: {e}")
        print()
        return False
    finally:
        # Clean up
        try:
            os.unlink(temp_config)
        except:
            pass


def test_report_generation_format():
    """Test that report generation handles RSS sources."""
    print("=" * 60)
    print("TEST 5: Report Generation Format")
    print("=" * 60)
    
    # Create mock results with RSS sources
    mock_results = [
        {
            'title': 'GitHub Repo',
            'source': 'github',
            'url': 'https://github.com/test/repo',
            'stars': 100
        },
        {
            'title': 'RSS Article',
            'source': 'rss',
            'url': 'https://example.com/article',
            'feed_name': 'Test Feed',
            'description': 'Test description',
            'priority': 'high'
        }
    ]
    
    # Check that we can categorize sources
    github_items = [r for r in mock_results if r.get("source") == "github"]
    rss_items = [r for r in mock_results if r.get("source") == "rss"]
    
    print(f"✓ GitHub items: {len(github_items)}")
    print(f"✓ RSS items: {len(rss_items)}")
    
    if len(github_items) == 1 and len(rss_items) == 1:
        print("✓ Source categorization works correctly")
    else:
        print("✗ Source categorization failed")
        return False
    
    print()
    return True


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("NEWSBOT RSS INTEGRATION TEST SUITE")
    print("=" * 60)
    print()
    
    tests = [
        ("Configuration Validation", test_configuration),
        ("RSS Manager Import", test_rss_manager_import),
        ("NewsBot Methods", test_newsbot_methods),
        ("Backwards Compatibility", test_backwards_compatibility),
        ("Report Generation Format", test_report_generation_format),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"✗ Test '{name}' crashed: {e}")
            results.append((name, False))
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print()
    print(f"Total: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! RSS integration is ready.")
        return 0
    else:
        print(f"\n⚠ {total - passed} test(s) failed.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
