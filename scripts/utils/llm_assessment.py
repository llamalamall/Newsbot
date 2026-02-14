"""
LLM-based article assessment utilities.
Provides functionality to assess article applicability and credibility using GitHub Models LLM.
"""

import logging
import json
from typing import Dict, Any, Optional, List
from openai import OpenAI


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
- Does the title appear clickbait or sensationalized?
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
        logging.error(f"Error in LLM credibility assessment: {str(e)}")
        return {
            "credible": True,  # Default to including on error
            "score": 0.5,
            "reason": f"Assessment error: {str(e)}",
            "flags": []
        }
