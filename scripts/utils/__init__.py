"""
Utility modules for NewsBot.
"""

from .credibility import assess_source_credibility, CREDIBLE_SOURCES
from .content_extractor import extract_article_content

__all__ = [
    'assess_source_credibility',
    'CREDIBLE_SOURCES',
    'extract_article_content'
]
