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


def format_report_for_docs(report_content: str, timestamp: str, metadata: Optional[Dict[str, Any]] = None) -> str:
    """Format a markdown report for GitHub Pages documentation.
    
    Args:
        report_content: Original markdown report content
        timestamp: Timestamp of the report (YYYYMMDD_HHMMSS format)
        metadata: Optional metadata about the report (e.g., result counts)
        
    Returns:
        Formatted markdown content suitable for GitHub Pages
    """
    # Parse timestamp into a readable date
    try:
        dt = datetime.strptime(timestamp, "%Y%m%d_%H%M%S")
        readable_date = dt.strftime("%B %d, %Y at %H:%M UTC")
    except ValueError:
        readable_date = timestamp
    
    # Add front matter for better GitHub Pages formatting
    formatted = f"---\nlayout: default\ntitle: Report - {readable_date}\n---\n\n"
    formatted += f"[← Back to Index](index.md)\n\n"
    formatted += report_content
    
    # Add footer with navigation
    formatted += f"\n\n---\n\n"
    formatted += f"[← Back to Index](index.md)\n"
    
    return formatted


def get_existing_reports(docs_dir: str) -> List[Dict[str, str]]:
    """Get list of existing reports in docs directory.
    
    Args:
        docs_dir: Path to the docs directory
        
    Returns:
        List of dictionaries containing report metadata (filename, timestamp, path)
    """
    reports = []
    
    if not os.path.exists(docs_dir):
        return reports
    
    for filename in os.listdir(docs_dir):
        if filename.startswith("report_") and filename.endswith(".md"):
            # Extract timestamp from filename
            timestamp = filename.replace("report_", "").replace(".md", "")
            reports.append({
                "filename": filename,
                "timestamp": timestamp,
                "path": os.path.join(docs_dir, filename)
            })
    
    # Sort by timestamp (newest first)
    reports.sort(key=lambda x: x["timestamp"], reverse=True)
    
    return reports


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
    domain = urlparse(url).netloc if url else ""
    domain = domain or "unknown-source"
    title_text = (title or "Untitled").strip()
    combined = f"{domain} - {title_text}" if title_text else domain

    if max_length > 3 and len(combined) > max_length:
        combined = combined[: max_length - 3].rstrip() + "..."

    return combined


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


def update_index(docs_dir: str, new_report_filename: str, new_report_timestamp: str, 
                 result_count: int = 0) -> None:
    """Update the docs/index.md with a new report entry.
    
    Args:
        docs_dir: Path to the docs directory
        new_report_filename: Filename of the new report
        new_report_timestamp: Timestamp of the new report
        result_count: Number of results in the report
    """
    index_path = os.path.join(docs_dir, "index.md")
    
    # Parse timestamp for readable date
    try:
        dt = datetime.strptime(new_report_timestamp, "%Y%m%d_%H%M%S")
        readable_date = dt.strftime("%B %d, %Y at %H:%M UTC")
    except ValueError:
        readable_date = new_report_timestamp
    
    # Read existing index if it exists
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            index_content = f.read()
        
        # Check if this report is already in the index
        if new_report_filename in index_content:
            logging.info(f"Report {new_report_filename} already exists in index, skipping update")
            return
    else:
        # Create new index with header
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

"""
    
    # Find where to insert the new report (after "## Latest Reports" section)
    if "## Latest Reports" in index_content:
        # Split at the Latest Reports section
        parts = index_content.split("## Latest Reports", 1)
        header = parts[0] + "## Latest Reports\n\n"
        
        # Extract existing report entries and footer
        remaining = parts[1] if len(parts) > 1 else ""
        
        # Remove the placeholder text if it exists
        if "*No reports yet" in remaining:
            # Split at the placeholder to remove it
            remaining_parts = remaining.split("*No reports yet", 1)
            if len(remaining_parts) > 1:
                # Keep only what comes after the placeholder (usually the footer)
                footer_start = remaining_parts[1].find("\n---")
                if footer_start >= 0:
                    remaining = remaining_parts[1][footer_start:]
                else:
                    remaining = ""
            else:
                remaining = remaining_parts[0]
        
        # Build new entry
        result_text = f" ({result_count} results)" if result_count > 0 else ""
        new_entry = f"- [{readable_date}]({new_report_filename}){result_text}\n"
        
        # Extract existing entries and footer
        lines = remaining.split('\n')
        entries = []
        footer = []
        in_footer = False
        
        for line in lines:
            if line.strip().startswith('---'):
                in_footer = True
            
            if in_footer:
                footer.append(line)
            elif line.strip().startswith('- ['):
                entries.append(line)
        
        # Parse entries to sort by timestamp (newest first)
        entry_list = []
        for entry in entries:
            # Try to extract timestamp from filename in the entry
            match = re.search(r'report_(\d{8}_\d{6})\.md', entry)
            if match:
                entry_timestamp = match.group(1)
                entry_list.append((entry_timestamp, entry))
            else:
                entry_list.append(('00000000_000000', entry))
        
        # Add new entry
        entry_list.append((new_report_timestamp, new_entry.strip()))
        
        # Sort by timestamp (newest first)
        entry_list.sort(key=lambda x: x[0], reverse=True)
        
        # Rebuild content
        sorted_entries = '\n'.join(entry[1] for entry in entry_list)
        footer_text = '\n'.join(footer) if footer else ""
        
        index_content = header + sorted_entries + '\n' + footer_text
    else:
        # Fallback: append at the end
        result_text = f" ({result_count} results)" if result_count > 0 else ""
        new_entry = f"\n- [{readable_date}]({new_report_filename}){result_text}\n"
        index_content += new_entry
    
    index_content = ensure_index_front_matter(index_content)

    # Write updated index
    with open(index_path, 'w') as f:
        f.write(index_content)
    
    logging.info(f"Updated docs/index.md with new report: {new_report_filename}")


def publish_report_to_docs(report_path: str, docs_dir: str = "docs", 
                           result_count: int = 0) -> Optional[str]:
    """Publish a report to the docs/ directory for GitHub Pages.
    
    Args:
        report_path: Path to the original report markdown file
        docs_dir: Target docs directory (default: "docs")
        result_count: Number of results in the report
        
    Returns:
        Path to the published docs file, or None if publishing failed
    """
    if not os.path.exists(report_path):
        logging.error(f"Report file not found: {report_path}")
        return None
    
    # Create docs directory if it doesn't exist
    os.makedirs(docs_dir, exist_ok=True)
    
    # Extract filename and timestamp
    filename = os.path.basename(report_path)
    timestamp = filename.replace("report_", "").replace(".md", "")
    
    # Check if this report already exists in docs
    docs_report_path = os.path.join(docs_dir, filename)
    if os.path.exists(docs_report_path):
        logging.info(f"Report already exists in docs: {filename}, skipping")
        return docs_report_path
    
    # Read original report
    with open(report_path, 'r') as f:
        report_content = f.read()
    
    # Format for docs
    formatted_content = format_report_for_docs(report_content, timestamp)
    
    # Write to docs directory
    with open(docs_report_path, 'w') as f:
        f.write(formatted_content)
    
    logging.info(f"Published report to docs: {docs_report_path}")
    
    # Update index
    update_index(docs_dir, filename, timestamp, result_count)
    
    return docs_report_path


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
                "published": article.get("published")
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
    article_entries: Optional[List[Dict[str, str]]] = None
) -> None:
    """Update index.md with structured links to repositories and articles.
    
    Args:
        docs_dir: Path to the docs directory
        timestamp: Timestamp of the report (YYYYMMDD_HHMMSS format)
        github_count: Number of GitHub repositories
        rss_count: Number of RSS articles
        article_entries: List of article metadata dictionaries
    """
    index_path = os.path.join(docs_dir, "index.md")
    
    # Parse timestamp for readable date
    try:
        dt = datetime.strptime(timestamp, "%Y%m%d_%H%M%S")
        readable_date = dt.strftime("%B %d, %Y at %H:%M UTC")
        date_only = dt.strftime("%B %d, %Y")
    except ValueError:
        readable_date = timestamp
        date_only = timestamp
    
    # Read existing index if it exists
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            index_content = f.read()
    else:
        # Create new index with header
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

## Content

### [GitHub Repositories](repositories.md)
Browse all discovered GitHub repositories in a searchable table format.

## Latest Articles

"""
    
    # Ensure the repositories link exists
    if "## Content" not in index_content:
        # Add content section before latest articles
        if "## Latest Articles" in index_content or "## Latest Reports" in index_content:
            parts = index_content.split("## Latest", 1)
            header_section = parts[0]
            remaining = "## Latest" + parts[1] if len(parts) > 1 else ""
            
            index_content = header_section + """## Content

### [GitHub Repositories](repositories.md)
Browse all discovered GitHub repositories in a searchable table format.

""" + remaining
    
    # Update or add articles section
    if article_entries and rss_count > 0:
        # Find where to insert new articles
        if "## Latest Articles" in index_content:
            parts = index_content.split("## Latest Articles", 1)
            header = parts[0] + "## Latest Articles\n\n"
            remaining = parts[1] if len(parts) > 1 else ""
            
            # Remove placeholder if it exists
            if "*No articles yet" in remaining:
                remaining_parts = remaining.split("*No articles yet", 1)
                if len(remaining_parts) > 1:
                    footer_start = remaining_parts[1].find("\n---")
                    if footer_start >= 0:
                        remaining = remaining_parts[1][footer_start:]
                    else:
                        remaining = ""
            
            # Parse existing article entries
            lines = remaining.split('\n')
            entries = []
            footer = []
            in_footer = False
            
            for line in lines:
                if line.strip().startswith('---'):
                    in_footer = True
                
                if in_footer:
                    footer.append(line)
                elif line.strip().startswith('###') or line.strip().startswith('-'):
                    entries.append(line)
            
            # Create new entry for this batch
            new_entry = f"### {date_only}\n\n"
            new_entry += f"*{rss_count} article{'s' if rss_count != 1 else ''} published*\n\n"
            
            # Add links to individual articles
            for entry in sort_articles_by_published(article_entries):
                article_file = entry.get("filename", "")
                if not article_file:
                    continue
                link_title = format_article_link_title(entry.get("title", ""), entry.get("url", ""))
                new_entry += f"- [{link_title}](articles/{article_file})\n"
            new_entry += "\n"
            
            # Combine with existing entries
            all_entries = new_entry + '\n'.join(entries)
            footer_text = '\n'.join(footer) if footer else ""
            
            index_content = header + all_entries + footer_text
        else:
            # Add articles section before footer
            if "---" in index_content:
                parts = index_content.rsplit("---", 1)
                main_content = parts[0]
                footer = "\n\n---" + parts[1]
                
                new_section = "## Latest Articles\n\n"
                new_section += f"### {date_only}\n\n"
                new_section += f"*{rss_count} article{'s' if rss_count != 1 else ''} published*\n\n"
                for entry in sort_articles_by_published(article_entries):
                    article_file = entry.get("filename", "")
                    if not article_file:
                        continue
                    link_title = format_article_link_title(entry.get("title", ""), entry.get("url", ""))
                    new_section += f"- [{link_title}](articles/{article_file})\n"
                new_section += "\n"
                
                index_content = main_content + new_section + footer
            else:
                # Just append
                new_section = "\n## Latest Articles\n\n"
                new_section += f"### {date_only}\n\n"
                new_section += f"*{rss_count} article{'s' if rss_count != 1 else ''} published*\n\n"
                for entry in sort_articles_by_published(article_entries):
                    article_file = entry.get("filename", "")
                    if not article_file:
                        continue
                    link_title = format_article_link_title(entry.get("title", ""), entry.get("url", ""))
                    new_section += f"- [{link_title}](articles/{article_file})\n"
                index_content += new_section
    
    # Ensure footer exists
    if "[View on GitHub]" not in index_content:
        if not index_content.endswith('\n'):
            index_content += '\n'
        index_content += "\n---\n\n[View on GitHub](https://github.com/llamalamall/Newsbot)\n"
    
    index_content = ensure_index_front_matter(index_content)

    # Write updated index
    with open(index_path, 'w') as f:
        f.write(index_content)
    
    logging.info(f"Updated docs/index.md with structured content")


def publish_structured_docs(results: List[Dict[str, Any]], timestamp: str,
                           docs_dir: str = "docs") -> Dict[str, Any]:
    """Publish documentation in the new structured format.
    
    Args:
        results: List of all results (GitHub repos and RSS articles)
        timestamp: Timestamp for this batch (YYYYMMDD_HHMMSS format)
        docs_dir: Target docs directory
        
    Returns:
        Dictionary with paths to published files
    """
    # Initialize docs directory
    initialize_docs_directory(docs_dir)
    
    # Separate GitHub repos and RSS articles
    github_items = [r for r in results if r.get("source") == "github"]
    rss_items = [r for r in results if r.get("source") == "rss"]
    
    published_files = {
        "repositories": None,
        "articles": [],
        "index": os.path.join(docs_dir, "index.md")
    }
    
    # Publish repositories page
    if github_items:
        repos_path = publish_repositories_page(github_items, docs_dir)
        published_files["repositories"] = repos_path
    
    # Publish individual article pages
    article_entries: List[Dict[str, str]] = []
    if rss_items:
        article_entries = publish_rss_article_pages(rss_items, timestamp, docs_dir)
        published_files["articles"] = [entry["path"] for entry in article_entries]
    
    # Update index with structured content
    update_index_with_structured_content(
        docs_dir, timestamp, 
        len(github_items), len(rss_items),
        article_entries
    )
    
    return published_files


def publish_latest_report(output_dir: str = "outputs", docs_dir: str = "docs") -> Optional[str]:
    """Find and publish the most recent report from outputs to docs.
    
    Args:
        output_dir: Directory containing output reports
        docs_dir: Target docs directory
        
    Returns:
        Path to published docs file, or None if no reports found
    """
    if not os.path.exists(output_dir):
        logging.warning(f"Output directory not found: {output_dir}")
        return None
    
    # Find all report files
    reports = []
    for filename in os.listdir(output_dir):
        if filename.startswith("report_") and filename.endswith(".md"):
            timestamp = filename.replace("report_", "").replace(".md", "")
            reports.append({
                "filename": filename,
                "timestamp": timestamp,
                "path": os.path.join(output_dir, filename)
            })
    
    if not reports:
        logging.warning("No reports found in output directory")
        return None
    
    # Sort by timestamp and get the latest
    reports.sort(key=lambda x: x["timestamp"], reverse=True)
    latest_report = reports[0]
    
    json_path = os.path.join(output_dir, f"results_{latest_report['timestamp']}.json")
    return publish_report_from_path(latest_report["path"], docs_dir, json_path)


def publish_report_from_path(
    report_path: str,
    docs_dir: str = "docs",
    results_path: Optional[str] = None
) -> Optional[str]:
    """Publish a specific report file to docs with structured content.

    Args:
        report_path: Path to the report markdown file
        docs_dir: Target docs directory
        results_path: Optional path to JSON results for structured publishing

    Returns:
        Path to the published index file, or None if publishing failed
    """
    if not os.path.exists(report_path):
        logging.error(f"Report file not found: {report_path}")
        return None

    if results_path is None:
        report_dir = os.path.dirname(report_path)
        filename = os.path.basename(report_path)
        timestamp = filename.replace("report_", "").replace(".md", "")
        results_path = os.path.join(report_dir, f"results_{timestamp}.json")
    else:
        filename = os.path.basename(report_path)
        timestamp = filename.replace("report_", "").replace(".md", "")

    if not results_path or not os.path.exists(results_path):
        logging.error(f"Results JSON not found: {results_path}")
        return None

    try:
        with open(results_path, 'r') as f:
            results = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logging.warning(f"Could not read results JSON: {e}")
        return None

    if not isinstance(results, list):
        logging.warning("Results JSON is not a list; skipping structured publish")
        return None

    initialize_docs_directory(docs_dir)
    published_files = publish_structured_docs(results, timestamp, docs_dir)
    return published_files.get("index")
