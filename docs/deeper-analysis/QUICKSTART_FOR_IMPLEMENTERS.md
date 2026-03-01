# Deeper Analysis - Quick Start for Future Implementation

This document provides a streamlined guide for developers who will implement the deeper analysis feature.

## Prerequisites

Before starting implementation:

1. ✅ Read [`DEEPER_ANALYSIS_PLAN.md`](../DEEPER_ANALYSIS_PLAN.md) - Complete architecture
2. ✅ Review [`DATA_SOURCES.md`](DATA_SOURCES.md) - Understand data collection approach
3. ✅ Familiarize with existing Newsbot codebase
4. ✅ Have access to GitHub repository with admin permissions

## Required API Credentials

### Must Have (Free)

- **GitHub Token** - Already available via `GITHUB_TOKEN` in Actions
- **Reddit API**
  - Get at: https://www.reddit.com/prefs/apps
  - Create "script" application
  - Note: Client ID, Client Secret, User Agent

### Optional (Enhance Analysis)

- **Twitter/X API** (paid) or use Nitter (free)
  - Official: https://developer.twitter.com/
  - Alternative: Self-host Nitter instance
- **YouTube Data API** (free with quota)
  - Get at: https://console.cloud.google.com/

## Setup Steps

### 1. Fork Repository & Create Branch

```bash
git clone https://github.com/your-username/Newsbot.git
cd Newsbot
git checkout -b feature/deeper-analysis
```

### 2. Install Additional Dependencies

Create `requirements_deeper_analysis.txt`:

```txt
praw>=7.7.0                # Reddit API
textblob>=0.17.0           # Sentiment analysis
jinja2>=3.1.2              # Report templates
```

Install:
```bash
pip install -r requirements_deeper_analysis.txt
```

### 3. Configure API Credentials

**For Local Development:**

Create `.env` file:
```bash
# Required
GITHUB_TOKEN=your_github_token
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=NewsbotDeeperAnalysis/1.0

# Optional
TWITTER_BEARER_TOKEN=your_twitter_token
YOUTUBE_API_KEY=your_youtube_key
```

**For GitHub Actions:**

Add secrets in repository settings:
- Settings → Secrets and variables → Actions → New repository secret
- Add each credential from above

### 4. Create Project Structure

```bash
mkdir -p scripts/data_collectors
mkdir -p scripts/analysis
mkdir -p prompts/deeper_analysis
mkdir -p templates
mkdir -p tests/deeper_analysis
```

## Implementation Roadmap

### Phase 1: Foundation (Weeks 1-2) ⚡ Start Here

**Goal:** Working trigger system that acknowledges analysis requests

**Tasks:**

1. **Create GitHub Actions Workflow**
   ```bash
   touch .github/workflows/deeper-analysis.yml
   ```
   
   Use template from `DEEPER_ANALYSIS_PLAN.md` section "Example Workflow Specification"

2. **Create Main Analysis Script**
   ```bash
   touch scripts/deeper_analysis.py
   ```
   
   Skeleton:
   ```python
   #!/usr/bin/env python3
   """
   Newsbot Deeper Analysis
   Manual-triggered comprehensive article validation
   """
   
   import argparse
   import logging
   
   def parse_target(target_str):
       """Parse target from trigger comment"""
       pass
   
   def validate_target(target):
       """Validate target is accessible"""
       pass
   
   def main():
       parser = argparse.ArgumentParser()
       parser.add_argument('--target', required=True)
       parser.add_argument('--issue-number', type=int)
       parser.add_argument('--output-dir', default='outputs/deeper-analysis')
       parser.add_argument('--config', default='config_deeper_analysis.json')
       
       args = parser.parse_args()
       
       # Implementation here
       print(f"Analyzing: {args.target}")
   
   if __name__ == '__main__':
       main()
   ```

3. **Test Workflow Trigger**
   - Create test issue
   - Post comment: `analyze-deep: https://example.com`
   - Verify workflow triggers
   - Check acknowledgment comment appears

**Success Criteria:**
- ✅ Workflow triggers on keyword in issue comment
- ✅ Script receives target correctly
- ✅ Posts "Analysis started" comment to issue

---

### Phase 2: Data Aggregation (Weeks 3-5)

**Goal:** Collect data from multiple sources reliably

**Priority Order:**

1. **Reddit Collector** (Week 3)
   ```bash
   touch scripts/data_collectors/reddit_collector.py
   ```
   
   Use code examples from `DATA_SOURCES.md` section "Reddit"

2. **Hacker News Collector** (Week 3)
   ```bash
   touch scripts/data_collectors/hn_collector.py
   ```
   
   Use Algolia HN API examples

3. **Extended GitHub Analysis** (Week 4)
   ```bash
   touch scripts/data_collectors/github_extended.py
   ```
   
   Extend existing `scripts/searchers/github_search.py`

4. **Twitter/X Collector** (Week 5 - Optional)
   ```bash
   touch scripts/data_collectors/twitter_collector.py
   ```
   
   Start with Nitter (free) before Twitter API

**Test Each Collector:**
```bash
# Example test
python scripts/data_collectors/reddit_collector.py --query "ai security automation"
```

**Success Criteria:**
- ✅ Each collector runs independently
- ✅ Returns structured data
- ✅ Handles rate limits gracefully
- ✅ Logs errors without crashing

---

### Phase 3: LLM Analysis Engine (Weeks 6-8)

**Goal:** Extract claims, detect hype, score enterprise readiness

**Prompts to Create:**

1. **Claim Extraction**
   ```bash
   touch prompts/deeper_analysis/claim_extraction.yaml
   touch prompts/deeper_analysis/claim_extraction_system.yaml
   ```

2. **Hype Detection**
   ```bash
   touch prompts/deeper_analysis/hype_detection.yaml
   touch prompts/deeper_analysis/hype_detection_system.yaml
   ```

3. **Enterprise Assessment**
   ```bash
   touch prompts/deeper_analysis/enterprise_assessment.yaml
   touch prompts/deeper_analysis/enterprise_assessment_system.yaml
   ```

4. **Security Effectiveness**
   ```bash
   touch prompts/deeper_analysis/security_effectiveness.yaml
   touch prompts/deeper_analysis/security_effectiveness_system.yaml
   ```

**Analysis Module:**
```bash
touch scripts/analysis/deeper_analyzer.py
```

**Success Criteria:**
- ✅ Extracts claims from article text
- ✅ Identifies hype words/phrases
- ✅ Scores enterprise readiness (0-10)
- ✅ Scores security effectiveness (0-10)
- ✅ Provides confidence scores

---

### Phase 4: Report Generation (Weeks 9-10)

**Goal:** Generate comprehensive markdown reports

**Tasks:**

1. **Create Report Template**
   ```bash
   touch templates/deeper_analysis_report.md.j2
   ```
   
   Use template from `DEEPER_ANALYSIS_PLAN.md` section "Output Format"

2. **Create Report Generator**
   ```bash
   touch scripts/reporters/deeper_report_generator.py
   ```
   
   Use Jinja2 for rendering

3. **Generate Test Reports**
   - Create 2-3 test reports with sample data
   - Verify formatting and completeness

**Success Criteria:**
- ✅ Generates well-formatted markdown
- ✅ All sections populated correctly
- ✅ Links and citations work
- ✅ Renders properly on GitHub Pages

---

### Phase 5: Integration & Publishing (Weeks 11-12)

**Goal:** Complete end-to-end workflow

**Tasks:**

1. **Issue Comment Poster**
   - Posts summary to triggering issue
   - Includes verdict and key findings
   - Links to full report

2. **Artifact Upload**
   - Uploads full results as workflow artifact
   - 90-day retention

3. **Auto-commit to Repository**
   - Commits report to `docs/deeper-analysis/`
   - Updates index page
   - Git commit and push

4. **End-to-End Testing**
   - Test with real articles
   - Verify all components work together
   - Performance optimization

**Success Criteria:**
- ✅ Complete workflow runs successfully
- ✅ Results posted to issue
- ✅ Report committed to repo
- ✅ Workflow completes in <15 minutes

---

### Phase 6: Documentation & Polish (Weeks 13-14)

**Goal:** User-ready documentation and examples

**Tasks:**

1. **User Guide**
   - How to trigger analyses
   - How to interpret results
   - Troubleshooting common issues

2. **Admin Guide**
   - Configuration options
   - API credential setup
   - Rate limit adjustment

3. **Example Analyses**
   - Run 2-3 real analyses
   - Include diverse article types
   - Document learnings

**Success Criteria:**
- ✅ Clear, comprehensive documentation
- ✅ Examples cover edge cases
- ✅ Users can trigger without help

---

## Testing Strategy

### Unit Tests

Create tests for each module:

```bash
# Test structure
tests/deeper_analysis/
├── test_reddit_collector.py
├── test_hn_collector.py
├── test_github_extended.py
├── test_deeper_analyzer.py
├── test_report_generator.py
└── test_integration.py
```

Example test:
```python
# tests/deeper_analysis/test_reddit_collector.py
import unittest
from scripts.data_collectors.reddit_collector import search_reddit

class TestRedditCollector(unittest.TestCase):
    def test_search_returns_results(self):
        results = search_reddit("security automation", max_results=5)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
```

### Integration Tests

Test complete workflow:

```python
# tests/deeper_analysis/test_integration.py
def test_end_to_end_analysis():
    """Test complete analysis workflow"""
    target = "https://example.com/test-article"
    
    # 1. Validate target
    assert validate_target(target)
    
    # 2. Collect data
    data = collect_all_sources(target)
    assert len(data) > 0
    
    # 3. Analyze
    analysis = analyze_with_llm(data)
    assert 'verdict' in analysis
    
    # 4. Generate report
    report = generate_report(analysis)
    assert len(report) > 1000  # Reasonable length
```

### Manual Testing Checklist

Before releasing:

- [ ] Trigger with URL works
- [ ] Trigger with article ID works
- [ ] Trigger with GitHub repo works
- [ ] Access control prevents unauthorized users
- [ ] Rate limiting enforced
- [ ] Reports generated correctly
- [ ] Issue comments posted
- [ ] Artifacts uploaded
- [ ] Reports committed to repo

---

## Development Workflow

### Daily Development

```bash
# 1. Pull latest changes
git pull origin feature/deeper-analysis

# 2. Create feature sub-branch
git checkout -b feature/deeper-analysis-reddit-collector

# 3. Make changes
# ... develop ...

# 4. Test locally
python -m pytest tests/deeper_analysis/

# 5. Commit
git add .
git commit -m "Add Reddit collector with tests"

# 6. Push
git push origin feature/deeper-analysis-reddit-collector

# 7. Create PR
# Open PR: feature/deeper-analysis-reddit-collector → feature/deeper-analysis
```

### Code Review Checklist

Before merging:

- [ ] Code follows PEP 8 style
- [ ] Functions have docstrings
- [ ] Type hints added
- [ ] Unit tests written
- [ ] Tests pass
- [ ] No hardcoded credentials
- [ ] Error handling implemented
- [ ] Logging added for debugging

---

## Configuration Management

### Development Config

`config_deeper_analysis.dev.json`:
```json
{
  "trigger_keywords": ["analyze-deep:", "test-analysis:"],
  "rate_limit": {
    "max_per_day": 100,
    "cooldown_hours": 0
  },
  "data_sources": {
    "reddit": { "enabled": true, "max_posts": 10 },
    "hackernews": { "enabled": true, "max_stories": 5 }
  },
  "llm_analysis": {
    "model": "gpt-4o",
    "temperature": 0.3
  }
}
```

### Production Config

`config_deeper_analysis.json`:
```json
{
  "trigger_keywords": ["analyze-deep:", "deep-analysis:", "investigate:", "/analyze-deep"],
  "rate_limit": {
    "max_per_day": 5,
    "cooldown_hours": 2
  },
  "data_sources": {
    "reddit": { "enabled": true, "max_posts": 50 },
    "hackernews": { "enabled": true, "max_stories": 20 },
    "twitter": { "enabled": true, "max_tweets": 100 },
    "github": { "enabled": true, "max_issues": 100 }
  }
}
```

---

## Troubleshooting

### Common Issues

**Issue:** Reddit API returns 401 Unauthorized

**Solution:**
- Verify `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are correct
- Check Reddit app is configured as "script" type
- Ensure user agent is descriptive

---

**Issue:** LLM returns inconsistent JSON

**Solution:**
- Add JSON parsing retry logic
- Use temperature=0.1-0.3 for more consistent output
- Include JSON schema in prompt
- Parse with regex fallback

---

**Issue:** Workflow times out after 6 hours

**Solution:**
- Reduce data collection limits
- Implement caching for repeated requests
- Parallelize data collection where possible
- Add timeout to individual API calls

---

## Resources

### Key Documentation
- [Architecture Plan](../DEEPER_ANALYSIS_PLAN.md)
- [Data Sources](DATA_SOURCES.md)
- [Trigger Keywords](TRIGGER_KEYWORDS.md)
- [Summary](SUMMARY.md)

### External Resources
- [PRAW Documentation](https://praw.readthedocs.io/)
- [Algolia HN API](https://hn.algolia.com/api)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)

### Code Examples
- Existing Newsbot LLM usage: `scripts/utils/llm_assessment.py`
- Report generation: `scripts/reporters/markdown_reporter.py`
- GitHub API usage: `scripts/searchers/github_search.py`

---

## Getting Help

**During Implementation:**

1. Review relevant planning document
2. Check existing Newsbot code for patterns
3. Search documentation (Ctrl+F)
4. Open issue with `deeper-analysis` label

**Questions About Architecture:**
- Refer to main `DEEPER_ANALYSIS_PLAN.md`
- Review architecture diagrams

**Questions About Data Sources:**
- Check `DATA_SOURCES.md` for API examples
- Refer to official API documentation

---

## Success Metrics

### Phase Completion

Track completion of each phase:

```markdown
- [ ] Phase 1: Foundation (Weeks 1-2)
- [ ] Phase 2: Data Aggregation (Weeks 3-5)
- [ ] Phase 3: LLM Analysis (Weeks 6-8)
- [ ] Phase 4: Report Generation (Weeks 9-10)
- [ ] Phase 5: Integration (Weeks 11-12)
- [ ] Phase 6: Documentation (Weeks 13-14)
```

### Quality Gates

Before moving to next phase:

- ✅ All unit tests pass
- ✅ Integration tests pass
- ✅ Code review completed
- ✅ Documentation updated
- ✅ No known critical bugs

---

## Final Checklist

Before launch:

- [ ] All 6 phases completed
- [ ] Comprehensive testing done
- [ ] User documentation written
- [ ] Admin documentation written
- [ ] Example analyses created
- [ ] API credentials secured in GitHub Secrets
- [ ] Rate limiting tested
- [ ] Access control tested
- [ ] Performance acceptable (<15 min per analysis)
- [ ] Error handling robust
- [ ] Logging comprehensive

---

**Ready to Start?** → Begin with Phase 1: Foundation

**Questions?** → Open an issue with `deeper-analysis` label

**Good luck!** 🚀
