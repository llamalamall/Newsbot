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

### [Rejected Articles](rejected.md)
View all articles that were evaluated but rejected from publication due to relevance or credibility criteria.

## Latest Articles

"""
    
    # Ensure the Content section exists with repositories link and rejected articles link
    if "## Content" not in index_content:
        # Add content section before latest articles
        if "## Latest Articles" in index_content or "## Latest Reports" in index_content:
            parts = index_content.split("## Latest", 1)
            header_section = parts[0]
            remaining = "## Latest" + parts[1] if len(parts) > 1 else ""
            
            index_content = header_section + """## Content

### [GitHub Repositories](repositories.md)
Browse all discovered GitHub repositories in a searchable table format.

### [Rejected Articles](rejected.md)
View all articles that were evaluated but rejected from publication due to relevance or credibility criteria.

""" + remaining
    elif "rejected.md" not in index_content:
        # Add rejected articles link to existing Content section
        if "### [GitHub Repositories](repositories.md)" in index_content:
            index_content = index_content.replace(
                "Browse all discovered GitHub repositories in a searchable table format.\n",
                "Browse all discovered GitHub repositories in a searchable table format.\n\n"
                "### [Rejected Articles](rejected.md)\n"
                "View all articles that were evaluated but rejected from publication due to relevance or credibility criteria.\n"
            )
    
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
            
            # Create new entry for this batch with table format
            new_entry = f"### {date_only}\n\n"
            new_entry += f"*{rss_count} article{'s' if rss_count != 1 else ''} published*\n\n"
            
            # Add table header
            new_entry += "| Source | Updated | Applicability | Credibility | Title |\n"
            new_entry += "|--------|---------|--------------|-------------|-------|\n"
            
            # Add table rows
            new_entry += generate_article_table_rows(article_entries)
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
                
                # Add table header
                new_section += "| Source | Updated | Applicability | Credibility | Title |\n"
                new_section += "|--------|---------|--------------|-------------|-------|\n"
                
                # Add table rows
                new_section += generate_article_table_rows(article_entries)
                new_section += "\n"
                
                index_content = main_content + new_section + footer
            else:
                # Just append
                new_section = "\n## Latest Articles\n\n"
                new_section += f"### {date_only}\n\n"
                new_section += f"*{rss_count} article{'s' if rss_count != 1 else ''} published*\n\n"
                
                # Add table header
                new_section += "| Source | Updated | Applicability | Credibility | Title |\n"
                new_section += "|--------|---------|--------------|-------------|-------|\n"
                
                # Add table rows
                new_section += generate_article_table_rows(article_entries)
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
    
    # Separate GitHub repos and RSS articles
    github_items = [r for r in results if r.get("source") == "github"]
    rss_items = [r for r in results if r.get("source") == "rss"]
    
    published_files = {
        "repositories": None,
        "articles": [],
        "rejected": None,
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
    
    # Publish rejected articles page
    rejected_path = publish_rejected_articles_page(output_dir, docs_dir)
    if rejected_path:
        published_files["rejected"] = rejected_path
    
    # Update index with structured content
    update_index_with_structured_content(
        docs_dir, timestamp, 
        len(github_items), len(rss_items),
        article_entries
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


