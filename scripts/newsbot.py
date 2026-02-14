#!/usr/bin/env python3
"""
Newsbot - AI-powered offensive security news aggregator
Searches for the latest articles, announcements, repositories, and blog posts
related to AI and automation in offensive security.
"""

import os
import json
import sys
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
from openai import OpenAI
import re

# Import from new modular structure
# Use try-except to handle both direct execution and module import
try:
    from .utils.credibility import assess_source_credibility, CREDIBLE_SOURCES
    from .utils.content_extractor import extract_article_content
    from .searchers.github_search import search_github_repos
    from .searchers.web_search import (
        search_with_web_context, search_with_llm, LLM_SUMMARY_PROMPT, perform_web_search
    )
    from .searchers.rss_search import search_rss_feeds
    from .reporters.markdown_reporter import generate_report, save_json_results
except ImportError:
    # Fallback for direct execution
    import sys
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    from utils.credibility import assess_source_credibility, CREDIBLE_SOURCES
    from utils.content_extractor import extract_article_content
    from searchers.github_search import search_github_repos
    from searchers.web_search import (
        search_with_web_context, search_with_llm, LLM_SUMMARY_PROMPT, perform_web_search
    )
    from searchers.rss_search import search_rss_feeds
    from reporters.markdown_reporter import generate_report, save_json_results

__all__ = ['NewsBot', 'main']

class NewsBot:
    """Main class for searching and aggregating security news."""
    
    # Expose constants for backward compatibility
    LLM_SUMMARY_PROMPT = LLM_SUMMARY_PROMPT
    CREDIBLE_SOURCES = CREDIBLE_SOURCES
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the NewsBot with configuration."""
        self.config = self.load_config(config_path)
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.results = []
        self.web_search_available = True  # Track if web search is available
        
        # Initialize RSS Feed Manager if enabled
        self.rss_manager = None
        if self.config.get('rss_enabled', False):
            try:
                from rss_feed_manager import RSSFeedManager
                rss_settings = self.config.get('rss_settings', {})
                self.rss_manager = RSSFeedManager(
                    timeout=rss_settings.get('request_timeout', 10),
                    cache_enabled=rss_settings.get('cache_enabled', True),
                    cache_ttl_hours=rss_settings.get('cache_ttl_hours', 6),
                    rate_limit_delay=rss_settings.get('rate_limit_delay', 0.5)
                )
                logging.info("RSS Feed Manager initialized")
            except Exception as e:
                logging.warning(f"Could not initialize RSS Feed Manager: {str(e)}")
                self.rss_manager = None
        
        # Initialize OpenAI client if token is available
        if self.github_token:
            self.openai_client = OpenAI(
                base_url="https://models.inference.ai.azure.com",
                api_key=self.github_token
            )
        else:
            self.openai_client = None

    def load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        with open(config_path, 'r') as f:
            return json.load(f)
    
    # Backward compatibility wrapper methods
    def assess_source_credibility(self, url: str) -> str:
        """Assess the credibility of a news source based on its domain.
        
        Args:
            url: The URL to assess
            
        Returns:
            'high', 'medium', or 'low' credibility rating
        """
        return assess_source_credibility(url)
    
    def extract_article_content(self, url: str) -> Optional[str]:
        """Extract main content from a web article.
        
        Args:
            url: URL of the article
            
        Returns:
            Extracted text content or None if extraction fails
        """
        return extract_article_content(url)

    def perform_web_search(self, query: str):
        """Perform a live web search for the given query.
        
        Args:
            query: Search query string
            
        Returns:
            List of search results with title, url, snippet, and credibility
        """
        return perform_web_search(query, assess_source_credibility, self.config)
    
    def search_with_web_context(self, query: str):
        """Search using both web search and LLM with full context integration.
        
        Args:
            query: The search topic/query
            
        Returns:
            List of processed and enriched results
        """
        return search_with_web_context(
            query=query,
            openai_client=self.openai_client,
            assess_credibility_func=assess_source_credibility,
            extract_content_func=extract_article_content,
            config=self.config
        )
    
    def _process_web_search_topic(self, topic: str) -> List[Dict[str, Any]]:
        """Process a single web search topic with fallback to LLM-only search.
        
        Args:
            topic: Search topic/query
            
        Returns:
            List of results for the topic
        """
        results = []
        logging.info(f"Enhanced web search for: {topic}")
        
        try:
            # Try the new web-enhanced search first
            web_enhanced_results = search_with_web_context(
                query=topic,
                openai_client=self.openai_client,
                assess_credibility_func=assess_source_credibility,
                extract_content_func=extract_article_content,
                config=self.config
            )
            if web_enhanced_results:
                results.extend(web_enhanced_results)
            else:
                # Fallback to original LLM-only search
                results.extend(self._fallback_llm_search(topic))
        except Exception as e:
            logging.error(f"Error processing topic '{topic}': {str(e)[:200]}")
            # Continue with next topic even if one fails
        
        return results

    def _fallback_llm_search(self, topic: str) -> List[Dict[str, Any]]:
        """Fallback to LLM-only search when web search returns no results.
        
        Args:
            topic: Search topic/query
            
        Returns:
            List of results from LLM search
        """
        results = []
        logging.info(f"Falling back to LLM-only search for: {topic}")
        llm_response = search_with_llm(topic, self.openai_client)
        
        if llm_response:
            try:
                # Try to parse JSON response
                json_match = re.search(r'\[.*\]', llm_response, re.DOTALL)
                if json_match:
                    llm_results = json.loads(json_match.group())
                    for item in llm_results:
                        item["source"] = "llm_search"
                        item["search_topic"] = topic
                        results.append(item)
            except json.JSONDecodeError:
                # If not JSON, store as text summary
                results.append({
                    "title": f"Summary: {topic}",
                    "description": llm_response,
                    "source": "llm_summary",
                    "search_topic": topic
                })
        
        return results

    def aggregate_news(self) -> List[Dict[str, Any]]:
        """Aggregate news from multiple sources including RSS feeds, GitHub, and web search."""
        logging.info("Aggregating news from multiple sources...")
        all_results = []
        
        # Determine content source mode
        content_source = self.config.get('content_source', 'dual')
        
        # Search GitHub repositories (always enabled)
        github_results = search_github_repos(
            github_token=self.github_token,
            github_topics=self.config.get("github_topics", []),
            days_back=self.config.get("days_back", 7),
            max_results_per_topic=self.config.get("max_results_per_topic", 10)
        )
        all_results.extend(github_results)
        
        # RSS feed search (if enabled)
        if content_source in ['rss', 'dual'] and self.config.get('rss_enabled', False):
            rss_results = search_rss_feeds(
                rss_manager=self.rss_manager,
                assess_credibility_func=assess_source_credibility,
                config=self.config
            )
            all_results.extend(rss_results)
        
        # Web search (if enabled and in dual or web mode)
        if content_source in ['web', 'dual'] and self.config.get('web_search_enabled', True):
            # Enhanced search using web context for each topic
            for topic in self.config.get("search_topics", []):
                topic_results = self._process_web_search_topic(topic)
                all_results.extend(topic_results)
        
        self.results = all_results
        return all_results


def main():
    """Main entry point."""
    # Configure logging at application level
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s', force=True)
    
    print("=" * 80)
    print("Newsbot - Offensive Security AI/Automation News Aggregator")
    print("=" * 80)
    print()
    
    # Check for required GITHUB_TOKEN
    has_github = bool(os.getenv("GITHUB_TOKEN"))
    
    if not has_github:
        print("Error: GITHUB_TOKEN environment variable not set")
        print("\nGITHUB_TOKEN is required for:")
        print("  - GitHub repository searches")
        print("  - LLM-based searches via GitHub Models")
        print("\nPlease set it:")
        print("  export GITHUB_TOKEN=your_token_here")
        sys.exit(1)
    
    print()
    
    # Initialize bot
    bot = NewsBot()
    
    # Aggregate news
    results = bot.aggregate_news()
    
    print()
    print(f"Total results found: {len(results)}")
    print()
    
    # Generate timestamp for filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Generate and save reports
    markdown_path = f"outputs/report_{timestamp}.md"
    json_path = f"outputs/results_{timestamp}.json"
    
    generate_report(results, markdown_path)
    save_json_results(results, json_path)
    
    print()
    print("=" * 80)
    print("Newsbot completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
