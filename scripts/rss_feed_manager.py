#!/usr/bin/env python3
"""
RSS Feed Manager for Newsbot.
Handles fetching, parsing, and caching of RSS/Atom feeds.
"""

import json
import logging
import os
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Set
from urllib.parse import urlparse
import feedparser
from dateutil import parser as date_parser


class RSSFeedManager:
    """Manages RSS/Atom feed fetching, parsing, and caching.
    
    This class handles all RSS feed operations including fetching feeds,
    parsing entries, filtering by date, and basic caching to reduce
    network calls.
    
    Attributes:
        timeout: Request timeout in seconds
        cache_enabled: Whether to cache feed results
        cache_ttl_hours: Cache time-to-live in hours
        rate_limit_delay: Delay between feed requests in seconds
    """
    
    # User-Agent for RSS feed requests
    USER_AGENT = 'Newsbot/1.0 (Security News Aggregator; +https://github.com/llamalamall/Newsbot)'
    
    def __init__(
        self,
        timeout: int = 10,
        cache_enabled: bool = True,
        cache_ttl_hours: int = 6,
        rate_limit_delay: float = 0.5,
        cache_dir: str = "cache"
    ):
        """Initialize the RSS Feed Manager.
        
        Args:
            timeout: Request timeout in seconds (default: 10)
            cache_enabled: Enable caching of feed results (default: True)
            cache_ttl_hours: Cache TTL in hours (default: 6)
            rate_limit_delay: Delay between requests (default: 0.5 seconds)
            cache_dir: Directory for persistent cache files (default: "cache")
        """
        self.timeout = timeout
        self.cache_enabled = cache_enabled
        self.cache_ttl_hours = cache_ttl_hours
        self.rate_limit_delay = rate_limit_delay
        self.cache_dir = cache_dir
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._last_request_time = 0
        self._seen_articles: Set[str] = set()
        self._seen_articles_file = os.path.join(cache_dir, "seen_articles.json")
        
        # Create cache directory if it doesn't exist
        if self.cache_enabled and cache_dir:
            os.makedirs(cache_dir, exist_ok=True)
            self._load_seen_articles()
        
        # Configure feedparser
        feedparser.USER_AGENT = self.USER_AGENT
    
    def _load_seen_articles(self):
        """Load previously seen articles from persistent storage."""
        if not os.path.exists(self._seen_articles_file):
            logging.debug("No existing seen articles cache found")
            return
        
        try:
            with open(self._seen_articles_file, 'r') as f:
                data = json.load(f)
                # Convert list back to set and filter old entries
                # Keep articles seen within the last N days, where N is at least 30 days
                # or 7x the cache TTL (whichever is larger). This ensures we don't re-report
                # articles too frequently while allowing old entries to expire eventually.
                cutoff_days = max(30, (self.cache_ttl_hours // 24) * 7)  # At least 30 days
                cutoff_date = datetime.now() - timedelta(days=cutoff_days)
                self._seen_articles = set()
                
                for entry in data:
                    # Entry format: {"url": "...", "seen_at": "..."}
                    if isinstance(entry, dict):
                        url = entry.get('url')
                        seen_at_str = entry.get('seen_at')
                        if url and seen_at_str:
                            try:
                                # Parse ISO format date string
                                # Replace 'Z' with '+00:00' for compatibility with fromisoformat()
                                # which doesn't accept 'Z' as timezone indicator prior to Python 3.11
                                seen_at = datetime.fromisoformat(seen_at_str.replace('Z', '+00:00'))
                                # Make timezone-naive for comparison
                                if seen_at.tzinfo:
                                    seen_at = seen_at.replace(tzinfo=None)
                                
                                if seen_at >= cutoff_date:
                                    self._seen_articles.add(url)
                                else:
                                    logging.debug(f"Skipping old seen article from {seen_at}: {url[:50]}...")
                            except (ValueError, TypeError) as e:
                                # Skip invalid dates but log them
                                logging.debug(f"Could not parse date '{seen_at_str}': {str(e)}")
                                continue
                    elif isinstance(entry, str):
                        # Legacy format: just URLs - always keep these
                        self._seen_articles.add(entry)
                
                logging.info(f"Loaded {len(self._seen_articles)} previously seen articles (cutoff: {cutoff_days} days)")
        except (json.JSONDecodeError, IOError) as e:
            logging.warning(f"Could not load seen articles cache: {str(e)}")
            self._seen_articles = set()
    
    def _save_seen_articles(self):
        """Save seen articles to persistent storage."""
        if not self.cache_enabled or not self.cache_dir:
            return
        
        try:
            # Save as list of dicts with metadata
            data = [
                {
                    'url': url,
                    'seen_at': datetime.now().isoformat()
                }
                for url in self._seen_articles
            ]
            
            with open(self._seen_articles_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            logging.debug(f"Saved {len(self._seen_articles)} seen articles to cache")
        except IOError as e:
            logging.warning(f"Could not save seen articles cache: {str(e)}")
    
    def _mark_article_as_seen(self, url: str):
        """Mark an article URL as seen.
        
        Args:
            url: Article URL to mark as seen
        """
        if url and self.cache_enabled:
            self._seen_articles.add(url)
    
    def _is_article_seen(self, url: str) -> bool:
        """Check if an article has been seen before.
        
        Args:
            url: Article URL to check
            
        Returns:
            True if article was previously seen, False otherwise
        """
        return url in self._seen_articles if url else False
    
    def _rate_limit(self):
        """Apply rate limiting to prevent overwhelming feed servers."""
        if self.rate_limit_delay > 0:
            elapsed = time.time() - self._last_request_time
            if elapsed < self.rate_limit_delay:
                time.sleep(self.rate_limit_delay - elapsed)
        self._last_request_time = time.time()
    
    def _is_cache_valid(self, url: str) -> bool:
        """Check if cached feed data is still valid.
        
        Args:
            url: Feed URL
            
        Returns:
            True if cache is valid, False otherwise
        """
        if not self.cache_enabled or url not in self._cache:
            return False
        
        cached_data = self._cache[url]
        cache_time = cached_data.get('cached_at')
        
        if not cache_time:
            return False
        
        cache_age = datetime.now() - cache_time
        max_age = timedelta(hours=self.cache_ttl_hours)
        
        return cache_age < max_age
    
    def _parse_date(self, date_tuple: Any) -> Optional[datetime]:
        """Parse various date formats from feed entries.
        
        Args:
            date_tuple: Date from feedparser (can be struct_time, string, etc.)
            
        Returns:
            datetime object or None if parsing fails
        """
        if not date_tuple:
            return None
        
        try:
            # feedparser returns time.struct_time for parsed dates
            if hasattr(date_tuple, 'tm_year'):
                return datetime(
                    date_tuple.tm_year,
                    date_tuple.tm_mon,
                    date_tuple.tm_mday,
                    date_tuple.tm_hour,
                    date_tuple.tm_min,
                    date_tuple.tm_sec
                )
            # Try parsing as string
            elif isinstance(date_tuple, str):
                return date_parser.parse(date_tuple)
        except Exception as e:
            logging.debug(f"Could not parse date {date_tuple}: {str(e)}")
        
        return None
    
    def fetch_feed(
        self,
        feed_url: str,
        feed_name: str = None,
        category: str = None
    ) -> List[Dict[str, Any]]:
        """Fetch and parse a single RSS/Atom feed.
        
        Args:
            feed_url: URL of the RSS/Atom feed
            feed_name: Human-readable name for the feed (optional)
            category: Category/type of feed (e.g., 'official', 'research')
            
        Returns:
            List of parsed feed entries with metadata
        """
        # Check cache first
        if self._is_cache_valid(feed_url):
            logging.debug(f"Using cached data for {feed_url}")
            return self._cache[feed_url]['entries']
        
        entries = []
        
        try:
            logging.info(f"Fetching RSS feed: {feed_name or feed_url}")
            
            # Apply rate limiting
            self._rate_limit()
            
            # Parse the feed
            feed = feedparser.parse(
                feed_url,
                request_headers={'User-Agent': self.USER_AGENT}
            )
            
            # Check for feed errors
            if hasattr(feed, 'bozo') and feed.bozo:
                if hasattr(feed, 'bozo_exception'):
                    logging.warning(
                        f"Feed parse error for {feed_url}: {feed.bozo_exception}"
                    )
            
            # Extract feed metadata
            feed_title = feed.feed.get('title', feed_name or 'Unknown Feed')
            
            # Process each entry
            for entry in feed.entries:
                try:
                    # Extract publication date
                    pub_date = None
                    for date_field in ['published_parsed', 'updated_parsed', 'created_parsed']:
                        if hasattr(entry, date_field):
                            pub_date = self._parse_date(getattr(entry, date_field))
                            if pub_date:
                                break
                    
                    # If no parsed date, try string dates
                    if not pub_date:
                        for date_field in ['published', 'updated', 'created']:
                            if hasattr(entry, date_field):
                                pub_date = self._parse_date(getattr(entry, date_field))
                                if pub_date:
                                    break
                    
                    # Extract content/summary
                    description = ''
                    if hasattr(entry, 'summary'):
                        description = entry.summary
                    elif hasattr(entry, 'description'):
                        description = entry.description
                    elif hasattr(entry, 'content'):
                        # content is usually a list of dicts
                        if isinstance(entry.content, list) and len(entry.content) > 0:
                            description = entry.content[0].get('value', '')
                    
                    # Build entry dict
                    parsed_entry = {
                        'title': entry.get('title', 'Untitled'),
                        'link': entry.get('link', ''),
                        'description': description,
                        'published': pub_date.isoformat() if pub_date else None,
                        'source': feed_title,
                        'feed_url': feed_url,
                        'feed_name': feed_name or feed_title,
                        'category': category,
                        'author': entry.get('author', None),
                        'tags': [tag.get('term', '') for tag in entry.get('tags', [])]
                    }
                    
                    # Skip if article was already seen (deduplication)
                    article_url = parsed_entry.get('link', '')
                    if article_url and self._is_article_seen(article_url):
                        logging.debug(f"Skipping already seen article: {article_url}")
                        continue
                    
                    entries.append(parsed_entry)
                    
                    # Mark article as seen
                    if article_url:
                        self._mark_article_as_seen(article_url)
                    
                except Exception as e:
                    logging.debug(f"Error parsing entry from {feed_url}: {str(e)}")
                    continue
            
            # Cache the results
            if self.cache_enabled and entries:
                self._cache[feed_url] = {
                    'entries': entries,
                    'cached_at': datetime.now()
                }
            
            logging.info(f"Fetched {len(entries)} entries from {feed_title}")
            
        except Exception as e:
            logging.error(f"Error fetching feed {feed_url}: {str(e)}")
        
        return entries
    
    def fetch_all_feeds(
        self,
        feeds: List[Dict[str, str]],
        max_parallel: int = 5
    ) -> List[Dict[str, Any]]:
        """Fetch multiple RSS feeds.
        
        Args:
            feeds: List of feed configs with 'url', 'name', and optional 'category'
            max_parallel: Maximum feeds to fetch in parallel (not implemented yet)
            
        Returns:
            Combined list of all entries from all feeds
        """
        all_entries = []
        
        for feed_config in feeds:
            url = feed_config.get('url')
            name = feed_config.get('name')
            category = feed_config.get('category')
            priority = feed_config.get('priority')
            
            if not url:
                logging.warning(f"Feed config missing URL: {feed_config}")
                continue
            
            try:
                entries = self.fetch_feed(url, name, category)
                
                # Add priority to each entry
                for entry in entries:
                    entry['priority'] = priority
                
                all_entries.extend(entries)
                
            except Exception as e:
                logging.error(f"Error fetching feed {name or url}: {str(e)}")
                continue
        
        logging.info(f"Fetched total of {len(all_entries)} entries from {len(feeds)} feeds")
        
        # Save seen articles to persistent storage after fetching all feeds
        self._save_seen_articles()
        
        return all_entries
    
    def filter_by_date(
        self,
        entries: List[Dict[str, Any]],
        days_back: int = 7
    ) -> List[Dict[str, Any]]:
        """Filter entries to only include recent articles.
        
        Args:
            entries: List of feed entries
            days_back: Number of days to look back (default: 7)
            
        Returns:
            Filtered list of entries within date range
        """
        if days_back <= 0:
            return entries
        
        cutoff_date = datetime.now() - timedelta(days=days_back)
        filtered = []
        
        for entry in entries:
            pub_date_str = entry.get('published')
            
            if not pub_date_str:
                # If no date, include it (better to have false positives)
                filtered.append(entry)
                continue
            
            try:
                # Parse ISO format date string
                if isinstance(pub_date_str, str):
                    pub_date = datetime.fromisoformat(pub_date_str.replace('Z', '+00:00'))
                    # Make timezone-naive for comparison
                    if pub_date.tzinfo:
                        pub_date = pub_date.replace(tzinfo=None)
                    
                    if pub_date >= cutoff_date:
                        filtered.append(entry)
                else:
                    # If not string, include it
                    filtered.append(entry)
                    
            except Exception as e:
                logging.debug(f"Error filtering by date: {str(e)}")
                # Include entry if we can't parse date
                filtered.append(entry)
        
        logging.info(f"Filtered {len(entries)} entries to {len(filtered)} within last {days_back} days")
        return filtered
    
    def filter_by_keywords(
        self,
        entries: List[Dict[str, Any]],
        keywords: List[str],
        min_matches: int = 1
    ) -> List[Dict[str, Any]]:
        """Filter entries by keyword relevance.
        
        Args:
            entries: List of feed entries
            keywords: List of keywords to match
            min_matches: Minimum number of keyword matches required
            
        Returns:
            Filtered list of entries matching keywords
        """
        if not keywords:
            return entries
        
        filtered = []
        
        for entry in entries:
            # Combine title, description, and tags for matching
            text = ' '.join([
                entry.get('title', ''),
                entry.get('description', ''),
                ' '.join(entry.get('tags', []))
            ]).lower()
            
            # Count keyword matches
            matches = sum(1 for keyword in keywords if keyword.lower() in text)
            
            if matches >= min_matches:
                entry['keyword_matches'] = matches
                filtered.append(entry)
        
        # Sort by number of matches (descending)
        filtered.sort(key=lambda x: x.get('keyword_matches', 0), reverse=True)
        
        logging.info(
            f"Filtered {len(entries)} entries to {len(filtered)} "
            f"matching {min_matches}+ keywords"
        )
        return filtered
    
    def is_feed_healthy(self, feed_url: str) -> bool:
        """Check if a feed is accessible and parseable.
        
        Args:
            feed_url: URL of the feed to check
            
        Returns:
            True if feed is healthy, False otherwise
        """
        try:
            feed = feedparser.parse(feed_url)
            
            # Check for critical errors
            if hasattr(feed, 'bozo') and feed.bozo:
                # Some bozo errors are acceptable (minor parsing issues)
                if hasattr(feed, 'bozo_exception'):
                    exception_type = type(feed.bozo_exception).__name__
                    # Only fail on critical errors
                    if exception_type in ['URLError', 'HTTPError', 'Timeout']:
                        return False
            
            # Check if we got any entries
            if not hasattr(feed, 'entries') or len(feed.entries) == 0:
                return False
            
            return True
            
        except Exception as e:
            logging.debug(f"Feed health check failed for {feed_url}: {str(e)}")
            return False
    
    def clear_cache(self, clear_seen_articles: bool = False):
        """Clear all cached feed data.
        
        Args:
            clear_seen_articles: If True, also clear the persistent seen articles cache
        """
        self._cache.clear()
        logging.info("Feed cache cleared")
        
        if clear_seen_articles:
            self._seen_articles.clear()
            if os.path.exists(self._seen_articles_file):
                try:
                    os.remove(self._seen_articles_file)
                    logging.info("Seen articles cache cleared")
                except OSError as e:
                    logging.warning(f"Could not remove seen articles file: {str(e)}")


def main():
    """Command-line interface for RSS feed manager."""
    import sys
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )
    
    if len(sys.argv) < 2:
        print("Usage: python rss_feed_manager.py <feed_url>")
        print("\nExample:")
        print("  python rss_feed_manager.py https://www.cisa.gov/cybersecurity-advisories/all.xml")
        sys.exit(1)
    
    feed_url = sys.argv[1]
    
    # Create manager
    manager = RSSFeedManager()
    
    # Fetch feed
    print(f"\nFetching feed: {feed_url}\n")
    entries = manager.fetch_feed(feed_url)
    
    # Display results
    print(f"Found {len(entries)} entries:\n")
    
    for i, entry in enumerate(entries[:10], 1):  # Show first 10
        print(f"{i}. {entry['title']}")
        print(f"   Published: {entry['published']}")
        print(f"   Link: {entry['link']}")
        if entry.get('description'):
            desc = entry['description'][:100] + '...' if len(entry['description']) > 100 else entry['description']
            print(f"   Description: {desc}")
        print()
    
    if len(entries) > 10:
        print(f"... and {len(entries) - 10} more entries")


if __name__ == '__main__':
    main()
