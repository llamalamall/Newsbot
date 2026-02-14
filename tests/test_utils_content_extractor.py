#!/usr/bin/env python3
"""
Unit tests for content extraction utilities.
Tests the article content extraction functionality.
"""

import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

from utils.content_extractor import extract_article_content, MAX_ARTICLE_CONTENT_LENGTH


class TestMaxArticleContentLength:
    """Test MAX_ARTICLE_CONTENT_LENGTH constant."""
    
    def test_constant_exists(self):
        """Test that MAX_ARTICLE_CONTENT_LENGTH constant is defined."""
        assert MAX_ARTICLE_CONTENT_LENGTH is not None
        assert isinstance(MAX_ARTICLE_CONTENT_LENGTH, int)
        assert MAX_ARTICLE_CONTENT_LENGTH > 0


class TestExtractArticleContent:
    """Test extract_article_content function."""
    
    @patch('utils.content_extractor.requests.get')
    def test_successful_extraction_with_article_tag(self, mock_get):
        """Test successful content extraction with article tag."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <head><title>Test Article</title></head>
            <body>
                <header>Header content</header>
                <article>
                    <h1>Main Article Title</h1>
                    <p>This is the main content of the article.</p>
                    <p>Another paragraph with important information.</p>
                </article>
                <footer>Footer content</footer>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/article")
        
        assert result is not None
        assert "Main Article Title" in result
        assert "main content" in result
        # Header and footer should be removed
        assert "Header content" not in result
        assert "Footer content" not in result
    
    @patch('utils.content_extractor.requests.get')
    def test_successful_extraction_with_main_tag(self, mock_get):
        """Test successful content extraction with main tag."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <body>
                <nav>Navigation</nav>
                <main>
                    <h1>Page Title</h1>
                    <p>Main content here.</p>
                </main>
                <footer>Footer</footer>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/page")
        
        assert result is not None
        assert "Page Title" in result
        assert "Main content" in result
        assert "Navigation" not in result
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_removes_scripts_and_styles(self, mock_get):
        """Test that scripts and styles are removed."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <head>
                <style>body { color: red; }</style>
            </head>
            <body>
                <article>
                    <p>Good content</p>
                    <script>alert('bad');</script>
                    <style>.bad { display: none; }</style>
                    <p>More good content</p>
                </article>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/article")
        
        assert result is not None
        assert "Good content" in result
        assert "More good content" in result
        assert "alert" not in result
        assert "color: red" not in result
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_fallback_to_body(self, mock_get):
        """Test fallback to body when no main content tag found."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <body>
                <div>
                    <p>Some content without semantic tags</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/simple")
        
        assert result is not None
        assert "Some content" in result
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_with_content_class(self, mock_get):
        """Test extraction with .content class selector."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <body>
                <div class="sidebar">Sidebar</div>
                <div class="content">
                    <h1>Article Title</h1>
                    <p>Article content</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/article")
        
        assert result is not None
        assert "Article Title" in result or "Article content" in result
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_length_limit(self, mock_get):
        """Test that extracted content is limited to MAX_ARTICLE_CONTENT_LENGTH."""
        long_content = "A" * (MAX_ARTICLE_CONTENT_LENGTH + 1000)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = f"""
        <html>
            <body>
                <article>
                    <p>{long_content}</p>
                </article>
            </body>
        </html>
        """.encode()
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/long")
        
        assert result is not None
        assert len(result) <= MAX_ARTICLE_CONTENT_LENGTH
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_cleans_whitespace(self, mock_get):
        """Test that excessive whitespace is cleaned."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <body>
                <article>
                    <p>Line 1</p>
                    
                    
                    
                    <p>Line 2</p>
                </article>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/article")
        
        assert result is not None
        # Should not have excessive newlines
        assert "\n\n\n\n" not in result
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_http_error(self, mock_get):
        """Test handling of HTTP errors."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("404 Not Found")
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/notfound")
        
        assert result is None
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_timeout(self, mock_get):
        """Test handling of request timeout."""
        mock_get.side_effect = Exception("Timeout")
        
        result = extract_article_content("https://example.com/slow")
        
        assert result is None
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_connection_error(self, mock_get):
        """Test handling of connection errors."""
        mock_get.side_effect = Exception("Connection refused")
        
        result = extract_article_content("https://unreachable.com/article")
        
        assert result is None
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_invalid_html(self, mock_get):
        """Test handling of invalid HTML."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"Not valid HTML <><><<"
        mock_get.return_value = mock_response
        
        # Should not crash, may return None or partial content
        result = extract_article_content("https://example.com/invalid")
        # Just verify it doesn't crash
        assert result is None or isinstance(result, str)
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_empty_content(self, mock_get):
        """Test handling of empty content."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <body>
                <article></article>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/empty")
        
        assert result is None or result == ""
    
    @patch('utils.content_extractor.requests.get')
    def test_user_agent_header(self, mock_get):
        """Test that User-Agent header is set."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"<html><body><article>Content</article></body></html>"
        mock_get.return_value = mock_response
        
        extract_article_content("https://example.com/article")
        
        # Verify User-Agent was set
        call_args = mock_get.call_args
        assert call_args is not None
        headers = call_args[1].get('headers', {})
        assert 'User-Agent' in headers
        assert 'Newsbot' in headers['User-Agent']
    
    @patch('utils.content_extractor.requests.get')
    def test_timeout_parameter(self, mock_get):
        """Test that timeout parameter is set."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"<html><body>Content</body></html>"
        mock_get.return_value = mock_response
        
        extract_article_content("https://example.com/article")
        
        # Verify timeout was set
        call_args = mock_get.call_args
        assert call_args is not None
        timeout = call_args[1].get('timeout')
        assert timeout is not None
        assert timeout > 0


class TestContentExtractionEdgeCases:
    """Test edge cases in content extraction."""
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_with_nested_tags(self, mock_get):
        """Test extraction with deeply nested tags."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <body>
                <article>
                    <div>
                        <div>
                            <div>
                                <p>Deeply nested content</p>
                            </div>
                        </div>
                    </div>
                </article>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/nested")
        
        assert result is not None
        assert "Deeply nested content" in result
    
    @patch('utils.content_extractor.requests.get')
    def test_extraction_multiple_paragraphs(self, mock_get):
        """Test extraction preserves paragraph structure."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <body>
                <article>
                    <p>First paragraph.</p>
                    <p>Second paragraph.</p>
                    <p>Third paragraph.</p>
                </article>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        
        result = extract_article_content("https://example.com/multi")
        
        assert result is not None
        assert "First paragraph" in result
        assert "Second paragraph" in result
        assert "Third paragraph" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
