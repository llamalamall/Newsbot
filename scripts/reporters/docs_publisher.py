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
    
    # Create .nojekyll to disable Jekyll processing
    nojekyll_path = os.path.join(docs_dir, ".nojekyll")
    if not os.path.exists(nojekyll_path):
        with open(nojekyll_path, 'w') as f:
            f.write("")
        logging.info("Created .nojekyll file")
    
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
- `.nojekyll` - Disables Jekyll processing for cleaner URLs
- `_config.yml` - Jekyll configuration for GitHub Pages

## Customization

You can customize the look and feel by:
- Editing `_config.yml` for Jekyll configuration (theme, title, description)
- Creating custom CSS in a `assets/` directory
- Modifying the report templates in the publisher script

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
- Verify .nojekyll file exists (disables default Jekyll processing)
- Wait 1-2 minutes after pushing changes

**Build failures:**
- Check the Actions tab for error messages
- Ensure _config.yml syntax is valid YAML
- Verify all markdown files have valid syntax

**Broken links:**
- Use relative links (e.g., `[link](report.md)` not `[link](/docs/report.md)`)
- Check that linked files exist in the docs/ folder

**Styling issues:**
- Verify _config.yml theme setting
- Check that front matter is properly formatted in report files
- Consider adding custom CSS in assets/ directory
"""
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        logging.info("Created docs/README.md")
    
    # Create _config.yml for Jekyll configuration
    config_path = os.path.join(docs_dir, "_config.yml")
    if not os.path.exists(config_path):
        config_content = """# Jekyll configuration for GitHub Pages
# This file configures how GitHub Pages renders the documentation

# Site settings
title: Newsbot - Security News Aggregator
description: Automated news aggregation for AI and automation in offensive security
baseurl: ""
url: "https://llamalamall.github.io"

# GitHub metadata
github:
  repository_url: https://github.com/llamalamall/Newsbot
  is_project_page: true

# Theme (using GitHub Pages default)
# You can change this to: jekyll-theme-cayman, jekyll-theme-minimal, etc.
theme: jekyll-theme-slate

# Markdown settings
markdown: kramdown
kramdown:
  input: GFM
  syntax_highlighter: rouge
  syntax_highlighter_opts:
    css_class: 'highlight'

# Plugins
plugins:
  - jekyll-relative-links
  - jekyll-optional-front-matter

# Enable relative links
relative_links:
  enabled: true
  collections: false

# Make all markdown files render without front matter
optional_front_matter:
  enabled: true

# Exclude files from processing
exclude:
  - README.md
  - .nojekyll

# Include dotfiles
include:
  - .nojekyll
"""
        with open(config_path, 'w') as f:
            f.write(config_content)
        logging.info("Created docs/_config.yml")
    
    logging.info(f"Docs directory initialized at: {docs_dir}")


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
    
    # Try to find corresponding JSON results file for result count
    result_count = 0
    json_path = os.path.join(output_dir, f"results_{latest_report['timestamp']}.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r') as f:
                results = json.load(f)
                result_count = len(results) if isinstance(results, list) else 0
        except (json.JSONDecodeError, IOError) as e:
            logging.warning(f"Could not read results JSON: {e}")
    
    # Initialize docs directory
    initialize_docs_directory(docs_dir)
    
    # Publish the report
    return publish_report_to_docs(latest_report["path"], docs_dir, result_count)
