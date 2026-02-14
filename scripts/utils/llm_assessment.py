"""
LLM-based article assessment utilities.
Provides functionality to assess article applicability and credibility using GitHub Models LLM.
"""

import logging
import json
from typing import Dict, Any, Optional, List
from openai import OpenAI, RateLimitError


_LLM_CALL_COUNT = 0


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
    content: Optional[str] = None,
    model: str = "gpt-4o"
) -> Dict[str, Any]:
    """Assess whether an article is applicable/relevant using LLM.
    
    Uses the provided keywords to determine if the article matches the
    project's focus areas (AI/automation in offensive security).
    
    Args:
        openai_client: OpenAI client configured for GitHub Models
        title: Article title
        description: Article description/summary
        keywords: List of keywords from config to guide assessment
        content: Optional full article content
        model: LLM model to use (default: gpt-4o)
        
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

    def handle_rate_limit(error: Exception) -> None:
        status_code = getattr(error, "status_code", None) or getattr(error, "status", None)
        if isinstance(error, RateLimitError) or status_code == 429:
            logging.error("LLM request rate-limited (HTTP 429). Exiting.")
            raise SystemExit(1)
    
    try:
        # Build the prompt with keywords
        keywords_str = ", ".join(keywords)
        
        # Include content if available, otherwise just use title and description
        article_text = f"Title: {title}\n\nDescription: {description}"
        if content and len(content) > 0:
            # Limit content to avoid token limits (roughly 3000 chars = ~750 tokens)
            article_text += f"\n\nContent Preview: {content[:3000]}"
        
        prompt = f"""You are an expert security researcher analyzing articles for relevance to AI and automation in offensive security.

Evaluate if the following article is relevant to these topics: {keywords_str}

Article:
{article_text}

Respond ONLY with a valid JSON object in this exact format:
{{
  "applicable": true or false,
  "score": 0.0 to 1.0,
  "reason": "brief explanation",
  "matched_keywords": ["keyword1", "keyword2"]
}}

Consider the article applicable if it relates to:
- AI/ML in security testing or offensive operations
- Automation of penetration testing or red team activities
- Machine learning for vulnerability detection or exploit development
- Automated malware analysis or reverse engineering
- Security tools using AI/automation
- Research on adversarial AI or security

Be selective - only mark as applicable if there's a clear, strong connection to the specified topics."""

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
                {"role": "system", "content": "You are a security research analyst. Respond only with valid JSON."},
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
        handle_rate_limit(e)
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
        handle_rate_limit(e)
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
    content: Optional[str] = None,
    model: str = "gpt-4o"
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
        content: Optional full article content
        model: LLM model to use (default: gpt-4o)
        
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

    def handle_rate_limit(error: Exception) -> None:
        status_code = getattr(error, "status_code", None) or getattr(error, "status", None)
        if isinstance(error, RateLimitError) or status_code == 429:
            logging.error("LLM request rate-limited (HTTP 429). Exiting.")
            raise SystemExit(1)
    
    try:
        # Include content if available
        article_text = f"Title: {title}\n\nDescription: {description}"
        if content and len(content) > 0:
            # Limit content to avoid token limits
            article_text += f"\n\nContent Preview: {content[:3000]}"
        
        prompt = f"""You are an expert at evaluating the credibility and quality of security news articles.

Analyze this article for credibility and trustworthiness:

Source: {source_name}
URL Domain Credibility: {domain_credibility}
URL: {url}

Article:
{article_text}

Respond ONLY with a valid JSON object in this exact format:
{{
  "credible": true or false,
  "score": 0.0 to 1.0,
  "reason": "brief explanation",
  "flags": ["flag1", "flag2"]
}}

Evaluate based on:
- Is the content substantive or superficial?
- Are there signs of misinformation or bias?
- Does it cite sources or provide evidence?
- Is it from a known credible source? (consider domain_credibility)
- Does it appear to be quality security research/news?

Common flags to check for:
- "clickbait_title" - Sensationalized or misleading title
- "low_quality_content" - Superficial or poorly written
- "no_sources" - Lacks citations or evidence
- "potential_bias" - Shows strong bias or agenda
- "unverified_claims" - Makes claims without proof

Only mark as not credible if there are serious quality or trustworthiness issues."""

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
                {"role": "system", "content": "You are a credibility analyst. Respond only with valid JSON."},
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
        handle_rate_limit(e)
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
        handle_rate_limit(e)
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
    model: str = "gpt-4o"
) -> List[int]:
    """Filter article titles for relevance using the LLM.

    Args:
        openai_client: OpenAI client configured for GitHub Models
        titles: List of article titles
        keywords: List of keywords from config to guide relevance
        model: LLM model to use (default: gpt-4o)

    Returns:
        List of indices for titles deemed relevant
    """
    if not openai_client:
        logging.warning("No OpenAI client available for LLM title filtering")
        return []

    if not titles:
        return []

    def handle_rate_limit(error: Exception) -> None:
        status_code = getattr(error, "status_code", None) or getattr(error, "status", None)
        if isinstance(error, RateLimitError) or status_code == 429:
            logging.error("LLM request rate-limited (HTTP 429). Exiting.")
            raise SystemExit(1)

    try:
        keywords_str = ", ".join(keywords) if keywords else "AI/automation in offensive security"
        title_list = "\n".join([f"{idx}: {title}" for idx, title in enumerate(titles)])

        prompt = f"""You are an expert security researcher. Select which article titles are relevant to: {keywords_str}

Titles:
{title_list}

Respond ONLY with valid JSON in this exact format:
{{
  \"relevant_indices\": [0, 2, 5]
}}

Be selective. Only include titles with a clear and strong connection to the topic."""

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
                {"role": "system", "content": "You are a security research analyst. Respond only with valid JSON."},
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
        handle_rate_limit(e)
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse LLM title filter response as JSON: {e}")
        logging.debug(f"Raw response: {result_text if 'result_text' in locals() else 'N/A'}")
        return []
    except Exception as e:
        handle_rate_limit(e)
        logging.error(f"Error in LLM title filtering: {str(e)}")
        return []
