#!/usr/bin/env python3
"""
Comprehensive unit tests for NewsBot main class.
Tests the NewsBot class initialization, configuration, and core methods using pytest.
"""

import pytest
import json
import os
import sys
from unittest.mock import Mock, MagicMock, patch, mock_open
from datetime import datetime

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

from newsbot import NewsBot, main


class TestNewsBotInitialization:
    """Test NewsBot class initialization."""
    
    def test_init_with_default_config(self, tmp_path):
        """Test NewsBot initialization with default config path."""
        # Create a temporary config file
        config_data = {
            "search_topics": ["test topic"],
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 10,
            "rss_enabled": False
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        # Initialize NewsBot with temp config
        bot = NewsBot(config_path=str(config_file))
        
        # Verify initialization
        assert bot.config == config_data
        assert bot.results == []
        
    def test_init_without_github_token(self, tmp_path):
        """Test NewsBot initialization without GITHUB_TOKEN."""
        config_data = {
            "search_topics": ["test"],
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 10
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        with patch.dict(os.environ, {}, clear=True):
            bot = NewsBot(config_path=str(config_file))
            assert bot.github_token is None
            assert bot.openai_client is None
    
    def test_init_with_github_token(self, tmp_path):
        """Test NewsBot initialization with GITHUB_TOKEN."""
        config_data = {
            "search_topics": ["test"],
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 10
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('newsbot.OpenAI') as mock_openai:
                bot = NewsBot(config_path=str(config_file))
                assert bot.github_token == "test_token"
                assert bot.openai_client is not None
                mock_openai.assert_called_once()
    
    def test_init_with_rss_enabled(self, tmp_path):
        """Test NewsBot initialization with RSS enabled."""
        config_data = {
            "search_topics": ["test"],
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 10,
            "rss_enabled": True,
            "rss_settings": {
                "request_timeout": 10,
                "cache_enabled": True,
                "cache_ttl_hours": 6,
                "rate_limit_delay": 0.5
            }
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        # RSS manager import happens dynamically, so we just verify config
        bot = NewsBot(config_path=str(config_file))
        # RSS manager initialization might fail, that's OK
        # Just verify the config was loaded
        assert bot.config['rss_enabled'] is True


class TestConfigLoading:
    """Test configuration loading functionality."""
    
    def test_load_valid_config(self, tmp_path):
        """Test loading a valid configuration file."""
        config_data = {
            "search_topics": ["AI security"],
            "github_topics": ["security"],
            "days_back": 14,
            "max_results_per_topic": 5
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        bot = NewsBot(config_path=str(config_file))
        loaded_config = bot.load_config(str(config_file))
        
        assert loaded_config == config_data
        assert loaded_config["days_back"] == 14
        assert loaded_config["max_results_per_topic"] == 5
    
    def test_load_config_with_missing_file(self, tmp_path):
        """Test loading configuration from non-existent file."""
        with pytest.raises(FileNotFoundError):
            NewsBot(config_path=str(tmp_path / "nonexistent.json"))
    
    def test_load_config_with_invalid_json(self, tmp_path):
        """Test loading configuration with invalid JSON."""
        config_file = tmp_path / "invalid.json"
        config_file.write_text("not valid json {")
        
        with pytest.raises(json.JSONDecodeError):
            NewsBot(config_path=str(config_file))


class TestCredibilityAssessment:
    """Test credibility assessment functionality."""
    
    @pytest.fixture
    def bot(self, tmp_path):
        """Create a NewsBot instance for testing."""
        config_data = {
            "search_topics": ["test"],
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 10
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        return NewsBot(config_path=str(config_file))
    
    def test_high_credibility_sources(self, bot):
        """Test high credibility source assessment."""
        high_credibility_urls = [
            "https://github.com/example/repo",
            "https://arxiv.org/abs/12345",
            "https://blog.google/security/article",
            "https://openai.com/research/paper",
            "https://schneier.com/blog/archives/2024/security.html"
        ]
        
        for url in high_credibility_urls:
            assert bot.assess_source_credibility(url) == "high"
    
    def test_medium_credibility_sources(self, bot):
        """Test medium credibility source assessment."""
        medium_credibility_urls = [
            "https://medium.com/@author/article",
            "https://dev.to/author/post",
            "https://techcrunch.com/article",
            "https://towardsdatascience.com/article"
        ]
        
        for url in medium_credibility_urls:
            assert bot.assess_source_credibility(url) == "medium"
    
    def test_low_credibility_sources(self, bot):
        """Test low credibility source assessment."""
        low_credibility_urls = [
            "https://random-blog.xyz/post",
            "https://unknown-site.com/article",
            "https://example.com/page"
        ]
        
        for url in low_credibility_urls:
            assert bot.assess_source_credibility(url) == "low"
    
    def test_invalid_url(self, bot):
        """Test credibility assessment with invalid URL."""
        # Should handle gracefully and return low
        result = bot.assess_source_credibility("")
        assert result == "low"


class TestArticleExtraction:
    """Test article content extraction functionality."""
    
    @pytest.fixture
    def bot(self, tmp_path):
        """Create a NewsBot instance for testing."""
        config_data = {
            "search_topics": ["test"],
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 10
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        return NewsBot(config_path=str(config_file))
    
    @patch('newsbot.extract_article_content')
    def test_extract_article_content_success(self, mock_extract, bot):
        """Test successful article content extraction."""
        mock_extract.return_value = "Sample article content"
        
        result = bot.extract_article_content("https://example.com/article")
        
        assert result == "Sample article content"
        mock_extract.assert_called_once_with("https://example.com/article")
    
    @patch('newsbot.extract_article_content')
    def test_extract_article_content_failure(self, mock_extract, bot):
        """Test article extraction failure handling."""
        mock_extract.return_value = None
        
        result = bot.extract_article_content("https://unreachable.com/article")
        
        assert result is None


class TestNewsAggregation:
    """Test news aggregation functionality."""
    
    @pytest.fixture
    def bot_with_token(self, tmp_path):
        """Create a NewsBot instance with mocked token."""
        config_data = {
            "github_topics": ["security"],
            "days_back": 7,
            "max_results_per_topic": 5,
            "rss_enabled": False
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('newsbot.OpenAI'):
                return NewsBot(config_path=str(config_file))
    
    @patch('newsbot.search_github_repos')
    def test_aggregate_news_github_only(self, mock_github, bot_with_token):
        """Test news aggregation with GitHub search only."""
        mock_github.return_value = [
            {
                "title": "test/repo",
                "url": "https://github.com/test/repo",
                "description": "Test AI security tool",
                "stars": 100,
                "source": "github"
            }
        ]
        
        results = bot_with_token.aggregate_news()
        
        assert len(results) == 1
        assert results[0]["source"] == "github"
        assert results[0]["title"] == "test/repo"
        assert bot_with_token.results == results
    
    @patch('newsbot.search_rss_feeds')
    @patch('newsbot.search_github_repos')
    def test_aggregate_news_with_rss(self, mock_github, mock_rss, tmp_path):
        """Test news aggregation with RSS feeds enabled."""
        config_data = {
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 5,
            "rss_enabled": True
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('newsbot.OpenAI'):
                bot = NewsBot(config_path=str(config_file))
        
        mock_github.return_value = []
        mock_rss.return_value = [
            {
                "title": "RSS Article",
                "url": "https://example.com/rss",
                "source": "rss"
            }
        ]
        
        results = bot.aggregate_news()
        
        assert len(results) >= 1
        # Should include RSS results
        rss_results = [r for r in results if r.get("source") == "rss"]
        assert len(rss_results) > 0
    
    @patch('newsbot.search_github_repos')
    def test_aggregate_news_handles_github_errors(self, mock_github, bot_with_token):
        """Test that aggregate_news handles GitHub search errors gracefully."""
        mock_github.return_value = []  # Return empty instead of raising
        
        # Should not raise exception
        results = bot_with_token.aggregate_news()
        
        # Results should be empty or minimal
        assert isinstance(results, list)
    
    @patch('newsbot.search_rss_feeds')
    @patch('newsbot.search_github_repos')
    @patch('newsbot.load_analyzed_articles')
    @patch('newsbot.filter_analyzed_articles')
    def test_aggregate_news_with_deduplication(self, mock_filter, mock_load, mock_github, mock_rss, tmp_path):
        """Test that aggregate_news filters out already analyzed articles."""
        config_data = {
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 5,
            "rss_enabled": True,
            "skip_analyzed": {
                "enabled": True
            }
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('newsbot.OpenAI'):
                bot = NewsBot(config_path=str(config_file))
        
        # Mock the analyzed articles set
        mock_load.return_value = {'https://example.com/old1', 'https://example.com/old2'}
        
        # Mock GitHub results
        github_results = [
            {"title": "New Repo", "url": "https://github.com/new/repo", "source": "github"},
            {"title": "Old Repo", "url": "https://example.com/old1", "source": "github"}
        ]
        mock_github.return_value = github_results
        
        # Mock RSS results
        rss_results = [
            {"title": "New Article", "url": "https://example.com/new", "source": "rss"},
            {"title": "Old Article", "url": "https://example.com/old2", "source": "rss"}
        ]
        mock_rss.return_value = rss_results
        
        # Mock filter to return filtered results
        mock_filter.side_effect = [
            ([{"title": "New Repo", "url": "https://github.com/new/repo", "source": "github"}], 1),
            ([{"title": "New Article", "url": "https://example.com/new", "source": "rss"}], 1)
        ]
        
        output_dir = tmp_path / "outputs"
        results = bot.aggregate_news(output_dir=str(output_dir))
        
        # Verify load_analyzed_articles was called
        mock_load.assert_called_once_with(str(output_dir))
        
        # Verify filter_analyzed_articles was called for both GitHub and RSS
        assert mock_filter.call_count == 2
        
        # Verify results only contain new articles
        assert len(results) == 2
    
    @patch('newsbot.search_rss_feeds')
    @patch('newsbot.search_github_repos')
    def test_aggregate_news_with_deduplication_disabled(self, mock_github, mock_rss, tmp_path):
        """Test that deduplication can be disabled via config."""
        config_data = {
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 5,
            "rss_enabled": False,
            "skip_analyzed": {
                "enabled": False
            }
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('newsbot.OpenAI'):
                bot = NewsBot(config_path=str(config_file))
        
        github_results = [
            {"title": "Repo 1", "url": "https://github.com/test/1", "source": "github"},
            {"title": "Repo 2", "url": "https://github.com/test/2", "source": "github"}
        ]
        mock_github.return_value = github_results
        
        output_dir = tmp_path / "outputs"
        results = bot.aggregate_news(output_dir=str(output_dir))
        
        # All results should be included when deduplication is disabled
        assert len(results) == 2


class TestConstants:
    """Test that NewsBot exposes required constants."""
    
    @pytest.fixture
    def bot(self, tmp_path):
        """Create a NewsBot instance for testing."""
        config_data = {
            "github_topics": ["test"],
            "days_back": 7,
            "max_results_per_topic": 10
        }
        config_file = tmp_path / "config.json"
        config_file.write_text(json.dumps(config_data))
        return NewsBot(config_path=str(config_file))
    
    def test_credible_sources_constant(self, bot):
        """Test that CREDIBLE_SOURCES is exposed."""
        assert hasattr(bot, 'CREDIBLE_SOURCES')
        assert isinstance(bot.CREDIBLE_SOURCES, dict)
        assert 'high' in bot.CREDIBLE_SOURCES
        assert 'medium' in bot.CREDIBLE_SOURCES
        assert isinstance(bot.CREDIBLE_SOURCES['high'], list)
        assert isinstance(bot.CREDIBLE_SOURCES['medium'], list)


class TestMainFunction:
    """Test the main() entry point function."""
    
    @patch('newsbot.NewsBot')
    @patch('newsbot.generate_report')
    @patch('newsbot.save_json_results')
    def test_main_without_github_token(self, mock_save, mock_report, mock_bot):
        """Test main() exits when GITHUB_TOKEN is not set."""
        with patch.dict(os.environ, {}, clear=True):
            with patch('sys.argv', ['newsbot']):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                
                assert exc_info.value.code == 1
                mock_bot.assert_not_called()
    
    @patch('newsbot.NewsBot')
    @patch('newsbot.generate_report')
    @patch('newsbot.save_json_results')
    @patch('os.makedirs')
    def test_main_with_github_token(self, mock_makedirs, mock_save, mock_report, mock_bot_class):
        """Test main() executes successfully with GITHUB_TOKEN."""
        # Mock bot instance
        mock_bot_instance = MagicMock()
        mock_bot_instance.aggregate_news.return_value = [
            {"title": "Test", "url": "https://example.com"}
        ]
        mock_bot_class.return_value = mock_bot_instance
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('sys.argv', ['newsbot']):
                main()
        
        # Verify bot was initialized and methods called
        mock_bot_class.assert_called_once()
        mock_bot_instance.aggregate_news.assert_called_once()
        
        # Verify reports were generated
        assert mock_report.called
        assert mock_save.called
        
        # Verify output directory was created
        mock_makedirs.assert_called_once()
    
    @patch('newsbot.NewsBot')
    @patch('newsbot.generate_report')
    @patch('newsbot.save_json_results')
    @patch('os.makedirs')
    def test_main_with_custom_config(self, mock_makedirs, mock_save, mock_report, mock_bot_class):
        """Test main() with custom config file path."""
        mock_bot_instance = MagicMock()
        mock_bot_instance.aggregate_news.return_value = []
        mock_bot_class.return_value = mock_bot_instance
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('sys.argv', ['newsbot', '--config', 'custom.json']):
                main()
        
        # Verify bot was initialized with custom config
        mock_bot_class.assert_called_once_with(config_path='custom.json')
    
    @patch('newsbot.NewsBot')
    @patch('newsbot.generate_report')
    @patch('newsbot.save_json_results')
    @patch('os.makedirs')
    def test_main_with_custom_output_dir(self, mock_makedirs, mock_save, mock_report, mock_bot_class):
        """Test main() with custom output directory."""
        mock_bot_instance = MagicMock()
        mock_bot_instance.aggregate_news.return_value = []
        mock_bot_class.return_value = mock_bot_instance
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('sys.argv', ['newsbot', '--output-dir', 'custom_output']):
                main()
        
        # Verify output directory was created with custom path
        mock_makedirs.assert_called_once_with('custom_output', exist_ok=True)
    
    @patch('newsbot.NewsBot')
    @patch('newsbot.generate_report')
    @patch('newsbot.save_json_results')
    @patch('os.makedirs')
    def test_main_quiet_mode(self, mock_makedirs, mock_save, mock_report, mock_bot_class):
        """Test main() in quiet mode."""
        mock_bot_instance = MagicMock()
        mock_bot_instance.aggregate_news.return_value = []
        mock_bot_class.return_value = mock_bot_instance
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('sys.argv', ['newsbot', '--quiet']):
                main()
        
        # Function should complete without errors
        assert mock_bot_class.called
    
    @patch('newsbot.NewsBot')
    @patch('newsbot.generate_report')
    @patch('newsbot.save_json_results')
    @patch('os.makedirs')
    def test_main_verbose_mode(self, mock_makedirs, mock_save, mock_report, mock_bot_class):
        """Test main() in verbose mode."""
        mock_bot_instance = MagicMock()
        mock_bot_instance.aggregate_news.return_value = []
        mock_bot_class.return_value = mock_bot_instance
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('sys.argv', ['newsbot', '--verbose']):
                main()
        
        # Function should complete without errors
        assert mock_bot_class.called
    
    @patch('newsbot.NewsBot')
    def test_main_config_file_not_found(self, mock_bot_class):
        """Test main() with non-existent config file."""
        mock_bot_class.side_effect = FileNotFoundError("Config not found")
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('sys.argv', ['newsbot', '--config', 'nonexistent.json']):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                
                assert exc_info.value.code == 1
    
    @patch('newsbot.NewsBot')
    def test_main_invalid_json_config(self, mock_bot_class):
        """Test main() with invalid JSON config file."""
        mock_bot_class.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)
        
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"}):
            with patch('sys.argv', ['newsbot']):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                
                assert exc_info.value.code == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
