"""
Report generation functionality.
Generates markdown reports and JSON output from aggregated results.
"""

import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None


def _generate_report_header(results: List[Dict[str, Any]]) -> str:
    """Generate the report header with summary information.
    
    Args:
        results: List of aggregated results
        
    Returns:
        Markdown header string
    """
    header = f"# Offensive Security AI/Automation News\n\n"
    header += f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
    header += f"## Summary\n\n"
    header += f"Found {len(results)} relevant items.\n\n"
    return header


def _generate_github_section(github_items: List[Dict[str, Any]]) -> str:
    """Generate GitHub repositories section of the report.
    
    Args:
        github_items: List of GitHub repository items
        
    Returns:
        Markdown section string
    """
    if not github_items:
        return ""
    
    section = f"## GitHub Repositories ({len(github_items)})\n\n"
    # Sort by stars
    github_items.sort(key=lambda x: x.get("stars", 0), reverse=True)
    for item in github_items:
        section += f"### [{item['title']}]({item['url']})\n\n"
        if item.get("description"):
            section += f"{item['description']}\n\n"
        section += f"- **Stars:** {item.get('stars', 'N/A')}\n"
        section += f"- **Updated:** {item.get('updated', 'N/A')}\n"
        section += f"- **Topic:** {item.get('topic', 'N/A')}\n\n"
    
    return section


def _generate_rss_section(rss_items: List[Dict[str, Any]]) -> str:
    """Generate RSS feed articles section of the report.
    
    Args:
        rss_items: List of RSS feed items
        
    Returns:
        Markdown section string
    """
    if not rss_items:
        return ""
    
    section = f"## RSS Feed Articles ({len(rss_items)})\n\n"
    section += "*Articles from curated RSS feeds*\n\n"
    
    # Sort by priority and keyword matches
    rss_items.sort(
        key=lambda x: (
            0 if x.get('priority') == 'high' else 1,
            -x.get('keyword_matches', 0)
        )
    )
    
    for item in rss_items:
        section += f"### {item.get('title', 'Untitled')}\n\n"
        if item.get("description"):
            # Clean HTML from description if present
            desc = item['description']
            if '<' in desc and '>' in desc and BeautifulSoup:
                desc = BeautifulSoup(desc, 'html.parser').get_text()
            # Truncate long descriptions
            if len(desc) > 500:
                desc = desc[:500] + "..."
            section += f"{desc}\n\n"
        
        if item.get("url"):
            section += f"**Link:** [{item.get('url')}]({item.get('url')})\n\n"
        
        section += f"**Source:** {item.get('feed_name', 'Unknown Feed')}"
        if item.get('feed_category'):
            section += f" ({item['feed_category']})"
        section += "\n\n"
        
        if item.get("credibility"):
            section += f"**Domain Credibility:** {item['credibility'].title()}\n\n"
        
        # LLM Assessment Information
        if item.get("llm_applicable") is not None:
            llm_score = item.get("llm_applicability_score", 0)
            section += f"**LLM Applicability:** {'✓ Relevant' if item.get('llm_applicable') else '✗ Not Relevant'} (score: {llm_score:.2f})\n\n"
            
            if item.get("llm_matched_keywords"):
                matched = ", ".join(item['llm_matched_keywords'])
                section += f"*Matched topics: {matched}*\n\n"
            
            if item.get("llm_applicability_reason"):
                section += f"*{item['llm_applicability_reason']}*\n\n"
        
        if item.get("llm_credible") is not None:
            llm_cred_score = item.get("llm_credibility_score", 0)
            section += f"**LLM Credibility:** {'✓ Credible' if item.get('llm_credible') else '✗ Questionable'} (score: {llm_cred_score:.2f})\n\n"
            
            if item.get("llm_credibility_flags"):
                flags = ", ".join(item['llm_credibility_flags'])
                section += f"*Flags: {flags}*\n\n"
            
            if item.get("llm_credibility_reason"):
                section += f"*{item['llm_credibility_reason']}*\n\n"
        
        if item.get("published"):
            section += f"*Published: {item['published']}*\n\n"
        
        if item.get("keyword_matches", 0) > 0:
            section += f"*Keyword matches: {item['keyword_matches']}*\n\n"
    
    return section


def _generate_report_footer(has_rss_items: bool) -> str:
    """Generate the report footer with credibility notice.
    
    Args:
        has_rss_items: Whether the report includes RSS items
        
    Returns:
        Markdown footer string
    """
    footer = "\n---\n\n"
    footer += "*Note: Results are filtered for credibility and relevance using both domain-based assessment and LLM analysis. "
    if has_rss_items:
        footer += "RSS feed articles are from curated sources and evaluated for applicability and quality.*\n"
    else:
        footer += "All sources are assessed for reliability.*\n"
    return footer


def generate_report(results: List[Dict[str, Any]], output_path: str = None) -> str:
    """Generate a markdown report of the findings with enhanced source citations.
    
    Args:
        results: List of aggregated results
        output_path: Optional path to save the report
        
    Returns:
        Generated markdown report as string
    """
    if not results:
        logging.warning("No results to report")
        return ""
    
    # Generate header
    report = _generate_report_header(results)
    
    # Group by source
    github_items = [r for r in results if r.get("source") == "github"]
    rss_items = [r for r in results if r.get("source") == "rss"]
    
    # Generate sections
    report += _generate_github_section(github_items)
    report += _generate_rss_section(rss_items)
    
    # Add footer
    report += _generate_report_footer(bool(rss_items))
    
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
        results: List of results to save
        output_path: Path to save the JSON file
    """
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    logging.info(f"JSON results saved to: {output_path}")
