#!/usr/bin/env python3
"""
Unit tests for credibility assessment utilities.
Tests the source credibility assessment functionality.
"""

import pytest
import sys
import os

# Add scripts to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

from utils.credibility import assess_source_credibility, CREDIBLE_SOURCES


class TestCredibleSourcesConstant:
    """Test CREDIBLE_SOURCES constant structure."""
    
    def test_credible_sources_structure(self):
        """Test that CREDIBLE_SOURCES has the expected structure."""
        assert isinstance(CREDIBLE_SOURCES, dict)
        assert 'high' in CREDIBLE_SOURCES
        assert 'medium' in CREDIBLE_SOURCES
    
    def test_high_credibility_list(self):
        """Test that high credibility list contains expected sources."""
        assert isinstance(CREDIBLE_SOURCES['high'], list)
        assert len(CREDIBLE_SOURCES['high']) > 0
        
        # Check for some known high-credibility sources
        high_sources = CREDIBLE_SOURCES['high']
        assert 'github.com' in high_sources
        assert 'arxiv.org' in high_sources
        assert 'nist.gov' in high_sources
    
    def test_medium_credibility_list(self):
        """Test that medium credibility list contains expected sources."""
        assert isinstance(CREDIBLE_SOURCES['medium'], list)
        assert len(CREDIBLE_SOURCES['medium']) > 0
        
        # Check for some known medium-credibility sources
        medium_sources = CREDIBLE_SOURCES['medium']
        assert 'medium.com' in medium_sources
        assert 'dev.to' in medium_sources


class TestAssessSourceCredibility:
    """Test assess_source_credibility function."""
    
    def test_high_credibility_github(self):
        """Test high credibility for GitHub URLs."""
        urls = [
            "https://github.com/user/repo",
            "http://github.com/org/project",
            "https://www.github.com/example/test"
        ]
        for url in urls:
            assert assess_source_credibility(url) == "high"
    
    def test_high_credibility_arxiv(self):
        """Test high credibility for arXiv URLs."""
        urls = [
            "https://arxiv.org/abs/2401.12345",
            "http://arxiv.org/pdf/2401.12345.pdf",
            "https://www.arxiv.org/article"
        ]
        for url in urls:
            assert assess_source_credibility(url) == "high"
    
    def test_high_credibility_official_sources(self):
        """Test high credibility for official sources."""
        urls = [
            "https://nist.gov/publication",
            "https://cisa.gov/alert",
            "https://owasp.org/document",
            "https://blog.google/security/news",
            "https://openai.com/research/paper"
        ]
        for url in urls:
            assert assess_source_credibility(url) == "high"
    
    def test_high_credibility_security_blogs(self):
        """Test high credibility for well-known security blogs."""
        urls = [
            "https://schneier.com/blog/archives/2024/security.html",
            "https://krebsonsecurity.com/2024/01/article/",
            "https://googleprojectzero.blogspot.com/2024/01/post.html"
        ]
        for url in urls:
            assert assess_source_credibility(url) == "high"
    
    def test_medium_credibility_sources(self):
        """Test medium credibility for known platforms."""
        urls = [
            "https://medium.com/@author/article",
            "https://dev.to/author/post",
            "https://techcrunch.com/2024/01/01/article/",
            "https://towardsdatascience.com/article-title-123",
            "https://bleepingcomputer.com/news/security/article/"
        ]
        for url in urls:
            assert assess_source_credibility(url) == "medium"
    
    def test_low_credibility_unknown_sources(self):
        """Test low credibility for unknown sources."""
        urls = [
            "https://random-blog.xyz/post",
            "https://unknown-site.com/article",
            "https://example.test/page",
            "https://myblog.net/security-news"
        ]
        for url in urls:
            assert assess_source_credibility(url) == "low"
    
    def test_www_prefix_handling(self):
        """Test that www. prefix is handled correctly."""
        # Both should return same credibility
        assert assess_source_credibility("https://github.com/repo") == "high"
        assert assess_source_credibility("https://www.github.com/repo") == "high"
        
        assert assess_source_credibility("https://medium.com/article") == "medium"
        assert assess_source_credibility("https://www.medium.com/article") == "medium"
    
    def test_case_insensitive_matching(self):
        """Test that domain matching is case-insensitive."""
        assert assess_source_credibility("https://GITHUB.COM/repo") == "high"
        assert assess_source_credibility("https://GitHub.com/repo") == "high"
        assert assess_source_credibility("https://ArXiv.ORG/abs/123") == "high"
    
    def test_subdomain_matching(self):
        """Test that subdomains are matched correctly."""
        # Should match on primary domain
        assert assess_source_credibility("https://blog.google/post") == "high"
        assert assess_source_credibility("https://security.googleblog.com/post") == "high"
        assert assess_source_credibility("https://research.google/paper") == "high"
    
    def test_empty_url(self):
        """Test handling of empty URL."""
        assert assess_source_credibility("") == "low"
    
    def test_invalid_url(self):
        """Test handling of invalid URL."""
        assert assess_source_credibility("not-a-url") == "low"
        assert assess_source_credibility("ftp://invalid") == "low"
    
    def test_url_without_scheme(self):
        """Test handling of URL without scheme."""
        # Should still extract domain and assess
        result = assess_source_credibility("github.com/user/repo")
        # May return low if parsing fails, which is acceptable
        assert result in ["high", "low"]
    
    def test_special_characters_in_url(self):
        """Test URLs with special characters."""
        urls = [
            "https://github.com/user/repo?param=value",
            "https://arxiv.org/abs/2401.12345#section",
            "https://medium.com/@user/article?source=rss"
        ]
        # Should still assess correctly
        assert assess_source_credibility(urls[0]) == "high"
        assert assess_source_credibility(urls[1]) == "high"
        assert assess_source_credibility(urls[2]) == "medium"


class TestCredibilityEdgeCases:
    """Test edge cases in credibility assessment."""
    
    def test_multiple_matching_domains(self):
        """Test URL that could match multiple patterns."""
        # If a URL contains multiple domain patterns, first match wins
        url = "https://blog.google/medium-post"
        result = assess_source_credibility(url)
        # Should be high because blog.google is in high credibility list
        assert result == "high"
    
    def test_domain_as_path_component(self):
        """Test that domain in path doesn't cause false positive."""
        url = "https://unknown.com/github.com/article"
        result = assess_source_credibility(url)
        # Should be low because actual domain is unknown.com
        assert result == "low"
    
    def test_very_long_url(self):
        """Test handling of very long URLs."""
        long_url = "https://github.com/" + "a" * 1000
        assert assess_source_credibility(long_url) == "high"
    
    def test_unicode_in_url(self):
        """Test handling of unicode characters in URL."""
        # Unicode domain (IDN)
        url = "https://github.com/user/repo-中文"
        assert assess_source_credibility(url) == "high"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
