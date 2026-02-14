# Newsbot Test Suite

This directory contains comprehensive unit and integration tests for the Newsbot project using pytest.

## Test Organization

### Unit Tests (pytest-based)

**test_newsbot_unit.py** - Comprehensive unit tests for the main NewsBot class
- NewsBot initialization (with/without tokens, with RSS enabled)
- Configuration loading and validation
- Credibility assessment wrapper methods
- Article extraction wrapper methods
- Web search functionality
- News aggregation from multiple sources
- Error handling and edge cases
- Main function entry point

**test_utils_credibility.py** - Tests for source credibility assessment
- High, medium, and low credibility source detection
- URL parsing and domain extraction
- Edge cases (empty URLs, invalid URLs, Unicode)
- Case-insensitive and subdomain matching

**test_utils_content_extractor.py** - Tests for article content extraction
- HTML parsing with BeautifulSoup
- Content extraction from various HTML structures
- Script and style tag removal
- Length limiting and whitespace cleanup
- Error handling for network issues
- User-Agent and timeout configuration

**test_searchers_github.py** - Tests for GitHub repository search
- Authentication and token handling
- Topic-based repository search
- AI/automation keyword filtering
- Date filtering and sorting
- Max results limiting
- Error handling for API issues

### Integration Tests (legacy format)

**test_integration.py** - Integration test for RSS feed functionality
**test_newsbot.py** - Legacy integration tests for various features
**test_rss_integration.py** - RSS feed configuration validation
**test_rss_manager.py** - RSS Feed Manager functionality

## Running Tests

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test File
```bash
pytest tests/test_newsbot_unit.py
```

### Run with Verbose Output
```bash
pytest tests/ -v
```

### Run Specific Test Class or Function
```bash
pytest tests/test_newsbot_unit.py::TestNewsBotInitialization
pytest tests/test_newsbot_unit.py::TestNewsBotInitialization::test_init_with_default_config
```

### Run Tests with Coverage (if pytest-cov installed)
```bash
pytest tests/ --cov=scripts --cov-report=html
```

## Test Markers

Tests are marked with the following categories (defined in `pytest.ini`):

- `unit` - Unit tests (isolated, no external dependencies)
- `integration` - Integration tests (may require external resources)
- `requires_token` - Tests requiring GITHUB_TOKEN
- `network` - Tests requiring network access

## Test Structure

All unit tests follow these principles:

1. **Isolation**: Tests use mocks and patches to avoid external dependencies
2. **Clarity**: Test names clearly describe what is being tested
3. **Coverage**: Tests cover success cases, error cases, and edge cases
4. **Organization**: Tests are organized into classes by functionality
5. **Assertions**: Clear, specific assertions with meaningful error messages

## Test Coverage

Current test coverage includes:

- ✅ NewsBot class initialization and configuration
- ✅ All wrapper methods (credibility, extraction, search)
- ✅ News aggregation from GitHub, RSS, and web sources
- ✅ Source credibility assessment utility
- ✅ Article content extraction utility
- ✅ GitHub repository search functionality
- ✅ Error handling and edge cases

## Dependencies

Test dependencies are listed in `requirements.txt`:

- `pytest>=7.4.0` - Testing framework
- `pytest-mock>=3.11.1` - Mocking support for pytest

Install with:
```bash
pip install -r requirements.txt
```

## Contributing

When adding new features or fixing bugs:

1. Write tests first (TDD approach recommended)
2. Ensure all tests pass before committing
3. Aim for high test coverage (>80%)
4. Use mocks to isolate unit tests
5. Add integration tests for complex workflows
6. Document any special test setup requirements

## CI/CD Integration

Tests are automatically run in GitHub Actions on:
- Push to main branch
- Pull request creation
- Pull request updates

See `.github/workflows/` for CI configuration.
