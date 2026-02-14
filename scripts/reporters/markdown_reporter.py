"""
Markdown report generator for NewsBot.
"""

import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any


def generate_report(results: List[Dict[str, Any]], output_path: str = None) -> str:
    """Generate a markdown report of the findings with enhanced source citations.
    
    Args:
        results: List of search results to include in the report
        output_path: Optional path to save the report (if None, returns string only)
        
    Returns:
        Generated markdown report as a string
    """
    if not results:
        logging.warning("No results to report")
        return ""
    
    report = f"# Offensive Security AI/Automation News\n\n"
    report += f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
    report += f"## Summary\n\n"
    report += f"Found {len(results)} relevant items.\n\n"
    
    # Group by source
    github_items = [r for r in results if r.get("source") == "github"]
    rss_items = [r for r in results if r.get("source") == "rss"]
    web_items = [r for r in results if r.get("source") in ["web_search_llm", "web_search_summary"]]
    llm_items = [r for r in results if r.get("source") in ["llm_search", "llm_summary"]]
    
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
    
    if rss_items:
        report += f"## RSS Feed Articles ({len(rss_items)})\n\n"
        report += "*Articles from curated RSS feeds*\n\n"
        
        # Sort by priority and keyword matches
        rss_items.sort(
            key=lambda x: (
                0 if x.get('priority') == 'high' else 1,
                -x.get('keyword_matches', 0)
            )
        )
        
        for item in rss_items:
            report += f"### {item.get('title', 'Untitled')}\n\n"
            if item.get("description"):
                # Clean HTML from description if present
                desc = item['description']
                if '<' in desc and '>' in desc:
                    from bs4 import BeautifulSoup
                    desc = BeautifulSoup(desc, 'html.parser').get_text()
                # Truncate long descriptions
                if len(desc) > 500:
                    desc = desc[:500] + "..."
                report += f"{desc}\n\n"
            
            if item.get("url"):
                report += f"**Link:** [{item.get('url')}]({item.get('url')})\n\n"
            
            report += f"**Source:** {item.get('feed_name', 'Unknown Feed')}"
            if item.get('feed_category'):
                report += f" ({item['feed_category']})"
            report += "\n\n"
            
            if item.get("credibility"):
                report += f"**Credibility:** {item['credibility'].title()}\n\n"
            
            if item.get("published"):
                report += f"*Published: {item['published']}*\n\n"
            
            if item.get("keyword_matches", 0) > 0:
                report += f"*Keyword matches: {item['keyword_matches']}*\n\n"
    
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
    if rss_items:
        report += "RSS feed articles are from curated, high-quality sources. "
    report += "Web search results are assessed for source reliability before inclusion.*\n"
    
    # Save report
    if output_path:
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(report)
        logging.info(f"Report saved to: {output_path}")
    
    return report


def save_json_results(results: List[Dict[str, Any]], output_path: str):
    """Save results as JSON.
    
    Args:
        results: List of search results to save
        output_path: Path to save the JSON file
    """
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    logging.info(f"JSON results saved to: {output_path}")
