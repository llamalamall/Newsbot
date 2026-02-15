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

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

from utils.llm_assessment import assess_article_applicability, assess_article_credibility


class TestAssessArticleApplicability:
    """Test assess_article_applicability function."""
    
    def test_applicability_with_no_client(self):
        """Test that function returns default values when client is None."""
        result = assess_article_applicability(
            openai_client=None,
            title="Test Article",
            description="Test description",
            keywords=["security", "AI"]
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
            keywords=["AI", "penetration testing", "automation"]
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
            keywords=["offensive security", "penetration testing"]
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
            content="Detailed content about LLM vulnerabilities and exploitation techniques..."
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
            keywords=["security"]
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
            keywords=["security"]
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
            content=long_content
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
            domain_credibility="high"
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
            domain_credibility="high"
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
            domain_credibility="low"
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
            domain_credibility="high"
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
            domain_credibility="medium"
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
            domain_credibility="medium"
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
            domain_credibility="high"
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
            keywords=["AI", "security"]
        )
        
        # Update mock for second call
        mock_message.content = json.dumps(credibility_response)
        
        cred_result = assess_article_credibility(
            openai_client=mock_client,
            title="AI Security Article",
            description="Article about AI security",
            url="https://example.com",
            source_name="Tech Blog",
            domain_credibility="medium"
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
        model="gpt-4o-mini"
    )

    assert isinstance(result, dict)
    assert "applicable" in result
    assert "score" in result
    assert 0.0 <= result["score"] <= 1.0
