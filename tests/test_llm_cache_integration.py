#!/usr/bin/env python3
"""
Integration test for LLM assessment caching.
Tests that LLM assessments are cached and reused correctly.
"""

import sys
import os
from unittest.mock import Mock, MagicMock, patch
import json

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

from rss_feed_manager import RSSFeedManager
from searchers.rss_search import search_rss_feeds
from utils.credibility import assess_source_credibility


def test_llm_cache_reduces_calls():
    """Test that LLM assessment caching reduces actual LLM API calls."""
    print("Testing LLM assessment caching...")
    print("=" * 60)
    
    # Create RSS manager with caching enabled
    rss_manager = RSSFeedManager(cache_enabled=True, cache_ttl_hours=6)
    
    # Mock OpenAI client
    mock_client = Mock()
    llm_call_count = 0
    
    def mock_llm_call(*args, **kwargs):
        """Count LLM calls and return mock response."""
        nonlocal llm_call_count
        llm_call_count += 1
        
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        # Return different responses for applicability vs credibility
        # based on system message
        system_msg = kwargs.get('messages', [{}])[0].get('content', '')
        
        if 'credibility' in system_msg.lower():
            result = {
                "credible": True,
                "score": 0.8,
                "reason": "Credible source",
                "flags": []
            }
        else:
            result = {
                "applicable": True,
                "score": 0.9,
                "reason": "Relevant to AI security",
                "matched_keywords": ["AI", "security"]
            }
        
        mock_message.content = json.dumps(result)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        return mock_response
    
    mock_client.chat.completions.create = Mock(side_effect=mock_llm_call)
    
    # Create test RSS entries (simulating cached RSS feed data)
    test_entries = [
        {
            'title': 'AI Security Tool',
            'link': 'https://example.com/article1',
            'description': 'New AI-powered penetration testing tool',
            'published': '2026-02-14T12:00:00',
            'source': 'Test Feed',
            'feed_url': 'https://example.com/feed',
            'feed_name': 'Test Feed',
            'category': 'research',
            'author': 'Test Author',
            'tags': ['ai', 'security'],
            'priority': 'high'
        },
        {
            'title': 'ML-based Malware Detection',
            'link': 'https://example.com/article2',
            'description': 'Machine learning approach to malware analysis',
            'published': '2026-02-14T10:00:00',
            'source': 'Test Feed',
            'feed_url': 'https://example.com/feed',
            'feed_name': 'Test Feed',
            'category': 'research',
            'author': 'Test Author',
            'tags': ['ml', 'malware'],
            'priority': 'high'
        }
    ]
    
    # Mock the RSS feed fetching to return our test data
    with patch.object(rss_manager, 'fetch_all_feeds', return_value=test_entries):
        with patch.object(rss_manager, 'filter_by_date', return_value=test_entries):
            with patch.object(rss_manager, 'filter_by_keywords', return_value=test_entries):
                
                # Configuration
                config = {
                    'rss_feeds': [{'url': 'https://example.com/feed', 'name': 'Test Feed'}],
                    'search_keywords': ['AI', 'security', 'malware'],
                    'llm_assessment': {
                        'enabled': True,
                        'model': 'gpt-4o-mini',
                        'applicability_threshold': 0.6,
                        'credibility_threshold': 0.5,
                        'filter_inapplicable': False,  # Don't filter to see all results
                        'filter_not_credible': False
                    }
                }
                
                # First run - should make LLM calls
                print("\n1. First run (no cache)...")
                llm_call_count = 0
                results1 = search_rss_feeds(
                    rss_manager=rss_manager,
                    assess_credibility_func=assess_source_credibility,
                    config=config,
                    openai_client=mock_client
                )
                first_run_calls = llm_call_count
                print(f"✓ First run completed")
                print(f"  - Articles processed: {len(results1)}")
                print(f"  - LLM calls made: {first_run_calls}")
                # 1 call for title filtering + 2 per article (applicability + credibility)
                expected_calls = 1 + (len(test_entries) * 2)
                print(f"  - Expected calls: {expected_calls} (1 title filter + {len(test_entries) * 2} assessments)")
                
                # Verify LLM was called for title filtering and each article (applicability + credibility)
                assert first_run_calls == expected_calls, \
                    f"Expected {expected_calls} LLM calls, got {first_run_calls}"
                
                # Second run - should use cache, no new LLM calls
                print("\n2. Second run (with cache)...")
                llm_call_count = 0
                results2 = search_rss_feeds(
                    rss_manager=rss_manager,
                    assess_credibility_func=assess_source_credibility,
                    config=config,
                    openai_client=mock_client
                )
                second_run_calls = llm_call_count
                print(f"✓ Second run completed")
                print(f"  - Articles processed: {len(results2)}")
                print(f"  - LLM calls made: {second_run_calls}")
                print(f"  - Expected: 1 (title filter only, assessments cached)")
                print(f"  - Assessment cache hits: {len(test_entries)}")
                
                # Verify only title filtering call was made (assessments from cache)
                assert second_run_calls == 1, \
                    f"Expected 1 LLM call (title filter only), got {second_run_calls}"
                
                # Verify results are the same
                assert len(results1) == len(results2), \
                    "Results should be the same with and without cache"
                
                # Verify LLM assessment data is present in both runs
                for r1, r2 in zip(results1, results2):
                    assert r1['llm_applicability_score'] == r2['llm_applicability_score']
                    assert r1['llm_credibility_score'] == r2['llm_credibility_score']
                
                print("\n3. Testing cache with new article...")
                # Add a new article
                new_entry = {
                    'title': 'New Security Research',
                    'link': 'https://example.com/article3',
                    'description': 'Latest security research',
                    'published': '2026-02-15T12:00:00',
                    'source': 'Test Feed',
                    'feed_url': 'https://example.com/feed',
                    'feed_name': 'Test Feed',
                    'category': 'research',
                    'author': 'Test Author',
                    'tags': ['security'],
                    'priority': 'high'
                }
                
                test_entries_with_new = test_entries + [new_entry]
                
                with patch.object(rss_manager, 'fetch_all_feeds', return_value=test_entries_with_new):
                    with patch.object(rss_manager, 'filter_by_date', return_value=test_entries_with_new):
                        with patch.object(rss_manager, 'filter_by_keywords', return_value=test_entries_with_new):
                            llm_call_count = 0
                            results3 = search_rss_feeds(
                                rss_manager=rss_manager,
                                assess_credibility_func=assess_source_credibility,
                                config=config,
                                openai_client=mock_client
                            )
                            third_run_calls = llm_call_count
                            print(f"✓ Third run completed")
                            print(f"  - Articles processed: {len(results3)}")
                            print(f"  - LLM calls made: {third_run_calls}")
                            print(f"  - Expected: 3 (1 title filter + 2 for new article)")
                            
                            # Should make title filter call + calls for the new article only
                            assert third_run_calls == 3, \
                                f"Expected 3 LLM calls (1 title filter + 2 for new article), got {third_run_calls}"
    
    print("\n" + "=" * 60)
    print("All caching tests passed! ✓")
    print("\nSummary:")
    print(f"  - First run: {first_run_calls} LLM calls")
    print(f"  - Second run: {second_run_calls} LLM calls ({first_run_calls - second_run_calls - 1} assessments cached)")
    print(f"  - Third run: {third_run_calls} LLM calls (2 old assessments cached)")
    print(f"  - Total assessment calls saved: {(first_run_calls - 1) + (first_run_calls - second_run_calls - 1)}")


if __name__ == '__main__':
    test_llm_cache_reduces_calls()
