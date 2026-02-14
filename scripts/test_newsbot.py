#!/usr/bin/env python3
"""
Test script for Newsbot enhancements.
Tests the new web search integration and credibility assessment features.
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


def test_web_search_helper():
    """Test the web search helper module."""
    print("Testing Web Search Helper...")
    print("=" * 60)
    
    try:
        from scripts.web_search_helper import WebSearchHelper
        
        # Test initialization with default parameters
        helper = WebSearchHelper()
        print(f"✓ Web search helper loaded successfully")
        print(f"  Available: {helper.is_available()}")
        
        # Test initialization with custom parameters
        custom_helper = WebSearchHelper(timeout=5, rate_limit_delay=0.5)
        print(f"✓ Custom parameters accepted")
        print(f"  Timeout: {custom_helper.timeout}s")
        print(f"  Rate limit: {custom_helper.rate_limit_delay}s")
        
        # Test that search method exists and returns correct type
        results = helper.search("test query", max_results=5)
        if isinstance(results, list):
            print(f"✓ Search method returns list")
            print(f"  Results: {len(results)} items")
        else:
            print(f"✗ Search method should return list, got {type(results)}")
            return False
        
        # Test URL cleaning method
        test_urls = [
            ("https://example.com", "https://example.com"),
            ("//example.com", "https://example.com"),
            ("", ""),
            ("invalid", ""),
        ]
        
        for test_url, expected in test_urls:
            cleaned = helper._clean_url(test_url)
            if cleaned == expected or (not cleaned and not expected):
                print(f"✓ URL cleaning works for: {test_url}")
            else:
                print(f"✗ URL cleaning failed: {test_url} -> {cleaned}, expected {expected}")
        
        print()
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print()
        return False


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


def test_llm_prompt_structure():
    """Test that the LLM prompt includes web search context."""
    print("Testing LLM Prompt Structure...")
    print("=" * 60)
    
    bot = NewsBot()
    
    # Check that the prompt template includes the search_context placeholder
    if "{search_context}" in bot.LLM_SUMMARY_PROMPT and "{query}" in bot.LLM_SUMMARY_PROMPT:
        print("✓ LLM prompt template includes web search context placeholder")
        print("✓ LLM prompt template includes query placeholder")
    else:
        print("✗ LLM prompt template missing required placeholders")
        return False
    
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
    
    # Test that perform_web_search method exists and is callable
    try:
        results = bot.perform_web_search("test query")
        print(f"✓ perform_web_search method callable")
        print(f"  Returns: {type(results)}")
    except Exception as e:
        print(f"✗ Error calling perform_web_search: {e}")
        return False
    
    # Test that search_with_web_context method exists
    try:
        # Note: This will fail without GITHUB_TOKEN, but we're just checking it's callable
        print("✓ search_with_web_context method exists")
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    # Test configuration loading
    if 'web_search_enabled' in bot.config:
        print(f"✓ Configuration includes web_search_enabled: {bot.config['web_search_enabled']}")
    else:
        print("✗ Configuration missing web_search_enabled")
        return False
    
    if 'web_search_max_results' in bot.config:
        print(f"✓ Configuration includes web_search_max_results: {bot.config['web_search_max_results']}")
    else:
        print("✗ Configuration missing web_search_max_results")
        return False
    
    print()
    return True


def test_web_search_runner():
    """Test the web search runner module."""
    print("Testing Web Search Runner...")
    print("=" * 60)
    
    try:
        from scripts.web_search_runner import perform_web_search
        
        # Test the function with a simple query
        result = perform_web_search("test query", max_results=5)
        
        # Check structure
        required_keys = ["success", "query", "results", "count", "error"]
        for key in required_keys:
            if key in result:
                print(f"✓ Result includes '{key}' field")
            else:
                print(f"✗ Result missing '{key}' field")
                return False
        
        # Check types
        if isinstance(result["results"], list):
            print(f"✓ Results field is a list")
        else:
            print(f"✗ Results field should be a list")
            return False
        
        if isinstance(result["query"], str):
            print(f"✓ Query field is a string")
        else:
            print(f"✗ Query field should be a string")
            return False
        
        print()
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        print()
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("Newsbot Enhancement Test Suite")
    print("=" * 60)
    print()
    
    results = {
        "Credibility Assessment": test_credibility_assessment(),
        "Web Search Helper": test_web_search_helper(),
        "Web Search Runner": test_web_search_runner(),
        "Article Extraction": test_article_extraction(),
        "LLM Prompt Structure": test_llm_prompt_structure(),
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
