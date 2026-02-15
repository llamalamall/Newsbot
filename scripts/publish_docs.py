#!/usr/bin/env python3
"""Helper script to publish Newsbot reports to docs using structured publishing.

Publishes reports using the structured documentation format with separate
repositories and articles pages.
"""

import argparse
import json
import logging
import os
import shutil
import sys
from typing import Optional

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
        description="Publish Newsbot reports to docs/ using structured format.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --latest
  %(prog)s --output-dir outputs --docs-dir docs
  %(prog)s --results-path outputs/results_YYYYMMDD_HHMMSS.json
  %(prog)s --latest --clean
""",
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--latest",
        action="store_true",
        help="publish the latest results from the output directory",
    )
    mode_group.add_argument(
        "--all",
        action="store_true",
        help="publish all results from the output directory",
    )
    mode_group.add_argument(
        "--results-path",
        type=str,
        help="publish a specific results JSON file",
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


def publish_results_file(results_path: str, docs_dir: str) -> Optional[str]:
    """Publish a results JSON file using structured publishing.

    Args:
        results_path: Path to the results JSON file
        docs_dir: Target docs directory

    Returns:
        Path to the published index file, or None if publishing failed
    """
    if not os.path.exists(results_path):
        logging.error("Results file not found: %s", results_path)
        return None

    # Extract timestamp from filename
    filename = os.path.basename(results_path)
    timestamp = filename.replace("results_", "").replace(".json", "")

    try:
        with open(results_path, 'r') as f:
            results = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logging.error("Could not read results JSON: %s", e)
        return None

    if not isinstance(results, list):
        logging.error("Results JSON is not a list")
        return None

    initialize_docs_directory(docs_dir)
    published_files = publish_structured_docs(results, timestamp, docs_dir)
    
    logging.info("Published %d repositories", len([r for r in results if r.get("source") == "github"]))
    logging.info("Published %d articles", len([r for r in results if r.get("source") == "rss"]))
    
    return published_files.get("index")


def find_latest_results(output_dir: str) -> Optional[str]:
    """Find the most recent results JSON file in the output directory.

    Args:
        output_dir: Directory containing output files

    Returns:
        Path to the latest results file, or None if not found
    """
    if not os.path.exists(output_dir):
        logging.error("Output directory not found: %s", output_dir)
        return None

    # Find all results files
    results_files = []
    for filename in os.listdir(output_dir):
        if filename.startswith("results_") and filename.endswith(".json"):
            timestamp = filename.replace("results_", "").replace(".json", "")
            results_files.append({
                "filename": filename,
                "timestamp": timestamp,
                "path": os.path.join(output_dir, filename)
            })

    if not results_files:
        logging.error("No results files found in: %s", output_dir)
        return None

    # Sort by timestamp and get the latest
    results_files.sort(key=lambda x: x["timestamp"], reverse=True)
    return results_files[0]["path"]


def main() -> int:
    """Run the docs publishing helper.

    Returns:
        Exit code (0 for success, 1 for failure).
    """
    args = parse_arguments()
    configure_logging(args.verbose)

    if args.clean:
        clean_docs(args.docs_dir)

    published_path: Optional[str] = None
    
    if args.latest:
        # Find and publish latest results
        latest_results = find_latest_results(args.output_dir)
        if not latest_results:
            return 1
        published_path = publish_results_file(latest_results, args.docs_dir)
        
    elif args.all:
        # Publish all results files
        if not os.path.exists(args.output_dir):
            logging.error("Output directory not found: %s", args.output_dir)
            return 1

        results_files = []
        for filename in os.listdir(args.output_dir):
            if filename.startswith("results_") and filename.endswith(".json"):
                results_files.append(os.path.join(args.output_dir, filename))

        if not results_files:
            logging.error("No results files found in: %s", args.output_dir)
            return 1

        results_files.sort()
        for results_path in results_files:
            published_path = publish_results_file(results_path, args.docs_dir)
            if not published_path:
                logging.error("Failed to publish results: %s", results_path)
                return 1
                
    else:
        # Publish specific results file
        published_path = publish_results_file(args.results_path, args.docs_dir)

    if not published_path:
        logging.error("No results were published.")
        return 1

    logging.info("Published docs index: %s", published_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
