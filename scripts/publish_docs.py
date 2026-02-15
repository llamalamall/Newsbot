#!/usr/bin/env python3
"""Helper script to publish Newsbot reports to docs.

Supports publishing the latest report from an outputs directory or a specific
report path with optional results metadata.
"""

import argparse
import json
import logging
import os
import shutil
import sys
from pathlib import Path
from typing import List, Optional

from reporters.docs_publisher import (
    initialize_docs_directory,
    publish_structured_docs,
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
  %(prog)s --all
  %(prog)s --output-dir outputs --docs-dir docs
  %(prog)s --all --clean
""",
    )

    parser.add_argument(
        "--all",
        action="store_true",
        default=True,
        help="publish all reports from the output directory (default mode)",
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


def load_combined_json_files(output_dir: str, prefix: str) -> List[dict]:
    """Load and concatenate JSON lists matching a prefix from the output directory.

    Args:
        output_dir: Directory containing output JSON files.
        prefix: File prefix to match (e.g., "results" or "rejected").

    Returns:
        Concatenated list of JSON items.
    """
    combined: List[dict] = []
    output_path = Path(output_dir)
    json_files = sorted(output_path.glob(f"{prefix}_*.json"))

    for json_file in json_files:
        try:
            with json_file.open("r") as handle:
                payload = json.load(handle)
            if isinstance(payload, list):
                combined.extend(payload)
            else:
                logging.warning("Skipping %s: expected list", json_file.name)
        except (json.JSONDecodeError, OSError) as exc:
            logging.warning("Skipping %s: %s", json_file.name, exc)

    return combined


def main() -> int:
    """Run the docs publishing helper.

    Returns:
        Exit code (0 for success, 1 for failure).
    """
    args = parse_arguments()
    configure_logging(args.verbose)

    if args.clean:
        clean_docs(args.docs_dir)

    # Publish all reports using structured docs format
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
    latest_report = report_files[-1]
    latest_timestamp = (
        os.path.basename(latest_report)
        .replace("report_", "")
        .replace(".md", "")
    )

    combined_results = load_combined_json_files(args.output_dir, "results")
    combined_rejected = load_combined_json_files(args.output_dir, "rejected")

    if not combined_results:
        logging.error("No results JSON files found in: %s", args.output_dir)
        return 1

    logging.info(
        "Loaded %s results and %s rejected items from %s",
        len(combined_results),
        len(combined_rejected),
        args.output_dir,
    )

    published_files = publish_structured_docs(
        combined_results,
        latest_timestamp,
        args.docs_dir,
    )
    published_path = published_files.get("index")

    if not published_path:
        logging.error("No report was published.")
        return 1

    logging.info("Published docs report: %s", published_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
