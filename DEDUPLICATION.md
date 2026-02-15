# Article Deduplication

## Overview

The Newsbot RSS Feed Manager now includes persistent article deduplication to prevent reporting the same articles across multiple runs.

## How It Works

### 1. Seen Articles Tracking

When the RSS Feed Manager fetches articles from feeds:
- Each article URL is checked against a cache of previously seen articles
- New articles are processed normally
- Previously seen articles are automatically skipped
- All processed article URLs are marked as "seen" and saved to disk

### 2. Persistent Storage

The deduplication cache is stored in:
```
cache/seen_articles.json
```

This file persists across runs and contains:
- Article URLs that have been previously reported
- Timestamp of when each article was first seen
- Automatic cleanup of old entries (>30 days or 7x cache TTL, whichever is larger)

### 3. Cache Structure

The cache file stores entries in JSON format:
```json
[
  {
    "url": "https://example.com/article1",
    "seen_at": "2026-02-15T12:00:00"
  },
  {
    "url": "https://example.com/article2", 
    "seen_at": "2026-02-14T10:30:00"
  }
]
```

## Configuration

### Enable/Disable Caching

In `config.json`, set the RSS settings:

```json
{
  "rss_settings": {
    "cache_enabled": true,
    "cache_ttl_hours": 6
  }
}
```

### Cache Directory

By default, the cache is stored in the `cache/` directory. This can be customized when creating the RSSFeedManager:

```python
manager = RSSFeedManager(
    cache_enabled=True,
    cache_dir="custom/cache/path"
)
```

## Cache Management

### Automatic Cleanup

The cache automatically:
- Filters out articles older than 30 days (or 7x cache TTL, whichever is larger)
- Removes expired entries when loading the cache
- Prevents unbounded cache growth

### Manual Cache Clearing

To clear the cache programmatically:

```python
# Clear in-memory cache only
manager.clear_cache()

# Clear both in-memory and persistent cache
manager.clear_cache(clear_seen_articles=True)
```

To manually delete the cache file:
```bash
rm cache/seen_articles.json
```

## Benefits

1. **No Duplicate Reports**: Articles are only reported once
2. **Persistent Across Runs**: Cache survives application restarts
3. **Automatic Cleanup**: Old entries expire automatically
4. **Efficient**: Fast URL lookup using in-memory set
5. **Configurable**: Can be disabled if deduplication is not needed

## Example Workflow

### Run 1: Initial Fetch
```
Fetching articles...
Found 5 new articles
- Article A [NEW] ✓ Reported
- Article B [NEW] ✓ Reported  
- Article C [NEW] ✓ Reported
- Article D [NEW] ✓ Reported
- Article E [NEW] ✓ Reported

Saved 5 articles to cache
```

### Run 2: Same Articles + New One
```
Loaded 5 previously seen articles
Fetching articles...
- Article A [SEEN] ✗ Skipped
- Article B [SEEN] ✗ Skipped
- Article C [SEEN] ✗ Skipped
- Article D [SEEN] ✗ Skipped
- Article E [SEEN] ✗ Skipped
- Article F [NEW] ✓ Reported

Saved 6 articles to cache
```

### Run 3: Mix of Old and New
```
Loaded 6 previously seen articles
Fetching articles...
- Article C [SEEN] ✗ Skipped
- Article F [SEEN] ✗ Skipped
- Article G [NEW] ✓ Reported
- Article H [NEW] ✓ Reported

Saved 8 articles to cache
```

## Technical Details

### Implementation

The deduplication is implemented in `scripts/rss_feed_manager.py`:

- `_load_seen_articles()`: Loads cache on initialization
- `_save_seen_articles()`: Persists cache to disk
- `_is_article_seen(url)`: Checks if URL was previously seen
- `_mark_article_as_seen(url)`: Marks URL as seen

### Integration

The deduplication happens automatically in `fetch_feed()`:
1. Articles are fetched from RSS feeds
2. Each article URL is checked against the seen cache
3. Seen articles are skipped with a debug log message
4. New articles are processed and marked as seen
5. Cache is saved after all feeds are fetched

### Testing

Comprehensive tests are available in `tests/test_deduplication.py`:
- Persistence across manager instances
- Cache file creation and loading
- Filtering of old entries
- Dynamic cutoff calculation
- Cache disabled behavior

Run tests with:
```bash
pytest tests/test_deduplication.py -v
```

## Troubleshooting

### Articles Still Appearing as Duplicates

1. Check if cache is enabled in configuration
2. Verify `cache/` directory has write permissions
3. Check logs for cache loading/saving messages
4. Ensure article URLs are consistent (same URL format)

### Cache File Not Created

1. Verify `cache_enabled=True` in settings
2. Check directory permissions for `cache/` folder
3. Look for error messages in logs

### Want to Reset Cache

Simply delete the cache file:
```bash
rm cache/seen_articles.json
```

Or programmatically:
```python
manager.clear_cache(clear_seen_articles=True)
```

## Related Files

- `scripts/rss_feed_manager.py` - Main implementation
- `tests/test_deduplication.py` - Test suite
- `.gitignore` - Excludes `cache/` directory from git
- `config.json` - Configuration settings
