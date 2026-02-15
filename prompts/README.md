# LLM Prompts

This directory contains all LLM prompts used by Newsbot for article assessment and analysis. Prompts are stored in separate YAML files managed by [prompt-engine-py](https://github.com/microsoft/prompt-engine-py), following [GitHub Models best practices for prompt storage](https://docs.github.com/en/github-models/use-github-models/storing-prompts-in-github-repositories).

## Organization

Prompts are organized by function and role using YAML format:

### Article Applicability Assessment
- **`assess_article_applicability.yaml`** - Main user prompt for evaluating if an article is relevant to AI/automation in offensive security
- **`assess_article_applicability_system.yaml`** - System role for applicability assessment

### Article Credibility Assessment
- **`assess_article_credibility.yaml`** - Main user prompt for evaluating article credibility and quality
- **`assess_article_credibility_system.yaml`** - System role for credibility assessment

### Title Filtering
- **`filter_titles_by_relevance.yaml`** - Main user prompt for filtering article titles by relevance
- **`filter_titles_by_relevance_system.yaml`** - System role for title filtering

### Batch Assessment
- **`assess_batch_internal.yaml`** - Main user prompt for batch processing multiple articles
- **`assess_batch_internal_system.yaml`** - System role for batch assessment

## Prompt Format

Prompts use the YAML format required by `prompt-engine-py`:

```yaml
type: prompt-engine
description: |
  Your prompt text here with {variable_placeholders}
  
  Multiple lines supported
examples: []
dialog: []
flow-reset-text: ""
config:
  model-config:
    max-tokens: 2048
  description-prefix: ""
  description-postfix: ""
  newline-operator: "\n"
  input-prefix: ""
  input-postfix: ""
  output-prefix: ""
  output-postfix: ""
```

## Prompt Variables

Prompts use Python's `.format()` method for variable substitution. Available variables in each prompt:

### assess_article_applicability.yaml
- `{keywords_str}` - Comma-separated list of keywords from config
- `{article_text}` - Formatted article content (title, description, optional content preview)

### assess_article_credibility.yaml
- `{source_name}` - Name of the RSS feed or source
- `{domain_credibility}` - Pre-assessed domain credibility ('high', 'medium', 'low')
- `{url}` - Article URL
- `{article_text}` - Formatted article content (title, description, optional content preview)

### filter_titles_by_relevance.yaml
- `{keywords_str}` - Comma-separated list of keywords from config
- `{title_list}` - Numbered list of article titles (e.g., "0: Title 1\n1: Title 2")

### assess_batch_internal.yaml
- `{num_articles}` - Number of articles in the batch
- `{keywords_str}` - Comma-separated list of keywords from config
- `{combined_articles}` - Formatted batch of articles with metadata

## Usage

Prompts are automatically loaded by `scripts/utils/llm_assessment.py` using the `_load_prompt()` function powered by `prompt-engine-py`. The function:

1. Looks for YAML prompt files in this directory
2. Uses `PromptEngine` from `prompt-engine-py` to load and parse prompts
3. Caches loaded prompt engines for performance
4. Raises `FileNotFoundError` if a prompt file is missing

Example:
```python
from utils.llm_assessment import _load_prompt

# Load a prompt template (returns the description field from YAML)
prompt_template = _load_prompt("assess_article_applicability")

# Format with variables
prompt = prompt_template.format(
    keywords_str="AI, automation, fuzzing",
    article_text="Title: Example\n\nDescription: Test"
)
```

## Modifying Prompts

When modifying prompts:

1. **Edit YAML files** - Prompts are now in YAML format managed by `prompt-engine-py`
2. **Preserve variable placeholders** - Ensure all `{variable}` placeholders remain intact in the `description` field
3. **Maintain YAML structure** - Keep the required fields: `type`, `description`, `examples`, `dialog`, `flow-reset-text`, `config`
4. **Test changes** - Run `pytest tests/test_utils_llm_assessment.py` to verify functionality
5. **Update this README** - Document any new variables or significant changes
6. **Clear cache** - Restart the application to reload modified prompts

## Best Practices

Following GitHub Models best practices and using `prompt-engine-py`:

- ✅ **Separate files** - Each prompt in its own YAML file for clarity and version control
- ✅ **Descriptive names** - File names clearly indicate purpose
- ✅ **Structured format** - YAML format enables advanced features like examples and dialog management
- ✅ **Version control** - Track prompt changes through git history
- ✅ **Documentation** - This README documents prompt structure and usage
- ✅ **No inline prompts** - All prompts extracted from source code
- ✅ **Industry standard** - Uses Microsoft's `prompt-engine-py` for prompt management

## References

- [prompt-engine-py on GitHub](https://github.com/microsoft/prompt-engine-py)
- [GitHub Models: Storing Prompts in GitHub Repositories](https://docs.github.com/en/github-models/use-github-models/storing-prompts-in-github-repositories)
- Main implementation: `scripts/utils/llm_assessment.py`
- Tests: `tests/test_utils_llm_assessment.py`
