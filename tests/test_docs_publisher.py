"""
Tests for the docs_publisher module.
"""

import os
import tempfile
import shutil
import json
from datetime import datetime
import pytest

# Import the module to test
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from reporters.docs_publisher import (
    format_report_for_docs,
    get_existing_reports,
    update_index,
    publish_report_to_docs,
    initialize_docs_directory
)


class TestFormatReportForDocs:
    """Tests for format_report_for_docs function."""
    
    def test_format_adds_front_matter(self):
        """Test that formatting adds YAML front matter."""
        report = "# Test Report\n\nSome content"
        timestamp = "20260215_013608"
        
        result = format_report_for_docs(report, timestamp)
        
        assert result.startswith("---\n")
        assert "layout: default\n" in result
        assert "title: Report - February 15, 2026 at 01:36 UTC\n" in result
        assert "---\n" in result
    
    def test_format_adds_navigation(self):
        """Test that formatting adds navigation links."""
        report = "# Test Report\n\nSome content"
        timestamp = "20260215_013608"
        
        result = format_report_for_docs(report, timestamp)
        
        assert "[← Back to Index](index.md)" in result
        # Should appear at both top and bottom
        assert result.count("[← Back to Index](index.md)") == 2
    
    def test_format_preserves_content(self):
        """Test that original content is preserved."""
        report = "# Test Report\n\nSome important content\n\n## Section 1"
        timestamp = "20260215_013608"
        
        result = format_report_for_docs(report, timestamp)
        
        assert "# Test Report" in result
        assert "Some important content" in result
        assert "## Section 1" in result
    
    def test_format_handles_invalid_timestamp(self):
        """Test formatting with an invalid timestamp."""
        report = "# Test Report"
        timestamp = "invalid_timestamp"
        
        result = format_report_for_docs(report, timestamp)
        
        # Should use the raw timestamp as fallback
        assert "title: Report - invalid_timestamp" in result


class TestGetExistingReports:
    """Tests for get_existing_reports function."""
    
    def test_get_reports_empty_directory(self):
        """Test getting reports from empty directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            reports = get_existing_reports(tmpdir)
            assert reports == []
    
    def test_get_reports_nonexistent_directory(self):
        """Test getting reports from non-existent directory."""
        reports = get_existing_reports("/nonexistent/path")
        assert reports == []
    
    def test_get_reports_with_files(self):
        """Test getting reports from directory with report files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create some test report files
            report1 = os.path.join(tmpdir, "report_20260215_120000.md")
            report2 = os.path.join(tmpdir, "report_20260214_120000.md")
            other_file = os.path.join(tmpdir, "other.md")
            
            for path in [report1, report2, other_file]:
                with open(path, 'w') as f:
                    f.write("test")
            
            reports = get_existing_reports(tmpdir)
            
            # Should only get report_*.md files
            assert len(reports) == 2
            # Should be sorted newest first
            assert reports[0]["filename"] == "report_20260215_120000.md"
            assert reports[1]["filename"] == "report_20260214_120000.md"


class TestUpdateIndex:
    """Tests for update_index function."""
    
    def test_create_new_index(self):
        """Test creating a new index from scratch."""
        with tempfile.TemporaryDirectory() as tmpdir:
            update_index(tmpdir, "report_20260215_120000.md", "20260215_120000", 10)
            
            index_path = os.path.join(tmpdir, "index.md")
            assert os.path.exists(index_path)
            
            with open(index_path, 'r') as f:
                content = f.read()
            
            assert "# Newsbot - Security News Aggregator" in content
            assert "## Latest Reports" in content
            assert "[February 15, 2026 at 12:00 UTC](report_20260215_120000.md) (10 results)" in content
    
    def test_update_existing_index(self):
        """Test updating an existing index with new report."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create initial index
            update_index(tmpdir, "report_20260214_120000.md", "20260214_120000", 5)
            
            # Add another report
            update_index(tmpdir, "report_20260215_120000.md", "20260215_120000", 10)
            
            index_path = os.path.join(tmpdir, "index.md")
            with open(index_path, 'r') as f:
                content = f.read()
            
            # Both reports should be present
            assert "report_20260214_120000.md" in content
            assert "report_20260215_120000.md" in content
            
            # Newer report should come first
            pos1 = content.index("report_20260215_120000.md")
            pos2 = content.index("report_20260214_120000.md")
            assert pos1 < pos2
    
    def test_skip_duplicate_report(self):
        """Test that duplicate reports are not added to index."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Add report twice
            update_index(tmpdir, "report_20260215_120000.md", "20260215_120000", 10)
            update_index(tmpdir, "report_20260215_120000.md", "20260215_120000", 10)
            
            index_path = os.path.join(tmpdir, "index.md")
            with open(index_path, 'r') as f:
                content = f.read()
            
            # Should only appear once
            assert content.count("report_20260215_120000.md") == 1
    
    def test_remove_placeholder_text(self):
        """Test that placeholder text is removed when first report is added."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create index with placeholder
            index_path = os.path.join(tmpdir, "index.md")
            with open(index_path, 'w') as f:
                f.write("## Latest Reports\n\n*No reports yet. Reports will appear here as they are generated.*\n\n---\n")
            
            # Add a report
            update_index(tmpdir, "report_20260215_120000.md", "20260215_120000", 10)
            
            with open(index_path, 'r') as f:
                content = f.read()
            
            # Placeholder should be gone
            assert "*No reports yet" not in content
            # Report should be present
            assert "report_20260215_120000.md" in content


class TestPublishReportToDocs:
    """Tests for publish_report_to_docs function."""
    
    def test_publish_new_report(self):
        """Test publishing a new report to docs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a test report
            report_path = os.path.join(tmpdir, "report_20260215_120000.md")
            with open(report_path, 'w') as f:
                f.write("# Test Report\n\nContent")
            
            # Create docs directory
            docs_dir = os.path.join(tmpdir, "docs")
            
            # Publish report
            result = publish_report_to_docs(report_path, docs_dir, 10)
            
            assert result is not None
            assert os.path.exists(result)
            
            # Check formatted content
            with open(result, 'r') as f:
                content = f.read()
            
            assert "---\nlayout: default\n" in content
            assert "# Test Report" in content
            assert "[← Back to Index](index.md)" in content
            
            # Check index was updated
            index_path = os.path.join(docs_dir, "index.md")
            assert os.path.exists(index_path)
    
    def test_skip_existing_report(self):
        """Test that existing reports are not republished."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a test report
            report_path = os.path.join(tmpdir, "report_20260215_120000.md")
            with open(report_path, 'w') as f:
                f.write("# Test Report\n\nContent")
            
            docs_dir = os.path.join(tmpdir, "docs")
            
            # Publish twice
            result1 = publish_report_to_docs(report_path, docs_dir, 10)
            result2 = publish_report_to_docs(report_path, docs_dir, 10)
            
            # Both should return same path
            assert result1 == result2
            
            # Index should only have one entry
            index_path = os.path.join(docs_dir, "index.md")
            with open(index_path, 'r') as f:
                content = f.read()
            
            assert content.count("report_20260215_120000.md") == 1
    
    def test_publish_nonexistent_report(self):
        """Test publishing a non-existent report."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            result = publish_report_to_docs("/nonexistent/report.md", docs_dir, 10)
            
            assert result is None


class TestInitializeDocsDirectory:
    """Tests for initialize_docs_directory function."""
    
    def test_initialize_creates_directory(self):
        """Test that initialization creates the docs directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            initialize_docs_directory(docs_dir)
            
            assert os.path.exists(docs_dir)
            assert os.path.isdir(docs_dir)
    
    def test_initialize_creates_nojekyll(self):
        """Test that .nojekyll file is created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            initialize_docs_directory(docs_dir)
            
            nojekyll_path = os.path.join(docs_dir, ".nojekyll")
            assert os.path.exists(nojekyll_path)
    
    def test_initialize_creates_index(self):
        """Test that index.md is created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            initialize_docs_directory(docs_dir)
            
            index_path = os.path.join(docs_dir, "index.md")
            assert os.path.exists(index_path)
            
            with open(index_path, 'r') as f:
                content = f.read()
            
            assert "# Newsbot - Security News Aggregator" in content
            assert "## About Newsbot" in content
            assert "## Latest Reports" in content
    
    def test_initialize_creates_readme(self):
        """Test that README.md is created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            initialize_docs_directory(docs_dir)
            
            readme_path = os.path.join(docs_dir, "README.md")
            assert os.path.exists(readme_path)
            
            with open(readme_path, 'r') as f:
                content = f.read()
            
            assert "# Newsbot Documentation" in content
            assert "Setup GitHub Pages" in content
    
    def test_initialize_idempotent(self):
        """Test that initialization is idempotent (can be run multiple times)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = os.path.join(tmpdir, "docs")
            
            # Initialize twice
            initialize_docs_directory(docs_dir)
            initialize_docs_directory(docs_dir)
            
            # All files should still exist
            assert os.path.exists(os.path.join(docs_dir, ".nojekyll"))
            assert os.path.exists(os.path.join(docs_dir, "index.md"))
            assert os.path.exists(os.path.join(docs_dir, "README.md"))


class TestEndToEndWorkflow:
    """Integration tests for complete docs publishing workflow."""
    
    def test_complete_workflow(self):
        """Test the complete workflow from initialization to multiple reports."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create some test reports
            outputs_dir = os.path.join(tmpdir, "outputs")
            os.makedirs(outputs_dir)
            
            report1_path = os.path.join(outputs_dir, "report_20260214_120000.md")
            report2_path = os.path.join(outputs_dir, "report_20260215_120000.md")
            
            with open(report1_path, 'w') as f:
                f.write("# Report 1\n\nOlder report")
            
            with open(report2_path, 'w') as f:
                f.write("# Report 2\n\nNewer report")
            
            # Initialize docs
            docs_dir = os.path.join(tmpdir, "docs")
            initialize_docs_directory(docs_dir)
            
            # Publish both reports
            publish_report_to_docs(report1_path, docs_dir, 5)
            publish_report_to_docs(report2_path, docs_dir, 10)
            
            # Verify structure
            assert os.path.exists(os.path.join(docs_dir, "report_20260214_120000.md"))
            assert os.path.exists(os.path.join(docs_dir, "report_20260215_120000.md"))
            assert os.path.exists(os.path.join(docs_dir, "index.md"))
            assert os.path.exists(os.path.join(docs_dir, ".nojekyll"))
            assert os.path.exists(os.path.join(docs_dir, "README.md"))
            
            # Verify index has both reports in correct order
            index_path = os.path.join(docs_dir, "index.md")
            with open(index_path, 'r') as f:
                content = f.read()
            
            # Newer report should come first
            pos1 = content.index("report_20260215_120000.md")
            pos2 = content.index("report_20260214_120000.md")
            assert pos1 < pos2
            
            # Verify result counts
            assert "(10 results)" in content
            assert "(5 results)" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
