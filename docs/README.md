# Newsbot Documentation

This directory contains formatted reports for GitHub Pages.

## Documentation Structure

The documentation is organized into the following components:

### Main Pages
- **`index.md`** - Main landing page with navigation to all content
- **`repositories.md`** - Table listing of all discovered GitHub repositories
- **`articles/`** - Directory containing individual RSS article pages

### Report Files (Legacy)
- **`report_YYYYMMDD_HHMMSS.md`** - Individual full report files (maintained for backward compatibility)

## New Structured Format

Starting with the latest version, Newsbot documentation is organized as follows:

1. **GitHub Repositories**: All discovered repositories are consolidated into a single `repositories.md` page with a searchable table format showing:
   - Repository name and link
   - Description
   - Star count
   - Last updated date
   - Primary topic

2. **RSS Articles**: Each RSS feed article gets its own dedicated page under `articles/`, named as `article_YYYYMMDD_HHMMSS_NNN.md`. Each article page includes:
   - Full article title and description
   - Publication date
   - Source feed information
   - LLM applicability and credibility assessments
   - Navigation links to previous/next articles

3. **Index Page**: The `index.md` serves as the central hub with:
   - Link to the repositories page
   - Chronological listing of all article pages organized by date
   - Links to legacy full report files

## Setup GitHub Pages

To publish these reports as a website:

1. Go to your repository **Settings** > **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Select the **main** branch and **/docs** folder
4. Click **Save**

GitHub will automatically publish the site at `https://<username>.github.io/<repository>/`

## Files

- `index.md` - Main landing page with links to all content
- `repositories.md` - Table of all GitHub repositories
- `articles/article_*.md` - Individual RSS article pages
- `report_YYYYMMDD_HHMMSS.md` - Legacy full report files
- `.nojekyll` - Disables Jekyll processing (allows plain markdown rendering with front matter)

## Customization

You can customize the look and feel by:
- Modifying the report templates in the publisher script
- Editing the front matter in individual report files
- Creating custom CSS in an `assets/` directory (requires custom HTML)

## Verifying GitHub Pages Setup

After configuring GitHub Pages, verify it's working:

1. **Check GitHub Pages is enabled:**
   - Go to **Settings** > **Pages**
   - Verify **Source** is set to "Deploy from a branch"
   - Confirm **Branch** is set to "main" and folder is "/docs"
   - Look for the green checkmark and site URL

2. **Visit your site:**
   - Your site will be at `https://<username>.github.io/<repository>/`
   - It may take a few minutes to deploy initially

3. **Check build status:**
   - Go to the **Actions** tab
   - Look for "pages build and deployment" workflow
   - Ensure it completed successfully (green checkmark)

## Troubleshooting

**Pages not appearing:**
- Ensure the repository is public (or you have GitHub Pro for private repos)
- Check that the docs/ folder contains index.md
- Verify .nojekyll file exists (disables Jekyll processing for plain rendering)
- Wait 1-2 minutes after pushing changes

**Build failures:**
- Check the Actions tab for error messages
- Verify all markdown files have valid syntax
- Ensure front matter is properly formatted in report files

**Broken links:**
- Use relative links (e.g., `[link](report.md)` not `[link](/docs/report.md)`)
- Check that linked files exist in the docs/ folder

**Styling issues:**
- GitHub Pages uses default GitHub markdown styling with .nojekyll
- Check that front matter is properly formatted in report files
- Consider removing .nojekyll to enable Jekyll themes (requires _config.yml)
