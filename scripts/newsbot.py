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
from typing import List, Dict, Any
import requests
from github import Github
from openai import OpenAI, OpenAIError  # GitHub Models uses OpenAI-compatible API


class NewsBot:
    """Main class for searching and aggregating security news."""
    
    # Prompt template for LLM searches. Use .format(query=...) to substitute the search topic.
    LLM_SUMMARY_PROMPT = """Search for and summarize the latest news, articles, blog posts, and announcements about: {query}

Focus on content from the last week that relates to:
- New tools or frameworks
- Research papers or blog posts
- Conference talks or presentations
- Code releases or updates
- Vulnerabilities or exploits
- Techniques or methodologies

Provide a structured summary with:
1. Title
2. Brief description
3. Source/URL (if available)
4. Key takeaways

Format as JSON array with objects containing: title, description, url, date, key_points."""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the NewsBot with configuration."""
        self.config = self.load_config(config_path)
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.results = []
        
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
        """Use LLM to search and summarize results for a topic via GitHub Models."""
        if not self.openai_client:
            logging.warning("OpenAI client not initialized, skipping LLM search")
            return ""
        
        try:
            prompt = self.LLM_SUMMARY_PROMPT.format(query=query)
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a security researcher assistant who helps find and summarize the latest offensive security news and developments, especially related to AI and automation."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            logging.error(f"OpenAI API error for '{query}': {e}")
            return ""
    
    def aggregate_news(self) -> List[Dict[str, Any]]:
        """Aggregate news from multiple sources."""
        logging.info("Aggregating news from multiple sources...")
        all_results = []
        
        # Search GitHub repositories
        github_results = self.search_github_repos()
        all_results.extend(github_results)
        
        # Search using LLM for each topic
        for topic in self.config.get("search_topics", []):
            logging.info(f"Searching for: {topic}")
            llm_response = self.search_with_llm(topic)
            
            if llm_response:
                try:
                    # Try to parse JSON response
                    # Look for JSON array in the response
                    import re
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
        
        self.results = all_results
        return all_results
    
    def generate_report(self, output_path: str = None) -> str:
        """Generate a markdown report of the findings."""
        if not self.results:
            logging.warning("No results to report")
            return ""
        
        report = f"# Offensive Security AI/Automation News\n\n"
        report += f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        report += f"## Summary\n\n"
        report += f"Found {len(self.results)} relevant items.\n\n"
        
        # Group by source
        github_items = [r for r in self.results if r.get("source") == "github"]
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
        
        if llm_items:
            report += f"## Articles, Blog Posts & Announcements ({len(llm_items)})\n\n"
            for item in llm_items:
                report += f"### {item.get('title', 'Untitled')}\n\n"
                if item.get("description"):
                    report += f"{item['description']}\n\n"
                if item.get("url"):
                    report += f"**Link:** {item['url']}\n\n"
                if item.get("key_points"):
                    report += f"**Key Points:**\n"
                    if isinstance(item["key_points"], list):
                        for point in item["key_points"]:
                            report += f"- {point}\n"
                    report += "\n"
                report += f"*Search topic: {item.get('search_topic', 'N/A')}*\n\n"
        
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
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
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
