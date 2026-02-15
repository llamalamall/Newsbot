#!/usr/bin/env python3
"""Helper script to publish Newsbot reports to docs.

Supports publishing the latest report from an outputs directory or a specific
report path with optional results metadata.
"""

import argparse
import logging
import os
import shutil
import sys
from typing import Optional

from reporters.docs_publisher import (
    initialize_docs_directory,
    publish_latest_report,
    publish_report_from_path,
)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        prog="publish_docs",
        description="Publish Newsbot reports to the docs/ directory.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --latest
  %(prog)s --output-dir outputs --docs-dir docs
  %(prog)s --report-path outputs/report_YYYYMMDD_HHMMSS.md
  %(prog)s --report-path outputs/report_YYYYMMDD_HHMMSS.md --results-path outputs/results_YYYYMMDD_HHMMSS.json
    %(prog)s --latest --clean
""",
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--latest",
        action="store_true",
        help="publish the latest report from the output directory",
    )
    mode_group.add_argument(
        "--all",
        action="store_true",
        help="publish all reports from the output directory",
    )
    mode_group.add_argument(
        "--report-path",
        type=str,
        help="publish a specific report markdown file",
    )

    parser.add_argument(
        "--results-path",
        type=str,
        default=None,
        help="optional results JSON file for result count",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        default="outputs",
        help="directory containing report outputs (default: outputs)",
    )

    parser.add_argument(
        "--docs-dir",
        type=str,
        default="docs",
        help="target docs directory (default: docs)",
    )

    parser.add_argument(
        "--clean",
        action="store_true",
        help="remove existing docs articles and repositories, then rebuild index.md",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="enable verbose logging output",
    )

    return parser.parse_args()


def configure_logging(verbose: bool) -> None:
    """Configure logging for the script.

    Args:
        verbose: Whether to enable verbose logging.
    """
    log_level = logging.DEBUG if verbose else logging.INFO
    log_format = "%(levelname)s: %(message)s"
    logging.basicConfig(level=log_level, format=log_format, force=True)


def clean_docs(docs_dir: str) -> None:
    """Remove generated docs content and rebuild the index.

    Args:
        docs_dir: Target docs directory.
    """
    articles_dir = os.path.join(docs_dir, "articles")
    repositories_path = os.path.join(docs_dir, "repositories.md")
    index_path = os.path.join(docs_dir, "index.md")

    if os.path.isdir(articles_dir):
        shutil.rmtree(articles_dir)
        logging.info("Removed articles directory: %s", articles_dir)

    if os.path.isfile(repositories_path):
        os.remove(repositories_path)
        logging.info("Removed repositories file: %s", repositories_path)

    if os.path.isfile(index_path):
        os.remove(index_path)
        logging.info("Removed index file: %s", index_path)

    initialize_docs_directory(docs_dir)


def main() -> int:
    """Run the docs publishing helper.

    Returns:
        Exit code (0 for success, 1 for failure).
    """
    args = parse_arguments()
    configure_logging(args.verbose)

    if args.clean:
        clean_docs(args.docs_dir)

    published_path: Optional[str]
    if args.latest:
        published_path = publish_latest_report(args.output_dir, args.docs_dir)
    elif args.all:
        published_path = None
        if not os.path.exists(args.output_dir):
            logging.error("Output directory not found: %s", args.output_dir)
            return 1

        report_files = []
        for filename in os.listdir(args.output_dir):
            if filename.startswith("report_") and filename.endswith(".md"):
                report_files.append(os.path.join(args.output_dir, filename))

        if not report_files:
            logging.error("No report files found in: %s", args.output_dir)
            return 1

        report_files.sort()
        for report_path in report_files:
            published_path = publish_report_from_path(
                report_path,
                docs_dir=args.docs_dir,
                results_path=None,
            )
            if not published_path:
                logging.error("Failed to publish report: %s", report_path)
                return 1
    else:
        published_path = publish_report_from_path(
            args.report_path,
            docs_dir=args.docs_dir,
            results_path=args.results_path,
        )

    if not published_path:
        logging.error("No report was published.")
        return 1

    logging.info("Published docs report: %s", published_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
