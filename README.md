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
- **LLM-Powered Search**: Uses GPT-4 to search and summarize the latest news and articles
- **Automated Scheduling**: Runs daily via GitHub Actions
- **Local Execution**: Helper script for running locally
- **Multiple Output Formats**: Generates both Markdown reports and JSON data
- **Configurable Topics**: Easy to customize search topics and parameters

## Prerequisites

At least one of the following API keys:
- **OpenAI API Key** (for LLM-powered searches)
- **GitHub Token** (for repository searches)

## Setup

### For GitHub Actions (Automated)

1. Fork or clone this repository
2. Add secrets to your GitHub repository:
   - `OPENAI_API_KEY`: Your OpenAI API key (optional but recommended)
   - Note: `GITHUB_TOKEN` is automatically provided by GitHub Actions
3. Enable GitHub Actions in your repository settings
4. The workflow will run:
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
   OPENAI_API_KEY=your_openai_api_key_here
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
   
   # Set environment variables
   export OPENAI_API_KEY=your_key_here
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
  "max_results_per_topic": 10
}
```

## Output

Results are saved in the `outputs/` directory:

- `report_YYYYMMDD_HHMMSS.md`: Markdown report with categorized findings
- `results_YYYYMMDD_HHMMSS.json`: JSON data for programmatic access

Example report structure:
```markdown
# Offensive Security AI/Automation News

## Summary
Found X relevant items.

## GitHub Repositories
### [owner/repo-name](url)
Description...
- Stars: 123
- Updated: 2024-01-15

## Articles, Blog Posts & Announcements
### Article Title
Description and key points...
```

## Workflow

1. **GitHub Search**: Searches for repositories with relevant topics updated in the last N days
2. **LLM Analysis**: Uses GPT-4 to search and summarize news for each configured topic
3. **Aggregation**: Combines results from all sources
4. **Report Generation**: Creates formatted Markdown and JSON outputs
5. **Artifact Storage**: Uploads results as GitHub Actions artifacts (when running in Actions)
6. **Git Commit**: Commits results to the repository (optional, in GitHub Actions)

## Project Structure

```
Newsbot/
├── .github/
│   └── workflows/
│       └── newsbot.yml          # GitHub Actions workflow
├── scripts/
│   └── newsbot.py               # Main Python script
├── outputs/                     # Generated reports (gitignored)
├── config.json                  # Configuration file
├── requirements.txt             # Python dependencies
├── run_local.sh                 # Local execution helper
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Security Considerations

- Never commit API keys to the repository
- Use GitHub Secrets for sensitive credentials
- Keep the `.env` file in `.gitignore`
- Review the code before running to understand what it does

## Troubleshooting

### No results found
- Check that your API keys are correctly set
- Verify the topics in `config.json` are specific enough
- Increase `days_back` to search a longer time period

### GitHub Actions not running
- Ensure GitHub Actions is enabled in repository settings
- Check that secrets are properly configured
- Review workflow logs in the Actions tab

### Local execution fails
- Ensure Python 3.8+ is installed
- Check that all dependencies are installed
- Verify environment variables are set correctly

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
