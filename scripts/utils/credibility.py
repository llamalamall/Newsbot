"""
Source credibility assessment utilities.
Provides functionality to assess the credibility of news sources based on domain.
"""

import logging
from urllib.parse import urlparse


# Credible news sources for security/tech news
CREDIBLE_SOURCES = {
    'high': [
        'arxiv.org', 'github.com', 'blog.google', 'openai.com', 'microsoft.com',
        'research.google', 'ai.meta.com', 'blog.cloudflare.com', 'security.googleblog.com',
        'blogs.microsoft.com', 'aws.amazon.com', 'engineering.fb.com', 'netflix.github.io',
        'github.blog', 'blog.github.com', 'nist.gov', 'cisa.gov', 'nvd.nist.gov',
        'owasp.org', 'sans.org', 'portswigger.net', 'schneier.com', 'krebsonsecurity.com',
        'blog.trailofbits.com', 'googleprojectzero.blogspot.com', 'thehackernews.com',
        'sec.cloudapps.cisco.com', 'blog.talosintelligence.com', 'talosintelligence.com',
        'cloud.google.com', 'crowdstrike.com', 'unit42.paloaltonetworks.com',
        'paloaltonetworks.com', 'isc.sans.edu'
    ],
    'medium': [
        'medium.com', 'towardsdatascience.com', 'dev.to', 'hackernoon.com',
        'researchgate.net', 'reddit.com/r/netsec', 'infosecurity-magazine.com',
        'bleepingcomputer.com', 'zdnet.com', 'arstechnica.com', 'wired.com',
        'techcrunch.com', 'venturebeat.com', 'darkreading.com',
        'blog.rapid7.com', 'rapid7.com', 'blog.qualys.com', 'qualys.com',
        'recordedfuture.com', 'sentinelone.com'
    ]
}


def assess_source_credibility(url: str) -> str:
    """Assess the credibility of a news source based on its domain.
    
    Args:
        url: The URL to assess
        
    Returns:
        'high', 'medium', or 'low' credibility rating
    """
    try:
        domain = urlparse(url).netloc.lower()
        # Remove www. prefix
        domain = domain.replace('www.', '')
        
        # Check against credible sources lists
        for credible_domain in CREDIBLE_SOURCES['high']:
            if credible_domain in domain:
                return 'high'
        
        for credible_domain in CREDIBLE_SOURCES['medium']:
            if credible_domain in domain:
                return 'medium'
        
        # Default to low if not recognized
        return 'low'
    except Exception as e:
        logging.warning(f"Error assessing credibility for {url}: {e}")
        return 'low'
