#!/usr/bin/env python3
"""
External web search runner for Newsbot.
This script performs web searches and outputs results in JSON format.
It's designed to be called as a subprocess from the main newsbot script.
"""

import sys
import json
import os
import logging
from typing import Dict, Any

# Add the parent directory to the path to import web_search_helper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from web_search_helper import WebSearchHelper


def perform_web_search(query: str, max_results: int = 10) -> Dict[str, Any]:
    """Perform a web search using the WebSearchHelper.
    
    This function uses the WebSearchHelper class to perform actual web searches
    using DuckDuckGo's HTML interface.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return (default: 10)
        
    Returns:
        Dictionary with search results and metadata containing:
            - success: Boolean indicating if search was successful
            - query: The original search query
            - results: List of search results (title, url, snippet)
            - count: Number of results found
            - error: Error message if search failed
    """
    result = {
        "success": False,
        "query": query,
        "results": [],
        "count": 0,
        "error": None
    }
    
    try:
        # Configure logging for the runner
        logging.basicConfig(
            level=logging.INFO,
            format='%(levelname)s: %(message)s'
        )
        
        # Create web search helper and perform search
        helper = WebSearchHelper()
        
        if not helper.is_available():
            result["error"] = "Web search helper is not available"
            return result
        
        # Perform the search
        search_results = helper.search(query, max_results=max_results)
        
        if search_results:
            result["success"] = True
            result["results"] = search_results
            result["count"] = len(search_results)
        else:
            result["error"] = "No search results found"
        
    except Exception as e:
        result["error"] = str(e)
        logging.error(f"Error in web search: {str(e)}")
    
    return result


def main():
    """Main entry point for command-line usage."""
    if len(sys.argv) < 2:
        print(json.dumps({
            "success": False,
            "error": "No query provided. Usage: web_search_runner.py <query> [max_results]"
        }))
        sys.exit(1)
    
    # Parse command line arguments
    max_results = 10
    if len(sys.argv) >= 3:
        try:
            max_results = int(sys.argv[-1])
            query = " ".join(sys.argv[1:-1])
        except ValueError:
            query = " ".join(sys.argv[1:])
    else:
        query = " ".join(sys.argv[1:])
    
    # Perform search
    result = perform_web_search(query, max_results)
    
    # Output as JSON
    print(json.dumps(result, indent=2))
    
    # Exit with appropriate code
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
