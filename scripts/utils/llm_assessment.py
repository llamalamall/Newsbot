"""
LLM-based article assessment utilities.
Provides functionality to assess article applicability and credibility using GitHub Models LLM.

APPLICABILITY ASSESSMENT LOGIC:
Articles must satisfy BOTH requirements to be considered applicable:
1. Contains keywords related to offensive security (penetration testing, red team, 
   vulnerability research, exploit development, malware analysis, etc.)
2. Explicitly describes the USE of AI, automation, or fuzzing within the article content

This dual requirement ensures that:
- Articles about traditional/manual security techniques (without AI/automation) are rejected
- Articles about AI/automation in non-security contexts are rejected
- Only articles that combine offensive security with AI/automation/fuzzing are surfaced

The prompts enforce this by instructing the LLM to be "highly selective" and only mark
articles as applicable when there is "explicit textual evidence" of AI/automation/fuzzing
being used for offensive security purposes.
"""

import logging
import json
import os
from typing import Dict, Any, Optional, List
from openai import OpenAI, RateLimitError


_LLM_CALL_COUNT = 0

# Path to prompts directory
_PROMPTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "prompts")

# Cache for loaded prompts
_PROMPT_CACHE = {}


def _load_prompt(prompt_name: str) -> str:
    """Load a prompt from the prompts directory.
    
    Prompts are cached after first load for performance.
    
    Args:
        prompt_name: Name of the prompt file (without .txt extension)
        
    Returns:
        The prompt text content
        
    Raises:
        FileNotFoundError: If the prompt file doesn't exist
    """
    if prompt_name in _PROMPT_CACHE:
        return _PROMPT_CACHE[prompt_name]
    
    prompt_path = os.path.join(_PROMPTS_DIR, f"{prompt_name}.txt")
    
    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    
    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompt_text = f.read()
    
    _PROMPT_CACHE[prompt_name] = prompt_text
    return prompt_text

# Batch processing token budget constants
# These values help ensure batch requests fit within model context windows
MAX_RESPONSE_TOKENS = 4000  # Maximum tokens allocated for LLM response
TOKENS_PER_ARTICLE = 300    # Estimated tokens needed for one article's assessment JSON
TOKEN_OVERHEAD = 500        # Extra tokens for prompt structure and formatting
MIN_CONTENT_PREVIEW = 500   # Minimum chars for content preview (even in large batches)
MAX_CONTENT_PREVIEW = 1000  # Maximum chars for content preview per article


def _handle_rate_limit(error: Exception) -> None:
    """Handle rate limit errors by checking status code and exiting if rate-limited.
    
    Args:
        error: Exception that may be a rate limit error
        
    Raises:
        SystemExit: If the error is a rate limit error (HTTP 429)
    """
    status_code = getattr(error, "status_code", None) or getattr(error, "status", None)
    if isinstance(error, RateLimitError) or status_code == 429:
        logging.error("LLM request rate-limited (HTTP 429). Exiting.")
        raise SystemExit(1)


def reset_llm_call_count() -> None:
    """Reset the running LLM call counter."""
    global _LLM_CALL_COUNT
    _LLM_CALL_COUNT = 0


def increment_llm_call_count() -> None:
    """Increment the running LLM call counter."""
    global _LLM_CALL_COUNT
    _LLM_CALL_COUNT += 1
    logging.debug("LLM call count updated", extra={"llm_calls": _LLM_CALL_COUNT})


def get_llm_call_count() -> int:
    """Return the running LLM call counter."""
    return _LLM_CALL_COUNT


def assess_article_applicability(
    openai_client: OpenAI,
    title: str,
    description: str,
    keywords: List[str],
    model: str,
    content: Optional[str] = None
) -> Dict[str, Any]:
    """Assess whether an article is applicable/relevant using LLM.
    
    Uses the provided keywords to determine if the article matches the
    project's focus areas (AI/automation/fuzzing in offensive security).
    
    Articles must meet BOTH criteria to be considered applicable:
    1. Contain keywords related to offensive security
    2. Explicitly describe the USE of AI, automation, or fuzzing
    
    Args:
        openai_client: OpenAI client configured for GitHub Models
        title: Article title
        description: Article description/summary
        keywords: List of keywords from config to guide assessment
        model: LLM model to use
        content: Optional full article content
        
    Returns:
        Dictionary with:
            - applicable: bool (whether article is relevant)
            - score: float (0.0-1.0 confidence score)
            - reason: str (explanation of the decision)
            - matched_keywords: List[str] (keywords that were relevant)
    """
    if not openai_client:
        logging.warning("No OpenAI client available for LLM assessment")
        return {
            "applicable": True,  # Default to including when LLM unavailable
            "score": 0.5,
            "reason": "LLM assessment unavailable",
            "matched_keywords": []
        }

    if not model:
        raise ValueError("LLM model must be provided for applicability assessment")

    try:
        # Build the prompt with keywords
        keywords_str = ", ".join(keywords)
        
        # Include content if available, otherwise just use title and description
        article_text = f"Title: {title}\n\nDescription: {description}"
        if content and len(content) > 0:
            # Limit content to avoid token limits (roughly 3000 chars = ~750 tokens)
            article_text += f"\n\nContent Preview: {content[:3000]}"
        
        # Load prompt template from file
        prompt_template = _load_prompt("assess_article_applicability")
        prompt = prompt_template.format(keywords_str=keywords_str, article_text=article_text)
        
        # Load system prompt from file
        system_prompt = _load_prompt("assess_article_applicability_system")

        logging.debug(
            "Running LLM applicability assessment",
            extra={
                "model": model,
                "keyword_count": len(keywords),
                "title_length": len(title),
                "description_length": len(description),
                "content_length": len(content) if content else 0
            }
        )
        
        # Call the LLM
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lower temperature for more consistent results
            max_tokens=500
        )
        increment_llm_call_count()

        logging.debug(
            "Received LLM applicability response",
            extra={"response_length": len(response.choices[0].message.content or "")}
        )
        
        # Parse the response
        result_text = response.choices[0].message.content.strip()
        
        # Try to extract JSON from the response
        # Sometimes LLM may include markdown code blocks
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0].strip()
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0].strip()
        
        result = json.loads(result_text)
        
        # Validate the result structure
        if not all(key in result for key in ["applicable", "score", "reason", "matched_keywords"]):
            raise ValueError("LLM response missing required fields")
        
        logging.debug(f"LLM applicability assessment: {result}")
        return result
        
    except RateLimitError as e:
        _handle_rate_limit(e)
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse LLM response as JSON: {e}")
        logging.debug(f"Raw response: {result_text if 'result_text' in locals() else 'N/A'}")
        return {
            "applicable": True,  # Default to including on error
            "score": 0.5,
            "reason": "LLM response parsing failed",
            "matched_keywords": []
        }
    except Exception as e:
        _handle_rate_limit(e)
        logging.error(f"Error in LLM applicability assessment: {str(e)}")
        return {
            "applicable": True,  # Default to including on error
            "score": 0.5,
            "reason": f"Assessment error: {str(e)}",
            "matched_keywords": []
        }


def assess_article_credibility(
    openai_client: OpenAI,
    title: str,
    description: str,
    url: str,
    source_name: str,
    domain_credibility: str,
    model: str,
    content: Optional[str] = None
) -> Dict[str, Any]:
    """Assess the credibility of an article using LLM.
    
    Evaluates content quality, source trustworthiness, and potential issues
    like clickbait, misinformation, or low-quality content.
    
    Args:
        openai_client: OpenAI client configured for GitHub Models
        title: Article title
        description: Article description/summary
        url: Article URL
        source_name: Name of the feed/source
        domain_credibility: Pre-assessed domain credibility ('high', 'medium', 'low')
        model: LLM model to use
        content: Optional full article content
        
    Returns:
        Dictionary with:
            - credible: bool (whether article appears credible)
            - score: float (0.0-1.0 confidence score)
            - reason: str (explanation of the decision)
            - flags: List[str] (any credibility concerns found)
    """
    if not openai_client:
        logging.warning("No OpenAI client available for LLM credibility assessment")
        return {
            "credible": True,  # Default to including when LLM unavailable
            "score": 0.5,
            "reason": "LLM assessment unavailable",
            "flags": []
        }

    if not model:
        raise ValueError("LLM model must be provided for credibility assessment")

    try:
        # Include content if available
        article_text = f"Title: {title}\n\nDescription: {description}"
        if content and len(content) > 0:
            # Limit content to avoid token limits
            article_text += f"\n\nContent Preview: {content[:3000]}"
        
        # Load prompt template from file
        prompt_template = _load_prompt("assess_article_credibility")
        prompt = prompt_template.format(
            source_name=source_name,
            domain_credibility=domain_credibility,
            url=url,
            article_text=article_text
        )
        
        # Load system prompt from file
        system_prompt = _load_prompt("assess_article_credibility_system")

        logging.debug(
            "Running LLM credibility assessment",
            extra={
                "model": model,
                "source_name": source_name,
                "domain_credibility": domain_credibility,
                "title_length": len(title),
                "description_length": len(description),
                "content_length": len(content) if content else 0
            }
        )
        
        # Call the LLM
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        increment_llm_call_count()

        logging.debug(
            "Received LLM credibility response",
            extra={"response_length": len(response.choices[0].message.content or "")}
        )
        
        # Parse the response
        result_text = response.choices[0].message.content.strip()
        
        # Try to extract JSON from the response
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0].strip()
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0].strip()
        
        result = json.loads(result_text)
        
        # Validate the result structure
        if not all(key in result for key in ["credible", "score", "reason", "flags"]):
            raise ValueError("LLM response missing required fields")
        
        logging.debug(f"LLM credibility assessment: {result}")
        return result
        
    except RateLimitError as e:
        _handle_rate_limit(e)
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse LLM credibility response as JSON: {e}")
        logging.debug(f"Raw response: {result_text if 'result_text' in locals() else 'N/A'}")
        return {
            "credible": True,  # Default to including on error
            "score": 0.5,
            "reason": "LLM response parsing failed",
            "flags": []
        }
    except Exception as e:
        _handle_rate_limit(e)
        logging.error(f"Error in LLM credibility assessment: {str(e)}")
        return {
            "credible": True,  # Default to including on error
            "score": 0.5,
            "reason": f"Assessment error: {str(e)}",
            "flags": []
        }


def filter_titles_by_relevance(
    openai_client: OpenAI,
    titles: List[str],
    keywords: List[str],
    model: str
) -> List[int]:
    """Filter article titles for relevance using the LLM.

    Args:
        openai_client: OpenAI client configured for GitHub Models
        titles: List of article titles
        keywords: List of keywords from config to guide relevance
        model: LLM model to use

    Returns:
        List of indices for titles deemed relevant
    """
    if not openai_client:
        logging.warning("No OpenAI client available for LLM title filtering")
        return []

    if not titles:
        return []

    if not model:
        raise ValueError("LLM model must be provided for title filtering")

    try:
        keywords_str = ", ".join(keywords) if keywords else "AI/automation in offensive security"
        title_list = "\n".join([f"{idx}: {title}" for idx, title in enumerate(titles)])

        # Load prompt template from file
        prompt_template = _load_prompt("filter_titles_by_relevance")
        prompt = prompt_template.format(keywords_str=keywords_str, title_list=title_list)
        
        # Load system prompt from file
        system_prompt = _load_prompt("filter_titles_by_relevance_system")

        logging.debug(
            "Running LLM title filtering",
            extra={
                "model": model,
                "title_count": len(titles),
                "keyword_count": len(keywords)
            }
        )

        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=300
        )
        increment_llm_call_count()

        logging.debug(
            "Received LLM title filter response",
            extra={"response_length": len(response.choices[0].message.content or "")}
        )

        result_text = response.choices[0].message.content.strip()
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0].strip()
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0].strip()

        result = json.loads(result_text)
        indices = result.get("relevant_indices", [])
        if not isinstance(indices, list):
            raise ValueError("LLM response 'relevant_indices' is not a list")

        valid_indices = [idx for idx in indices if isinstance(idx, int) and 0 <= idx < len(titles)]
        logging.debug(
            "LLM title filter selected indices",
            extra={"selected_count": len(valid_indices)}
        )
        return valid_indices

    except RateLimitError as e:
        _handle_rate_limit(e)
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse LLM title filter response as JSON: {e}")
        logging.debug(f"Raw response: {result_text if 'result_text' in locals() else 'N/A'}")
        return []
    except Exception as e:
        _handle_rate_limit(e)
        logging.error(f"Error in LLM title filtering: {str(e)}")
        return []


def assess_articles_batch(
    openai_client: OpenAI,
    articles: List[Dict[str, Any]],
    keywords: List[str],
    model: str,
    batch_size: int = 5
) -> List[Dict[str, Any]]:
    """Assess applicability and credibility of multiple articles in batches.
    
    This function processes multiple articles together in a single LLM call when they
    fit within the context window. This is more efficient than individual calls.
    
    Articles must meet BOTH criteria to be considered applicable:
    1. Contain keywords related to offensive security
    2. Explicitly describe the USE of AI, automation, or fuzzing
    
    Args:
        openai_client: OpenAI client configured for GitHub Models
        articles: List of article dictionaries with keys:
            - title: str
            - description: str
            - url: str (optional, for credibility assessment)
            - source_name: str (optional, for credibility assessment)
            - domain_credibility: str (optional, for credibility assessment)
            - content: str (optional, full article content)
        keywords: List of keywords from config to guide assessment
        model: LLM model to use
        batch_size: Maximum number of articles to assess in one call (default: 5)
        
    Returns:
        List of dictionaries, one per article, containing:
            - applicable: bool (whether article is relevant)
            - applicability_score: float (0.0-1.0 confidence score)
            - applicability_reason: str (explanation)
            - matched_keywords: List[str] (keywords that were relevant)
            - credible: bool (whether article appears credible)
            - credibility_score: float (0.0-1.0 confidence score)
            - credibility_reason: str (explanation)
            - flags: List[str] (credibility concerns)
    """
    if not openai_client:
        logging.warning("No OpenAI client available for LLM batch assessment")
        return [
            {
                "applicable": True,
                "applicability_score": 0.5,
                "applicability_reason": "LLM assessment unavailable",
                "matched_keywords": [],
                "credible": True,
                "credibility_score": 0.5,
                "credibility_reason": "LLM assessment unavailable",
                "flags": []
            }
            for _ in articles
        ]
    
    if not articles:
        return []
    
    if not model:
        raise ValueError("LLM model must be provided for batch assessment")

    # Process articles in batches
    all_results = []
    for i in range(0, len(articles), batch_size):
        batch = articles[i:i + batch_size]
        
        # If batch has only one article, use single-article assessment for compatibility
        if len(batch) == 1:
            article = batch[0]
            app_result = assess_article_applicability(
                openai_client=openai_client,
                title=article.get("title", ""),
                description=article.get("description", ""),
                keywords=keywords,
                content=article.get("content"),
                model=model
            )
            cred_result = assess_article_credibility(
                openai_client=openai_client,
                title=article.get("title", ""),
                description=article.get("description", ""),
                url=article.get("url", ""),
                source_name=article.get("source_name", "Unknown"),
                domain_credibility=article.get("domain_credibility", "unknown"),
                content=article.get("content"),
                model=model
            )
            all_results.append({
                "applicable": app_result["applicable"],
                "applicability_score": app_result["score"],
                "applicability_reason": app_result["reason"],
                "matched_keywords": app_result["matched_keywords"],
                "credible": cred_result["credible"],
                "credibility_score": cred_result["score"],
                "credibility_reason": cred_result["reason"],
                "flags": cred_result["flags"]
            })
            continue
        
        # Process batch of multiple articles
        batch_results = _assess_batch_internal(
            openai_client=openai_client,
            articles=batch,
            keywords=keywords,
            model=model
        )
        all_results.extend(batch_results)
    
    return all_results


def _assess_batch_internal(
    openai_client: OpenAI,
    articles: List[Dict[str, Any]],
    keywords: List[str],
    model: str
) -> List[Dict[str, Any]]:
    """Internal function to assess a batch of articles with a single LLM call.
    
    Args:
        openai_client: OpenAI client configured for GitHub Models
        articles: List of article dictionaries (should be 2 or more)
        keywords: List of keywords from config to guide assessment
        model: LLM model to use
        
    Returns:
        List of assessment results, one per article
    """
    try:
        keywords_str = ", ".join(keywords)
        
        # Build the batch prompt
        articles_text = []
        for idx, article in enumerate(articles):
            title = article.get("title", "Untitled")
            description = article.get("description", "")
            url = article.get("url", "")
            source_name = article.get("source_name", "Unknown")
            domain_credibility = article.get("domain_credibility", "unknown")
            content = article.get("content", "")
            
            article_text = f"""Article {idx}:
Title: {title}
Description: {description}
URL: {url}
Source: {source_name}
Domain Credibility: {domain_credibility}"""
            
            if content and len(content) > 0:
                # Scale content preview based on batch size to fit within context window
                # Maintains readability while allowing more articles per batch
                content_limit = max(MIN_CONTENT_PREVIEW, min(MAX_CONTENT_PREVIEW, 2500 // len(articles)))
                article_text += f"\nContent Preview: {content[:content_limit]}"
            
            articles_text.append(article_text)
        
        combined_articles = "\n\n---\n\n".join(articles_text)
        
        # Load prompt template from file
        prompt_template = _load_prompt("assess_batch_internal")
        prompt = prompt_template.format(
            num_articles=len(articles),
            keywords_str=keywords_str,
            combined_articles=combined_articles
        )
        
        # Load system prompt from file
        system_prompt = _load_prompt("assess_batch_internal_system")

        logging.debug(
            "Running LLM batch assessment",
            extra={
                "model": model,
                "batch_size": len(articles),
                "keyword_count": len(keywords)
            }
        )
        
        # Call the LLM
        # Scale max_tokens based on batch size to ensure adequate response capacity
        max_response_tokens = min(MAX_RESPONSE_TOKENS, TOKENS_PER_ARTICLE * len(articles) + TOKEN_OVERHEAD)
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=max_response_tokens
        )
        increment_llm_call_count()
        
        logging.debug(
            "Received LLM batch response",
            extra={"response_length": len(response.choices[0].message.content or "")}
        )
        
        # Parse the response
        result_text = response.choices[0].message.content.strip()
        
        # Try to extract JSON from the response
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0].strip()
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0].strip()
        
        results = json.loads(result_text)
        
        # Validate the results
        if not isinstance(results, list):
            raise ValueError("LLM response is not a JSON array")
        
        if len(results) != len(articles):
            logging.warning(
                f"LLM returned {len(results)} results for {len(articles)} articles, falling back to individual assessment"
            )
            # Fallback to individual assessment
            return _fallback_individual_assessment(openai_client, articles, keywords, model)
        
        # Validate each result structure
        for idx, result in enumerate(results):
            required_keys = [
                "applicable", "applicability_score", "applicability_reason", "matched_keywords",
                "credible", "credibility_score", "credibility_reason", "flags"
            ]
            if not all(key in result for key in required_keys):
                logging.warning(f"Result {idx} missing required fields, falling back to individual assessment")
                return _fallback_individual_assessment(openai_client, articles, keywords, model)
        
        logging.debug(f"LLM batch assessment completed for {len(results)} articles")
        return results
        
    except RateLimitError as e:
        _handle_rate_limit(e)
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse LLM batch response as JSON: {e}")
        logging.debug(f"Raw response: {result_text if 'result_text' in locals() else 'N/A'}")
        # Fallback to individual assessment
        return _fallback_individual_assessment(openai_client, articles, keywords, model)
    except Exception as e:
        _handle_rate_limit(e)
        logging.error(f"Error in LLM batch assessment: {str(e)}")
        # Fallback to individual assessment
        return _fallback_individual_assessment(openai_client, articles, keywords, model)


def _fallback_individual_assessment(
    openai_client: OpenAI,
    articles: List[Dict[str, Any]],
    keywords: List[str],
    model: str
) -> List[Dict[str, Any]]:
    """Fallback to individual article assessment when batch processing fails.
    
    Args:
        openai_client: OpenAI client configured for GitHub Models
        articles: List of article dictionaries
        keywords: List of keywords from config
        model: LLM model to use
        
    Returns:
        List of assessment results, one per article
    """
    logging.info(f"Falling back to individual assessment for {len(articles)} articles")
    results = []
    
    for article in articles:
        app_result = assess_article_applicability(
            openai_client=openai_client,
            title=article.get("title", ""),
            description=article.get("description", ""),
            keywords=keywords,
            content=article.get("content"),
            model=model
        )
        cred_result = assess_article_credibility(
            openai_client=openai_client,
            title=article.get("title", ""),
            description=article.get("description", ""),
            url=article.get("url", ""),
            source_name=article.get("source_name", "Unknown"),
            domain_credibility=article.get("domain_credibility", "unknown"),
            content=article.get("content"),
            model=model
        )
        results.append({
            "applicable": app_result["applicable"],
            "applicability_score": app_result["score"],
            "applicability_reason": app_result["reason"],
            "matched_keywords": app_result["matched_keywords"],
            "credible": cred_result["credible"],
            "credibility_score": cred_result["score"],
            "credibility_reason": cred_result["reason"],
            "flags": cred_result["flags"]
        })
    
    return results
