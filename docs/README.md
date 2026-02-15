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
- Adding a `_config.yml` file for Jekyll configuration
- Creating custom CSS in a `assets/` directory
- Modifying the report templates in the publisher script
