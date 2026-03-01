# Deeper Analysis Documentation

This directory contains planning and architecture documentation for the **Newsbot Deeper Article Analysis** feature.

## Overview

The Deeper Analysis feature provides on-demand, comprehensive validation of articles, blog posts, and repositories identified by Newsbot. Unlike the default automated workflow, deeper analysis is manually triggered via GitHub Actions and performs multi-source investigation to validate claims, detect hype, and assess real-world value.

## Documents in This Directory

### Core Planning Documents

1. **[DEEPER_ANALYSIS_PLAN.md](../DEEPER_ANALYSIS_PLAN.md)** (in parent `docs/` directory)
   - Main architecture and implementation plan
   - Complete workflow design
   - Report structure and format
   - Implementation phases (14-week roadmap)
   - Technical requirements and dependencies

2. **[DATA_SOURCES.md](DATA_SOURCES.md)**
   - Detailed specifications for each data source
   - API integration guides (Reddit, HN, Twitter, GitHub, etc.)
   - Data collection techniques and code examples
   - Credibility assessment criteria
   - Cost estimates and rate limiting strategies

3. **[TRIGGER_KEYWORDS.md](TRIGGER_KEYWORDS.md)**
   - List of supported trigger keywords
   - Usage examples and syntax
   - Access control and permissions
   - Rate limiting policies

4. **[REPORT_TEMPLATE.md](REPORT_TEMPLATE.md)**
   - Complete report structure template
   - Section descriptions and guidelines
   - Scoring rubrics
   - Example reports

## Quick Reference

### How to Trigger Deeper Analysis

**Syntax:**
```
analyze-deep: <URL or article ID>
```

**Examples:**
```
analyze-deep: https://blog.example.com/new-security-tool
analyze-deep: article_20260215_200451_013
analyze-deep: https://github.com/org/security-repo
```

**Who Can Trigger:**
- Repository collaborators (write access or higher)
- Organization members (if repo is org-owned)

**Rate Limits:**
- Maximum 5 analyses per day (configurable)
- Minimum 2-hour cooldown between analyses

### What Gets Analyzed

1. **Article Claims** - Extracts and validates explicit claims
2. **Community Sentiment** - Aggregates opinions from Reddit, HN, Twitter
3. **GitHub Repository Health** - Analyzes code quality, issues, maintenance
4. **Hype Detection** - Identifies unsupported marketing claims
5. **Enterprise Readiness** - Assesses production suitability (0-10 score)
6. **Security Effectiveness** - Evaluates offensive security value (0-10 score)

### Data Sources Analyzed

**Tier 1 (Primary):**
- Reddit (r/netsec, r/AskNetsec, r/redteamsec, etc.)
- Hacker News discussions
- GitHub repository analysis

**Tier 2 (Secondary):**
- Twitter/X security community
- Security forums (Exploit-DB, Packet Storm)
- YouTube tutorials and demos

**Tier 3 (Optional):**
- Google Scholar citations
- Conference talk mentions

### Report Output

**Location:** `docs/deeper-analysis/deep_analysis_[ID]_[DATE].md`

**Sections:**
- Executive Summary with verdict (VALIDATED / PARTIALLY VALIDATED / OVERHYPED / UNVERIFIED)
- Claim-by-claim analysis with evidence strength
- Multi-source investigation results
- Hype vs. Reality assessment
- Enterprise Readiness score (0-10)
- Security Effectiveness score (0-10)
- Community Sentiment analysis
- Recommendations

**Also Posted:**
- GitHub issue comment with quick summary
- Workflow artifact with full results
- Committed to repository (auto-updated index)

## Implementation Status

**Current Status:** Planning Phase ✅

**Implementation Phases:**

- [ ] Phase 1: Foundation (Weeks 1-2)
  - GitHub Actions workflow
  - Trigger keyword detection
  - Target validation

- [ ] Phase 2: Data Aggregation (Weeks 3-5)
  - Reddit integration
  - Hacker News integration
  - Twitter/X integration
  - Extended GitHub analysis

- [ ] Phase 3: LLM Analysis Engine (Weeks 6-8)
  - Claim extraction prompts
  - Hype detection algorithms
  - Evidence matching
  - Scoring systems

- [ ] Phase 4: Report Generation (Weeks 9-10)
  - Report template rendering
  - Structured output

- [ ] Phase 5: Integration & Publishing (Weeks 11-12)
  - Issue comment posting
  - Artifact upload
  - Auto-commit to repo

- [ ] Phase 6: Documentation & Polish (Weeks 13-14)
  - User guides
  - Example analyses
  - Troubleshooting

## Key Design Principles

### 1. Manual Trigger Only
- **Never** runs automatically as part of daily workflow
- Requires explicit user action via issue comment
- Prevents accidental API costs and respects rate limits

### 2. Evidence-Based Analysis
- All findings must have verifiable sources
- Confidence scores (0.0-1.0) for each assessment
- Clear attribution for all claims and evidence

### 3. Hype-Aware
- Actively identifies marketing language
- Flags unsupported superlatives and claims
- Distinguishes between marketing copy and verified capabilities

### 4. Enterprise-Focused
- Prioritizes large-scale production indicators
- Assesses scalability and support
- Evaluates integration with enterprise tools

### 5. Security Effectiveness First
- Emphasizes vulnerability discovery evidence
- Values red team adoption and offensive security integration
- Seeks proof of real-world penetration testing effectiveness

## Technical Architecture

```
GitHub Issue Comment (with keyword)
    ↓
GitHub Actions Workflow Triggered
    ↓
Target Validation & Parsing
    ↓
Multi-Source Data Collection
    ├── Reddit API
    ├── Hacker News API
    ├── Twitter/X Search
    ├── GitHub Repository Analysis
    ├── Security Forums
    └── YouTube/Scholar (optional)
    ↓
LLM-Powered Analysis
    ├── Claim Extraction
    ├── Evidence Matching
    ├── Hype Detection
    ├── Enterprise Assessment
    └── Security Effectiveness
    ↓
Report Generation (Markdown)
    ↓
Post Results to GitHub
    ├── Issue Comment (summary)
    ├── Workflow Artifact
    └── Commit to docs/deeper-analysis/
```

## Configuration Files

### Main Config: `config_deeper_analysis.json`

```json
{
  "trigger_keywords": ["analyze-deep:", "deep-analysis:", "investigate:", "/analyze-deep"],
  "rate_limit": {
    "max_per_day": 5,
    "cooldown_hours": 2
  },
  "data_sources": {
    "reddit": { "enabled": true, ... },
    "hackernews": { "enabled": true, ... },
    "twitter": { "enabled": true, ... },
    "github": { "enabled": true, ... }
  },
  "llm_analysis": {
    "model": "gpt-4o",
    "temperature": 0.3
  }
}
```

### Environment Variables

Required in GitHub Secrets:
- `GITHUB_TOKEN` (auto-provided)
- `REDDIT_CLIENT_ID`
- `REDDIT_CLIENT_SECRET`
- `REDDIT_USER_AGENT`
- `TWITTER_BEARER_TOKEN` (optional)
- `YOUTUBE_API_KEY` (optional)

## Cost Estimates

**Per Analysis:**
- LLM API calls: ~$0.10-0.50 (primary cost)
- Other APIs: Free (within quotas)
- **Total: ~$0.10-0.60**

**Monthly (at max rate of 5/day):**
- ~$15-90 per month (150 analyses)
- Most cost from GitHub Models LLM usage

## Security and Privacy

### Data Handling
- **No PII storage** - only public data
- **Anonymization** - option to anonymize usernames
- **Attribution** - all sources cited
- **Respect robots.txt** - ethical web scraping

### Access Control
- Restricted to repository collaborators
- Optional maintainer approval workflow
- Rate limiting prevents abuse
- All analysis requests logged

### API Credentials
- Stored in GitHub Secrets
- Never logged or exposed
- Regular rotation recommended

## Example Use Cases

### 1. Validate Hyped Tool
**Scenario:** New "AI-powered" security tool claims revolutionary capabilities

**Trigger:**
```
analyze-deep: https://example.com/revolutionary-ai-security-tool
```

**Analysis Focus:**
- Validate AI usage claims
- Check for enterprise deployments
- Assess actual vulnerability discoveries
- Detect marketing hype

### 2. Research Before Adoption
**Scenario:** Considering adopting a tool for enterprise red team

**Trigger:**
```
analyze-deep: https://github.com/vendor/offensive-tool
```

**Analysis Focus:**
- Enterprise readiness indicators
- Community health and support
- Issue response times
- Real-world effectiveness evidence

### 3. Investigate Conference Buzz
**Scenario:** Tool mentioned at Black Hat getting social media buzz

**Trigger:**
```
analyze-deep: article_20260215_200451_013
```

**Analysis Focus:**
- Separate hype from substance
- Find practitioner experiences
- Check for peer review or validation
- Assess community sentiment

## Contributing

To contribute to deeper analysis planning or implementation:

1. Review existing planning documents
2. Suggest improvements via issues
3. Propose new data sources
4. Refine scoring criteria
5. Improve report templates

## Related Documentation

- [Main README](../../README.md) - Newsbot overview
- [QUICKSTART](../../QUICKSTART.md) - Getting started with Newsbot
- [CONTRIBUTING](../../CONTRIBUTING.md) - Contribution guidelines

## Questions?

For questions about deeper analysis planning:
- Open an issue with the `enhancement` label
- Tag with `deeper-analysis` label
- Reference relevant planning documents

---

**Status:** Planning Complete ✅  
**Next Step:** Begin Phase 1 Implementation  
**Target:** Q2 2026
