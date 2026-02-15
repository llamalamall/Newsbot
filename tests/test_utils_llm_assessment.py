#!/usr/bin/env python3
"""
Unit tests for LLM assessment utilities.
Tests the LLM-based article applicability and credibility assessment functionality.
"""

import pytest
import sys
import os
import json
from unittest.mock import Mock, MagicMock, patch
from openai import OpenAI

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(REPO_ROOT, 'scripts')
CONFIG_PATH = os.path.join(REPO_ROOT, 'config.json')

# Add scripts to path
sys.path.insert(0, SCRIPTS_DIR)

with open(CONFIG_PATH, 'r') as config_file:
    _CONFIG = json.load(config_file)

LLM_MODEL = _CONFIG.get("llm_assessment", {}).get("model")
if not LLM_MODEL:
    raise RuntimeError("llm_assessment.model is required in config.json for tests")

from utils.llm_assessment import (
    assess_article_applicability,
    assess_article_credibility,
    assess_articles_batch
)


class TestAssessArticleApplicability:
    """Test assess_article_applicability function."""
    
    def test_applicability_with_no_client(self):
        """Test that function returns default values when client is None."""
        result = assess_article_applicability(
            openai_client=None,
            title="Test Article",
            description="Test description",
            keywords=["security", "AI"],
            model=LLM_MODEL
        )
        
        assert isinstance(result, dict)
        assert "applicable" in result
        assert "score" in result
        assert "reason" in result
        assert "matched_keywords" in result
        assert result["applicable"] is True  # Default to including
        assert result["score"] == 0.5
        assert "unavailable" in result["reason"].lower()
    
    def test_applicability_with_valid_response(self):
        """Test successful LLM applicability assessment."""
        # Mock OpenAI client
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        # Create a valid JSON response
        json_response = {
            "applicable": True,
            "score": 0.85,
            "reason": "Article discusses AI in penetration testing",
            "matched_keywords": ["AI", "penetration testing"]
        }
        mock_message.content = json.dumps(json_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_applicability(
            openai_client=mock_client,
            title="AI-Powered Penetration Testing Tools",
            description="New tools using machine learning for automated security testing",
            keywords=["AI", "penetration testing", "automation"],
            model=LLM_MODEL
        )
        
        assert result["applicable"] is True
        assert result["score"] == 0.85
        assert "penetration testing" in result["reason"].lower()
        assert "AI" in result["matched_keywords"]
        assert "penetration testing" in result["matched_keywords"]
    
    def test_applicability_with_markdown_json(self):
        """Test parsing when LLM returns JSON wrapped in markdown code blocks."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        json_response = {
            "applicable": False,
            "score": 0.2,
            "reason": "Article is about general cloud computing, not security",
            "matched_keywords": []
        }
        # Wrap in markdown code block
        mock_message.content = f"```json\n{json.dumps(json_response)}\n```"
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_applicability(
            openai_client=mock_client,
            title="Cloud Computing Trends",
            description="Overview of cloud infrastructure",
            keywords=["offensive security", "penetration testing"],
            model=LLM_MODEL
        )
        
        assert result["applicable"] is False
        assert result["score"] == 0.2
        assert len(result["matched_keywords"]) == 0
    
    def test_applicability_with_content(self):
        """Test that content is included when provided."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        json_response = {
            "applicable": True,
            "score": 0.9,
            "reason": "Detailed analysis of LLM security vulnerabilities",
            "matched_keywords": ["LLM security", "AI"]
        }
        mock_message.content = json.dumps(json_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_applicability(
            openai_client=mock_client,
            title="LLM Security Research",
            description="Research on vulnerabilities in large language models",
            keywords=["LLM security", "AI", "automation"],
            content="Detailed content about LLM vulnerabilities and exploitation techniques...",
            model=LLM_MODEL
        )
        
        assert result["applicable"] is True
        assert result["score"] == 0.9
        
        # Verify the API was called
        mock_client.chat.completions.create.assert_called_once()
        call_args = mock_client.chat.completions.create.call_args
        # Check that content was included in the prompt
        user_message = call_args[1]['messages'][1]['content']
        assert "Content Preview:" in user_message
    
    def test_applicability_handles_json_parse_error(self):
        """Test that function handles JSON parsing errors gracefully."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        # Return invalid JSON
        mock_message.content = "This is not valid JSON"
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_applicability(
            openai_client=mock_client,
            title="Test Article",
            description="Test description",
            keywords=["security"],
            model=LLM_MODEL
        )
        
        # Should return default values on error
        assert result["applicable"] is True
        assert result["score"] == 0.5
        assert "parsing failed" in result["reason"].lower()
    
    def test_applicability_handles_api_error(self):
        """Test that function handles API errors gracefully."""
        mock_client = Mock()
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        
        result = assess_article_applicability(
            openai_client=mock_client,
            title="Test Article",
            description="Test description",
            keywords=["security"],
            model=LLM_MODEL
        )
        
        # Should return default values on error
        assert result["applicable"] is True
        assert result["score"] == 0.5
        assert "error" in result["reason"].lower()
    
    def test_applicability_truncates_long_content(self):
        """Test that long content is truncated to avoid token limits."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        json_response = {
            "applicable": True,
            "score": 0.75,
            "reason": "Relevant content",
            "matched_keywords": ["security"]
        }
        mock_message.content = json.dumps(json_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        # Create very long content (>3000 chars)
        long_content = "A" * 5000
        
        result = assess_article_applicability(
            openai_client=mock_client,
            title="Test",
            description="Test",
            keywords=["security"],
            content=long_content,
            model=LLM_MODEL
        )
        
        # Verify the API was called
        call_args = mock_client.chat.completions.create.call_args
        user_message = call_args[1]['messages'][1]['content']
        
        # Content should be truncated
        assert long_content[:3000] in user_message
        assert len(user_message) < len(long_content) + 1000  # Much shorter than original


class TestAssessArticleCredibility:
    """Test assess_article_credibility function."""
    
    def test_credibility_with_no_client(self):
        """Test that function returns default values when client is None."""
        result = assess_article_credibility(
            openai_client=None,
            title="Test Article",
            description="Test description",
            url="https://example.com/article",
            source_name="Test Source",
            domain_credibility="high",
            model=LLM_MODEL
        )
        
        assert isinstance(result, dict)
        assert "credible" in result
        assert "score" in result
        assert "reason" in result
        assert "flags" in result
        assert result["credible"] is True
        assert result["score"] == 0.5
        assert "unavailable" in result["reason"].lower()
    
    def test_credibility_with_valid_response(self):
        """Test successful LLM credibility assessment."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        json_response = {
            "credible": True,
            "score": 0.9,
            "reason": "Well-researched article from reputable source with citations",
            "flags": []
        }
        mock_message.content = json.dumps(json_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_credibility(
            openai_client=mock_client,
            title="Research Paper on ML Security",
            description="Peer-reviewed research with detailed methodology",
            url="https://arxiv.org/abs/2024.12345",
            source_name="arXiv",
            domain_credibility="high",
            model=LLM_MODEL
        )
        
        assert result["credible"] is True
        assert result["score"] == 0.9
        assert "reputable" in result["reason"].lower() or "research" in result["reason"].lower()
        assert len(result["flags"]) == 0
    
    def test_credibility_with_flags(self):
        """Test credibility assessment with credibility flags."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        json_response = {
            "credible": False,
            "score": 0.3,
            "reason": "Clickbait title and no sources cited",
            "flags": ["clickbait_title", "no_sources"]
        }
        mock_message.content = json.dumps(json_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_credibility(
            openai_client=mock_client,
            title="You Won't Believe This Security Hack!!!",
            description="Amazing trick revealed",
            url="https://example.com/clickbait",
            source_name="Unknown Blog",
            domain_credibility="low",
            model=LLM_MODEL
        )
        
        assert result["credible"] is False
        assert result["score"] == 0.3
        assert "clickbait_title" in result["flags"]
        assert "no_sources" in result["flags"]
    
    def test_credibility_considers_domain_credibility(self):
        """Test that domain credibility is passed to LLM."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        json_response = {
            "credible": True,
            "score": 0.8,
            "reason": "From trusted source",
            "flags": []
        }
        mock_message.content = json.dumps(json_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_credibility(
            openai_client=mock_client,
            title="Security Advisory",
            description="Official security announcement",
            url="https://cisa.gov/advisory",
            source_name="CISA",
            domain_credibility="high",
            model=LLM_MODEL
        )
        
        # Verify the API was called with domain credibility
        call_args = mock_client.chat.completions.create.call_args
        user_message = call_args[1]['messages'][1]['content']
        assert "high" in user_message.lower()
        assert "CISA" in user_message
    
    def test_credibility_handles_json_parse_error(self):
        """Test that function handles JSON parsing errors gracefully."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        mock_message.content = "Not valid JSON"
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_credibility(
            openai_client=mock_client,
            title="Test",
            description="Test",
            url="https://example.com",
            source_name="Test",
            domain_credibility="medium",
            model=LLM_MODEL
        )
        
        assert result["credible"] is True
        assert result["score"] == 0.5
        assert "parsing failed" in result["reason"].lower()
    
    def test_credibility_handles_api_error(self):
        """Test that function handles API errors gracefully."""
        mock_client = Mock()
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        
        result = assess_article_credibility(
            openai_client=mock_client,
            title="Test",
            description="Test",
            url="https://example.com",
            source_name="Test",
            domain_credibility="medium",
            model=LLM_MODEL
        )
        
        assert result["credible"] is True
        assert result["score"] == 0.5
        assert "error" in result["reason"].lower()
    
    def test_credibility_with_markdown_json(self):
        """Test parsing when LLM returns JSON wrapped in markdown."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        json_response = {
            "credible": True,
            "score": 0.85,
            "reason": "High quality content",
            "flags": []
        }
        mock_message.content = f"```\n{json.dumps(json_response)}\n```"
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = assess_article_credibility(
            openai_client=mock_client,
            title="Test",
            description="Test",
            url="https://example.com",
            source_name="Test",
            domain_credibility="high",
            model=LLM_MODEL
        )
        
        assert result["credible"] is True
        assert result["score"] == 0.85


class TestLLMAssessmentIntegration:
    """Integration tests for LLM assessment functions."""
    
    def test_both_assessments_can_be_called_together(self):
        """Test that both assessments can be used together."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        # First call for applicability
        applicability_response = {
            "applicable": True,
            "score": 0.8,
            "reason": "Relevant",
            "matched_keywords": ["AI", "security"]
        }
        
        # Second call for credibility
        credibility_response = {
            "credible": True,
            "score": 0.85,
            "reason": "Credible",
            "flags": []
        }
        
        # Set up mock to return different responses
        mock_message.content = json.dumps(applicability_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        app_result = assess_article_applicability(
            openai_client=mock_client,
            title="AI Security Article",
            description="Article about AI security",
            keywords=["AI", "security"],
            model=LLM_MODEL
        )
        
        # Update mock for second call
        mock_message.content = json.dumps(credibility_response)
        
        cred_result = assess_article_credibility(
            openai_client=mock_client,
            title="AI Security Article",
            description="Article about AI security",
            url="https://example.com",
            source_name="Tech Blog",
            domain_credibility="medium",
            model=LLM_MODEL
        )
        
        # Both should succeed
        assert app_result["applicable"] is True
        assert app_result["score"] == 0.8
        assert cred_result["credible"] is True
        assert cred_result["score"] == 0.85


@pytest.mark.integration
@pytest.mark.requires_token
@pytest.mark.network
def test_llm_single_live_call():
    """Perform a single live LLM call when explicitly enabled.

    Set RUN_LLM_INTEGRATION=1 and GITHUB_TOKEN to run this test.
    """
    if os.getenv("RUN_LLM_INTEGRATION") != "1":
        pytest.skip("RUN_LLM_INTEGRATION not enabled")

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        pytest.skip("GITHUB_TOKEN not set")

    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=token
    )

    result = assess_article_applicability(
        openai_client=client,
        title="AI-assisted security testing tool",
        description="A short overview of automating penetration testing with LLMs.",
        keywords=["AI", "automation", "penetration testing"],
        model=LLM_MODEL
    )

    assert isinstance(result, dict)
    assert "applicable" in result
    assert "score" in result
    assert 0.0 <= result["score"] <= 1.0


class TestBatchAssessment:
    """Test batch assessment functionality."""
    
    def test_batch_assessment_with_no_client(self):
        """Test that batch function returns default values when client is None."""
        articles = [
            {"title": "Test 1", "description": "Description 1"},
            {"title": "Test 2", "description": "Description 2"}
        ]
        
        results = assess_articles_batch(
            openai_client=None,
            articles=articles,
            keywords=["security", "AI"],
            model=LLM_MODEL
        )
        
        assert len(results) == 2
        for result in results:
            assert result["applicable"] is True
            assert result["applicability_score"] == 0.5
            assert "unavailable" in result["applicability_reason"].lower()
            assert result["credible"] is True
            assert result["credibility_score"] == 0.5
    
    def test_batch_assessment_empty_list(self):
        """Test that batch function handles empty list."""
        mock_client = Mock()
        
        results = assess_articles_batch(
            openai_client=mock_client,
            articles=[],
            keywords=["security"],
            model=LLM_MODEL
        )
        
        assert results == []
        # Should not make any API calls
        mock_client.chat.completions.create.assert_not_called()
    
    def test_batch_assessment_single_article_uses_individual_assessment(self):
        """Test that single article batch uses individual assessment functions."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        # Mock response for individual assessment
        applicability_response = {
            "applicable": True,
            "score": 0.85,
            "reason": "Relevant",
            "matched_keywords": ["AI"]
        }
        credibility_response = {
            "credible": True,
            "score": 0.9,
            "reason": "Credible",
            "flags": []
        }
        
        # Set up to return different responses for applicability and credibility
        mock_message.content = json.dumps(applicability_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        
        # First call returns applicability, second returns credibility
        mock_client.chat.completions.create.side_effect = [
            mock_response,
            Mock(choices=[Mock(message=Mock(content=json.dumps(credibility_response)))])
        ]
        
        articles = [{"title": "Test", "description": "Test desc", "url": "http://test.com"}]
        
        results = assess_articles_batch(
            openai_client=mock_client,
            articles=articles,
            keywords=["AI", "security"],
            model=LLM_MODEL
        )
        
        assert len(results) == 1
        assert results[0]["applicable"] is True
        assert results[0]["applicability_score"] == 0.85
        assert results[0]["credible"] is True
        assert results[0]["credibility_score"] == 0.9
        # Should make 2 calls (one for applicability, one for credibility)
        assert mock_client.chat.completions.create.call_count == 2
    
    def test_batch_assessment_multiple_articles(self):
        """Test batch assessment with multiple articles."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        # Create batch response with 3 articles
        batch_response = [
            {
                "applicable": True,
                "applicability_score": 0.85,
                "applicability_reason": "AI security article",
                "matched_keywords": ["AI", "security"],
                "credible": True,
                "credibility_score": 0.9,
                "credibility_reason": "High quality",
                "flags": []
            },
            {
                "applicable": False,
                "applicability_score": 0.3,
                "applicability_reason": "Not related",
                "matched_keywords": [],
                "credible": True,
                "credibility_score": 0.7,
                "credibility_reason": "Decent source",
                "flags": []
            },
            {
                "applicable": True,
                "applicability_score": 0.75,
                "applicability_reason": "Automation topic",
                "matched_keywords": ["automation"],
                "credible": False,
                "credibility_score": 0.4,
                "credibility_reason": "Clickbait",
                "flags": ["clickbait_title"]
            }
        ]
        
        mock_message.content = json.dumps(batch_response)
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        articles = [
            {"title": "AI Security", "description": "Article about AI in security", "url": "http://test1.com"},
            {"title": "Cloud Computing", "description": "General cloud article", "url": "http://test2.com"},
            {"title": "Automation", "description": "Clickbait article", "url": "http://test3.com"}
        ]
        
        results = assess_articles_batch(
            openai_client=mock_client,
            articles=articles,
            keywords=["AI", "security", "automation"],
            model=LLM_MODEL
        )
        
        assert len(results) == 3
        assert results[0]["applicable"] is True
        assert results[0]["applicability_score"] == 0.85
        assert results[1]["applicable"] is False
        assert results[1]["applicability_score"] == 0.3
        assert results[2]["applicable"] is True
        assert results[2]["credible"] is False
        assert "clickbait_title" in results[2]["flags"]
        # Should make only 1 call for batch
        assert mock_client.chat.completions.create.call_count == 1
    
    def test_batch_assessment_with_markdown_json(self):
        """Test batch assessment handles markdown-wrapped JSON."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        batch_response = [
            {
                "applicable": True,
                "applicability_score": 0.8,
                "applicability_reason": "Relevant",
                "matched_keywords": ["security"],
                "credible": True,
                "credibility_score": 0.85,
                "credibility_reason": "Good quality",
                "flags": []
            }
        ]
        
        # Wrap in markdown code block
        mock_message.content = f"```json\n{json.dumps(batch_response)}\n```"
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        
        articles = [{"title": "Test", "description": "Test"}]
        
        results = assess_articles_batch(
            openai_client=mock_client,
            articles=articles,
            keywords=["security"],
            model=LLM_MODEL,
            batch_size=5
        )
        
        # Should fall back to individual assessment since batch size is 1
        assert len(results) == 1
    
    def test_batch_assessment_handles_mismatched_count(self):
        """Test batch assessment falls back when response count doesn't match."""
        mock_client = Mock()
        mock_response = Mock()
        mock_choice = Mock()
        mock_message = Mock()
        
        # Return only 2 results for 3 articles (mismatch)
        batch_response = [
            {
                "applicable": True,
                "applicability_score": 0.8,
                "applicability_reason": "Relevant",
                "matched_keywords": ["security"],
                "credible": True,
                "credibility_score": 0.85,
                "credibility_reason": "Good",
                "flags": []
            },
            {
                "applicable": False,
                "applicability_score": 0.3,
                "applicability_reason": "Not relevant",
                "matched_keywords": [],
                "credible": True,
                "credibility_score": 0.7,
                "credibility_reason": "OK",
                "flags": []
            }
        ]
        
        # First call returns mismatched batch, subsequent calls return individual assessments
        individual_app = {"applicable": True, "score": 0.5, "reason": "Fallback", "matched_keywords": []}
        individual_cred = {"credible": True, "score": 0.5, "reason": "Fallback", "flags": []}
        
        mock_client.chat.completions.create.side_effect = [
            Mock(choices=[Mock(message=Mock(content=json.dumps(batch_response)))]),
            # Fallback individual assessments for 3 articles (6 calls total)
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_app)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_cred)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_app)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_cred)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_app)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_cred)))])
        ]
        
        articles = [
            {"title": "Test 1", "description": "Desc 1"},
            {"title": "Test 2", "description": "Desc 2"},
            {"title": "Test 3", "description": "Desc 3"}
        ]
        
        results = assess_articles_batch(
            openai_client=mock_client,
            articles=articles,
            keywords=["security"],
            model=LLM_MODEL,
            batch_size=5
        )
        
        # Should get results via fallback
        assert len(results) == 3
        for result in results:
            assert result["applicable"] is True
            assert result["applicability_score"] == 0.5
    
    def test_batch_assessment_respects_batch_size(self):
        """Test that batch assessment splits articles according to batch_size."""
        mock_client = Mock()
        
        # Create response for a batch
        batch_response_1 = [
            {
                "applicable": True,
                "applicability_score": 0.8,
                "applicability_reason": "Relevant",
                "matched_keywords": ["AI"],
                "credible": True,
                "credibility_score": 0.85,
                "credibility_reason": "Good",
                "flags": []
            },
            {
                "applicable": True,
                "applicability_score": 0.75,
                "applicability_reason": "Relevant",
                "matched_keywords": ["security"],
                "credible": True,
                "credibility_score": 0.8,
                "credibility_reason": "Good",
                "flags": []
            }
        ]
        
        # For single article (batch of 1), it uses individual assessment
        individual_app = {"applicable": False, "score": 0.3, "reason": "Not relevant", "matched_keywords": []}
        individual_cred = {"credible": True, "score": 0.7, "reason": "OK", "flags": []}
        
        mock_client.chat.completions.create.side_effect = [
            Mock(choices=[Mock(message=Mock(content=json.dumps(batch_response_1)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_app)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_cred)))])
        ]
        
        articles = [
            {"title": "Test 1", "description": "Desc 1"},
            {"title": "Test 2", "description": "Desc 2"},
            {"title": "Test 3", "description": "Desc 3"}
        ]
        
        results = assess_articles_batch(
            openai_client=mock_client,
            articles=articles,
            keywords=["AI", "security"],
            model=LLM_MODEL,
            batch_size=2  # Force split: batch of 2, then individual for the 3rd
        )
        
        assert len(results) == 3
        # Should make 3 calls: 1 for batch of 2, 2 for individual (applicability + credibility)
        assert mock_client.chat.completions.create.call_count == 3
        assert results[0]["applicable"] is True
        assert results[1]["applicable"] is True
        assert results[2]["applicable"] is False
    
    def test_batch_assessment_handles_json_parse_error(self):
        """Test batch assessment falls back on JSON parse error."""
        mock_client = Mock()
        
        # First call returns invalid JSON, then fallback individual calls
        individual_app = {"applicable": True, "score": 0.5, "reason": "Fallback", "matched_keywords": []}
        individual_cred = {"credible": True, "score": 0.5, "reason": "Fallback", "flags": []}
        
        mock_client.chat.completions.create.side_effect = [
            Mock(choices=[Mock(message=Mock(content="Not valid JSON"))]),
            # Fallback calls
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_app)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_cred)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_app)))]),
            Mock(choices=[Mock(message=Mock(content=json.dumps(individual_cred)))])
        ]
        
        articles = [
            {"title": "Test 1", "description": "Desc 1"},
            {"title": "Test 2", "description": "Desc 2"}
        ]
        
        results = assess_articles_batch(
            openai_client=mock_client,
            articles=articles,
            keywords=["security"],
            model=LLM_MODEL
        )
        
        # Should get results via fallback
        assert len(results) == 2
        for result in results:
            assert result["applicable"] is True
