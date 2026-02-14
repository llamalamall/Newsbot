#!/usr/bin/env python3
"""
Unit tests for GitHub search functionality.
Tests the GitHub repository search module.
"""

import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

from searchers.github_search import search_github_repos


class TestSearchGitHubRepos:
    """Test search_github_repos function."""
    
    def test_search_without_token(self):
        """Test search returns empty list when no token provided."""
        results = search_github_repos(
            github_token=None,
            github_topics=["security"],
            days_back=7,
            max_results_per_topic=10
        )
        
        assert results == []
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_search_with_valid_token(self, mock_auth, mock_github):
        """Test search with valid GitHub token."""
        # Mock repository object
        mock_repo = Mock()
        mock_repo.full_name = "test/repo"
        mock_repo.html_url = "https://github.com/test/repo"
        mock_repo.description = "AI security testing tool"
        mock_repo.stargazers_count = 100
        mock_repo.updated_at = datetime.now()
        
        # Mock search results - return a list directly
        # GitHub API uses slicing like [:max_results_per_topic]
        mock_search = [mock_repo]
        
        # Mock GitHub instance
        mock_g = Mock()
        mock_g.search_repositories.return_value = mock_search
        mock_github.return_value = mock_g
        
        # Mock auth
        mock_auth_instance = Mock()
        mock_auth.Token.return_value = mock_auth_instance
        
        results = search_github_repos(
            github_token="test_token",
            github_topics=["security"],
            days_back=7,
            max_results_per_topic=10
        )
        
        assert isinstance(results, list)
        assert len(results) > 0
        assert results[0]["title"] == "test/repo"
        assert results[0]["source"] == "github"
        assert "url" in results[0]
        assert "description" in results[0]
        assert "stars" in results[0]
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_search_filters_by_ai_keywords(self, mock_auth, mock_github):
        """Test that search filters repositories by AI/automation keywords."""
        # Mock repo with AI keywords
        mock_repo_ai = Mock()
        mock_repo_ai.full_name = "test/ai-tool"
        mock_repo_ai.html_url = "https://github.com/test/ai-tool"
        mock_repo_ai.description = "AI-powered security scanner"
        mock_repo_ai.stargazers_count = 50
        mock_repo_ai.updated_at = datetime.now()
        
        # Mock repo without AI keywords
        mock_repo_no_ai = Mock()
        mock_repo_no_ai.full_name = "test/regular-tool"
        mock_repo_no_ai.html_url = "https://github.com/test/regular-tool"
        mock_repo_no_ai.description = "Regular security tool"
        mock_repo_no_ai.stargazers_count = 30
        mock_repo_no_ai.updated_at = datetime.now()
        
        # Mock search results with both repos
        mock_search = [mock_repo_ai, mock_repo_no_ai]
        
        mock_g = Mock()
        mock_g.search_repositories.return_value = mock_search
        mock_github.return_value = mock_g
        
        mock_auth.Token.return_value = Mock()
        
        results = search_github_repos(
            github_token="test_token",
            github_topics=["security"],
            days_back=7,
            max_results_per_topic=10
        )
        
        # Should only include AI repo
        assert len(results) == 1
        assert results[0]["title"] == "test/ai-tool"
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_search_multiple_topics(self, mock_auth, mock_github):
        """Test search with multiple topics."""
        mock_repo = Mock()
        mock_repo.full_name = "test/repo"
        mock_repo.html_url = "https://github.com/test/repo"
        mock_repo.description = "AI security tool"
        mock_repo.stargazers_count = 100
        mock_repo.updated_at = datetime.now()
        
        mock_search = [mock_repo]
        
        mock_g = Mock()
        mock_g.search_repositories.return_value = mock_search
        mock_github.return_value = mock_g
        
        mock_auth.Token.return_value = Mock()
        
        topics = ["security", "penetration-testing", "red-team"]
        results = search_github_repos(
            github_token="test_token",
            github_topics=topics,
            days_back=7,
            max_results_per_topic=5
        )
        
        # Should search each topic
        assert mock_g.search_repositories.call_count == len(topics)
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_search_respects_max_results(self, mock_auth, mock_github):
        """Test that search respects max_results_per_topic limit."""
        # Create many mock repos
        mock_repos = []
        for i in range(20):
            mock_repo = Mock()
            mock_repo.full_name = f"test/repo{i}"
            mock_repo.html_url = f"https://github.com/test/repo{i}"
            mock_repo.description = f"AI tool {i}"
            mock_repo.stargazers_count = i
            mock_repo.updated_at = datetime.now()
            mock_repos.append(mock_repo)
        
        mock_g = Mock()
        mock_g.search_repositories.return_value = mock_repos
        mock_github.return_value = mock_g
        
        mock_auth.Token.return_value = Mock()
        
        max_results = 5
        results = search_github_repos(
            github_token="test_token",
            github_topics=["security"],
            days_back=7,
            max_results_per_topic=max_results
        )
        
        # Should limit to max_results
        assert len(results) <= max_results
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_search_includes_date_filter(self, mock_auth, mock_github):
        """Test that search query includes date filter."""
        mock_g = Mock()
        mock_g.search_repositories.return_value = []
        mock_github.return_value = mock_g
        
        mock_auth.Token.return_value = Mock()
        
        days_back = 7
        search_github_repos(
            github_token="test_token",
            github_topics=["security"],
            days_back=days_back,
            max_results_per_topic=10
        )
        
        # Verify search was called with date filter
        call_args = mock_g.search_repositories.call_args
        assert call_args is not None
        query = call_args[1]['query']
        assert 'pushed:>=' in query
        assert 'topic:security' in query
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_search_sorts_by_updated(self, mock_auth, mock_github):
        """Test that search results are sorted by updated date."""
        mock_g = Mock()
        mock_g.search_repositories.return_value = []
        mock_github.return_value = mock_g
        
        mock_auth.Token.return_value = Mock()
        
        search_github_repos(
            github_token="test_token",
            github_topics=["security"],
            days_back=7,
            max_results_per_topic=10
        )
        
        # Verify sort and order parameters
        call_args = mock_g.search_repositories.call_args
        assert call_args[1]['sort'] == 'updated'
        assert call_args[1]['order'] == 'desc'
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_search_handles_topic_error(self, mock_auth, mock_github):
        """Test that search handles errors for individual topics gracefully."""
        # First topic succeeds
        mock_repo = Mock()
        mock_repo.full_name = "test/repo"
        mock_repo.html_url = "https://github.com/test/repo"
        mock_repo.description = "AI tool"
        mock_repo.stargazers_count = 50
        mock_repo.updated_at = datetime.now()
        
        # Mock to fail on second topic, succeed on first
        mock_g = Mock()
        mock_g.search_repositories.side_effect = [
            [mock_repo],  # First topic succeeds
            Exception("Rate limit exceeded")  # Second topic fails
        ]
        mock_github.return_value = mock_g
        
        mock_auth.Token.return_value = Mock()
        
        results = search_github_repos(
            github_token="test_token",
            github_topics=["security", "pentest"],
            days_back=7,
            max_results_per_topic=10
        )
        
        # Should return results from successful topic
        assert len(results) == 1
        assert results[0]["title"] == "test/repo"
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_search_handles_github_api_error(self, mock_auth, mock_github):
        """Test that search handles GitHub API initialization errors."""
        mock_github.side_effect = Exception("API Error")
        
        results = search_github_repos(
            github_token="test_token",
            github_topics=["security"],
            days_back=7,
            max_results_per_topic=10
        )
        
        # Should return empty list on error
        assert results == []
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_result_structure(self, mock_auth, mock_github):
        """Test that results have the expected structure."""
        mock_repo = Mock()
        mock_repo.full_name = "user/project"
        mock_repo.html_url = "https://github.com/user/project"
        mock_repo.description = "AI security automation tool"
        mock_repo.stargazers_count = 250
        mock_repo.updated_at = datetime(2024, 1, 15, 12, 0, 0)
        
        mock_g = Mock()
        mock_g.search_repositories.return_value = [mock_repo]
        mock_github.return_value = mock_g
        
        mock_auth.Token.return_value = Mock()
        
        results = search_github_repos(
            github_token="test_token",
            github_topics=["ai-security"],
            days_back=7,
            max_results_per_topic=10
        )
        
        assert len(results) == 1
        result = results[0]
        
        # Verify required fields
        assert "title" in result
        assert "url" in result
        assert "description" in result
        assert "stars" in result
        assert "updated" in result
        assert "source" in result
        assert "topic" in result
        
        # Verify values
        assert result["title"] == "user/project"
        assert result["url"] == "https://github.com/user/project"
        assert result["description"] == "AI security automation tool"
        assert result["stars"] == 250
        assert result["source"] == "github"
        assert result["topic"] == "ai-security"
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_repo_without_description(self, mock_auth, mock_github):
        """Test handling of repositories without description."""
        mock_repo = Mock()
        mock_repo.full_name = "test/no-desc"
        mock_repo.html_url = "https://github.com/test/no-desc"
        mock_repo.description = None
        mock_repo.stargazers_count = 10
        mock_repo.updated_at = datetime.now()
        
        mock_g = Mock()
        mock_g.search_repositories.return_value = [mock_repo]
        mock_github.return_value = mock_g
        
        mock_auth.Token.return_value = Mock()
        
        results = search_github_repos(
            github_token="test_token",
            github_topics=["security"],
            days_back=7,
            max_results_per_topic=10
        )
        
        # Should not include repo without description (can't match AI keywords)
        assert len(results) == 0
    
    @patch('searchers.github_search.Github')
    @patch('searchers.github_search.Auth')
    def test_ai_keyword_matching(self, mock_auth, mock_github):
        """Test various AI/automation keyword matching."""
        keywords_to_test = [
            ("AI powered tool", True),
            ("LLM integration", True),
            ("ML based scanner", True),
            ("machine learning security", True),
            ("automation framework", True),
            ("automated testing", True),
            ("GPT integration", True),
            ("regular tool", False),
            ("basic scanner", False),
        ]
        
        for description, should_match in keywords_to_test:
            mock_repo = Mock()
            mock_repo.full_name = "test/tool"
            mock_repo.html_url = "https://github.com/test/tool"
            mock_repo.description = description
            mock_repo.stargazers_count = 50
            mock_repo.updated_at = datetime.now()
            
            mock_g = Mock()
            mock_g.search_repositories.return_value = [mock_repo]
            mock_github.return_value = mock_g
            
            mock_auth.Token.return_value = Mock()
            
            results = search_github_repos(
                github_token="test_token",
                github_topics=["security"],
                days_back=7,
                max_results_per_topic=10
            )
            
            if should_match:
                assert len(results) == 1, f"Should match: {description}"
            else:
                assert len(results) == 0, f"Should not match: {description}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
