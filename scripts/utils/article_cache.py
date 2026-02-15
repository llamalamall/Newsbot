"""
Article cache functionality for detecting and skipping already analyzed articles.
Provides utilities to track and filter out articles that have already been processed.
"""

import json
import logging
import os
from typing import List, Dict, Any, Set
from pathlib import Path


def generate_article_id(article: Dict[str, Any]) -> str:
    """Generate a unique identifier for an article.
    
    Uses the URL as the primary identifier since it uniquely identifies an article.
    
    Args:
        article: Article dictionary with at least a 'url' field
        
    Returns:
        Unique string identifier for the article
    """
    url = article.get('url', '')
    if not url:
        # Fallback to title if URL is missing (shouldn't happen in normal operation)
        return article.get('title', '').lower().strip()
    return url.strip()


def load_analyzed_articles(output_dir: str) -> Set[str]:
    """Load previously analyzed articles from JSON files in the output directory.
    
    Scans all results_*.json files in the output directory and extracts article URLs
    to create a set of already-analyzed article identifiers.
    
    Args:
        output_dir: Directory containing previous output JSON files
        
    Returns:
        Set of article identifiers (URLs) that have been previously analyzed
    """
    analyzed_ids = set()
    
    if not os.path.exists(output_dir):
        logging.debug(f"Output directory does not exist: {output_dir}")
        return analyzed_ids
    
    # Find all results JSON files (only results, not rejected)
    output_path = Path(output_dir)
    json_files = list(output_path.glob('results_*.json'))
    
    if not json_files:
        logging.debug(f"No previous results found in {output_dir}")
        return analyzed_ids
    
    logging.info(f"Loading previously analyzed articles from {len(json_files)} result file(s)...")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                results = json.load(f)
                
            if not isinstance(results, list):
                logging.warning(f"Unexpected format in {json_file.name}, expected list")
                continue
            
            for article in results:
                article_id = generate_article_id(article)
                if article_id:  # Only add non-empty IDs
                    analyzed_ids.add(article_id)
                else:
                    logging.debug(f"Skipping article with no URL or title in {json_file.name}")
                    
        except json.JSONDecodeError as e:
            logging.warning(f"Failed to parse {json_file.name}: {e}")
        except Exception as e:
            logging.warning(f"Error reading {json_file.name}: {e}")
    
    logging.info(f"Loaded {len(analyzed_ids)} previously analyzed articles")
    return analyzed_ids


def filter_analyzed_articles(
    articles: List[Dict[str, Any]], 
    analyzed_ids: Set[str]
) -> tuple[List[Dict[str, Any]], int]:
    """Filter out articles that have already been analyzed.
    
    Args:
        articles: List of article dictionaries to filter
        analyzed_ids: Set of article identifiers that have been previously analyzed
        
    Returns:
        Tuple of (filtered_articles, skipped_count):
            - filtered_articles: List of new articles not in analyzed_ids
            - skipped_count: Number of articles that were skipped
    """
    if not analyzed_ids:
        # No articles to filter, return all
        return articles, 0
    
    new_articles = []
    skipped_count = 0
    
    for article in articles:
        article_id = generate_article_id(article)
        if article_id and article_id in analyzed_ids:
            skipped_count += 1
            logging.debug(f"Skipping already analyzed article: {article.get('title', 'Untitled')}")
        else:
            new_articles.append(article)
    
    if skipped_count > 0:
        logging.info(f"Skipped {skipped_count} already analyzed article(s)")
        logging.info(f"Processing {len(new_articles)} new article(s)")
    
    return new_articles, skipped_count
