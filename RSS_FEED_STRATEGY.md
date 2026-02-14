# RSS Feed Migration Strategy

## Overview

This document outlines the comprehensive strategy for migrating from web search engine (DuckDuckGo HTML scraping) to a curated RSS feed aggregation system for Newsbot.

## Problem with Current Implementation

The current web search implementation has several limitations:

1. **Fragility**: HTML scraping can break when search engines change their layout
2. **Rate Limiting**: Strict limits on number of requests
3. **Content Quality**: Mixed results with ads and noise
4. **Limited Control**: No control over result ranking
5. **Access Issues**: May not work in restricted environments

## Benefits of RSS Feed Aggregation

1. **Reliability**: Structured RSS/Atom feeds are stable
2. **Cost**: Free access to most feeds (no API fees)
3. **Quality**: Curated sources provide relevant content
4. **Control**: Full control over source selection
5. **Performance**: No rate limits on reasonable polling
6. **Offline Capability**: Feeds can be cached

## Curated RSS Feed Sources (37+ feeds)

### Official Security Organizations (High Priority)
- **CISA**: https://www.cisa.gov/cybersecurity-advisories/all.xml
- **US-CERT**: https://www.cisa.gov/uscert/ncas/current-activity.xml
- **NIST NVD**: https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml

### Security Research & Blogs (High Priority)
- **Google Project Zero**: https://googleprojectzero.blogspot.com/feeds/posts/default
- **Trail of Bits Blog**: https://blog.trailofbits.com/feed/
- **Schneier on Security**: https://www.schneier.com/blog/atom.xml
- **Krebs on Security**: https://krebsonsecurity.com/feed/
- **The Hacker News**: https://thehackernews.com/feeds/posts/default

### AI & ML Security (High Priority)
- **OpenAI Blog**: https://openai.com/blog/rss.xml
- **Google AI Blog**: https://ai.googleblog.com/feeds/posts/default
- **Microsoft Security Blog**: https://www.microsoft.com/en-us/security/blog/feed/
- **Anthropic Blog**: https://www.anthropic.com/blog/rss.xml

### Security Tools & Frameworks (Medium Priority)
- **Metasploit Blog**: https://blog.rapid7.com/tag/metasploit/feed/
- **OWASP Blog**: https://owasp.org/blog/feed.xml
- **Kali Linux Blog**: https://www.kali.org/rss.xml
- **PortSwigger (Burp Suite)**: https://portswigger.net/blog/rss

### Security News Sites (Medium Priority)
- **BleepingComputer**: https://www.bleepingcomputer.com/feed/
- **Dark Reading**: https://www.darkreading.com/rss.xml
- **InfoSecurity Magazine**: https://www.infosecurity-magazine.com/rss/news/
- **SecurityWeek**: https://www.securityweek.com/feed/

### Academic & Research (Medium Priority)
- **arXiv CS.CR (Cryptography & Security)**: http://arxiv.org/rss/cs.CR
- **arXiv CS.AI (Artificial Intelligence)**: http://arxiv.org/rss/cs.AI
- **arXiv CS.LG (Machine Learning)**: http://arxiv.org/rss/cs.LG

### GitHub & Development (Low Priority - Supplement)
- **GitHub Security Blog**: https://github.blog/category/security/feed/
- **GitHub Engineering Blog**: https://github.blog/category/engineering/feed/

### Additional Quality Sources
- **Ars Technica Security**: https://feeds.arstechnica.com/arstechnica/security
- **Wired Security**: https://www.wired.com/feed/category/security/latest/rss
- **ZDNet Security**: https://www.zdnet.com/topic/security/rss.xml
- **TechCrunch Security**: https://techcrunch.com/category/security/feed/

### Red Team & Penetration Testing
- **Penetration Testing Lab**: https://pentestlab.blog/feed/
- **Red Team Journal**: https://redteamjournal.com/feed/
- **NetSPI Blog**: https://www.netspi.com/blog/feed/

### Reverse Engineering & Malware Analysis
- **Malwarebytes Labs**: https://blog.malwarebytes.com/feed/
- **Virus Bulletin**: https://www.virusbulletin.com/rss
- **Recorded Future**: https://www.recordedfuture.com/feed

### Cloud Security
- **AWS Security Blog**: https://aws.amazon.com/blogs/security/feed/
- **Google Cloud Security Blog**: https://cloud.google.com/blog/products/identity-security/rss
- **Azure Security Blog**: https://azure.microsoft.com/en-us/blog/topics/security/feed/

## Implementation Architecture

### Core Components

#### 1. RSSFeedManager Class
Located in `scripts/rss_feed_manager.py`

**Responsibilities:**
- Fetch and parse RSS/Atom feeds
- Cache feed data to reduce network calls
- Handle feed errors gracefully
- Extract article metadata (title, link, description, date)
- Filter articles by date range

**Key Methods:**
- `fetch_feed(url: str) -> List[Dict]`: Fetch and parse a single feed
- `fetch_all_feeds() -> List[Dict]`: Fetch all configured feeds
- `filter_by_date(entries: List, days_back: int) -> List`: Filter by date
- `is_feed_healthy(url: str) -> bool`: Check feed availability

#### 2. RSS Feed Processor
Located in `scripts/feed_processor.py` (optional - can be part of RSSFeedManager)

**Responsibilities:**
- Keyword-based relevance filtering
- Content scoring and ranking
- Deduplication across feeds
- LLM-based relevance assessment (optional)

**Key Methods:**
- `filter_by_keywords(entries: List, keywords: List) -> List`
- `calculate_relevance_score(entry: Dict) -> float`
- `deduplicate_entries(entries: List) -> List`

#### 3. Integration with NewsBot
Modify `scripts/newsbot.py`

**Changes:**
- Add `search_rss_feeds()` method
- Update `aggregate_news()` to include RSS results
- Add dual-mode support (RSS primary, web search fallback)
- Update report generation for RSS sources

### Configuration Structure

Add to `config.json`:

```json
{
  "content_source": "dual",
  "rss_enabled": true,
  "rss_feeds": [
    {
      "name": "CISA Cybersecurity Advisories",
      "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml",
      "priority": "high",
      "category": "official"
    },
    {
      "name": "Google Project Zero",
      "url": "https://googleprojectzero.blogspot.com/feeds/posts/default",
      "priority": "high",
      "category": "research"
    }
  ],
  "rss_settings": {
    "max_age_days": 7,
    "min_relevance_score": 0.6,
    "cache_enabled": true,
    "cache_ttl_hours": 6,
    "request_timeout": 10,
    "max_feeds_parallel": 5
  }
}
```

## Implementation Phases

### Phase 1: RSS Infrastructure (Week 1-2)
- [x] Add `feedparser>=6.0.10` dependency
- [x] Add `python-dateutil>=2.8.2` dependency
- [x] Create `RSSFeedManager` class
- [x] Implement basic feed polling
- [x] Add feed configuration to `config.json`

### Phase 2: Content Processing (Week 2-3)
- [ ] Implement keyword-based filtering
- [ ] Integrate with existing article extraction
- [ ] Adapt LLM prompts for RSS content
- [ ] Add relevance scoring

### Phase 3: Migration & Testing (Week 3-4)
- [ ] Dual-mode operation (RSS + Web Search)
- [ ] Testing and validation
- [ ] Update documentation
- [ ] Performance benchmarking

### Phase 4: Production Deployment (Week 4+)
- [ ] Switch to RSS as primary source
- [ ] Web search as fallback only
- [ ] Monitoring and optimization
- [ ] Community feedback integration

## Technical Details

### Dependencies

Add to `requirements.txt`:
```
feedparser>=6.0.10          # RSS/Atom feed parsing
python-dateutil>=2.8.2      # Date parsing and manipulation
```

### Feed Parsing Example

```python
import feedparser
from datetime import datetime, timedelta

def fetch_feed(feed_url: str, days_back: int = 7) -> List[Dict]:
    """Fetch and parse RSS feed."""
    feed = feedparser.parse(feed_url)
    cutoff_date = datetime.now() - timedelta(days=days_back)
    
    articles = []
    for entry in feed.entries:
        # Parse publication date
        pub_date = entry.get('published_parsed') or entry.get('updated_parsed')
        if pub_date:
            article_date = datetime(*pub_date[:6])
            if article_date >= cutoff_date:
                articles.append({
                    'title': entry.get('title', 'Untitled'),
                    'link': entry.get('link', ''),
                    'description': entry.get('summary', ''),
                    'published': article_date.isoformat(),
                    'source': feed.feed.get('title', 'Unknown')
                })
    
    return articles
```

### Relevance Filtering

```python
def filter_by_keywords(entries: List[Dict], keywords: List[str]) -> List[Dict]:
    """Filter entries by keyword relevance."""
    filtered = []
    for entry in entries:
        text = f"{entry['title']} {entry['description']}".lower()
        if any(keyword.lower() in text for keyword in keywords):
            filtered.append(entry)
    return filtered
```

## Success Metrics

### Quantitative Metrics
- **Content Coverage**: 20-50 relevant articles per day
- **Source Diversity**: 15+ unique sources contributing
- **Freshness**: Average article age < 2 days
- **Reliability**: Feed parsing uptime > 99%
- **Performance**: Report generation < 5 minutes

### Qualitative Metrics
- Content quality and relevance (manual review)
- Source credibility (% from high-credibility sources)
- Topic coverage breadth
- User satisfaction feedback

## Migration Strategy

### Week 1-2: Parallel Operation
- Run both RSS and web search simultaneously
- Compare results quality
- Identify gaps in coverage
- Tune filtering parameters

### Week 3-4: Gradual Transition
- Make RSS primary source
- Use web search for supplemental content only
- Monitor performance and quality
- Adjust feed list based on results

### Week 4+: Full Migration
- RSS as primary content source
- Web search as optional fallback
- Regular feed health monitoring
- Community-driven feed additions

## Potential Challenges & Solutions

### Challenge 1: Feed Availability
**Problem**: Not all sources offer RSS feeds  
**Solution**: 
- Focus on sources with feeds
- Use web search for sources without feeds
- Consider RSS-bridge or feed generators for some sites

### Challenge 2: Content Volume
**Problem**: Too many articles from all feeds  
**Solution**:
- Aggressive keyword filtering
- Relevance threshold (min score 0.6)
- LLM-based summarization
- Prioritize high-priority feeds

### Challenge 3: Feed Maintenance
**Problem**: Feeds may break or change URLs  
**Solution**:
- Automated health checks
- Regular feed validation
- Community reporting mechanism
- Quarterly feed audit

### Challenge 4: Relevance Filtering
**Problem**: RSS content may be too broad  
**Solution**:
- Strong keyword filtering
- Multiple keyword matches required
- LLM-powered relevance assessment
- Title and description analysis

## Monitoring & Maintenance

### Daily Monitoring
- Feed fetch success rate
- Number of articles collected
- Number of articles after filtering
- Processing time

### Weekly Review
- Feed health status
- Source diversity
- Content quality sampling
- Performance metrics

### Monthly Maintenance
- Add new feeds from community
- Remove consistently failing feeds
- Update keyword filters
- Review and adjust priorities

## Expected Outcomes

After full implementation:

1. **Reliability**: 99%+ uptime (no scraping fragility)
2. **Quality**: 80%+ of content from high-credibility sources
3. **Coverage**: 30-50 relevant articles per day
4. **Performance**: Report generation in < 5 minutes
5. **Cost**: $0 in API fees (vs. potential $100+/month for search APIs)
6. **Stability**: No breaking changes from external services
7. **Control**: Full control over sources and prioritization

## Community Engagement

We welcome community contributions:

1. **Feed Suggestions**: Submit PR with new feed URLs
2. **Feed Validation**: Report broken or outdated feeds
3. **Keyword Refinement**: Suggest better keyword filters
4. **Category Organization**: Propose feed categorization
5. **Quality Feedback**: Report low-quality sources

## References

- [RSS 2.0 Specification](https://www.rssboard.org/rss-specification)
- [Atom Syndication Format](https://www.ietf.org/rfc/rfc4287.txt)
- [feedparser Documentation](https://feedparser.readthedocs.io/)
- [python-dateutil Documentation](https://dateutil.readthedocs.io/)

## Conclusion

This RSS feed migration strategy provides a robust, reliable, and cost-effective alternative to web search scraping. The phased approach ensures smooth transition while maintaining service quality throughout the migration process.

The curated feed list covers all major areas of offensive security and AI/automation, with 37+ high-quality sources that provide comprehensive coverage of the target topics.

Implementation will be done in phases with dual-mode operation during migration, ensuring no disruption to existing functionality while enabling superior content aggregation capabilities.
