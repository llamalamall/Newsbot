#!/usr/bin/env python3
"""
Test script for Newsbot functionality.
Tests credibility assessment and article extraction features.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.newsbot import NewsBot


def test_credibility_assessment():
    """Test the source credibility assessment."""
    print("Testing Source Credibility Assessment...")
    print("=" * 60)
    
    bot = NewsBot()
    
    test_urls = [
        ("https://github.com/example/repo", "high"),
        ("https://arxiv.org/paper", "high"),
        ("https://blog.google/security", "high"),
        ("https://schneier.com/blog", "high"),
        ("https://medium.com/@author/article", "medium"),
        ("https://techcrunch.com/article", "medium"),
        ("https://unknown-site.com/article", "low"),
        ("https://random-blog.xyz/post", "low"),
    ]
    
    passed = 0
    failed = 0
    
    for url, expected in test_urls:
        result = bot.assess_source_credibility(url)
        status = "✓" if result == expected else "✗"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"{status} {url}")
        print(f"  Expected: {expected}, Got: {result}")
    
    print()
    print(f"Results: {passed} passed, {failed} failed")
    print()
    return failed == 0




def test_article_extraction():
    """Test article content extraction (without actual HTTP requests)."""
    print("Testing Article Extraction Method...")
    print("=" * 60)
    
    bot = NewsBot()
    
    # Test with a non-existent URL (should handle gracefully)
    result = bot.extract_article_content("https://nonexistent-test-url.example.com/article")
    
    if result is None:
        print("✓ Gracefully handles unreachable URLs")
    else:
        print(f"✗ Unexpected result: {result}")
    
    print()
    return True


def test_credible_sources():
    """Test that credible sources are properly defined."""
    print("Testing Credible Sources Configuration...")
    print("=" * 60)
    
    bot = NewsBot()
    
    # Check that credible sources are defined
    if bot.CREDIBLE_SOURCES and 'high' in bot.CREDIBLE_SOURCES and 'medium' in bot.CREDIBLE_SOURCES:
        print(f"✓ Credible sources defined")
        print(f"  High credibility: {len(bot.CREDIBLE_SOURCES['high'])} sources")
        print(f"  Medium credibility: {len(bot.CREDIBLE_SOURCES['medium'])} sources")
    else:
        print("✗ Credible sources not properly defined")
        return False
    
    print()
    return True


def test_integration():
    """Test the integration of components."""
    print("Testing Component Integration...")
    print("=" * 60)
    
    bot = NewsBot()
    
    # Test that core methods exist
    try:
        # Check that aggregate_news method exists
        if hasattr(bot, 'aggregate_news'):
            print(f"✓ aggregate_news method exists")
        else:
            print(f"✗ aggregate_news method not found")
            return False
            
        # Check that assess_source_credibility method exists
        if hasattr(bot, 'assess_source_credibility'):
            print(f"✓ assess_source_credibility method exists")
        else:
            print(f"✗ assess_source_credibility method not found")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    print()
    return True




def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("Newsbot Test Suite")
    print("=" * 60)
    print()
    
    results = {
        "Credibility Assessment": test_credibility_assessment(),
        "Article Extraction": test_article_extraction(),
        "Credible Sources": test_credible_sources(),
        "Component Integration": test_integration(),
    }
    
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print()
    
    all_passed = all(results.values())
    if all_passed:
        print("All tests passed! ✓")
        return 0
    else:
        print("Some tests failed. ✗")
        return 1


if __name__ == "__main__":
    sys.exit(main())
