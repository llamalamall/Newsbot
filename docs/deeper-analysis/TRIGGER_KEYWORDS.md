# Trigger Keywords and Usage Guide

This document specifies the keywords and syntax for triggering deeper article analysis via GitHub Actions.

## Supported Trigger Keywords

### Primary Keyword

**`analyze-deep:`**

The primary and recommended trigger keyword. Clear, explicit, and easy to remember.

**Syntax:**
```
analyze-deep: <target>
```

**Examples:**
```
analyze-deep: https://blog.example.com/article
analyze-deep: article_20260215_200451_013
analyze-deep: https://github.com/org/repo
```

---

### Alternative Keywords

For flexibility and natural language, these alternatives are also supported:

#### `deep-analysis:`

**Syntax:**
```
deep-analysis: <target>
```

**Example:**
```
deep-analysis: https://example.com/security-tool-review
```

#### `investigate:`

**Syntax:**
```
investigate: <target>
```

**Example:**
```
investigate: article_20260216_020926_008
```

#### `/analyze-deep`

Slash command style (GitHub-native feel)

**Syntax:**
```
/analyze-deep <target>
```

**Example:**
```
/analyze-deep https://github.com/vendor/tool
```

---

## Target Specification

### Supported Target Types

#### 1. Full Article URL

Direct link to the article, blog post, or web page to analyze.

**Format:**
```
analyze-deep: https://www.example.com/path/to/article
```

**Valid URLs:**
- Blog posts: `https://blog.company.com/post-title`
- News articles: `https://news.site.com/article`
- Security advisories: `https://vendor.com/security-advisory`
- Any publicly accessible web page

**Requirements:**
- Must be publicly accessible (no authentication required)
- Must return HTTP 200 status
- Content must be parseable (not binary files)

---

#### 2. Article ID from Newsbot Report

Reference to an article in recent Newsbot reports using its unique identifier.

**Format:**
```
analyze-deep: article_YYYYMMDD_HHMMSS_XXX
```

**Example:**
```
analyze-deep: article_20260215_200451_013
```

**Where to Find Article IDs:**
- In `docs/articles/` directory filenames
- In daily Newsbot reports
- In `docs/index.md` listing

**Benefits:**
- No need to copy/paste URL
- Guaranteed to exist in system
- Auto-loads article metadata

---

#### 3. GitHub Repository URL

Analyze a GitHub repository directly.

**Format:**
```
analyze-deep: https://github.com/owner/repo
```

**Examples:**
```
analyze-deep: https://github.com/offensive-security/exploit-database
analyze-deep: https://github.com/projectdiscovery/nuclei
```

**What Gets Analyzed:**
- Repository health and metrics
- Issue and PR analysis
- Community activity
- Code quality indicators
- Maintenance status
- Integration with offensive security ecosystem

---

## Comment Placement

### Valid Comment Locations

Trigger keywords work in:

1. **New issue comments** (most common)
2. **Issue descriptions** (when opening new issue)
3. **Reply comments** in existing threads

### Example Issue Comment

```markdown
I saw this article in today's Newsbot report and it seems interesting but also potentially overhyped. Can we get a deeper analysis?

analyze-deep: article_20260216_020926_008

Thanks!
```

### Multiple Analyses in One Comment

**Not Supported** - Only the first valid trigger in a comment will be processed.

If you need to analyze multiple targets, post separate comments:

```markdown
analyze-deep: https://example.com/article-1
```

```markdown
analyze-deep: https://example.com/article-2
```

---

## Access Control

### Who Can Trigger

**Allowed:**
- Repository **collaborators** (write access or higher)
- **Organization members** (if repository is organization-owned)
- **Repository maintainers** (admin access)

**Not Allowed:**
- External contributors without write access
- Anonymous users
- Bots (except explicitly whitelisted)

### Permission Levels

| GitHub Role | Can Trigger | Notes |
|-------------|-------------|-------|
| Admin | ✅ Yes | Full access |
| Write | ✅ Yes | Standard collaborator |
| Triage | ❌ No | Read-only + issue management |
| Read | ❌ No | Read-only |
| External Contributor | ❌ No | Pull request only |

### Permission Denied Response

If a user without permissions attempts to trigger:

```markdown
❌ Only repository collaborators can trigger deep analysis.

You need write access or higher to use this feature. Please contact a repository maintainer if you believe this analysis would be valuable.
```

---

## Rate Limiting

### Limits

**Per Repository:**
- **Maximum:** 5 analyses per day
- **Cooldown:** 2 hours between analyses (configurable)

**Per User:**
- No per-user limit (only repository-wide limit applies)

### Rate Limit Exceeded Response

```markdown
⚠️ **Rate Limit Exceeded**

The daily limit of 5 deep analyses has been reached. Please try again tomorrow.

**Current Status:**
- Analyses today: 5/5
- Next available: 2026-02-17 at 09:00 UTC
- Cooldown: 2 hours between analyses
```

### Cooldown Period Response

```markdown
⚠️ **Cooldown Period Active**

The last analysis completed less than 2 hours ago. Please wait for the cooldown period to end.

**Status:**
- Last analysis: 30 minutes ago
- Next available: 1 hour 30 minutes
- You can track progress in [issue #XX](#)
```

---

## Configuration

### Customizing Rate Limits

Edit `config_deeper_analysis.json`:

```json
{
  "rate_limit": {
    "max_per_day": 5,           // Maximum analyses per day
    "cooldown_hours": 2,        // Hours between analyses
    "per_user_limit": null      // Set to enable per-user limits
  }
}
```

### Customizing Trigger Keywords

Edit `config_deeper_analysis.json`:

```json
{
  "trigger_keywords": [
    "analyze-deep:",
    "deep-analysis:",
    "investigate:",
    "/analyze-deep",
    "your-custom-keyword:"      // Add custom keywords
  ]
}
```

**Case Sensitivity:** Keywords are case-insensitive

- `analyze-deep:` ✅
- `ANALYZE-DEEP:` ✅
- `Analyze-Deep:` ✅

### Enabling Maintainer Approval

For additional control, require maintainer approval before analysis runs:

```json
{
  "require_approval": true,
  "approvers": ["maintainer1", "maintainer2"]
}
```

When enabled, workflow posts:

```markdown
🔍 **Deep Analysis Requested**

**Target:** [target]
**Requested by:** @username

**Maintainer Approval Required**

@maintainer1 @maintainer2 - Please review and approve by commenting:
```
approve-analysis
```

---

## Workflow Response Messages

### Analysis Started

```markdown
🔍 **Deep Analysis Started**

**Target:** `https://example.com/article`
**Status:** Data collection in progress...
**Estimated time:** 10-15 minutes

You can track progress in the [Actions tab](https://github.com/owner/repo/actions/runs/12345)
```

### Analysis Complete

```markdown
## 🔍 Deep Analysis Complete

**Target:** Example Article Title
**Verdict:** PARTIALLY VALIDATED

---

### Key Findings

- ✅ **Validated:** Tool has documented enterprise deployments
- ⚠️ **Questionable:** "10x faster" claim lacks benchmarks
- ❌ **Hype Detected:** "Revolutionary" and "game-changing" unsupported

### Scores

- 🏢 **Enterprise Readiness:** 7/10
- 🔒 **Security Effectiveness:** 6/10
- 💬 **Community Sentiment:** Mixed

---

📄 **Full Report:** [View Report](link)
📦 **Artifact:** [Download](link)

---

*Analysis powered by Newsbot Deeper Analysis*
```

### Analysis Failed

```markdown
❌ **Deep Analysis Failed**

An error occurred during analysis. Please check the [workflow logs](link) for details.

**Common issues:**
- Target URL is inaccessible
- Article ID not found in recent reports
- API rate limits exceeded
- Network connectivity issues

**Troubleshooting:**
- Verify the target URL is publicly accessible
- Check that article ID is correct (from docs/articles/)
- Wait a few minutes and try again if rate limited
```

---

## Best Practices

### 1. Be Specific with Targets

**Good:**
```
analyze-deep: https://blog.vendor.com/2026/02/new-ai-security-tool
```

**Avoid:**
```
analyze-deep: vendor.com
```

### 2. Provide Context in Issue

Help reviewers understand why analysis is needed:

```markdown
This article claims to have discovered 50+ critical CVEs using AI automation, 
but it feels overhyped. Would be great to validate these claims.

analyze-deep: https://example.com/ai-discovers-50-cves
```

### 3. Wait for Completion

Analyses take 10-15 minutes. Don't trigger duplicates:

- ❌ Posting multiple triggers for same target
- ❌ Canceling and restarting immediately
- ✅ Wait for completion or failure notification

### 4. Use Article IDs for Recent Reports

Simpler and more reliable:

**Instead of:**
```
analyze-deep: https://www.recordedfuture.com/blog/autonomous-threat-operations-in-action
```

**Use:**
```
analyze-deep: article_20260216_020926_008
```

---

## Troubleshooting

### Trigger Not Working

**Check:**
1. ✅ Keyword is spelled correctly (`analyze-deep:` not `analyze-deeper:`)
2. ✅ Space after colon: `analyze-deep: URL` not `analyze-deep:URL`
3. ✅ You have write access to the repository
4. ✅ Rate limit not exceeded (max 5/day)
5. ✅ Cooldown period has passed (2 hours between)

### Invalid Target

**Symptoms:**
```
❌ Could not parse target from comment.
```

**Fix:**
Ensure target follows one of these formats:
- Full URL: `https://example.com/path`
- Article ID: `article_20260215_200451_013`
- GitHub repo: `https://github.com/owner/repo`

### API Rate Limits

**Symptoms:**
```
❌ Deep Analysis Failed
API rate limits exceeded
```

**Fix:**
- Wait for rate limit reset (typically 1 hour)
- Reduce frequency of analyses
- Check GitHub Actions quotas

---

## Examples

### Example 1: Analyze Newsbot Article

```markdown
Great daily report! I'm particularly interested in this article about 
autonomous threat hunting. Let's do a deeper dive.

analyze-deep: article_20260216_020926_008
```

### Example 2: Investigate External Article

```markdown
Found this article on Twitter claiming a new tool can find SQL injection 
10x faster than existing tools. Sounds suspicious.

analyze-deep: https://blog.vendor.com/sql-injection-ai-tool
```

### Example 3: Evaluate GitHub Repository

```markdown
This repository was mentioned in r/netsec with claims of enterprise-ready 
offensive security automation. Let's validate.

analyze-deep: https://github.com/vendor/security-automation
```

### Example 4: Research Before Adoption

```markdown
We're considering this tool for our red team. Need comprehensive analysis 
before making a decision.

investigate: https://github.com/projectdiscovery/nuclei
```

---

## Summary

**Quick Reference:**

| Trigger | Format | Example |
|---------|--------|---------|
| Primary | `analyze-deep: <target>` | `analyze-deep: https://example.com` |
| Alternative | `deep-analysis: <target>` | `deep-analysis: article_123` |
| Alternative | `investigate: <target>` | `investigate: https://github.com/org/repo` |
| Slash Command | `/analyze-deep <target>` | `/analyze-deep article_123` |

**Requirements:**
- ✅ Repository collaborator (write access)
- ✅ Within rate limits (5/day, 2hr cooldown)
- ✅ Valid target (URL or article ID)
- ✅ Public accessibility (no auth required)

**Response Time:** 10-15 minutes per analysis

---

**Document Version:** 1.0  
**Last Updated:** February 2026
