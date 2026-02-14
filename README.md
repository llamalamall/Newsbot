# Newsbot - Offensive Security AI/Automation News Aggregator

An automated news aggregator that uses LLMs and GitHub Actions to search for the latest articles, announcements, repositories, and blog posts related to AI and automation in offensive security.

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
- **Live Web Search Integration**: Performs real-time web searches for current news and articles
- **Source Credibility Assessment**: Automatically vets news sources for reliability
- **Article Content Extraction**: Pulls full text and key excerpts from linked articles
- **LLM-Powered Analysis**: Uses GitHub Models (GPT-4o) with web search context for enhanced summarization
- **Intelligent Filtering**: Prioritizes high-credibility sources and filters low-quality content
- **Automated Scheduling**: Runs daily via GitHub Actions
- **Local Execution**: Helper script for running locally
- **Multiple Output Formats**: Generates both Markdown reports and JSON data with source citations
- **Configurable Topics**: Easy to customize search topics and parameters
- **Robust Error Handling**: Gracefully handles search failures and unreachable sources

## Prerequisites

- **GitHub Token** (required for both repository searches and LLM access via GitHub Models)

## Setup

### For GitHub Actions (Automated)

1. Fork or clone this repository
2. Enable GitHub Actions in your repository settings
   - Note: `GITHUB_TOKEN` is automatically provided by GitHub Actions
3. The workflow will run:
   - Daily at 9 AM UTC (configurable in `.github/workflows/newsbot.yml`)
   - On manual trigger via the Actions tab
   - On push to main branch (for testing)

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

- `search_topics`: Topics to search for using LLM
- `search_keywords`: Keywords to filter results
- `github_topics`: GitHub topics to search
- `days_back`: How many days back to search (default: 7)
- `max_results_per_topic`: Maximum results per topic (default: 10)
- `web_search_enabled`: Enable/disable web search functionality (default: true)
- `web_search_max_results`: Maximum results per web search (default: 10)
- `web_search_timeout`: Request timeout in seconds (default: 10)
- `web_search_rate_limit`: Delay between requests in seconds (default: 1.0)

Example:
```json
{
  "search_topics": [
    "AI offensive security automation",
    "LLM penetration testing"
  ],
  "github_topics": [
    "offensive-security",
    "penetration-testing"
  ],
  "days_back": 7,
  "max_results_per_topic": 10,
  "web_search_enabled": true,
  "web_search_max_results": 10,
  "web_search_timeout": 10,
  "web_search_rate_limit": 1.0
}
```

### Web Search Configuration

The web search functionality uses DuckDuckGo's HTML interface, which doesn't require API keys:

- **web_search_enabled**: Toggle to enable or disable web search entirely. Set to `false` to use only GitHub repository search and LLM analysis.
- **web_search_max_results**: Controls how many search results to retrieve per query. Higher values may take longer.
- **web_search_timeout**: Maximum time to wait for search requests. Increase if experiencing timeouts.
- **web_search_rate_limit**: Delay between search requests to avoid overwhelming the service. Minimum recommended: 1.0 second.

## Source Credibility Assessment

Newsbot automatically assesses the credibility of news sources to ensure high-quality results:

### High Credibility Sources
- Official security organizations (NIST, CISA, OWASP)
- Major tech companies (Google, Microsoft, AWS, GitHub)
- Respected security firms (Trail of Bits, Google Project Zero)
- Academic sources (arXiv, research publications)
- Well-known security blogs (Schneier, Krebs on Security)

### Medium Credibility Sources
- Established tech news sites (Ars Technica, TechCrunch)
- Developer platforms (Medium, Dev.to)
- Industry publications

### Low Credibility Sources
- Unrecognized domains
- Sites not on the credibility lists

Only high and medium credibility sources are included in the final reports. Low-credibility sources are filtered out to maintain quality.

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

## Web Search Results (N)
*Results from live web searches with credibility assessment*

### Article Title
Description and summary...
**Source:** [https://example.com/article](https://example.com/article)
**Credibility:** High
**Key Points:**
- Point 1
- Point 2
*Published: 2024-01-15*
*Search topic: AI offensive security*

## Articles, Blog Posts & Announcements (N)
### Article Title
Description and key points...
**Link:** https://example.com
**Source Credibility:** Medium
```

Reports now include:
- Source credibility ratings for all web-sourced content
- Direct citations to original articles
- Publication dates when available
- Clear categorization of results by source type
- Filtering of low-credibility sources

## Workflow

1. **GitHub Search**: Searches for repositories with relevant topics updated in the last N days
2. **Live Web Search**: Performs real-time web searches for current news articles and blog posts
3. **Source Credibility Vetting**: Assesses the credibility of discovered sources (high/medium/low)
4. **Content Extraction**: Attempts to extract full article text from high-credibility sources
5. **LLM Analysis**: Uses GitHub Models (GPT-4o) with web search context to analyze and summarize news
6. **Intelligent Filtering**: Filters out low-credibility sources and promotional content
7. **Aggregation**: Combines results from all sources with credibility ratings
8. **Report Generation**: Creates formatted Markdown and JSON outputs with source citations
9. **Artifact Storage**: Uploads results as GitHub Actions artifacts (when running in Actions)
10. **Git Commit**: Commits results to the repository (optional, in GitHub Actions)

## Project Structure

```
Newsbot/
├── .github/
│   └── workflows/
│       └── newsbot.yml          # GitHub Actions workflow
├── scripts/
│   ├── newsbot.py               # Main Python script
│   ├── web_search_helper.py     # Web search helper module
│   ├── web_search_runner.py     # External web search runner
│   └── test_newsbot.py          # Test suite
├── outputs/                     # Generated reports (gitignored)
├── config.json                  # Configuration file
├── requirements.txt             # Python dependencies
├── run_local.sh                 # Local execution helper
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

### Module Descriptions

- **newsbot.py**: Main application that orchestrates GitHub searches, web searches, and LLM analysis
- **web_search_helper.py**: Helper module that performs web searches using DuckDuckGo's HTML interface. Includes rate limiting, error handling, and result parsing.
- **web_search_runner.py**: Standalone runner that can be called as a subprocess for web searches. Outputs results in JSON format.
- **test_newsbot.py**: Comprehensive test suite for all components including web search functionality, credibility assessment, and integration tests.

## Security and Privacy Considerations

### API Keys and Credentials
- Never commit API keys to the repository
- Use GitHub Secrets for sensitive credentials (GITHUB_TOKEN is automatically provided in Actions)
- Keep the `.env` file in `.gitignore`
- Review the code before running to understand what it does

### Web Scraping and Content Extraction
- Newsbot respects robots.txt and website terms of service
- Content extraction is limited and used only for summarization purposes
- User-Agent headers identify the bot and provide contact information
- Requests include appropriate timeouts to avoid overloading servers
- Failed requests are handled gracefully without retry storms

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

## Future Development

### RSS Feed Migration Strategy

We are planning to migrate from web search to curated RSS feeds for more reliable and targeted content discovery. This will provide:
- More stable content sources (no scraping fragility)
- Better quality control (curated sources only)
- Improved coverage of offensive security + AI topics
- No rate limiting or API costs

**See the full strategy**: [RSS_FEED_STRATEGY.md](RSS_FEED_STRATEGY.md)

Key highlights:
- 37+ curated RSS feeds from trusted security sources
- Phased migration plan with dual-mode operation
- Comprehensive implementation guide
- Feed categories: Official advisories, research, tools, AI security, academic

**Track progress**: See [issue template](.github/ISSUE_TEMPLATE/rss-feed-migration.md) for implementation roadmap

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Contributing Feed Suggestions
We're building a curated list of RSS feeds for offensive security and AI/automation. If you know of high-quality sources, please:
- Open an issue using the RSS Feed Migration template
- Suggest feeds with their URL and description
- Help us improve content quality and coverage

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is for educational and research purposes. Always ensure you have permission to access and analyze any systems or data. The authors are not responsible for any misuse of this tool.
