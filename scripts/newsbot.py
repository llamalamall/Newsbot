#!/usr/bin/env python3
"""
Newsbot - AI-powered offensive security news aggregator
Searches for the latest articles, announcements, repositories, and blog posts
related to AI and automation in offensive security.
"""

# Standard library
import argparse
import json
import logging
import os
import re
import sys
from datetime import datetime
from typing import List, Dict, Any, Optional

# Third-party
from openai import OpenAI

# Local
# Import from new modular structure
# Use try-except to handle both direct execution and module import
try:
    from .utils.credibility import assess_source_credibility, CREDIBLE_SOURCES
    from .utils.content_extractor import extract_article_content
    from .searchers.github_search import search_github_repos
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
    from searchers.rss_search import search_rss_feeds
    from reporters.markdown_reporter import generate_report, save_json_results

__all__ = ['NewsBot', 'main', 'parse_arguments']

class NewsBot:
    """Main class for searching and aggregating security news."""
    
    # Default values for RSS settings
    DEFAULT_RSS_TIMEOUT = 10  # seconds
    DEFAULT_RSS_CACHE_TTL_HOURS = 6  # hours
    DEFAULT_RSS_RATE_LIMIT_DELAY = 0.5  # seconds
    
    # Expose constants for backward compatibility
    CREDIBLE_SOURCES = CREDIBLE_SOURCES
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the NewsBot with configuration."""
        self.config = self.load_config(config_path)
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.results = []
        
        # Initialize RSS Feed Manager if enabled
        self.rss_manager = None
        if self.config.get('rss_enabled', False):
            try:
                from rss_feed_manager import RSSFeedManager
                rss_settings = self.config.get('rss_settings', {})
                self.rss_manager = RSSFeedManager(
                    timeout=rss_settings.get('request_timeout', self.DEFAULT_RSS_TIMEOUT),
                    cache_enabled=rss_settings.get('cache_enabled', True),
                    cache_ttl_hours=rss_settings.get('cache_ttl_hours', self.DEFAULT_RSS_CACHE_TTL_HOURS),
                    rate_limit_delay=rss_settings.get('rate_limit_delay', self.DEFAULT_RSS_RATE_LIMIT_DELAY)
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

    def aggregate_news(self) -> List[Dict[str, Any]]:
        """Aggregate news from GitHub and RSS feeds."""
        logging.info("Aggregating news from multiple sources...")
        all_results = []
        
        # Search GitHub repositories (if enabled)
        if self.config.get("github_enabled", True):
            github_results = search_github_repos(
                github_token=self.github_token,
                github_topics=self.config.get("github_topics", []),
                days_back=self.config.get("days_back", 7),
                max_results_per_topic=self.config.get("max_results_per_topic", 10)
            )
            all_results.extend(github_results)
        else:
            logging.info("GitHub search disabled by configuration")
        
        # RSS feed search (if enabled)
        if self.config.get('rss_enabled', False):
            rss_results = search_rss_feeds(
                rss_manager=self.rss_manager,
                assess_credibility_func=assess_source_credibility,
                config=self.config,
                openai_client=self.openai_client
            )
            all_results.extend(rss_results)
        
        self.results = all_results
        return all_results


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments.
    
    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(
        prog='newsbot',
        description='Newsbot - Offensive Security AI/Automation News Aggregator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s                          # Run with default config
  %(prog)s --config my_config.json  # Use custom config file
  %(prog)s --output-dir ./reports   # Save to custom output directory
  %(prog)s --quiet                  # Run with minimal output
  %(prog)s --verbose                # Run with detailed logging
        '''
    )
    
    parser.add_argument(
        '--config',
        type=str,
        default='config.json',
        metavar='PATH',
        help='path to configuration file (default: config.json)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='outputs',
        metavar='DIR',
        help='directory for output files (default: outputs)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='enable verbose logging output'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='suppress non-error output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    return parser.parse_args()


def main():
    """Main entry point."""
    # Parse command-line arguments
    args = parse_arguments()
    
    # Configure logging based on verbosity
    if args.verbose:
        log_level = logging.DEBUG
        log_format = '%(asctime)s - %(name)s - %(levelname)s: %(message)s'
    elif args.quiet:
        log_level = logging.ERROR
        log_format = '%(levelname)s: %(message)s'
    else:
        log_level = logging.INFO
        log_format = '%(levelname)s: %(message)s'
    
    logging.basicConfig(level=log_level, format=log_format, force=True)
    
    # Check for required GITHUB_TOKEN (based on config if available)
    has_github = bool(os.getenv("GITHUB_TOKEN"))
    requires_token = False
    requires_reasons = []
    if os.path.exists(args.config):
        try:
            with open(args.config, 'r') as config_file:
                config = json.load(config_file)
            github_enabled = config.get("github_enabled", True)
            rss_enabled = config.get("rss_enabled", False)
            llm_enabled = config.get("llm_assessment", {}).get("enabled", False)
            requires_token = github_enabled or (rss_enabled and llm_enabled)
            if github_enabled:
                requires_reasons.append("  - GitHub repository searches")
            if rss_enabled and llm_enabled:
                requires_reasons.append("  - LLM-based RSS assessment via GitHub Models")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Invalid configuration file: {e}")
            sys.exit(1)
    
    if requires_token and not has_github:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        print("\nGITHUB_TOKEN is required for:", file=sys.stderr)
        for reason in requires_reasons:
            print(reason, file=sys.stderr)
        print("\nPlease set it:", file=sys.stderr)
        print("  export GITHUB_TOKEN=your_token_here", file=sys.stderr)
        sys.exit(1)
    
    # Display banner unless quiet mode
    if not args.quiet:
        print("=" * 80)
        print("Newsbot - Offensive Security AI/Automation News Aggregator")
        print("=" * 80)
        print()
    
    if args.verbose:
        logging.debug(f"Using config file: {args.config}")
        logging.debug(f"Output directory: {args.output_dir}")
    
    if not args.quiet:
        print()
    
    # Initialize bot with custom config path
    try:
        bot = NewsBot(config_path=args.config)
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {args.config}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in configuration file: {e}")
        sys.exit(1)
    
    # Aggregate news
    results = bot.aggregate_news()
    
    if not args.quiet:
        print()
        print(f"Total results found: {len(results)}")
        print()
    else:
        logging.info(f"Total results found: {len(results)}")
    
    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Generate timestamp for filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Generate and save reports
    markdown_path = os.path.join(args.output_dir, f"report_{timestamp}.md")
    json_path = os.path.join(args.output_dir, f"results_{timestamp}.json")
    
    generate_report(results, markdown_path)
    save_json_results(results, json_path)
    
    if not args.quiet:
        print()
        print("=" * 80)
        print("Newsbot completed successfully!")
        print("=" * 80)
    else:
        logging.info("Newsbot completed successfully!")


if __name__ == "__main__":
    main()
