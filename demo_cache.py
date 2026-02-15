#!/usr/bin/env python3
"""
Demonstration script showing LLM assessment cache in action.
Run this to see the difference between cached and uncached runs.
"""

import sys
import os
from datetime import datetime

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts'))

from rss_feed_manager import RSSFeedManager

def main():
    print("=" * 70)
    print("LLM Assessment Cache Demonstration")
    print("=" * 70)
    print()
    
    # Create manager with caching enabled
    manager = RSSFeedManager(
        cache_enabled=True,
        cache_ttl_hours=6
    )
    
    print("1. Simulating article assessments...")
    print("-" * 70)
    
    # Simulate some article URLs and their assessments
    articles = [
        {
            'url': 'https://example.com/ai-security-tool',
            'title': 'New AI-Powered Security Tool',
            'assessment': {
                'applicability': {
                    'applicable': True,
                    'score': 0.92,
                    'reason': 'Directly relates to AI in offensive security',
                    'matched_keywords': ['AI', 'security', 'automation']
                },
                'credibility': {
                    'credible': True,
                    'score': 0.85,
                    'reason': 'Published by reputable security research firm',
                    'flags': []
                }
            }
        },
        {
            'url': 'https://example.com/ml-malware-detection',
            'title': 'Machine Learning for Malware Detection',
            'assessment': {
                'applicability': {
                    'applicable': True,
                    'score': 0.88,
                    'reason': 'Covers ML application in security analysis',
                    'matched_keywords': ['machine learning', 'malware', 'analysis']
                },
                'credibility': {
                    'credible': True,
                    'score': 0.90,
                    'reason': 'Academic research from known institution',
                    'flags': []
                }
            }
        },
        {
            'url': 'https://example.com/automated-pentest',
            'title': 'Automated Penetration Testing Framework',
            'assessment': {
                'applicability': {
                    'applicable': True,
                    'score': 0.95,
                    'reason': 'Core topic: automation in penetration testing',
                    'matched_keywords': ['automation', 'penetration testing', 'red team']
                },
                'credibility': {
                    'credible': True,
                    'score': 0.88,
                    'reason': 'Open source project with good documentation',
                    'flags': []
                }
            }
        }
    ]
    
    # First run - cache the assessments
    print("\nFIRST RUN (populating cache):")
    print()
    for i, article in enumerate(articles, 1):
        url = article['url']
        title = article['title']
        assessment = article['assessment']
        
        # Set cache
        manager.set_llm_assessment_cache(url, assessment)
        print(f"  {i}. Cached: {title}")
        print(f"     - Applicability: {assessment['applicability']['score']:.2f}")
        print(f"     - Credibility: {assessment['credibility']['score']:.2f}")
    
    print("\n" + "-" * 70)
    print("\n2. Retrieving from cache...")
    print("-" * 70)
    
    # Second run - retrieve from cache
    print("\nSECOND RUN (using cache):")
    print()
    cache_hits = 0
    for i, article in enumerate(articles, 1):
        url = article['url']
        title = article['title']
        
        # Get from cache
        cached = manager.get_llm_assessment_cache(url)
        
        if cached:
            cache_hits += 1
            print(f"  {i}. ✓ Cache hit: {title}")
            print(f"     - Applicability: {cached['applicability']['score']:.2f} (from cache)")
            print(f"     - Credibility: {cached['credibility']['score']:.2f} (from cache)")
        else:
            print(f"  {i}. ✗ Cache miss: {title}")
    
    print("\n" + "-" * 70)
    print("\n3. Cache Statistics")
    print("-" * 70)
    print()
    print(f"  Articles processed: {len(articles)}")
    print(f"  Cache hits: {cache_hits}")
    print(f"  Cache hit rate: {(cache_hits/len(articles)*100):.1f}%")
    print(f"  LLM calls saved: {cache_hits * 2} (2 per article)")
    print()
    print("  Impact: In a real scenario, this would save {0} LLM API calls".format(cache_hits * 2))
    print("          and reduce processing time significantly.")
    
    print("\n" + "-" * 70)
    print("\n4. Testing new article (cache miss)")
    print("-" * 70)
    print()
    
    new_article = {
        'url': 'https://example.com/brand-new-article',
        'title': 'Brand New Security Research'
    }
    
    cached = manager.get_llm_assessment_cache(new_article['url'])
    if cached:
        print(f"  ✓ Cache hit for new article (unexpected!)")
    else:
        print(f"  ✗ Cache miss for new article (expected)")
        print(f"     This article would trigger fresh LLM assessment")
    
    print("\n" + "=" * 70)
    print("Demonstration Complete")
    print("=" * 70)
    print()
    print("KEY TAKEAWAY:")
    print("  With caching enabled, previously analyzed articles are retrieved")
    print("  from cache instead of making expensive LLM API calls.")
    print("  This provides significant cost savings and performance improvement.")
    print()

if __name__ == '__main__':
    main()
