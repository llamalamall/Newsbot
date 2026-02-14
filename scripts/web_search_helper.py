#!/usr/bin/env python3
"""
Web search helper module for Newsbot.
This module provides web search functionality that can be integrated with the main bot.
"""

import os
import sys
import json
import logging
import time
import re
from typing import List, Dict, Any, Optional
from urllib.parse import quote_plus, urlparse
import requests
from bs4 import BeautifulSoup


class WebSearchHelper:
    """Helper class for performing web searches and processing results.
    
    This class implements web search functionality using DuckDuckGo's HTML interface,
    which doesn't require API keys. Results are parsed and formatted for use in the
    NewsBot pipeline.
    
    Attributes:
        search_enabled: Whether web search functionality is enabled
        timeout: Request timeout in seconds
        user_agent: User agent string for requests
        rate_limit_delay: Delay between requests in seconds
    """
    
    def __init__(self, timeout: int = 10, rate_limit_delay: float = 1.0):
        """Initialize the web search helper.
        
        Args:
            timeout: Request timeout in seconds (default: 10)
            rate_limit_delay: Delay between requests in seconds (default: 1.0)
        """
        self.search_enabled = True
        self.timeout = timeout
        self.rate_limit_delay = rate_limit_delay
        self.user_agent = (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )
        self._last_request_time = 0
        
    def _rate_limit(self):
        """Apply rate limiting to prevent overwhelming the search service."""
        current_time = time.time()
        time_since_last_request = current_time - self._last_request_time
        if time_since_last_request < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - time_since_last_request)
        self._last_request_time = time.time()
        
    def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Perform a web search and return results.
        
        This method uses DuckDuckGo's HTML search to find relevant content.
        It doesn't require API keys and respects rate limiting.
        
        Args:
            query: The search query
            max_results: Maximum number of results to return (default: 10)
            
        Returns:
            List of search results with title, url, and snippet. Each result is a dict with:
                - title: Page title
                - url: URL of the result
                - snippet: Brief description/snippet from the search result
        """
        results = []
        
        try:
            logging.info(f"Performing web search for: {query}")
            
            # Apply rate limiting
            self._rate_limit()
            
            # Encode query for URL
            encoded_query = quote_plus(query)
            
            # DuckDuckGo HTML search URL
            search_url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
            
            # Make request with appropriate headers
            headers = {
                'User-Agent': self.user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            
            response = requests.get(
                search_url,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            # Parse the HTML response
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all search result elements
            # DuckDuckGo HTML uses div elements with class 'result'
            result_divs = soup.find_all('div', class_='result')
            
            for result_div in result_divs[:max_results]:
                try:
                    # Extract title and URL from the result link
                    title_link = result_div.find('a', class_='result__a')
                    if not title_link:
                        continue
                        
                    title = title_link.get_text(strip=True)
                    url = title_link.get('href', '')
                    
                    # Extract snippet/description
                    snippet_elem = result_div.find('a', class_='result__snippet')
                    snippet = snippet_elem.get_text(strip=True) if snippet_elem else ''
                    
                    # Clean up URL (DuckDuckGo sometimes uses redirect URLs)
                    url = self.clean_url(url)
                    
                    if url and title:
                        results.append({
                            'title': title,
                            'url': url,
                            'snippet': snippet
                        })
                        
                except Exception as e:
                    logging.debug(f"Error parsing search result: {str(e)}")
                    continue
            
            logging.info(f"Found {len(results)} search results for: {query}")
            return results
            
        except requests.RequestException as e:
            logging.error(f"Web search request error: {str(e)}")
            return []
        except Exception as e:
            logging.error(f"Web search error: {str(e)}")
            return []
    
    def clean_url(self, url: str) -> str:
        """Clean and validate a URL from search results.
        
        Args:
            url: URL to clean
            
        Returns:
            Cleaned URL or empty string if invalid
        """
        if not url:
            return ''
            
        # Remove DuckDuckGo redirect prefix if present
        if url.startswith('//'):
            url = 'https:' + url
        
        # Basic URL validation
        try:
            parsed = urlparse(url)
            if parsed.scheme in ('http', 'https') and parsed.netloc:
                return url
        except Exception:
            pass
            
        return ''
    
    def is_available(self) -> bool:
        """Check if web search is available.
        
        Returns:
            True if web search is enabled and can be used
        """
        return self.search_enabled


def main():
    """Command-line interface for web search helper."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Web Search Helper for Newsbot')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--max-results', type=int, default=10, 
                        help='Maximum number of results (default: 10)')
    parser.add_argument('--json', action='store_true',
                        help='Output results as JSON')
    
    args = parser.parse_args()
    
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # Perform search
    helper = WebSearchHelper()
    results = helper.search(args.query, args.max_results)
    
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"\nSearch results for: {args.query}\n")
        print(f"Found {len(results)} results\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result.get('title', 'No title')}")
            print(f"   {result.get('url', 'No URL')}")
            print(f"   {result.get('snippet', 'No snippet')}\n")


if __name__ == '__main__':
    main()
