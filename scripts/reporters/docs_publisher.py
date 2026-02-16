"""
Documentation publisher for GitHub Pages.
Formats reports and updates the docs/ folder for human-friendly GitHub Pages.
"""

import os
import re
import json
import shutil
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
from urllib.parse import urlparse
from email.utils import parsedate_to_datetime
def ensure_index_front_matter(index_content: str) -> str:
    """Ensure index.md has Jekyll front matter.

    Args:
        index_content: Current index content.

    Returns:
        Index content with front matter prepended if missing.
    """
    if index_content.lstrip().startswith("---\n"):
        return index_content

    front_matter = "---\nlayout: default\ntitle: Newsbot - Security News Aggregator\n---\n\n"
    return front_matter + index_content


def format_article_link_title(title: str, url: str, max_length: int = 80) -> str:
    """Format article link text with domain and title preview.

    Args:
        title: Article title.
        url: Article URL.
        max_length: Maximum length before truncation.

    Returns:
        Formatted link text.
    """
    domain = extract_domain_from_url(url)
    title_text = (title or "Untitled").strip()
    combined = f"{domain} - {title_text}" if title_text else domain

    if max_length > 3 and len(combined) > max_length:
        combined = combined[: max_length - 3].rstrip() + "..."

    return combined


def extract_domain_from_url(url: str) -> str:
    """Extract domain from URL.
    
    Args:
        url: Article URL.
        
    Returns:
        Domain string or "unknown" if URL is empty/invalid.
    """
    if not url:
        return "unknown"
    domain = urlparse(url).netloc
    return domain if domain else "unknown"


def format_date_only(value: Optional[str]) -> str:
    """Format a timestamp-like string as YYYY-MM-DD.

    Args:
        value: Timestamp string (ISO or RFC 2822), or None.

    Returns:
        Date string in YYYY-MM-DD format, or "N/A" if unavailable.
    """
    if not value:
        return "N/A"

    if isinstance(value, str):
        if "T" in value:
            try:
                dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                pass
        try:
            dt = parsedate_to_datetime(value)
            return dt.strftime("%Y-%m-%d")
        except (TypeError, ValueError):
            return value.split(" ")[0]

    return str(value)


def generate_article_table_rows(article_entries: List[Dict[str, Any]]) -> str:
    """Generate Markdown table rows for articles.
    
    Args:
        article_entries: List of article metadata dictionaries.
        
    Returns:
        Markdown table rows as a string.
    """
    rows = ""
    for entry in sort_articles_by_published(article_entries):
        article_file = entry.get("filename", "")
        if not article_file:
            continue
        
        # Extract domain from URL
        domain = extract_domain_from_url(entry.get("url", ""))
        
        # Get scores
        applicability = entry.get("llm_applicability_score", 0)
        credibility = entry.get("llm_credibility_score", 0)
        
        # Get full title (no truncation)
        title = entry.get("title", "Untitled Article")
        # Escape pipe characters in title for table formatting
        title = title.replace('|', '\\|')
        
        # Create title link
        title_link = f"[{title}](articles/{article_file})"

        updated_raw = entry.get("updated") or entry.get("published")
        updated_date = format_date_only(updated_raw)

        rows += f"| {domain} | {updated_date} | {applicability:.2f} | {credibility:.2f} | {title_link} |\n"
    
    return rows


def sort_articles_by_published(entries: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Sort article entries in reverse chronological order.

    Args:
        entries: List of article metadata dictionaries.

    Returns:
        Sorted list of article metadata dictionaries.
    """
    def sort_key(entry: Dict[str, str]) -> datetime:
        published = entry.get("published")
        if not published:
            return datetime.min
        try:
            return parsedate_to_datetime(published)
        except (TypeError, ValueError):
            return datetime.min

    return sorted(entries, key=sort_key, reverse=True)
def initialize_docs_directory(docs_dir: str = "docs") -> None:
    """Initialize the docs directory with required files for GitHub Pages.
    
    Args:
        docs_dir: Target docs directory (default: "docs")
    """
    os.makedirs(docs_dir, exist_ok=True)
    
    # Create index.md if it doesn't exist
    index_path = os.path.join(docs_dir, "index.md")
    if not os.path.exists(index_path):
        index_content = """# Newsbot - Security News Aggregator

Welcome to the Newsbot documentation. This page provides access to all generated security news reports.

## About Newsbot

Newsbot is an automated news aggregator that searches for the latest articles, announcements, repositories, and blog posts related to AI and automation in offensive security.

### Features
- **GitHub Repository Search**: Finds recently updated repositories with relevant topics
- **RSS Feed Aggregation**: Monitors security blogs, research feeds, and official advisories
- **Smart Article Deduplication**: Automatically detects and skips already analyzed articles
- **LLM-Powered Assessment**: Uses AI to evaluate article applicability and credibility
- **Automated Daily Updates**: Runs via GitHub Actions

## Latest Reports

*No reports yet. Reports will appear here as they are generated.*

---

[View on GitHub](https://github.com/llamalamall/Newsbot)
"""
        index_content = ensure_index_front_matter(index_content)
        with open(index_path, 'w') as f:
            f.write(index_content)
        logging.info("Created docs/index.md")
    
    # Create README.md for docs directory
    readme_path = os.path.join(docs_dir, "README.md")
    if not os.path.exists(readme_path):
        readme_content = """# Newsbot Documentation

This directory contains formatted reports for GitHub Pages.

## Setup GitHub Pages

To publish these reports as a website:

1. Go to your repository **Settings** > **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Select the **main** branch and **/docs** folder
4. Click **Save**

GitHub will automatically publish the site at `https://<username>.github.io/<repository>/`

## Files

- `index.md` - Main landing page with links to all reports
- `report_YYYYMMDD_HHMMSS.md` - Individual report files

## Customization

You can customize the look and feel by:
- Modifying the report templates in the publisher script
- Editing the front matter in individual report files
- Creating custom CSS in an `assets/` directory (requires custom HTML)

## Verifying GitHub Pages Setup

After configuring GitHub Pages, verify it's working:

1. **Check GitHub Pages is enabled:**
   - Go to **Settings** > **Pages**
   - Verify **Source** is set to "Deploy from a branch"
   - Confirm **Branch** is set to "main" and folder is "/docs"
   - Look for the green checkmark and site URL

2. **Visit your site:**
   - Your site will be at `https://<username>.github.io/<repository>/`
   - It may take a few minutes to deploy initially

3. **Check build status:**
   - Go to the **Actions** tab
   - Look for "pages build and deployment" workflow
   - Ensure it completed successfully (green checkmark)

## Troubleshooting

**Pages not appearing:**
- Ensure the repository is public (or you have GitHub Pro for private repos)
- Check that the docs/ folder contains index.md
- Wait 1-2 minutes after pushing changes

**Build failures:**
- Check the Actions tab for error messages
- Verify all markdown files have valid syntax
- Ensure front matter is properly formatted in report files

**Broken links:**
- Use relative links (e.g., `[link](report.md)` not `[link](/docs/report.md)`)
- Check that linked files exist in the docs/ folder

**Styling issues:**
 - GitHub Pages uses default GitHub markdown styling
 - Check that front matter is properly formatted in report files
"""
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        logging.info("Created docs/README.md")
    
    logging.info(f"Docs directory initialized at: {docs_dir}")


def publish_repositories_page(github_items: List[Dict[str, Any]], docs_dir: str = "docs") -> Optional[str]:
    """Publish a dedicated page for GitHub repositories in table format.
    
    Args:
        github_items: List of GitHub repository items
        docs_dir: Target docs directory
        
    Returns:
        Path to the published repositories page, or None if failed
    """
    from .markdown_reporter import generate_repositories_page
    
    # Generate the repositories page content
    page_content = generate_repositories_page(github_items)
    
    # Add front matter
    formatted_content = "---\nlayout: default\ntitle: GitHub Repositories\n---\n\n"
    formatted_content += "[← Back to Index](index.md)\n\n"
    formatted_content += page_content
    formatted_content += "\n\n---\n\n[← Back to Index](index.md)\n"
    
    # Write to docs directory
    repos_path = os.path.join(docs_dir, "repositories.md")
    try:
        with open(repos_path, 'w') as f:
            f.write(formatted_content)
        logging.info(f"Published repositories page to: {repos_path}")
        return repos_path
    except IOError as e:
        logging.error(f"Failed to publish repositories page: {e}")
        return None


def publish_rss_article_pages(
    rss_items: List[Dict[str, Any]],
    timestamp: str,
    docs_dir: str = "docs"
) -> List[Dict[str, str]]:
    """Publish individual pages for each RSS article.
    
    Args:
        rss_items: List of RSS feed items
        timestamp: Timestamp for this batch of articles (YYYYMMDD_HHMMSS format)
        docs_dir: Target docs directory
        
    Returns:
        List of published article metadata dictionaries
    """
    from .markdown_reporter import generate_rss_article_page
    
    if not rss_items:
        return []
    
    # Create articles subdirectory
    articles_dir = os.path.join(docs_dir, "articles")
    os.makedirs(articles_dir, exist_ok=True)
    
    # Sort articles by priority and keyword matches
    rss_items.sort(
        key=lambda x: (
            0 if x.get('priority') == 'high' else 1,
            -x.get('keyword_matches', 0)
        )
    )
    
    published_entries = []
    total_articles = len(rss_items)
    
    for idx, article in enumerate(rss_items, 1):
        # Generate filename
        article_filename = f"article_{timestamp}_{idx:03d}.md"
        article_path = os.path.join(articles_dir, article_filename)
        
        # Generate page content
        page_content = generate_rss_article_page(article)
        
        # Add front matter and navigation
        try:
            dt = datetime.strptime(timestamp, "%Y%m%d_%H%M%S")
            readable_date = dt.strftime("%B %d, %Y")
        except ValueError:
            readable_date = timestamp
        
        article_title = article.get('title', 'Untitled Article')[:50]  # Truncate for title
        formatted_content = f"---\nlayout: default\ntitle: {article_title}\n---\n\n"
        formatted_content += "[← Back to Index](../index.md)\n\n"
        formatted_content += page_content
        formatted_content += "\n---\n\n"
        
        # Add navigation to other articles
        if idx > 1:
            prev_filename = f"article_{timestamp}_{idx-1:03d}.md"
            formatted_content += f"[← Previous Article]({prev_filename}) | "
        formatted_content += "[Back to Index](../index.md)"
        if idx < total_articles:
            next_filename = f"article_{timestamp}_{idx+1:03d}.md"
            formatted_content += f" | [Next Article →]({next_filename})"
        formatted_content += "\n"
        
        # Write to file
        try:
            with open(article_path, 'w') as f:
                f.write(formatted_content)
            published_entries.append({
                "filename": article_filename,
                "path": article_path,
                "title": article.get("title", "Untitled Article"),
                "url": article.get("url", ""),
                "published": article.get("published"),
                "updated": article.get("updated") or article.get("published"),
                "llm_applicability_score": article.get("llm_applicability_score", 0),
                "llm_credibility_score": article.get("llm_credibility_score", 0)
            })
            logging.info(f"Published article page: {article_filename}")
        except IOError as e:
            logging.error(f"Failed to publish article page {article_filename}: {e}")
    
    return published_entries


def update_index_with_structured_content(
    docs_dir: str,
    timestamp: str,
    github_count: int,
    rss_count: int,
    article_entries: Optional[List[Dict[str, str]]] = None,
    github_items: Optional[List[Dict[str, Any]]] = None
) -> None:
    """Update index.md with latest analysis summary and links to comprehensive pages.
    
    Args:
        docs_dir: Path to the docs directory
        timestamp: Timestamp of the report (YYYYMMDD_HHMMSS format)
        github_count: Number of GitHub repositories in latest run
        rss_count: Number of RSS articles in latest run
        article_entries: List of article metadata dictionaries from latest run
        github_items: List of GitHub repository items from latest run
    """
    index_path = os.path.join(docs_dir, "index.md")
    
    # Build the complete index content from scratch for latest analysis
    index_content = """# Newsbot - Latest Analysis

This page shows the **most recent analysis** from Newsbot. For comprehensive historical data, see the links below.

## Comprehensive Archives

- **[All Articles](articles.md)** - Complete archive of all analyzed articles, organized by month
- **[All Repositories](repositories.md)** - Complete archive of all analyzed repositories, organized by month
- **[Rejected Articles](rejected.md)** - Articles that didn't meet relevance or credibility criteria

"""
    
    # Add latest articles summary
    if article_entries and rss_count > 0:
        index_content += f"## Latest Articles\n\n"
        index_content += f"*{rss_count} article{'s' if rss_count != 1 else ''} from most recent analysis*\n\n"
        index_content += "| Source | Updated | Applicability | Credibility | Title |\n"
        index_content += "|--------|---------|--------------|-------------|-------|\n"
        index_content += generate_article_table_rows(article_entries)
        index_content += "\n"
        index_content += "[View all articles →](articles.md)\n\n"
    else:
        index_content += "## Latest Articles\n\n"
        index_content += "*No articles in most recent analysis*\n\n"
    
    # Add latest repositories summary
    if github_items and github_count > 0:
        index_content += f"## Latest Repositories\n\n"
        index_content += f"*{github_count} repositor{'ies' if github_count != 1 else 'y'} from most recent analysis*\n\n"
        index_content += "| Repository | Description | Stars | Applicability | Updated | Topic |\n"
        index_content += "|------------|-------------|-------|---------------|---------|-------|\n"
        
        # Sort by stars
        sorted_repos = sorted(github_items, key=lambda x: x.get("stars", 0), reverse=True)
        
        for repo in sorted_repos:
            title = repo.get("title", "Unknown")
            url = repo.get("url", "")
            description = repo.get("description", "")
            stars = repo.get("stars", 0)
            updated = repo.get("updated", "")
            topic = repo.get("topic", "N/A")
            applicability = repo.get("llm_applicability_score", 0)

            # Escape pipe characters and truncate
            if description:
                description = description.replace('|', '\\|')
                if len(description) > 100:
                    description = description[:97] + "..."
            
            # Create title link
            if url:
                title_link = f"[{title}]({url})"
            else:
                title_link = title
            
            # Format date
            date_str = format_date_only(updated)
            
            index_content += f"| {title_link} | {description} | {stars} | {applicability:.2f} {date_str} | {topic} |\n"
        
        index_content += "\n"
        index_content += "[View all repositories →](repositories.md)\n\n"
    else:
        index_content += "## Latest Repositories\n\n"
        index_content += "*No repositories in most recent analysis*\n\n"
    
    # Add footer
    index_content += "---\n\n"
    index_content += "[View on GitHub](https://github.com/llamalamall/Newsbot)\n"
    
    # Add front matter
    index_content = ensure_index_front_matter(index_content)

    # Write updated index
    with open(index_path, 'w') as f:
        f.write(index_content)
    
    logging.info(f"Updated docs/index.md with latest analysis summary")


def publish_structured_docs(results: List[Dict[str, Any]], timestamp: str,
                           docs_dir: str = "docs", output_dir: str = "outputs") -> Dict[str, Any]:
    """Publish documentation in the new structured format.
    
    Args:
        results: List of all results (GitHub repos and RSS articles)
        timestamp: Timestamp for this batch (YYYYMMDD_HHMMSS format)
        docs_dir: Target docs directory
        output_dir: Output directory containing rejected articles (default: "outputs")
        
    Returns:
        Dictionary with paths to published files
    """
    # Initialize docs directory
    initialize_docs_directory(docs_dir)
    
    # Separate GitHub repos and RSS articles from latest run
    github_items = [r for r in results if r.get("source") == "github"]
    rss_items = [r for r in results if r.get("source") == "rss"]
    
    published_files = {
        "repositories": None,
        "articles": [],
        "comprehensive_articles": None,
        "comprehensive_repositories": None,
        "rejected": None,
        "index": os.path.join(docs_dir, "index.md")
    }
    
    # Publish comprehensive articles page (ALL articles from output_dir)
    comprehensive_articles_path = publish_comprehensive_articles_page(output_dir, docs_dir)
    if comprehensive_articles_path:
        published_files["comprehensive_articles"] = comprehensive_articles_path
    
    # Publish comprehensive repositories page (ALL repositories from output_dir)
    comprehensive_repos_path = publish_comprehensive_repositories_page(output_dir, docs_dir)
    if comprehensive_repos_path:
        published_files["comprehensive_repositories"] = comprehensive_repos_path
    
    # Publish individual article pages for latest run
    article_entries: List[Dict[str, str]] = []
    if rss_items:
        article_entries = publish_rss_article_pages(rss_items, timestamp, docs_dir)
        published_files["articles"] = [entry["path"] for entry in article_entries]
    
    # Publish rejected articles page
    rejected_path = publish_rejected_articles_page(output_dir, docs_dir)
    if rejected_path:
        published_files["rejected"] = rejected_path
    
    # Update index with latest analysis summary
    update_index_with_structured_content(
        docs_dir, timestamp, 
        len(github_items), len(rss_items),
        article_entries,
        github_items
    )
    
    return published_files


def load_rejected_articles(output_dir: str = "outputs") -> List[Dict[str, Any]]:
    """Load and aggregate all rejected articles from JSON files.
    
    Args:
        output_dir: Directory containing rejected_*.json files
        
    Returns:
        List of all rejected articles from all JSON files
    """
    rejected_articles = []
    
    if not os.path.exists(output_dir):
        logging.warning(f"Output directory not found: {output_dir}")
        return rejected_articles
    
    # Find all rejected JSON files
    for filename in os.listdir(output_dir):
        if filename.startswith("rejected_") and filename.endswith(".json"):
            filepath = os.path.join(output_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        rejected_articles.extend(data)
                        logging.info(f"Loaded {len(data)} rejected articles from {filename}")
            except (json.JSONDecodeError, IOError) as e:
                logging.warning(f"Could not read rejected articles from {filename}: {e}")
    
    logging.info(f"Total rejected articles loaded: {len(rejected_articles)}")
    return rejected_articles


def generate_rejected_articles_page(rejected_articles: List[Dict[str, Any]]) -> str:
    """Generate the rejected articles documentation page content.
    
    Args:
        rejected_articles: List of rejected article dictionaries
        
    Returns:
        Markdown content for the rejected articles page
    """
    content = """# Rejected Articles

This page lists all articles that were evaluated but rejected from publication. Articles are rejected when they do not meet Newsbot's relevance or credibility criteria.

## What Constitutes a "Rejected" Article?

Articles are rejected for the following reasons:

### Rejection Type: Relevance

Articles can be rejected as not relevant if they:

1. **Missing AI Keywords** (`missing_ai_keywords`): GitHub repositories that lack keywords related to AI, automation, or fuzzing in offensive security contexts. These repositories may be related to security but don't involve the use of AI or automation.

2. **LLM Applicability Below Threshold** (`llm_applicability_below_threshold`): RSS feed articles that were assessed by the LLM (Large Language Model) but scored below the configured applicability threshold. This typically means:
   - The article doesn't contain sufficient content about offensive security topics (penetration testing, red team operations, vulnerability research, exploit development, etc.), OR
   - The article doesn't explicitly describe the **use** of AI, automation, or fuzzing techniques

   Both requirements must be satisfied for an article to be considered applicable.

### Rejection Type: Credibility

1. **LLM Credibility Below Threshold** (`llm_credibility_below_threshold`): RSS feed articles that scored below the configured credibility threshold. This indicates potential issues with:
   - Source reliability
   - Content quality or accuracy
   - Lack of technical depth
   - Promotional or marketing-focused content

## Rejected Articles Table

Total rejected articles: **{total}**

| Title | Topic | Rejection Type | Rejection Reason |
|-------|-------|----------------|------------------|
"""
    
    # Sort articles by topic, then by rejection type
    sorted_articles = sorted(
        rejected_articles,
        key=lambda x: (
            x.get('topic', 'unknown'),
            x.get('rejection_type', 'unknown'),
            x.get('title', 'Untitled')
        )
    )
    
    # Add table rows
    for article in sorted_articles:
        title = article.get('title', 'Untitled')
        url = article.get('url', '')
        topic = article.get('topic', 'N/A')
        rejection_type = article.get('rejection_type', 'N/A')
        rejection_reason = article.get('rejection_reason', 'N/A')
        
        # Format title as link if URL is available
        if url:
            title_cell = f"[{title}]({url})"
        else:
            title_cell = title
        
        # Format rejection reason with threshold if available
        rejection_threshold = article.get('rejection_threshold')
        if rejection_threshold is not None:
            rejection_reason_cell = f"{rejection_reason} (threshold: {rejection_threshold})"
        else:
            rejection_reason_cell = rejection_reason
        
        content += f"| {title_cell} | {topic} | {rejection_type} | {rejection_reason_cell} |\n"
    
    content = content.format(total=len(rejected_articles))
    
    content += """
---

[← Back to Index](index.md)
"""
    
    return content


def publish_rejected_articles_page(output_dir: str = "outputs", docs_dir: str = "docs") -> Optional[str]:
    """Publish the rejected articles page to docs.
    
    Args:
        output_dir: Directory containing rejected_*.json files
        docs_dir: Target docs directory
        
    Returns:
        Path to the published rejected articles page, or None if failed
    """
    # Load all rejected articles
    rejected_articles = load_rejected_articles(output_dir)
    
    if not rejected_articles:
        logging.warning("No rejected articles found, skipping rejected articles page")
        return None
    
    # Generate page content
    page_content = generate_rejected_articles_page(rejected_articles)
    
    # Add front matter
    formatted_content = "---\nlayout: default\ntitle: Rejected Articles\n---\n\n"
    formatted_content += page_content
    
    # Write to docs directory
    rejected_path = os.path.join(docs_dir, "rejected.md")
    try:
        with open(rejected_path, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        logging.info(f"Published rejected articles page to: {rejected_path}")
        return rejected_path
    except IOError as e:
        logging.error(f"Failed to publish rejected articles page: {e}")
        return None


def load_all_analyzed_articles(output_dir: str = "outputs") -> List[Dict[str, Any]]:
    """Load all analyzed articles from results_*.json files.
    
    This function loads ALL articles without using skip_analyzed logic,
    as it's meant to create a comprehensive historical record.
    
    Args:
        output_dir: Directory containing results_*.json files
        
    Returns:
        List of all analyzed articles from all results files
    """
    all_articles = []
    
    if not os.path.exists(output_dir):
        logging.warning(f"Output directory not found: {output_dir}")
        return all_articles
    
    # Find all results JSON files
    for filename in sorted(os.listdir(output_dir)):
        if filename.startswith("results_") and filename.endswith(".json"):
            filepath = os.path.join(output_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        # Filter for RSS articles only
                        rss_articles = [item for item in data if item.get("source") == "rss"]
                        all_articles.extend(rss_articles)
                        logging.info(f"Loaded {len(rss_articles)} articles from {filename}")
            except (json.JSONDecodeError, IOError) as e:
                logging.warning(f"Could not read articles from {filename}: {e}")
    
    logging.info(f"Total analyzed articles loaded: {len(all_articles)}")
    return all_articles


def load_all_analyzed_repositories(output_dir: str = "outputs") -> List[Dict[str, Any]]:
    """Load all analyzed repositories from results_*.json files.
    
    This function loads ALL repositories without using skip_analyzed logic,
    as it's meant to create a comprehensive historical record.
    
    Args:
        output_dir: Directory containing results_*.json files
        
    Returns:
        List of all analyzed repositories from all results files
    """
    all_repositories = []
    
    if not os.path.exists(output_dir):
        logging.warning(f"Output directory not found: {output_dir}")
        return all_repositories
    
    # Find all results JSON files
    for filename in sorted(os.listdir(output_dir)):
        if filename.startswith("results_") and filename.endswith(".json"):
            filepath = os.path.join(output_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        # Filter for GitHub repositories only
                        github_repos = [item for item in data if item.get("source") == "github"]
                        all_repositories.extend(github_repos)
                        logging.info(f"Loaded {len(github_repos)} repositories from {filename}")
            except (json.JSONDecodeError, IOError) as e:
                logging.warning(f"Could not read repositories from {filename}: {e}")
    
    logging.info(f"Total analyzed repositories loaded: {len(all_repositories)}")
    return all_repositories


def group_articles_by_month(articles: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Group articles by month based on their published date.
    
    Args:
        articles: List of article dictionaries
        
    Returns:
        Dictionary with month strings as keys (e.g., "2026-02") and lists of articles as values
    """
    from collections import defaultdict
    from email.utils import parsedate_to_datetime
    
    grouped = defaultdict(list)
    
    for article in articles:
        published = article.get("published") or article.get("updated")
        if not published:
            grouped["Unknown"].append(article)
            continue
        
        try:
            # Parse the date
            if isinstance(published, str):
                if "T" in published:
                    dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
                else:
                    dt = parsedate_to_datetime(published)
                
                month_key = dt.strftime("%Y-%m")
                grouped[month_key].append(article)
            else:
                grouped["Unknown"].append(article)
        except (TypeError, ValueError) as e:
            logging.warning(f"Could not parse date '{published}': {e}")
            grouped["Unknown"].append(article)
    
    return dict(grouped)


def group_repositories_by_month(repositories: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Group repositories by month based on their updated date.
    
    Args:
        repositories: List of repository dictionaries
        
    Returns:
        Dictionary with month strings as keys (e.g., "2026-02") and lists of repositories as values
    """
    from collections import defaultdict
    
    grouped = defaultdict(list)
    
    for repo in repositories:
        updated = repo.get("updated")
        if not updated:
            grouped["Unknown"].append(repo)
            continue
        
        try:
            # Parse the date
            if isinstance(updated, str):
                dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
                month_key = dt.strftime("%Y-%m")
                grouped[month_key].append(repo)
            else:
                grouped["Unknown"].append(repo)
        except (TypeError, ValueError) as e:
            logging.warning(f"Could not parse date '{updated}': {e}")
            grouped["Unknown"].append(repo)
    
    return dict(grouped)


def generate_comprehensive_articles_page(articles: List[Dict[str, Any]]) -> str:
    """Generate the comprehensive articles page with all articles organized by month.
    
    Args:
        articles: List of all analyzed article dictionaries
        
    Returns:
        Markdown content for the comprehensive articles page
    """
    from email.utils import parsedate_to_datetime
    
    content = """# All Analyzed Articles

This page contains **all articles ever analyzed** by Newsbot, organized by month.

"""
    
    if not articles:
        content += "*No articles found.*\n"
        return content
    
    # Group articles by month
    grouped = group_articles_by_month(articles)
    
    # Sort months in reverse chronological order
    sorted_months = sorted(grouped.keys(), reverse=True)
    
    # Add summary
    content += f"**Total articles:** {len(articles)}\n\n"
    content += f"**Months covered:** {len(sorted_months)}\n\n"
    content += "[← Back to Index](index.md)\n\n"
    content += "---\n\n"
    
    # Generate a table for each month
    for month in sorted_months:
        month_articles = grouped[month]
        
        # Format month header
        if month != "Unknown":
            try:
                dt = datetime.strptime(month, "%Y-%m")
                month_display = dt.strftime("%B %Y")
            except ValueError:
                month_display = month
        else:
            month_display = "Unknown Date"
        
        content += f"## {month_display}\n\n"
        content += f"*{len(month_articles)} article{'s' if len(month_articles) != 1 else ''}*\n\n"
        
        # Sort articles by applicability score (descending), then by date (descending)
        def sort_key(article):
            # Primary sort: applicability score (higher first)
            applicability = article.get("llm_applicability_score", 0)
            
            # Secondary sort: date (newer first)
            published = article.get("published") or article.get("updated")
            try:
                if published:
                    if isinstance(published, str):
                        if "T" in published:
                            dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
                        else:
                            dt = parsedate_to_datetime(published)
                        date_val = dt
                    else:
                        date_val = datetime.min
                else:
                    date_val = datetime.min
            except (TypeError, ValueError):
                date_val = datetime.min
            
            return (-applicability, -date_val.timestamp() if date_val != datetime.min else 0)
        
        sorted_articles = sorted(month_articles, key=sort_key)
        
        # Generate table
        content += "| Source | Date | Applicability | Credibility | Title |\n"
        content += "|--------|------|--------------|-------------|-------|\n"
        
        for article in sorted_articles:
            # Extract domain
            domain = extract_domain_from_url(article.get("url", ""))
            
            # Get scores
            applicability = article.get("llm_applicability_score", 0)
            credibility = article.get("llm_credibility_score", 0)
            
            # Get title and URL
            title = article.get("title", "Untitled Article")
            url = article.get("url", "")
            
            # Escape pipe characters
            title = title.replace('|', '\\|')
            
            # Create title link
            if url:
                title_link = f"[{title}]({url})"
            else:
                title_link = title
            
            # Get date
            published_raw = article.get("published") or article.get("updated")
            date_str = format_date_only(published_raw)
            
            content += f"| {domain} | {date_str} | {applicability:.2f} | {credibility:.2f} | {title_link} |\n"
        
        content += "\n"
    
    content += "---\n\n"
    content += "[← Back to Index](index.md)\n"
    
    return content


def generate_comprehensive_repositories_page(repositories: List[Dict[str, Any]]) -> str:
    """Generate the comprehensive repositories page with all repos organized by month.
    
    Args:
        repositories: List of all analyzed repository dictionaries
        
    Returns:
        Markdown content for the comprehensive repositories page
    """
    content = """# All Analyzed Repositories

This page contains **all GitHub repositories ever analyzed** by Newsbot, organized by month.

"""
    
    if not repositories:
        content += "*No repositories found.*\n"
        return content
    
    # Group repositories by month
    grouped = group_repositories_by_month(repositories)
    
    # Sort months in reverse chronological order
    sorted_months = sorted(grouped.keys(), reverse=True)
    
    # Add summary
    content += f"**Total repositories:** {len(repositories)}\n\n"
    content += f"**Months covered:** {len(sorted_months)}\n\n"
    content += "[← Back to Index](index.md)\n\n"
    content += "---\n\n"
    
    # Generate a table for each month
    for month in sorted_months:
        month_repos = grouped[month]
        
        # Format month header
        if month != "Unknown":
            try:
                dt = datetime.strptime(month, "%Y-%m")
                month_display = dt.strftime("%B %Y")
            except ValueError:
                month_display = month
        else:
            month_display = "Unknown Date"
        
        content += f"## {month_display}\n\n"
        content += f"*{len(month_repos)} repositor{'ies' if len(month_repos) != 1 else 'y'}*\n\n"
        
        # Sort repositories by star count (descending), then by updated date (descending)
        def sort_key(repo):
            # Primary sort: stars (higher first)
            stars = repo.get("stars", 0)
            
            # Secondary sort: date (newer first)
            updated = repo.get("updated")
            try:
                if updated:
                    if isinstance(updated, str):
                        dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
                        date_val = dt
                    else:
                        date_val = datetime.min
                else:
                    date_val = datetime.min
            except (TypeError, ValueError):
                date_val = datetime.min
            
            return (-stars, -date_val.timestamp() if date_val != datetime.min else 0)
        
        sorted_repos = sorted(month_repos, key=sort_key)
        
        # Generate table
        content += "| Repository | Description | Stars | Updated | Topic |\n"
        content += "|------------|-------------|-------|---------|-------|\n"
        
        for repo in sorted_repos:
            # Get repository info
            title = repo.get("title", "Unknown")
            url = repo.get("url", "")
            description = repo.get("description", "")
            stars = repo.get("stars", 0)
            updated = repo.get("updated", "")
            topic = repo.get("topic", "N/A")
            
            # Escape pipe characters
            if description:
                description = description.replace('|', '\\|')
                # Truncate long descriptions
                if len(description) > 100:
                    description = description[:97] + "..."
            
            # Create title link
            if url:
                title_link = f"[{title}]({url})"
            else:
                title_link = title
            
            # Format date
            date_str = format_date_only(updated)
            
            content += f"| {title_link} | {description} | {stars} | {date_str} | {topic} |\n"
        
        content += "\n"
    
    content += "---\n\n"
    content += "[← Back to Index](index.md)\n"
    
    return content


def publish_comprehensive_articles_page(output_dir: str = "outputs", docs_dir: str = "docs") -> Optional[str]:
    """Publish the comprehensive articles page to docs.
    
    This page contains ALL articles ever analyzed, without skip_analyzed logic.
    
    Args:
        output_dir: Directory containing results_*.json files
        docs_dir: Target docs directory
        
    Returns:
        Path to the published articles page, or None if failed
    """
    # Load all analyzed articles (no skip_analyzed)
    all_articles = load_all_analyzed_articles(output_dir)
    
    if not all_articles:
        logging.warning("No articles found, creating empty articles page")
    
    # Generate page content
    page_content = generate_comprehensive_articles_page(all_articles)
    
    # Add front matter
    formatted_content = "---\nlayout: default\ntitle: All Analyzed Articles\n---\n\n"
    formatted_content += page_content
    
    # Write to docs directory
    articles_path = os.path.join(docs_dir, "articles.md")
    try:
        with open(articles_path, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        logging.info(f"Published comprehensive articles page to: {articles_path}")
        return articles_path
    except IOError as e:
        logging.error(f"Failed to publish comprehensive articles page: {e}")
        return None


def publish_comprehensive_repositories_page(output_dir: str = "outputs", docs_dir: str = "docs") -> Optional[str]:
    """Publish the comprehensive repositories page to docs.
    
    This page contains ALL repositories ever analyzed, without skip_analyzed logic.
    
    Args:
        output_dir: Directory containing results_*.json files
        docs_dir: Target docs directory
        
    Returns:
        Path to the published repositories page, or None if failed
    """
    # Load all analyzed repositories (no skip_analyzed)
    all_repositories = load_all_analyzed_repositories(output_dir)
    
    if not all_repositories:
        logging.warning("No repositories found, creating empty repositories page")
    
    # Generate page content
    page_content = generate_comprehensive_repositories_page(all_repositories)
    
    # Add front matter
    formatted_content = "---\nlayout: default\ntitle: All Analyzed Repositories\n---\n\n"
    formatted_content += page_content
    
    # Write to docs directory
    repos_path = os.path.join(docs_dir, "repositories.md")
    try:
        with open(repos_path, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        logging.info(f"Published comprehensive repositories page to: {repos_path}")
        return repos_path
    except IOError as e:
        logging.error(f"Failed to publish comprehensive repositories page: {e}")
        return None


