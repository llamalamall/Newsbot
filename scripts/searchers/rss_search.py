"""
RSS feed search functionality.
Searches and aggregates content from RSS feeds with optional LLM assessment.
"""

import logging
from typing import List, Dict, Any, Optional

# Import dataclass models
try:
    from ..models import RSSResult
    from ..utils.llm_assessment import (
        assess_article_applicability,
        assess_article_credibility,
        filter_titles_by_relevance,
        get_llm_call_count,
        reset_llm_call_count
    )
except ImportError:
    # Fallback for direct execution
    import sys
    import os
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    from models import RSSResult
    from utils.llm_assessment import (
        assess_article_applicability,
        assess_article_credibility,
        filter_titles_by_relevance,
        get_llm_call_count,
        reset_llm_call_count
    )


def search_rss_feeds(
    rss_manager,
    assess_credibility_func,
    config: Dict[str, Any],
    openai_client=None,
    rejected_results: Optional[List[Dict[str, Any]]] = None
) -> List[Dict[str, Any]]:
    """Search and aggregate content from RSS feeds.
    
    This method fetches all configured RSS feeds, filters them by date
    and keywords, and optionally uses LLM to assess applicability and credibility.
    
    Args:
        rss_manager: RSSFeedManager instance
        assess_credibility_func: Function to assess URL credibility
        config: Configuration dictionary
        openai_client: Optional OpenAI client for LLM assessment
        rejected_results: Optional list to append filtered-out articles
        
    Returns:
        List of relevant RSS feed entries
    """
    results = []
    
    if not rss_manager:
        logging.info("RSS Feed Manager not initialized, skipping RSS search")
        return results
    
    reset_llm_call_count()

    try:
        logging.info("Fetching RSS feeds...")
        
        # Get RSS feed configuration
        feeds = config.get('rss_feeds', [])
        if not feeds:
            logging.warning("No RSS feeds configured")
            return results
        
        # Get RSS settings
        rss_settings = config.get('rss_settings', {})
        max_age_days = rss_settings.get('max_age_days', config.get('days_back', 7))
        min_keyword_matches = rss_settings.get('min_keyword_matches', 1)
        
        # Get LLM assessment settings
        llm_settings = config.get('llm_assessment', {})
        llm_enabled = llm_settings.get('enabled', False)
        llm_model = llm_settings.get('model', 'gpt-4o-mini')
        applicability_threshold = llm_settings.get('applicability_threshold', 0.6)
        credibility_threshold = llm_settings.get('credibility_threshold', 0.5)
        filter_inapplicable = llm_settings.get('filter_inapplicable', True)
        filter_not_credible = llm_settings.get('filter_not_credible', True)
        
        # Fetch all feeds
        all_entries = rss_manager.fetch_all_feeds(feeds)
        
        # Filter by date
        recent_entries = rss_manager.filter_by_date(all_entries, max_age_days)
        
        # Filter by keywords (fallback if LLM returns no results)
        keywords = config.get('search_keywords', [])
        filtered_entries = recent_entries
        if llm_enabled and openai_client:
            titles = [entry.get('title', '') for entry in recent_entries]
            relevant_indices = filter_titles_by_relevance(
                openai_client=openai_client,
                titles=titles,
                keywords=keywords,
                model=llm_model
            )
            if relevant_indices:
                filtered_entries = [recent_entries[idx] for idx in relevant_indices]
            else:
                logging.info("LLM title filtering returned no results; applying keyword filtering")
                if keywords:
                    filtered_entries = rss_manager.filter_by_keywords(
                        recent_entries,
                        keywords,
                        min_keyword_matches
                    )
        elif keywords:
            filtered_entries = rss_manager.filter_by_keywords(
                recent_entries,
                keywords,
                min_keyword_matches
            )
        
        logging.info(f"Processing {len(filtered_entries)} articles after keyword filtering...")
        
        # Convert to NewsBot result format and apply LLM assessment if enabled
        for entry in filtered_entries:
            # Assess source credibility first (domain-based)
            url = entry.get('link', '')
            credibility = assess_credibility_func(url) if url else None
            
            # Create initial result
            result = RSSResult(
                title=entry.get('title', 'Untitled'),
                url=url,
                description=entry.get('description', ''),
                source='rss',
                credibility=credibility,
                published=entry.get('published'),
                feed_name=entry.get('feed_name', 'Unknown Feed'),
                feed_category=entry.get('category'),
                priority=entry.get('priority', 'medium'),
                keyword_matches=entry.get('keyword_matches', 0),
                author=entry.get('author'),
                tags=entry.get('tags', [])
            )
            
            # Apply LLM assessment if enabled and client is available
            if llm_enabled and openai_client:
                try:
                    # Assess applicability
                    applicability_result = assess_article_applicability(
                        openai_client=openai_client,
                        title=result.title,
                        description=result.description,
                        keywords=keywords,
                        model=llm_model
                    )
                    
                    result.llm_applicable = applicability_result.get('applicable', True)
                    result.llm_applicability_score = applicability_result.get('score', 0.5)
                    result.llm_applicability_reason = applicability_result.get('reason', '')
                    result.llm_matched_keywords = applicability_result.get('matched_keywords', [])
                    
                    # Assess credibility with LLM
                    credibility_result = assess_article_credibility(
                        openai_client=openai_client,
                        title=result.title,
                        description=result.description,
                        url=result.url,
                        source_name=result.feed_name,
                        domain_credibility=result.credibility or 'unknown',
                        model=llm_model
                    )
                    
                    result.llm_credible = credibility_result.get('credible', True)
                    result.llm_credibility_score = credibility_result.get('score', 0.5)
                    result.llm_credibility_reason = credibility_result.get('reason', '')
                    result.llm_credibility_flags = credibility_result.get('flags', [])
                    
                    # Apply filtering based on LLM assessment
                    # Filter if applicability score is below threshold
                    if filter_inapplicable and result.llm_applicability_score < applicability_threshold:
                        logging.debug(f"Filtered out (inapplicable, score={result.llm_applicability_score:.2f}): {result.title[:50]}...")
                        if rejected_results is not None:
                            rejected = result.to_dict()
                            rejected["rejection_type"] = "relevance"
                            rejected["rejection_reason"] = "llm_applicability_below_threshold"
                            rejected["rejection_threshold"] = applicability_threshold
                            rejected_results.append(rejected)
                        continue
                    
                    # Filter if credibility score is below threshold
                    if filter_not_credible and result.llm_credibility_score < credibility_threshold:
                        logging.debug(f"Filtered out (not credible, score={result.llm_credibility_score:.2f}): {result.title[:50]}...")
                        if rejected_results is not None:
                            rejected = result.to_dict()
                            rejected["rejection_type"] = "credibility"
                            rejected["rejection_reason"] = "llm_credibility_below_threshold"
                            rejected["rejection_threshold"] = credibility_threshold
                            rejected_results.append(rejected)
                        continue
                    
                except Exception as e:
                    logging.warning(f"LLM assessment failed for '{result.title[:50]}...': {str(e)}")
                    # Continue with the article even if LLM assessment fails
            
            results.append(result.to_dict())
        
        logging.info(f"Found {len(results)} relevant articles from RSS feeds after LLM filtering")
        
    except Exception as e:
        logging.error(f"Error in RSS feed search: {str(e)}")
    finally:
        logging.info(f"Total LLM calls for RSS search: {get_llm_call_count()}")
    
    return results
