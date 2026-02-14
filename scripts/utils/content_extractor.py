"""
Article content extraction utilities.
Provides functionality to extract main content from web articles.
"""

import logging
import re
from typing import Optional
import requests
from bs4 import BeautifulSoup


# Maximum characters to extract from article content for LLM processing
MAX_ARTICLE_CONTENT_LENGTH = 5000

# HTTP request timeout in seconds
HTTP_REQUEST_TIMEOUT = 10  # seconds


def extract_article_content(url: str) -> Optional[str]:
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
        response = requests.get(url, headers=headers, timeout=HTTP_REQUEST_TIMEOUT)
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
            return text[:MAX_ARTICLE_CONTENT_LENGTH] if text else None
        
        return None
    except Exception as e:
        logging.debug(f"Could not extract content from {url}: {str(e)[:100]}")
        return None
