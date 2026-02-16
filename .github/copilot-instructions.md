# Newsbot - GitHub Copilot Instructions

## ⚡ CRITICAL: LLM Call Efficiency

**READ THIS FIRST:** Newsbot's most important performance requirement is **minimizing LLM API calls**.

### Golden Rules
1. ✅ **ALWAYS** check the `outputs/` directory before making LLM calls - it contains extensive previous analysis
2. ✅ **NEVER** re-analyze articles that exist in `results_*.json` or `rejected_*.json` files
3. ✅ **ALWAYS** ensure `skip_analyzed` feature is enabled and working
4. ✅ **ALWAYS** use batch processing (`batch_size`) when making LLM calls
5. ❌ **NEVER** disable or bypass the article caching system

### Why This Matters
- The `outputs/` directory contains hundreds/thousands of previously analyzed articles
- Each article has already been assessed by an LLM for applicability and credibility
- Re-analyzing these articles wastes API calls, costs money, and slows down the system
- The `skip_analyzed` feature automatically prevents this - keep it enabled

### Quick Reference
- **Outputs location:** `/outputs/` (results_*.json, rejected_*.json)
- **Config setting:** `"skip_analyzed": {"enabled": true}` (default, keep it this way)
- **Code module:** `scripts/utils/article_cache.py`
- **Key functions:** `load_analyzed_articles()`, `filter_analyzed_articles()`

---

## Project Overview

Newsbot is an automated news aggregator that uses LLMs and GitHub Actions to search for and aggregate the latest articles, announcements, repositories, and blog posts related to AI and automation in offensive security.

**Key Features:**
- GitHub repository search with topic filtering
- LLM-powered content search and summarization using GitHub Models (GPT-4o mini)
- Automated daily execution via GitHub Actions
- Local execution support with helper scripts
- Multiple output formats (Markdown reports and JSON data)
- Configurable search topics and parameters
- **Efficient LLM usage with article caching and deduplication**

**Target Audience:** Security researchers, red teams, and professionals interested in AI/automation in offensive security.

**Critical Performance Principle:** Minimize LLM API calls by leveraging the extensive data already available in the `outputs/` directory. Previous runs contain comprehensive article assessments (applicability and credibility scores) that should NEVER be re-analyzed.

## Tech Stack

- **Language:** Python 3.11+
- **Core Libraries:**
  - `requests` - HTTP requests
  - `beautifulsoup4` - HTML parsing
  - `openai` - GitHub Models API (OpenAI-compatible)
  - `python-dotenv` - Environment variable management
  - `PyGithub` - GitHub API interactions
- **CI/CD:** GitHub Actions
- **LLM Provider:** GitHub Models (GPT-4o mini via Azure AI)

## Coding Standards

### Python Style
- Follow **PEP 8** for all Python code
- Use **type hints** for function parameters and return values
- Add **docstrings** to all functions, classes, and modules using Google-style format
- Keep functions focused and modular (single responsibility principle)
- Use descriptive variable and function names

### Code Structure
- Organize code into classes and functions with clear responsibilities
- Use the `NewsBot` class pattern for main functionality
- Keep configuration in `config.json` (not hardcoded)
- Use environment variables for sensitive data (tokens, API keys)

### Example Code Pattern
```python
def search_repositories(self, topics: List[str], days_back: int = 7) -> List[Dict[str, Any]]:
    """Search GitHub repositories with specified topics.
    
    Args:
        topics: List of GitHub topics to search for
        days_back: Number of days to look back (default: 7)
        
    Returns:
        List of repository dictionaries with metadata
    """
    # Implementation here
```

## File Organization

```
Newsbot/
├── .github/
│   ├── workflows/
│   │   └── newsbot.yml          # GitHub Actions workflow
│   └── copilot-instructions.md  # This file
├── scripts/
│   └── newsbot.py               # Main Python script
├── outputs/                     # Generated reports (gitignored)
├── config.json                  # Configuration file
├── requirements.txt             # Python dependencies
├── run_local.sh                 # Local execution helper
└── README.md                    # Documentation
```

## Configuration and Environment

### Environment Variables
- `GITHUB_TOKEN` - Required for both GitHub API and GitHub Models LLM access
- Never commit tokens or API keys to the repository
- Use `.env` file for local development (keep in `.gitignore`)
- Use GitHub Secrets for GitHub Actions workflows

### Configuration File
- `config.json` contains all search parameters
- Must include: `search_topics`, `github_topics`, `days_back`, `max_results_per_topic`
- Keep configuration flexible and easily customizable

### Critical LLM Optimization Settings
- **`skip_analyzed.enabled`** (default: `true`) - **NEVER disable this**. Prevents re-analyzing articles already processed in previous runs
- **`llm_assessment.batch_size`** (default: `5`) - Process multiple articles in a single LLM call for efficiency
- **`llm_assessment.enabled`** - Can be disabled for testing or when working with pre-analyzed data

**When making code changes:**
1. **ALWAYS** check if data exists in `outputs/` directory before making LLM calls
2. **NEVER** re-analyze articles that are in `results_*.json` or `rejected_*.json` files
3. Verify `skip_analyzed` feature is working correctly
4. Look for opportunities to reduce redundant LLM calls in your changes

## Testing Guidelines

- Test all changes locally using `./run_local.sh` before committing
- Ensure no existing functionality is broken
- Verify outputs are generated correctly in `outputs/` directory
- Test both local execution and GitHub Actions workflow (when applicable)
- Check error handling for API failures and missing credentials

### LLM Call Optimization Testing
**Before any code changes affecting article processing:**
1. Check baseline LLM call count in logs from a test run
2. Verify `skip_analyzed` is preventing redundant LLM calls
3. After changes, compare LLM call counts to ensure no regression
4. **Critical:** If testing with existing data in `outputs/`, expect ZERO LLM calls for already-analyzed articles

## Security Best Practices

### Credentials and Secrets
- **NEVER** commit API keys, tokens, or credentials to the repository
- Use environment variables for all sensitive data
- Keep `.env` file in `.gitignore`
- Use GitHub Secrets for automated workflows
- Review code before running to understand data access

### API Usage
- Validate all API responses before processing
- Handle rate limiting gracefully
- Use HTTPS for all external API calls
- Implement proper error handling for failed requests

### Input Validation
- Validate configuration file structure before use
- Sanitize any user-provided search queries
- Check file paths before writing outputs

## GitHub Actions Workflow

- Runs daily at 9 AM UTC (configurable via cron schedule)
- Can be triggered manually via workflow_dispatch
- Runs on push to main branch (for testing)
- Requires `contents: write` and `models: read` permissions
- Outputs saved as artifacts with 30-day retention
- Results automatically committed back to repository

## Common Patterns

### Error Handling
```python
try:
    # API call or operation
    result = self.some_operation()
except OpenAIError as e:
    logging.error(f"LLM API error: {e}")
    # Handle gracefully
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    # Handle gracefully
```

### Logging
- Use Python's `logging` module
- Log important operations and errors
- Use appropriate log levels (INFO, WARNING, ERROR)

## LLM Usage Best Practices

**Core Principle:** Minimize LLM API calls to reduce costs and improve performance.

### Before Making Any LLM Call

1. **Check if data exists** - Search `outputs/` directory for previous analysis
2. **Verify skip_analyzed is enabled** - Confirm `config.json` has `"skip_analyzed": {"enabled": true}`
3. **Use batching** - Process multiple items in a single LLM call when possible
4. **Consider alternatives** - Can the task be done with regex, keyword matching, or other methods?

### The Article Caching System

**How it works:**
- `load_analyzed_articles()` scans all `results_*.json` and `rejected_*.json` files in `outputs/`
- Extracts article URLs to create a set of previously analyzed articles
- `filter_analyzed_articles()` removes these from new article lists before LLM assessment
- Articles are identified by their URL (unique identifier)

**When implementing new features:**
- If feature involves article analysis, integrate with the caching system
- Check if article URL exists in `analyzed_ids` before processing
- Pass `analyzed_ids` parameter through the call chain
- Log skipped articles for transparency

**Example pattern:**
```python
# Load analyzed articles
analyzed_ids = load_analyzed_articles(output_dir)

# Filter before expensive operations
new_articles, skipped = filter_analyzed_articles(articles, analyzed_ids)
logging.info(f"Skipped {skipped} previously analyzed articles")

# Only process new articles with LLM
if new_articles and llm_assessment_enabled:
    assessed = assess_articles_batch(client, new_articles, ...)
```

### LLM Call Count Monitoring

- The codebase tracks LLM calls via `get_llm_call_count()`
- Logs display "Total LLM calls" at the end of each search operation
- **When debugging or testing:** Check this count to verify caching is working
- **Expected behavior:** Re-running on same data should result in zero LLM calls

## Contributing

When contributing to Newsbot, follow these guidelines:

1. Fork the repository
2. Create a feature branch with descriptive name
3. Follow all coding standards and best practices
4. Test changes locally
5. Write clear commit messages
6. Submit pull request with detailed description

### Special Considerations for Contributions

**When modifying article processing or assessment logic:**
1. **Verify LLM efficiency** - Ensure changes don't increase redundant LLM calls
2. **Test with existing outputs** - Run with populated `outputs/` directory to verify caching works
3. **Document LLM call counts** - Include before/after LLM call counts in PR description
4. **Preserve skip_analyzed** - Never remove or bypass article caching functionality

**When adding new features:**
1. **Check outputs first** - Review existing JSON files to see if data is already available
2. **Integrate with caching** - New article-related features must respect `analyzed_ids`
3. **Batch when possible** - Group LLM operations to minimize API calls
4. **Add monitoring** - Log LLM call counts for new operations

## Output Format

- Generate both Markdown reports and JSON data
- Use timestamped filenames: `report_YYYYMMDD_HHMMSS.md`
- Structure reports with clear sections and categories
- Include metadata (stars, update dates) for repositories
- Format JSON for programmatic access and further processing

### Understanding the Outputs Directory Structure

The `outputs/` directory is a **critical resource** containing previous analysis results:

**Files Generated Per Run:**
- `results_YYYYMMDD_HHMMSS.json` - Articles that passed LLM assessment (applicable and credible)
  - Example: `results_20260215_174538.json`
- `rejected_YYYYMMDD_HHMMSS.json` - Articles filtered out by LLM assessment
  - Example: `rejected_20260215_174538.json`
- `report_YYYYMMDD_HHMMSS.md` - Human-readable report
  - Example: `report_20260215_174538.md`

**What's Stored in JSON Files:**
- Article URL (used as unique identifier)
- Title and description
- Source information
- LLM assessment scores (applicability, credibility) for RSS articles
- Assessment explanations and matched keywords
- Domain credibility information

**Key Principle:** Any article URL found in these files has already been analyzed by an LLM and should NEVER be re-analyzed. The `skip_analyzed` feature automatically loads these files and filters out known articles.

## Anti-Patterns to Avoid

- ❌ Hardcoding API keys or tokens in source code
- ❌ Ignoring error handling for API calls
- ❌ Writing code without type hints or docstrings
- ❌ Creating monolithic functions (keep them focused)
- ❌ Committing sensitive data or large binary files
- ❌ Modifying `.gitignore` to allow sensitive files
- ❌ **Making redundant LLM calls for already-analyzed articles**
- ❌ **Disabling or bypassing the `skip_analyzed` feature**
- ❌ **Not checking `outputs/` directory before implementing LLM-based features**
- ❌ **Re-implementing functionality that already exists in the caching system**

## References

- [Project README](../README.md) - Main documentation
- [Contributing Guide](../CONTRIBUTING.md) - Contribution guidelines
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/) - Python code style
- [GitHub Models Documentation](https://docs.github.com/en/github-models) - LLM API reference
