# LLM Prompts

This directory contains all LLM prompts used by Newsbot for article assessment and analysis. Prompts are stored in separate files following [GitHub Models best practices for prompt storage](https://docs.github.com/en/github-models/use-github-models/storing-prompts-in-github-repositories).

## Organization

Prompts are organized by function and role:

### Article Applicability Assessment
- **`assess_article_applicability.txt`** - Main user prompt for evaluating if an article is relevant to AI/automation in offensive security
- **`assess_article_applicability_system.txt`** - System role for applicability assessment

### Article Credibility Assessment
- **`assess_article_credibility.txt`** - Main user prompt for evaluating article credibility and quality
- **`assess_article_credibility_system.txt`** - System role for credibility assessment

### Title Filtering
- **`filter_titles_by_relevance.txt`** - Main user prompt for filtering article titles by relevance
- **`filter_titles_by_relevance_system.txt`** - System role for title filtering

### Batch Assessment
- **`assess_batch_internal.txt`** - Main user prompt for batch processing multiple articles
- **`assess_batch_internal_system.txt`** - System role for batch assessment

## Prompt Variables

Prompts use Python's `.format()` method for variable substitution. Available variables in each prompt:

### assess_article_applicability.txt
- `{keywords_str}` - Comma-separated list of keywords from config
- `{article_text}` - Formatted article content (title, description, optional content preview)

### assess_article_credibility.txt
- `{source_name}` - Name of the RSS feed or source
- `{domain_credibility}` - Pre-assessed domain credibility ('high', 'medium', 'low')
- `{url}` - Article URL
- `{article_text}` - Formatted article content (title, description, optional content preview)

### filter_titles_by_relevance.txt
- `{keywords_str}` - Comma-separated list of keywords from config
- `{title_list}` - Numbered list of article titles (e.g., "0: Title 1\n1: Title 2")

### assess_batch_internal.txt
- `{num_articles}` - Number of articles in the batch
- `{keywords_str}` - Comma-separated list of keywords from config
- `{combined_articles}` - Formatted batch of articles with metadata

## Usage

Prompts are automatically loaded by `scripts/utils/llm_assessment.py` using the `_load_prompt()` function. The function:

1. Looks for prompts in this directory
2. Caches loaded prompts for performance
3. Raises `FileNotFoundError` if a prompt file is missing

Example:
```python
from utils.llm_assessment import _load_prompt

# Load a prompt template
prompt_template = _load_prompt("assess_article_applicability")

# Format with variables
prompt = prompt_template.format(
    keywords_str="AI, automation, fuzzing",
    article_text="Title: Example\n\nDescription: Test"
)
```

## Modifying Prompts

When modifying prompts:

1. **Preserve variable placeholders** - Ensure all `{variable}` placeholders remain intact
2. **Test changes** - Run `pytest tests/test_utils_llm_assessment.py` to verify functionality
3. **Update this README** - Document any new variables or significant changes
4. **Clear cache** - Restart the application to reload modified prompts

## Best Practices

Following GitHub Models best practices:

- ✅ **Separate files** - Each prompt in its own file for clarity and version control
- ✅ **Descriptive names** - File names clearly indicate purpose
- ✅ **Version control** - Track prompt changes through git history
- ✅ **Documentation** - This README documents prompt structure and usage
- ✅ **No inline prompts** - All prompts extracted from source code

## References

- [GitHub Models: Storing Prompts in GitHub Repositories](https://docs.github.com/en/github-models/use-github-models/storing-prompts-in-github-repositories)
- Main implementation: `scripts/utils/llm_assessment.py`
- Tests: `tests/test_utils_llm_assessment.py`
