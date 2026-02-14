# Quick Start Guide

Get started with Newsbot in 5 minutes!

## Option 1: GitHub Actions (Recommended)

1. **Fork this repository** to your GitHub account

2. **Enable GitHub Actions**:
   - Go to the "Actions" tab in your repository
   - Click "I understand my workflows, go ahead and enable them"
   - Note: `GITHUB_TOKEN` is automatically provided by GitHub Actions for both repository searches and LLM access via GitHub Models

3. **Run manually** (optional):
   - Go to Actions → Newsbot workflow
   - Click "Run workflow"
   - Check the results in the "Artifacts" section

4. **Automated runs**:
   - The workflow runs automatically daily at 9 AM UTC
   - Customize the schedule in `.github/workflows/newsbot.yml`

## Option 2: Local Execution

1. **Clone the repository**:
   ```bash
   git clone https://github.com/llamalamall/Newsbot.git
   cd Newsbot
   ```

2. **Set up GitHub token**:
   ```bash
   cp .env.example .env
   # Edit .env and add your GitHub token
   nano .env
   ```

3. **Run Newsbot**:
   ```bash
   ./run_local.sh
   ```

4. **Check results**:
   ```bash
   ls outputs/
   cat outputs/report_*.md
   ```

## Next Steps

- Customize `config.json` to change search topics
- Review `outputs/example_report.md` to see what reports look like
- Run `python scripts/demo_features.py` to see enhanced features in action
- Run `python tests/test_newsbot.py` to verify functionality
- Read the full [README.md](README.md) for detailed documentation
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## What's New

**Enhanced Web Search Integration:**
- Live web searches for current news and articles
- Automatic source credibility assessment (high/medium/low)
- Article content extraction from credible sources
- LLM analysis enhanced with web search context
- Improved reports with source citations and credibility ratings
- Robust error handling for partial failures

## Troubleshooting

**No results found?**
- Ensure GITHUB_TOKEN is set
- Check the topics in `config.json`
- Increase `days_back` in config to search further back

**GitHub Actions not running?**
- Verify GitHub Actions is enabled in repository settings
- Review workflow logs in the Actions tab

**Permission errors?**
```bash
chmod +x run_local.sh
```

Need help? [Open an issue](https://github.com/llamalamall/Newsbot/issues)!
