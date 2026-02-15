# Newsbot - Offensive Security AI/Automation News Aggregator

An automated news aggregator that uses GitHub Actions to search for the latest articles, announcements, repositories, and blog posts related to AI and automation in offensive security.

## Overview

Newsbot automatically searches for and aggregates content related to:
- Offensive security with AI/automation
- AI-powered penetration testing
- Machine learning for red teams
- Automated reverse engineering
- AI-assisted malware analysis
- Automated binary analysis
- CVE reachability analysis
- Supply chain attack detection
- Security testing frameworks
- Automated exploit generation

## Features

- **GitHub Repository Search**: Finds recently updated repositories with relevant topics
- **RSS Feed Aggregation**: Monitors security blogs, research feeds, and official advisories
- **Smart Article Deduplication**: Automatically detects and skips articles that have already been analyzed in previous runs
  - URL-based identification ensures accurate duplicate detection
  - Configurable via `skip_analyzed.enabled` setting
  - Reduces redundant processing and LLM API calls
- **LLM-Powered Article Assessment**: Uses GitHub Models (GPT-4o mini) to evaluate article applicability and credibility
  - **Applicability Assessment**: Determines if articles are relevant to AI/automation in offensive security
  - **Credibility Evaluation**: Assesses content quality, identifies clickbait, and flags potential issues
  - **Keyword-Based Analysis**: Leverages configured search keywords for contextual evaluation
  - **Transparent Scoring**: Provides confidence scores and explanations for each assessment
- **Source Credibility Assessment**: Automatically vets RSS sources for reliability using domain-based analysis
- **Intelligent Filtering**: Prioritizes high-credibility sources and filters low-quality content
- **Automated Scheduling**: Runs daily via GitHub Actions
- **Local Execution**: Helper script for running locally
- **Multiple Output Formats**: Generates both Markdown reports and JSON data with source citations
- **Configurable Topics**: Easy to customize search topics and parameters
- **Robust Error Handling**: Gracefully handles search failures and unreachable sources

## Prerequisites

- **GitHub Token** (required for GitHub repository searches)

## Setup

### For GitHub Actions (Automated)

1. Fork or clone this repository
2. Enable GitHub Actions in your repository settings
   - Note: `GITHUB_TOKEN` is automatically provided by GitHub Actions

#### Workflow Triggers

The Newsbot workflow can be triggered in three ways:

**1. Automatic Daily Schedule**
- Runs automatically every day at 9 AM UTC
- Uses the `schedule` trigger with cron expression: `'0 9 * * *'`
- No manual intervention required
- Schedule can be customized by editing the cron expression in `.github/workflows/newsbot.yml`

**2. Manual Trigger (On-Demand)**
- Trigger the workflow manually whenever needed
- Steps to manually run:
  1. Navigate to the **Actions** tab in your GitHub repository
  2. Click on **"Newsbot - Security News Aggregator"** in the left sidebar
  3. Click the **"Run workflow"** button (top right)
  4. Select the branch (usually `main`)
  5. Click **"Run workflow"** to start execution
- Uses the `workflow_dispatch` trigger
- Useful for testing or getting immediate updates

**3. Automatic on Push**
- Runs automatically when code is pushed to the `main` branch
- Primarily for testing workflow changes
- Can be disabled by removing the `push` trigger from the workflow file

### For Local Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/llamalamall/Newsbot.git
   cd Newsbot
   ```

2. Create a `.env` file in the root directory:
   ```bash
   GITHUB_TOKEN=your_github_token_here
   ```

3. Run the helper script:
   ```bash
   ./run_local.sh
   ```

   Or manually:
   ```bash
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Set environment variable
   export GITHUB_TOKEN=your_token_here
   
   # Run newsbot
   python scripts/newsbot.py
   ```

## Configuration

Edit `config.json` to customize:

### Core Settings

- `search_keywords`: Keywords to filter results (used for RSS filtering)
- `github_topics`: GitHub topics to search
- `days_back`: How many days back to search (default: 7)
- `max_results_per_topic`: Maximum results per topic (default: 10)
- `github_enabled`: Enable/disable GitHub repository search (default: true)

### RSS Feed Configuration

- `rss_enabled`: Enable/disable RSS feed functionality (default: true)
- `rss_feeds`: Array of RSS feed configurations (see format below)
- `rss_settings`: RSS-specific settings
  - `max_age_days`: Maximum age of articles to include (default: 7)
  - `min_keyword_matches`: Minimum keyword matches for relevance (default: 1)
  - `cache_enabled`: Enable feed caching to reduce network calls (default: true)
  - `cache_ttl_hours`: Cache time-to-live in hours (default: 6)
  - `request_timeout`: Request timeout in seconds (default: 10)
  - `rate_limit_delay`: Delay between feed requests in seconds (default: 0.5)

### LLM Assessment Configuration

- `llm_assessment`: Settings for LLM-based article evaluation
  - `enabled`: Enable/disable LLM assessment (default: true)
  - `model`: LLM model to use (default: "gpt-4o-mini")
  - `applicability_threshold`: Minimum score to consider article applicable (default: 0.6)
  - `credibility_threshold`: Minimum score to consider article credible (default: 0.5)
  - `filter_inapplicable`: Remove articles deemed not applicable (default: true)
  - `filter_not_credible`: Remove articles deemed not credible (default: true)

**How LLM Assessment Works:**
1. **Applicability**: The LLM evaluates if an article is relevant to your configured `search_keywords` and topics related to AI/automation in offensive security
2. **Credibility**: The LLM assesses article quality by checking for clickbait titles, lack of sources, bias, and other credibility concerns
3. **Filtering**: Articles below the threshold scores are automatically filtered out (configurable)
4. **Transparency**: Each assessment includes a confidence score (0.0-1.0) and explanation in the output

### Article Deduplication Configuration

- `skip_analyzed`: Settings for automatic article deduplication
  - `enabled`: When `true`, automatically detects and skips articles already analyzed in previous runs (default: `true`)
  - Articles are identified by URL and compared against all `results_*.json` files in the output directory
  - Significantly reduces redundant processing and LLM API calls on subsequent runs
  - Logging clearly reports the number of articles skipped (e.g., "Skipped 5 already analyzed RSS articles")
  - Can be disabled by setting `enabled` to `false` to re-analyze all articles

**RSS Feed Format:**
```json
{
  "name": "Human-readable name",
  "url": "https://example.com/feed.xml",
  "priority": "high|medium|low",
  "category": "official|research|news|ai|tools|academic|etc."
}
```

**Default Feeds Include (20 total):**
- **Official**: CISA, US-CERT
- **Research**: Google Project Zero, Trail of Bits, Schneier on Security, Krebs on Security
- **AI/ML**: OpenAI Blog, Google AI Blog, Microsoft Security Blog
- **News**: The Hacker News, BleepingComputer, Dark Reading
- **Academic**: arXiv (Security, AI, ML categories)
- **Tools**: PortSwigger Research
- **Red Team**: Penetration Testing Lab, NetSPI
- **Malware**: Malwarebytes Labs

See `RSS_FEED_STRATEGY.md` for 37+ recommended feeds and complete implementation details.

### Example Configuration

```json
{
  "search_keywords": [
    "offensive security",
    "penetration testing",
    "AI automation"
  ],
  "github_topics": [
    "offensive-security",
    "penetration-testing"
  ],
  "days_back": 7,
  "max_results_per_topic": 10,
  "github_enabled": true,
  "rss_enabled": true,
  "rss_feeds": [
    {
      "name": "CISA Cybersecurity Advisories",
      "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml",
      "priority": "high",
      "category": "official"
    }
  ],
  "rss_settings": {
    "max_age_days": 7,
    "min_keyword_matches": 1,
    "cache_enabled": true
  },
  "llm_assessment": {
    "enabled": true,
    "model": "gpt-4o-mini",
    "applicability_threshold": 0.6,
    "credibility_threshold": 0.5,
    "filter_inapplicable": true,
    "filter_not_credible": true
  },
  "skip_analyzed": {
    "enabled": true
  }
}
```

## Source Credibility Assessment

Newsbot uses a two-tier approach to assess article quality and relevance:

### Domain-Based Credibility Assessment

Evaluates RSS feed sources based on their domain:

**High Credibility Sources:**
- Official security organizations (NIST, CISA, OWASP)
- Major tech companies (Google, Microsoft, AWS, GitHub)
- Respected security firms (Trail of Bits, Google Project Zero)
- Academic sources (arXiv, research publications)
- Well-known security blogs (Schneier, Krebs on Security)

**Medium Credibility Sources:**
- Established tech news sites (Ars Technica, TechCrunch)
- Developer platforms (Medium, Dev.to)
- Industry publications

**Low Credibility Sources:**
- Unrecognized domains
- Sites not on the credibility lists

### LLM-Based Content Assessment

Uses GitHub Models (GPT-4o mini) to evaluate individual articles:

**Applicability Assessment:**
- Analyzes article content against configured search keywords
- Determines relevance to AI/automation in offensive security
- Provides confidence score (0.0-1.0) and explanation
- Lists matched keywords/topics

**Credibility Evaluation:**
- Checks for clickbait or sensationalized titles
- Assesses content quality and depth
- Identifies missing citations or sources
- Flags potential bias or unverified claims
- Considers domain credibility rating
- Provides confidence score and detailed reasoning

Only articles meeting both domain and LLM credibility thresholds are included in reports.

## Output

Results are saved in the `outputs/` directory:

- `report_YYYYMMDD_HHMMSS.md`: Markdown report with categorized findings
- `results_YYYYMMDD_HHMMSS.json`: JSON data for programmatic access

Example report structure:
```markdown
# Offensive Security AI/Automation News

## Summary
Found X relevant items.

## GitHub Repositories (N)
### [owner/repo-name](url)
Description...
- Stars: 123
- Updated: 2024-01-15
- Topic: offensive-security

## RSS Feed Articles (N)
### Article Title
Description and summary...
**Link:** https://example.com/article
**Source:** Security Blog (research)
**Domain Credibility:** High
**LLM Applicability:** ✓ Relevant (score: 0.85)
*Matched topics: AI automation, penetration testing*
*Article discusses AI-powered security testing tools with practical applications*
**LLM Credibility:** ✓ Credible (score: 0.90)
*Well-researched article with citations and technical details*
**Published:** 2024-01-15
```

Reports now include:
- **LLM assessment results** with applicability and credibility scores
- **Transparent explanations** for why articles were included or filtered
- **Matched keywords** showing relevance to configured topics
- **Credibility flags** identifying any concerns (clickbait, bias, etc.)
- Source credibility ratings for RSS feed content
- Direct citations to original articles
- Publication dates when available
- Clear categorization of results by source type (GitHub, RSS)

## Workflow

1. **GitHub Search**: Searches for repositories with relevant topics updated in the last N days
2. **RSS Feed Aggregation**: Fetches and filters articles from configured RSS feeds
3. **Article Deduplication**: Compares incoming articles with previously analyzed ones and skips duplicates to save processing time and API calls
4. **Keyword Filtering**: Initial filtering by configured search keywords
5. **Domain Credibility Assessment**: Evaluates RSS sources based on domain (high/medium/low)
6. **LLM Assessment** (if enabled):
   - **Applicability**: Analyzes article relevance to AI/automation in offensive security
   - **Credibility**: Evaluates content quality and trustworthiness
7. **Intelligent Filtering**: Filters articles by LLM scores and thresholds
8. **Aggregation**: Combines results from GitHub and RSS feeds with assessment data
9. **Report Generation**: Creates formatted Markdown and JSON outputs with detailed assessments
10. **Artifact Storage**: Uploads results as GitHub Actions artifacts (when running in Actions)
11. **Git Commit**: Commits results to the repository (optional, in GitHub Actions)

## Project Structure

```
Newsbot/
├── .github/
│   └── workflows/
│       └── newsbot.yml          # GitHub Actions workflow
├── scripts/
│   ├── newsbot.py               # Main Python script
│   └── searchers/               # Search provider modules
├── tests/                       # Test suite
│   ├── test_newsbot.py          # Newsbot functionality tests
│   ├── test_rss_manager.py      # RSS manager tests
│   ├── test_integration.py      # Integration tests
│   └── test_rss_integration.py  # RSS integration tests
├── outputs/                     # Generated reports (gitignored)
├── config.json                  # Configuration file
├── requirements.txt             # Python dependencies
├── run_local.sh                 # Local execution helper
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

### Module Descriptions

- **newsbot.py**: Main application that orchestrates GitHub searches and RSS feed aggregation
- **searchers/**: Search providers for GitHub and RSS feeds
- **tests/**: Comprehensive test suite for all components including credibility assessment, RSS integration, and integration tests.

## Security and Privacy Considerations

### API Keys and Credentials
- Never commit API keys to the repository
- Use GitHub Secrets for sensitive credentials (GITHUB_TOKEN is automatically provided in Actions)
- Keep the `.env` file in `.gitignore`
- Review the code before running to understand what it does

### Rate Limiting
- Be mindful of API rate limits when using search APIs
- GitHub Actions runs are limited to prevent excessive usage
- Local execution should be throttled when performing many searches
- Consider implementing delays between requests if needed

### Data Privacy
- No personal data is collected or stored
- All search queries are related to public security research topics
- Results are limited to publicly available information
- Compliance with applicable data protection regulations is maintained

## Troubleshooting

### No results found
- Check that GITHUB_TOKEN is correctly set
- Verify the topics in `config.json` are specific enough
- Increase `days_back` to search a longer time period

### GitHub Actions not running
- Ensure GitHub Actions is enabled in repository settings
- Review workflow logs in the Actions tab

### Local execution fails
- Ensure Python 3.8+ is installed
- Check that all dependencies are installed
- Verify GITHUB_TOKEN environment variable is set correctly

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is for educational and research purposes. Always ensure you have permission to access and analyze any systems or data. The authors are not responsible for any misuse of this tool.
