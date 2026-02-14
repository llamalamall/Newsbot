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
import re
from datetime import datetime
from typing import List, Dict, Any, Optional
from openai import OpenAI

# Import utility modules (try both absolute and relative imports for compatibility)
try:
    from scripts.utils.credibility import assess_source_credibility, CREDIBLE_SOURCES
    from scripts.utils.content_extractor import extract_article_content, MAX_ARTICLE_CONTENT_LENGTH
    from scripts.searchers.github_search import search_github_repos
    from scripts.searchers.web_search import search_with_llm, perform_web_search, search_with_web_context
    from scripts.searchers.web_search import LLM_SUMMARY_PROMPT, MAX_CONTEXT_SNIPPET_LENGTH
    from scripts.searchers.rss_search import search_rss_feeds
    from scripts.reporters.markdown_reporter import generate_report, save_json_results
except ImportError:
    # Fallback to relative imports when scripts is in sys.path
    from utils.credibility import assess_source_credibility, CREDIBLE_SOURCES
    from utils.content_extractor import extract_article_content, MAX_ARTICLE_CONTENT_LENGTH
    from searchers.github_search import search_github_repos
    from searchers.web_search import search_with_llm, perform_web_search, search_with_web_context
    from searchers.web_search import LLM_SUMMARY_PROMPT, MAX_CONTEXT_SNIPPET_LENGTH
    from searchers.rss_search import search_rss_feeds
    from reporters.markdown_reporter import generate_report, save_json_results


class NewsBot:
    """Main class for searching and aggregating security news."""
    
    # Re-export constants for backward compatibility
    CREDIBLE_SOURCES = CREDIBLE_SOURCES
    LLM_SUMMARY_PROMPT = LLM_SUMMARY_PROMPT
    MAX_CONTEXT_SNIPPET_LENGTH = MAX_CONTEXT_SNIPPET_LENGTH
    MAX_ARTICLE_CONTENT_LENGTH = MAX_ARTICLE_CONTENT_LENGTH
    
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
    
    # Wrapper methods for backward compatibility
    def assess_source_credibility(self, url: str) -> str:
        """Assess the credibility of a news source (wrapper for backward compatibility)."""
        return assess_source_credibility(url)
    
    def extract_article_content(self, url: str) -> Optional[str]:
        """Extract main content from a web article (wrapper for backward compatibility)."""
        return extract_article_content(url)
    
    def perform_web_search(self, query: str) -> List[Dict[str, Any]]:
        """Perform a live web search (wrapper for backward compatibility)."""
        web_search_func = perform_web_search(self.config, assess_source_credibility)
        return web_search_func(query)
    
    def search_github_repos(self) -> List[Dict[str, Any]]:
        """Search GitHub for relevant repositories (wrapper for backward compatibility)."""
        return search_github_repos(self.github_token, self.config)
    
    def search_rss_feeds(self) -> List[Dict[str, Any]]:
        """Search RSS feeds (wrapper for backward compatibility)."""
        return search_rss_feeds(self.rss_manager, self.config, assess_source_credibility)
    
    def search_with_web_context(self, query: str) -> List[Dict[str, Any]]:
        """Search with web context (wrapper for backward compatibility)."""
        web_search_func = perform_web_search(self.config, assess_source_credibility)
        return search_with_web_context(
            query,
            web_search_func,
            assess_source_credibility,
            extract_article_content,
            self.openai_client
        )
    
    def search_with_llm(self, query: str) -> str:
        """Search with LLM (wrapper for backward compatibility)."""
        return search_with_llm(self.openai_client, query)
    
    def aggregate_news(self) -> List[Dict[str, Any]]:
        """Aggregate news from multiple sources including RSS feeds, GitHub, and web search."""
        logging.info("Aggregating news from multiple sources...")
        all_results = []
        
        # Determine content source mode
        content_source = self.config.get('content_source', 'dual')
        
        # Search GitHub repositories (always enabled)
        github_results = search_github_repos(self.github_token, self.config)
        all_results.extend(github_results)
        
        # RSS feed search (if enabled)
        if content_source in ['rss', 'dual'] and self.config.get('rss_enabled', False):
            rss_results = search_rss_feeds(
                self.rss_manager,
                self.config,
                assess_source_credibility
            )
            all_results.extend(rss_results)
        
        # Web search (if enabled and in dual or web mode)
        if content_source in ['web', 'dual'] and self.config.get('web_search_enabled', True):
            # Create web search function with config and credibility assessment
            web_search_func = perform_web_search(self.config, assess_source_credibility)
            
            # Enhanced search using web context for each topic
            for topic in self.config.get("search_topics", []):
                logging.info(f"Enhanced web search for: {topic}")
                
                try:
                    # Try the new web-enhanced search first
                    web_enhanced_results = search_with_web_context(
                        topic,
                        web_search_func,
                        assess_source_credibility,
                        extract_article_content,
                        self.openai_client
                    )
                    if web_enhanced_results:
                        all_results.extend(web_enhanced_results)
                    else:
                        # Fallback to original LLM-only search
                        logging.info(f"Falling back to LLM-only search for: {topic}")
                        llm_response = search_with_llm(self.openai_client, topic)
                        
                        if llm_response:
                            try:
                                # Try to parse JSON response
                                json_match = re.search(r'\[.*\]', llm_response, re.DOTALL)
                                if json_match:
                                    llm_results = json.loads(json_match.group())
                                    for item in llm_results:
                                        item["source"] = "llm_search"
                                        item["search_topic"] = topic
                                        all_results.append(item)
                            except json.JSONDecodeError:
                                # If not JSON, store as text summary
                                all_results.append({
                                    "title": f"Summary: {topic}",
                                    "description": llm_response,
                                    "source": "llm_summary",
                                    "search_topic": topic
                                })
                except Exception as e:
                    logging.error(f"Error processing topic '{topic}': {str(e)[:200]}")
                    # Continue with next topic even if one fails
                    continue
        
        self.results = all_results
        return all_results
    
    def generate_report(self, output_path: str = None) -> str:
        """Generate a markdown report of the findings with enhanced source citations.
        
        Args:
            output_path: Optional path to save the report
            
        Returns:
            Generated markdown report as a string
        """
        return generate_report(self.results, output_path)
    
    def save_json_results(self, output_path: str):
        """Save results as JSON.
        
        Args:
            output_path: Path to save the JSON file
        """
        save_json_results(self.results, output_path)


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
    
    bot.generate_report(markdown_path)
    bot.save_json_results(json_path)
    
    print()
    print("=" * 80)
    print("Newsbot completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
