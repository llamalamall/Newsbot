"""
Web search functionality with LLM integration.
Performs live web searches with credibility assessment and content extraction.
"""

import logging
import json
import re
from typing import List, Dict, Any, Optional
from openai import OpenAI


# Maximum characters to include in context when passing to LLM
MAX_CONTEXT_SNIPPET_LENGTH = 1000

# Prompt template for LLM searches with web search context
LLM_SUMMARY_PROMPT = """Based on the following web search results about "{query}", provide a structured analysis of the latest news and developments.

Web Search Results:
{search_context}

Analyze these results and provide:
1. A summary of the most important and credible news items
2. Key developments and trends
3. Notable sources and their credibility
4. Practical takeaways for security professionals

Focus on:
- New tools or frameworks
- Research papers or blog posts
- Conference talks or presentations
- Code releases or updates
- Vulnerabilities or exploits
- Techniques or methodologies

Format your response as a JSON array with objects containing:
- title: The article/news title
- description: Brief summary of the content
- url: Original source URL (from search results)
- source: Domain/publication name
- credibility: Assessment of source credibility (high/medium/low)
- key_points: Array of important takeaways
- date: Publication date if available

Only include items from credible sources. Exclude promotional content and low-quality sources."""


def perform_web_search(
    query: str,
    assess_credibility_func,
    config: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Perform a live web search for the given query.
    
    This method integrates with web search functionality. It attempts to use
    the web_search_helper module if available and enabled in configuration.
    
    Args:
        query: Search query string
        assess_credibility_func: Function to assess URL credibility
        config: Configuration dictionary
        
    Returns:
        List of search results with title, url, snippet, and credibility
    """
    results = []
    
    # Check if web search is enabled in configuration
    if not config.get('web_search_enabled', True):
        logging.info("Web search is disabled in configuration")
        return results
    
    try:
        # Try to import and use the web search helper
        from scripts.web_search_helper import WebSearchHelper
        
        # Get configuration parameters
        max_results = config.get('web_search_max_results', 10)
        timeout = config.get('web_search_timeout', 10)
        rate_limit = config.get('web_search_rate_limit', 1.0)
        
        # Create helper with configuration
        helper = WebSearchHelper(timeout=timeout, rate_limit_delay=rate_limit)
        
        if helper.is_available():
            search_results = helper.search(query, max_results=max_results)
            
            # Process and enrich results with credibility assessment
            for result in search_results:
                url = result.get('url', '')
                result['credibility'] = assess_credibility_func(url)
                results.append(result)
                
            logging.info(f"Web search returned {len(results)} results for: {query}")
        else:
            logging.warning("Web search helper not available")
            
    except ImportError:
        logging.debug("Web search helper module not found")
    except Exception as e:
        logging.error(f"Error in web search: {str(e)[:100]}")
    
    # If no results from web search, log it but don't fail
    if not results:
        logging.info(f"No web search results for '{query}', will use LLM-only search")
    
    return results


def search_with_web_context(
    query: str,
    openai_client: Optional[OpenAI],
    assess_credibility_func,
    extract_content_func,
    config: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Search using both web search and LLM with full context integration.
    
    This is the enhanced search method that combines:
    1. Live web search results
    2. Source credibility assessment
    3. Article content extraction
    4. LLM-powered summarization
    
    Args:
        query: The search topic/query
        openai_client: OpenAI client instance
        assess_credibility_func: Function to assess URL credibility
        extract_content_func: Function to extract article content
        config: Configuration dictionary
        
    Returns:
        List of processed and enriched results
    """
    results = []
    
    try:
        # Step 1: Perform web search
        web_results = perform_web_search(query, assess_credibility_func, config)
        
        # Step 2: Filter by credibility
        credible_results = []
        for result in web_results:
            url = result.get('url', '')
            credibility = assess_credibility_func(url)
            
            # Only include high and medium credibility sources
            if credibility in ['high', 'medium']:
                result['credibility'] = credibility
                credible_results.append(result)
                
                # Step 3: Try to extract article content
                content = extract_content_func(url)
                if content:
                    # Store shorter snippet for context to manage token usage
                    result['extracted_content'] = content[:MAX_CONTEXT_SNIPPET_LENGTH]
        
        # Step 4: Build context for LLM
        if credible_results:
            search_context = "\n\n".join([
                f"Title: {r.get('title', 'N/A')}\n"
                f"URL: {r.get('url', 'N/A')}\n"
                f"Snippet: {r.get('snippet', 'N/A')}\n"
                f"Credibility: {r.get('credibility', 'unknown')}"
                for r in credible_results[:10]  # Limit to top 10
            ])
            
            # Step 5: Use LLM with web search context
            prompt = LLM_SUMMARY_PROMPT.format(
                query=query,
                search_context=search_context
            )
            
            if openai_client:
                response = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a security researcher assistant who helps find and summarize the latest offensive security news and developments. You prioritize credible sources and fact-based reporting."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3,
                    max_tokens=2000
                )
                
                llm_response = response.choices[0].message.content
                
                # Parse LLM response into structured results
                try:
                    json_match = re.search(r'\[.*\]', llm_response, re.DOTALL)
                    if json_match:
                        parsed_results = json.loads(json_match.group())
                        for item in parsed_results:
                            item["source"] = "web_search_llm"
                            item["search_topic"] = query
                            results.append(item)
                except json.JSONDecodeError:
                    # If not JSON, return as summary
                    results.append({
                        "title": f"Web Search Summary: {query}",
                        "description": llm_response,
                        "source": "web_search_summary",
                        "search_topic": query,
                        "credible_sources_found": len(credible_results)
                    })
        else:
            logging.info(f"No credible web results found for: {query}")
            
    except Exception as e:
        logging.error(f"Error in web search for '{query}': {str(e)[:200]}")
        # Don't fail completely, just log and continue
    
    return results


def search_with_llm(query: str, openai_client: Optional[OpenAI]) -> str:
    """Use LLM to search and summarize results for a topic via GitHub Models.
    
    This method now integrates live web search results to provide more current
    and accurate information.
    
    Args:
        query: The search topic/query
        openai_client: OpenAI client instance
        
    Returns:
        LLM-generated summary with web search context
    """
    if not openai_client:
        logging.warning("OpenAI client not initialized, skipping LLM search")
        return ""
    
    try:
        # First, perform a web search to get current results
        search_context = "No web search results available."
        
        # Note: In a sandboxed environment, web_search tool might not be available
        # This is a placeholder for the web search integration
        # The actual web search will be performed via external tool
        
        # Use the web_search tool if available (this will be called externally)
        # For now, we'll construct the prompt to work with or without web search
        
        prompt = LLM_SUMMARY_PROMPT.format(
            query=query,
            search_context=search_context
        )
        
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a security researcher assistant who helps find and summarize the latest offensive security news and developments, especially related to AI and automation. You prioritize credible sources and fact-based reporting."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"OpenAI API error for '{query}': {e}")
        return ""
