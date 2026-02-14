#!/usr/bin/env python3
"""
Demonstration of Newsbot's enhanced web search capabilities.
This script shows how the new features work together.
"""

import sys
import os
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.newsbot import NewsBot


def demo_credibility_assessment():
    """Demonstrate the credibility assessment feature."""
    print("\n" + "=" * 70)
    print("DEMONSTRATION: Source Credibility Assessment")
    print("=" * 70)
    print()
    print("Newsbot automatically assesses the credibility of news sources.")
    print("This ensures only high-quality, trustworthy sources are included.")
    print()
    
    bot = NewsBot()
    
    example_sources = [
        "https://arxiv.org/abs/2024.12345",
        "https://blog.cloudflare.com/new-security-feature",
        "https://github.blog/security-updates",
        "https://krebsonsecurity.com/2024/01/latest-breach/",
        "https://medium.com/security-article",
        "https://unknown-blog.example/random-post",
    ]
    
    print("Example Sources and Their Credibility Ratings:")
    print("-" * 70)
    
    for url in example_sources:
        credibility = bot.assess_source_credibility(url)
        emoji = "🟢" if credibility == "high" else "🟡" if credibility == "medium" else "🔴"
        print(f"{emoji} {credibility.upper():8} | {url}")
    
    print()
    print("✓ High credibility sources include: official security orgs, major tech")
    print("  companies, respected research institutions, and known security blogs")
    print("✓ Medium credibility sources include: established tech news sites and")
    print("  developer platforms")
    print("✗ Low credibility sources are filtered out from final reports")
    print()


def demo_web_search_workflow():
    """Demonstrate the web search workflow."""
    print("\n" + "=" * 70)
    print("DEMONSTRATION: Web Search Workflow")
    print("=" * 70)
    print()
    print("Enhanced Newsbot workflow:")
    print()
    
    workflow_steps = [
        "1. User provides search topic: 'AI offensive security automation'",
        "2. Newsbot performs live web search for current articles",
        "3. Results are filtered by source credibility",
        "4. Article content is extracted from high-credibility sources",
        "5. Web search results are passed to LLM as context",
        "6. LLM analyzes and summarizes with source citations",
        "7. Final report includes credibility ratings and links",
    ]
    
    for step in workflow_steps:
        print(f"  {step}")
    
    print()
    print("Benefits:")
    print("  ✓ More current and accurate information")
    print("  ✓ Proper source attribution and citations")
    print("  ✓ Quality filtering through credibility assessment")
    print("  ✓ Graceful handling of failures")
    print()


def demo_llm_integration():
    """Demonstrate LLM integration with web search context."""
    print("\n" + "=" * 70)
    print("DEMONSTRATION: LLM Integration with Web Search")
    print("=" * 70)
    print()
    print("The LLM prompt is enhanced with web search context:")
    print()
    
    # Show a sample of what the prompt looks like
    sample_web_results = """
Title: New AI Security Tool Released
URL: https://github.com/example/ai-security-tool
Snippet: Researchers announce new automated security testing framework...
Credibility: high

Title: AI in Penetration Testing
URL: https://blog.cloudflare.com/ai-pentesting
Snippet: How AI is transforming offensive security practices...
Credibility: high
"""
    
    print("Example Web Search Context:")
    print("-" * 70)
    print(sample_web_results)
    print("-" * 70)
    print()
    print("This context is passed to the LLM along with the query, enabling:")
    print("  ✓ Fact-based responses grounded in current sources")
    print("  ✓ Proper citation of original articles")
    print("  ✓ Verification against credible sources")
    print("  ✓ Detection of promotional or low-quality content")
    print()


def demo_error_handling():
    """Demonstrate robust error handling."""
    print("\n" + "=" * 70)
    print("DEMONSTRATION: Robust Error Handling")
    print("=" * 70)
    print()
    print("Newsbot handles various failure scenarios gracefully:")
    print()
    
    scenarios = [
        ("Web search API unavailable", "Falls back to LLM-only search"),
        ("Article URL unreachable", "Continues with other sources"),
        ("Low-credibility sources found", "Filters them out automatically"),
        ("LLM API error", "Logs error and continues with next topic"),
        ("Partial failures", "Processes successful results, reports failures"),
    ]
    
    print("Failure Scenario               | Newsbot Response")
    print("-" * 70)
    
    for scenario, response in scenarios:
        print(f"{scenario:32} | {response}")
    
    print()
    print("✓ No single failure stops the entire aggregation process")
    print("✓ Users receive meaningful error messages")
    print("✓ Partial results are still useful and reported")
    print()


def demo_output_format():
    """Demonstrate the enhanced output format."""
    print("\n" + "=" * 70)
    print("DEMONSTRATION: Enhanced Output Format")
    print("=" * 70)
    print()
    print("Sample report section with new features:")
    print()
    
    sample_report = """
## Web Search Results (3)

*Results from live web searches with credibility assessment*

### New AI-Powered Security Testing Framework Released

Researchers announce breakthrough in automated penetration testing using
large language models to identify vulnerabilities...

**Source:** [https://arxiv.org/abs/2024.12345](https://arxiv.org/abs/2024.12345)
**Credibility:** High

**Key Points:**
- Novel approach to automated exploit generation
- Reduces manual testing time by 60%
- Open-source implementation available

*Published: 2024-02-10*
*Search topic: AI offensive security automation*

---

*Note: Results are filtered for credibility and relevance. 
Web search results are assessed for source reliability before inclusion.*
"""
    
    print(sample_report)
    print()
    print("Key Enhancements:")
    print("  ✓ Source URLs with direct links")
    print("  ✓ Credibility ratings displayed")
    print("  ✓ Publication dates when available")
    print("  ✓ Key points extracted from articles")
    print("  ✓ Clear indication of search topic")
    print()


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 70)
    print("NEWSBOT ENHANCED FEATURES DEMONSTRATION")
    print("=" * 70)
    print()
    print("This demonstration shows the new capabilities added to Newsbot:")
    print("  • Live web search integration")
    print("  • Source credibility assessment")
    print("  • Article content extraction")
    print("  • Enhanced LLM prompts with web context")
    print("  • Improved reporting with citations")
    print()
    
    demo_credibility_assessment()
    demo_web_search_workflow()
    demo_llm_integration()
    demo_error_handling()
    demo_output_format()
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("Newsbot now combines:")
    print("  1. Live web searches for current, factual information")
    print("  2. Intelligent source credibility filtering")
    print("  3. Article content extraction and analysis")
    print("  4. LLM-powered summarization with context")
    print("  5. Robust error handling and graceful degradation")
    print()
    print("Result: More accurate, credible, and useful security news aggregation")
    print("with proper source attribution and citations.")
    print()
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
