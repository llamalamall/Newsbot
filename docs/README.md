# Newsbot Documentation

This directory contains formatted reports for GitHub Pages.

## Setup GitHub Pages

To publish these reports as a website:

1. Go to your repository **Settings** > **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Select the **main** branch and **/docs** folder
4. Click **Save**

GitHub will automatically publish the site at `https://<username>.github.io/<repository>/`

## Files

- `index.md` - Main landing page with links to all reports
- `report_YYYYMMDD_HHMMSS.md` - Individual report files
- `.nojekyll` - Disables Jekyll processing for cleaner URLs

## Customization

You can customize the look and feel by:
- Editing `_config.yml` for Jekyll configuration (theme, title, description)
- Creating custom CSS in a `assets/` directory
- Modifying the report templates in the publisher script

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
- Verify .nojekyll file exists (disables default Jekyll processing)
- Wait 1-2 minutes after pushing changes

**Build failures:**
- Check the Actions tab for error messages
- Ensure _config.yml syntax is valid YAML
- Verify all markdown files have valid syntax

**Broken links:**
- Use relative links (e.g., `[link](report.md)` not `[link](/docs/report.md)`)
- Check that linked files exist in the docs/ folder

**Styling issues:**
- Verify _config.yml theme setting
- Check that front matter is properly formatted in report files
- Consider adding custom CSS in assets/ directory
