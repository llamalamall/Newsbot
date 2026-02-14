# Newsbot - GitHub Copilot Instructions

## Project Overview

Newsbot is an automated news aggregator that uses LLMs and GitHub Actions to search for and aggregate the latest articles, announcements, repositories, and blog posts related to AI and automation in offensive security.

**Key Features:**
- GitHub repository search with topic filtering
- LLM-powered content search and summarization using GitHub Models (GPT-4o)
- Automated daily execution via GitHub Actions
- Local execution support with helper scripts
- Multiple output formats (Markdown reports and JSON data)
- Configurable search topics and parameters

**Target Audience:** Security researchers, red teams, and professionals interested in AI/automation in offensive security.

## Tech Stack

- **Language:** Python 3.11+
- **Core Libraries:**
  - `requests` - HTTP requests
  - `beautifulsoup4` - HTML parsing
  - `openai` - GitHub Models API (OpenAI-compatible)
  - `python-dotenv` - Environment variable management
  - `PyGithub` - GitHub API interactions
- **CI/CD:** GitHub Actions
- **LLM Provider:** GitHub Models (GPT-4o via Azure AI)

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

## Testing Guidelines

- Test all changes locally using `./run_local.sh` before committing
- Ensure no existing functionality is broken
- Verify outputs are generated correctly in `outputs/` directory
- Test both local execution and GitHub Actions workflow (when applicable)
- Check error handling for API failures and missing credentials

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

## Contributing

1. Fork the repository
2. Create a feature branch with descriptive name
3. Follow all coding standards and best practices
4. Test changes locally
5. Write clear commit messages
6. Submit pull request with detailed description

## Output Format

- Generate both Markdown reports and JSON data
- Use timestamped filenames: `report_YYYYMMDD_HHMMSS.md`
- Structure reports with clear sections and categories
- Include metadata (stars, update dates) for repositories
- Format JSON for programmatic access and further processing

## Anti-Patterns to Avoid

- ❌ Hardcoding API keys or tokens in source code
- ❌ Ignoring error handling for API calls
- ❌ Writing code without type hints or docstrings
- ❌ Creating monolithic functions (keep them focused)
- ❌ Committing sensitive data or large binary files
- ❌ Modifying `.gitignore` to allow sensitive files

## References

- [Project README](../README.md) - Main documentation
- [Contributing Guide](../CONTRIBUTING.md) - Contribution guidelines
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/) - Python code style
- [GitHub Models Documentation](https://docs.github.com/en/github-models) - LLM API reference
