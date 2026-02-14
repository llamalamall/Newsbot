"""
RSS feed search functionality.
Searches and aggregates content from RSS feeds.
"""

import logging
from typing import List, Dict, Any, Optional

# Import dataclass models
try:
    from ..models import RSSResult
except ImportError:
    # Fallback for direct execution
    import sys
    import os
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    from models import RSSResult


def search_rss_feeds(
    rss_manager,
    assess_credibility_func,
    config: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Search and aggregate content from RSS feeds.
    
    This method fetches all configured RSS feeds, filters them by date
    and keywords, and returns relevant articles.
    
    Args:
        rss_manager: RSSFeedManager instance
        assess_credibility_func: Function to assess URL credibility
        config: Configuration dictionary
        
    Returns:
        List of relevant RSS feed entries
    """
    results = []
    
    if not rss_manager:
        logging.info("RSS Feed Manager not initialized, skipping RSS search")
        return results
    
    try:
        logging.info("Fetching RSS feeds...")
        
        # Get RSS feed configuration
        feeds = config.get('rss_feeds', [])
        if not feeds:
            logging.warning("No RSS feeds configured")
            return results
        
        # Get RSS settings
        rss_settings = config.get('rss_settings', {})
        max_age_days = rss_settings.get('max_age_days', config.get('days_back', 7))
        min_keyword_matches = rss_settings.get('min_keyword_matches', 1)
        
        # Fetch all feeds
        all_entries = rss_manager.fetch_all_feeds(feeds)
        
        # Filter by date
        recent_entries = rss_manager.filter_by_date(all_entries, max_age_days)
        
        # Filter by keywords
        keywords = config.get('search_keywords', [])
        if keywords:
            filtered_entries = rss_manager.filter_by_keywords(
                recent_entries,
                keywords,
                min_keyword_matches
            )
        else:
            filtered_entries = recent_entries
        
        # Convert to NewsBot result format
        for entry in filtered_entries:
            result = RSSResult(
                title=entry.get('title', 'Untitled'),
                url=entry.get('link', ''),
                description=entry.get('description', ''),
                source='rss',
                published=entry.get('published'),
                feed_name=entry.get('feed_name', 'Unknown Feed'),
                feed_category=entry.get('category'),
                priority=entry.get('priority', 'medium'),
                keyword_matches=entry.get('keyword_matches', 0),
                author=entry.get('author'),
                tags=entry.get('tags', [])
            )
            
            # Assess source credibility
            if result.url:
                result.credibility = assess_credibility_func(result.url)
            
            results.append(result.to_dict())
        
        logging.info(f"Found {len(results)} relevant articles from RSS feeds")
        
    except Exception as e:
        logging.error(f"Error in RSS feed search: {str(e)}")
    
    return results
