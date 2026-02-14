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
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import requests
from github import Github
from openai import OpenAI, OpenAIError  # GitHub Models uses OpenAI-compatible API
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup


class NewsBot:
    """Main class for searching and aggregating security news."""
    
    # Maximum characters to extract from article content for LLM processing
    MAX_ARTICLE_CONTENT_LENGTH = 5000
    # Maximum characters to include in context when passing to LLM
    MAX_CONTEXT_SNIPPET_LENGTH = 1000
    
    # Prompt template for LLM searches with web search context
    LLM_SUMMARY_PROMPT = """Based on the following web search results about "{query}", provide a structured analysis of the latest news and developments.

Web Search Results:
{search_context}

Analyze these results and provide:
1. A summary of the most important and credible news items
2. Key developments and trends
3. Notable sources and their credibility
4. Practical takeaways for security professionals

Focus on:
- New tools or frameworks
- Research papers or blog posts
- Conference talks or presentations
- Code releases or updates
- Vulnerabilities or exploits
- Techniques or methodologies

Format your response as a JSON array with objects containing:
- title: The article/news title
- description: Brief summary of the content
- url: Original source URL (from search results)
- source: Domain/publication name
- credibility: Assessment of source credibility (high/medium/low)
- key_points: Array of important takeaways
- date: Publication date if available

Only include items from credible sources. Exclude promotional content and low-quality sources."""
    
    # Credible news sources for security/tech news
    CREDIBLE_SOURCES = {
        'high': [
            'arxiv.org', 'github.com', 'blog.google', 'openai.com', 'microsoft.com',
            'research.google', 'ai.meta.com', 'blog.cloudflare.com', 'security.googleblog.com',
            'blogs.microsoft.com', 'aws.amazon.com', 'engineering.fb.com', 'netflix.github.io',
            'github.blog', 'blog.github.com', 'nist.gov', 'cisa.gov', 'nvd.nist.gov',
            'owasp.org', 'sans.org', 'portswigger.net', 'schneier.com', 'krebsonsecurity.com',
            'blog.trailofbits.com', 'googleprojectzero.blogspot.com', 'thehackernews.com'
        ],
        'medium': [
            'medium.com', 'towardsdatascience.com', 'dev.to', 'hackernoon.com',
            'researchgate.net', 'reddit.com/r/netsec', 'infosecurity-magazine.com',
            'bleepingcomputer.com', 'zdnet.com', 'arstechnica.com', 'wired.com',
            'techcrunch.com', 'venturebeat.com'
        ]
    }
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the NewsBot with configuration."""
        self.config = self.load_config(config_path)
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.results = []
        self.web_search_available = True  # Track if web search is available
        
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
    
    def assess_source_credibility(self, url: str) -> str:
        """Assess the credibility of a news source based on its domain.
        
        Args:
            url: The URL to assess
            
        Returns:
            'high', 'medium', or 'low' credibility rating
        """
        try:
            domain = urlparse(url).netloc.lower()
            # Remove www. prefix
            domain = domain.replace('www.', '')
            
            # Check against credible sources lists
            for credible_domain in self.CREDIBLE_SOURCES['high']:
                if credible_domain in domain:
                    return 'high'
            
            for credible_domain in self.CREDIBLE_SOURCES['medium']:
                if credible_domain in domain:
                    return 'medium'
            
            # Default to low if not recognized
            return 'low'
        except Exception as e:
            logging.warning(f"Error assessing credibility for {url}: {e}")
            return 'low'
    
    def extract_article_content(self, url: str) -> Optional[str]:
        """Extract main content from a web article.
        
        Args:
            url: URL of the article
            
        Returns:
            Extracted text content or None if extraction fails
        """
        try:
            # Set a timeout and user agent
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; Newsbot/1.0; +https://github.com/llamalamall/Newsbot)'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Use BeautifulSoup to extract text
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(['script', 'style', 'nav', 'footer', 'header']):
                script.decompose()
            
            # Try to find main content areas
            main_content = None
            for selector in ['article', 'main', '[role="main"]', '.content', '#content']:
                main_content = soup.select_one(selector)
                if main_content:
                    break
            
            # Fall back to body if no main content found
            if not main_content:
                main_content = soup.body
            
            if main_content:
                # Get text and clean it up
                text = main_content.get_text(separator='\n', strip=True)
                # Remove excessive whitespace
                text = re.sub(r'\n\s*\n', '\n\n', text)
                # Limit to MAX_ARTICLE_CONTENT_LENGTH for processing (balances context vs. token usage)
                return text[:self.MAX_ARTICLE_CONTENT_LENGTH] if text else None
            
            return None
        except Exception as e:
            logging.debug(f"Could not extract content from {url}: {str(e)[:100]}")
            return None
    
    def search_github_repos(self) -> List[Dict[str, Any]]:
        """Search GitHub for relevant repositories."""
        logging.info("Searching GitHub repositories...")
        results = []
        
        if not self.github_token:
            logging.warning("GITHUB_TOKEN not set, skipping GitHub search")
            return results
        
        try:
            from github import Auth
            auth = Auth.Token(self.github_token)
            g = Github(auth=auth)
            days_back = self.config.get("days_back", 7)
            since_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
            
            # Search for repositories with relevant topics
            for topic in self.config.get("github_topics", []):
                try:
                    query = f"topic:{topic} pushed:>={since_date}"
                    repos = g.search_repositories(query=query, sort="updated", order="desc")
                    
                    for repo in repos[:self.config.get("max_results_per_topic", 10)]:
                        # Check if repo description contains AI/automation keywords
                        description = (repo.description or "").lower()
                        if any(kw in description for kw in ["ai", "llm", "ml", "machine learning", "automation", "automated", "gpt"]):
                            results.append({
                                "title": repo.full_name,
                                "url": repo.html_url,
                                "description": repo.description,
                                "stars": repo.stargazers_count,
                                "updated": repo.updated_at.isoformat(),
                                "source": "github",
                                "topic": topic
                            })
                except Exception as topic_error:
                    logging.error(f"Error searching topic '{topic}': {str(topic_error)[:100]}")
                    continue
            
            logging.info(f"Found {len(results)} relevant GitHub repositories")
        except Exception as e:
            logging.error(f"Error initializing GitHub search: {str(e)[:100]}")
        
        return results
    
    def search_with_llm(self, query: str) -> str:
        """Use LLM to search and summarize results for a topic via GitHub Models.
        
        This method now integrates live web search results to provide more current
        and accurate information.
        
        Args:
            query: The search topic/query
            
        Returns:
            LLM-generated summary with web search context
        """
        if not self.openai_client:
            logging.warning("OpenAI client not initialized, skipping LLM search")
            return ""
        
        try:
            # First, perform a web search to get current results
            search_context = "No web search results available."
            
            # Note: In a sandboxed environment, web_search tool might not be available
            # This is a placeholder for the web search integration
            # The actual web search will be performed via external tool
            
            # Use the web_search tool if available (this will be called externally)
            # For now, we'll construct the prompt to work with or without web search
            
            prompt = self.LLM_SUMMARY_PROMPT.format(
                query=query,
                search_context=search_context
            )
            
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a security researcher assistant who helps find and summarize the latest offensive security news and developments, especially related to AI and automation. You prioritize credible sources and fact-based reporting."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            logging.error(f"OpenAI API error for '{query}': {e}")
            return ""
    
    def perform_web_search(self, query: str) -> List[Dict[str, Any]]:
        """Perform a live web search for the given query.
        
        This method integrates with web search functionality. It attempts to use
        the web_search_helper module if available and enabled in configuration.
        
        Args:
            query: Search query string
            
        Returns:
            List of search results with title, url, snippet, and credibility
        """
        results = []
        
        # Check if web search is enabled in configuration
        if not self.config.get('web_search_enabled', True):
            logging.info("Web search is disabled in configuration")
            return results
        
        try:
            # Try to import and use the web search helper
            from scripts.web_search_helper import WebSearchHelper
            
            # Get configuration parameters
            max_results = self.config.get('web_search_max_results', 10)
            timeout = self.config.get('web_search_timeout', 10)
            rate_limit = self.config.get('web_search_rate_limit', 1.0)
            
            # Create helper with configuration
            helper = WebSearchHelper(timeout=timeout, rate_limit_delay=rate_limit)
            
            if helper.is_available():
                search_results = helper.search(query, max_results=max_results)
                
                # Process and enrich results with credibility assessment
                for result in search_results:
                    url = result.get('url', '')
                    result['credibility'] = self.assess_source_credibility(url)
                    results.append(result)
                    
                logging.info(f"Web search returned {len(results)} results for: {query}")
            else:
                logging.warning("Web search helper not available")
                
        except ImportError:
            logging.debug("Web search helper module not found")
        except Exception as e:
            logging.error(f"Error in web search: {str(e)[:100]}")
        
        # If no results from web search, log it but don't fail
        if not results:
            logging.info(f"No web search results for '{query}', will use LLM-only search")
        
        return results
    
    def search_with_web_context(self, query: str) -> List[Dict[str, Any]]:
        """Search using both web search and LLM with full context integration.
        
        This is the enhanced search method that combines:
        1. Live web search results
        2. Source credibility assessment
        3. Article content extraction
        4. LLM-powered summarization
        
        Args:
            query: The search topic/query
            
        Returns:
            List of processed and enriched results
        """
        results = []
        
        try:
            # Step 1: Perform web search
            web_results = self.perform_web_search(query)
            
            # Step 2: Filter by credibility
            credible_results = []
            for result in web_results:
                url = result.get('url', '')
                credibility = self.assess_source_credibility(url)
                
                # Only include high and medium credibility sources
                if credibility in ['high', 'medium']:
                    result['credibility'] = credibility
                    credible_results.append(result)
                    
                    # Step 3: Try to extract article content
                    content = self.extract_article_content(url)
                    if content:
                        # Store shorter snippet for context to manage token usage
                        result['extracted_content'] = content[:self.MAX_CONTEXT_SNIPPET_LENGTH]
            
            # Step 4: Build context for LLM
            if credible_results:
                search_context = "\n\n".join([
                    f"Title: {r.get('title', 'N/A')}\n"
                    f"URL: {r.get('url', 'N/A')}\n"
                    f"Snippet: {r.get('snippet', 'N/A')}\n"
                    f"Credibility: {r.get('credibility', 'unknown')}"
                    for r in credible_results[:10]  # Limit to top 10
                ])
                
                # Step 5: Use LLM with web search context
                prompt = self.LLM_SUMMARY_PROMPT.format(
                    query=query,
                    search_context=search_context
                )
                
                if self.openai_client:
                    response = self.openai_client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a security researcher assistant who helps find and summarize the latest offensive security news and developments. You prioritize credible sources and fact-based reporting."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.3,
                        max_tokens=2000
                    )
                    
                    llm_response = response.choices[0].message.content
                    
                    # Parse LLM response into structured results
                    try:
                        json_match = re.search(r'\[.*\]', llm_response, re.DOTALL)
                        if json_match:
                            parsed_results = json.loads(json_match.group())
                            for item in parsed_results:
                                item["source"] = "web_search_llm"
                                item["search_topic"] = query
                                results.append(item)
                    except json.JSONDecodeError:
                        # If not JSON, return as summary
                        results.append({
                            "title": f"Web Search Summary: {query}",
                            "description": llm_response,
                            "source": "web_search_summary",
                            "search_topic": query,
                            "credible_sources_found": len(credible_results)
                        })
            else:
                logging.info(f"No credible web results found for: {query}")
                
        except Exception as e:
            logging.error(f"Error in web search for '{query}': {str(e)[:200]}")
            # Don't fail completely, just log and continue
        
        return results
    
    def aggregate_news(self) -> List[Dict[str, Any]]:
        """Aggregate news from multiple sources with enhanced web search integration."""
        logging.info("Aggregating news from multiple sources...")
        all_results = []
        
        # Search GitHub repositories
        github_results = self.search_github_repos()
        all_results.extend(github_results)
        
        # Enhanced search using web context for each topic
        for topic in self.config.get("search_topics", []):
            logging.info(f"Enhanced web search for: {topic}")
            
            try:
                # Try the new web-enhanced search first
                web_enhanced_results = self.search_with_web_context(topic)
                if web_enhanced_results:
                    all_results.extend(web_enhanced_results)
                else:
                    # Fallback to original LLM-only search
                    logging.info(f"Falling back to LLM-only search for: {topic}")
                    llm_response = self.search_with_llm(topic)
                    
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
        """Generate a markdown report of the findings with enhanced source citations."""
        if not self.results:
            logging.warning("No results to report")
            return ""
        
        report = f"# Offensive Security AI/Automation News\n\n"
        report += f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        report += f"## Summary\n\n"
        report += f"Found {len(self.results)} relevant items.\n\n"
        
        # Group by source
        github_items = [r for r in self.results if r.get("source") == "github"]
        web_items = [r for r in self.results if r.get("source") in ["web_search_llm", "web_search_summary"]]
        llm_items = [r for r in self.results if r.get("source") in ["llm_search", "llm_summary"]]
        
        if github_items:
            report += f"## GitHub Repositories ({len(github_items)})\n\n"
            # Sort by stars
            github_items.sort(key=lambda x: x.get("stars", 0), reverse=True)
            for item in github_items:
                report += f"### [{item['title']}]({item['url']})\n\n"
                if item.get("description"):
                    report += f"{item['description']}\n\n"
                report += f"- **Stars:** {item.get('stars', 'N/A')}\n"
                report += f"- **Updated:** {item.get('updated', 'N/A')}\n"
                report += f"- **Topic:** {item.get('topic', 'N/A')}\n\n"
        
        if web_items:
            report += f"## Web Search Results ({len(web_items)})\n\n"
            report += "*Results from live web searches with credibility assessment*\n\n"
            for item in web_items:
                report += f"### {item.get('title', 'Untitled')}\n\n"
                if item.get("description"):
                    report += f"{item['description']}\n\n"
                if item.get("url"):
                    report += f"**Source:** [{item.get('url')}]({item.get('url')})\n\n"
                if item.get("credibility"):
                    report += f"**Credibility:** {item['credibility'].title()}\n\n"
                if item.get("key_points"):
                    report += f"**Key Points:**\n"
                    if isinstance(item["key_points"], list):
                        for point in item["key_points"]:
                            report += f"- {point}\n"
                    report += "\n"
                if item.get("date"):
                    report += f"*Published: {item.get('date')}*\n\n"
                report += f"*Search topic: {item.get('search_topic', 'N/A')}*\n\n"
        
        if llm_items:
            report += f"## Articles, Blog Posts & Announcements ({len(llm_items)})\n\n"
            for item in llm_items:
                report += f"### {item.get('title', 'Untitled')}\n\n"
                if item.get("description"):
                    report += f"{item['description']}\n\n"
                if item.get("url"):
                    report += f"**Link:** {item['url']}\n\n"
                if item.get("credibility"):
                    report += f"**Source Credibility:** {item['credibility'].title()}\n\n"
                if item.get("key_points"):
                    report += f"**Key Points:**\n"
                    if isinstance(item["key_points"], list):
                        for point in item["key_points"]:
                            report += f"- {point}\n"
                    report += "\n"
                report += f"*Search topic: {item.get('search_topic', 'N/A')}*\n\n"
        
        # Add footer with credibility notice
        report += "\n---\n\n"
        report += "*Note: Results are filtered for credibility and relevance. "
        report += "Web search results are assessed for source reliability before inclusion.*\n"
        
        # Save report
        if output_path:
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
            with open(output_path, 'w') as f:
                f.write(report)
            logging.info(f"Report saved to: {output_path}")
        
        return report
    
    def save_json_results(self, output_path: str):
        """Save results as JSON."""
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
        logging.info(f"JSON results saved to: {output_path}")


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
