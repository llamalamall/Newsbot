---
layout: default
title: Rejected Articles
---

# Rejected Articles

This page lists all articles that were evaluated but rejected from publication. Articles are rejected when they do not meet Newsbot's relevance or credibility criteria.

## What Constitutes a "Rejected" Article?

Articles are rejected for the following reasons:

### Rejection Type: Relevance

Articles can be rejected as not relevant if they:

1. **Missing AI Keywords** (`missing_ai_keywords`): GitHub repositories that lack keywords related to AI, automation, or fuzzing in offensive security contexts. These repositories may be related to security but don't involve the use of AI or automation.

2. **LLM Applicability Below Threshold** (`llm_applicability_below_threshold`): RSS feed articles that were assessed by the LLM (Large Language Model) but scored below the configured applicability threshold. This typically means:
   - The article doesn't contain sufficient content about offensive security topics (penetration testing, red team operations, vulnerability research, exploit development, etc.), OR
   - The article doesn't explicitly describe the **use** of AI, automation, or fuzzing techniques

   Both requirements must be satisfied for an article to be considered applicable.

### Rejection Type: Credibility

1. **LLM Credibility Below Threshold** (`llm_credibility_below_threshold`): RSS feed articles that scored below the configured credibility threshold. This indicates potential issues with:
   - Source reliability
   - Content quality or accuracy
   - Lack of technical depth
   - Promotional or marketing-focused content

## Rejected Articles Table

Total rejected articles: **962**

| Title | Topic | Rejection Type | Rejection Reason |
|-------|-------|----------------|------------------|
| [AakarshakKaushal00/guardrail-layer](https://github.com/AakarshakKaushal00/guardrail-layer) | ai-security | applicability | Focuses on data privacy and access control using AI, not offensive security or automated offensive tooling. |
| [Carricacha/local-rag-system](https://github.com/Carricacha/local-rag-system) | ai-security | applicability | Repository is about Retrieval-Augmented Generation (RAG) for private AI memory, not offensive security or automated security testing. |
| [CloudDefenseAI/secure-agents-md](https://github.com/CloudDefenseAI/secure-agents-md) | ai-security | applicability | Focuses on governance and secure coding practices for AI agents but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [CtacPyc/AI-Home-Guardian](https://github.com/CtacPyc/AI-Home-Guardian) | ai-security | applicability | Repository focuses on home security and AI-driven surveillance, not offensive security or penetration testing. No evidence of AI/automation for offensive security. |
| [JohannFreddyLoayzaHuana/awesome-ai-coding-tools](https://github.com/JohannFreddyLoayzaHuana/awesome-ai-coding-tools) | ai-security | applicability | Repository is a curated list of AI coding tools, not focused on offensive security or automation for security testing. |
| [Laserman652/AIPhishingDetector](https://github.com/Laserman652/AIPhishingDetector) | ai-security | applicability | Repository uses AI for phishing detection (defensive, not offensive security); does not demonstrate offensive security, penetration testing, or red teaming use cases. |
| [LaurenceGab/ai-monitoring-layer](https://github.com/LaurenceGab/ai-monitoring-layer) | ai-security | applicability | Focuses on monitoring and anomaly detection for web apps, not on offensive security or automation/fuzzing for security testing. |
| [LoonMORTI/promptshield](https://github.com/LoonMORTI/promptshield) | ai-security | applicability | Focuses on protecting LLM applications from prompt injection and jailbreaks, which is defensive security, not offensive. No evidence of AI/automation being used for offensive security. |
| [Luxvil/ai-coding-rules](https://github.com/Luxvil/ai-coding-rules) | ai-security | applicability | Repository focuses on enhancing AI coding assistants but lacks any explicit connection to offensive security or automation/fuzzing for security purposes. |
| [ParraX123/meta-ai-bug-bounty](https://github.com/ParraX123/meta-ai-bug-bounty) | ai-security | applicability | Focuses on analyzing vulnerabilities in Meta AI's group chat but does not explicitly mention use of AI, automation, or fuzzing for offensive security; appears to be a manual or research-focused project. |
| [Phinchanbora/llm-evaluation](https://github.com/Phinchanbora/llm-evaluation) | ai-security | applicability | Benchmarks LLMs and mentions red-team tools, but lacks explicit offensive security automation or AI-driven attack/fuzzing context. |
| [Poeth01/SecureAI-PolicyGuard](https://github.com/Poeth01/SecureAI-PolicyGuard) | ai-security | applicability | Focuses on AI-driven data classification and compliance, not offensive security or automation/fuzzing for attacks. |
| [Rul1an/assay](https://github.com/Rul1an/assay) | ai-security | applicability | Repository focuses on runtime security and policy enforcement for AI agents but lacks explicit evidence of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [Sarb-jot/system-prompt-research](https://github.com/Sarb-jot/system-prompt-research) | ai-security | applicability | Researches prompt engineering and LLM security, but does not demonstrate offensive security tooling or automated attack/defense. |
| [Suleymkr/maais-runtime](https://github.com/Suleymkr/maais-runtime) | ai-security | applicability | Focuses on securing AI agents (defensive); no indication of offensive security, penetration testing, or automation for attacks. |
| [Trusera/ai-bom](https://github.com/Trusera/ai-bom) | ai-security | applicability | Focuses on AI asset inventory and bill of materials, not offensive security or automation/fuzzing for attacks. |
| [Wasi69/Australian-AI-Security](https://github.com/Wasi69/Australian-AI-Security) | ai-security | applicability | Repository is a resource for AI security standards and frameworks, not a tool for offensive security or automation/fuzzing. |
| [Yasas9029/ai-design-engineering-cc-plugins](https://github.com/Yasas9029/ai-design-engineering-cc-plugins) | ai-security | applicability | Repository focuses on AI-driven agentic applications and design engineering, not offensive security or automation/fuzzing for security testing. |
| [Yosuraki/claude4-audit-recon](https://github.com/Yosuraki/claude4-audit-recon) | ai-security | applicability | Focuses on ethical auditing and introspection of AI models without offensive security or automation context. |
| [Zain3311/CVE-2025-49844](https://github.com/Zain3311/CVE-2025-49844) | ai-security | applicability | Repository is an exploit PoC for a Redis vulnerability with offensive security context, but there is no explicit evidence of AI, automation, or fuzzing being used in the exploit or its description. |
| [always-further/nono](https://github.com/always-further/nono) | ai-security | applicability | Focuses on sandboxing and securing AI agents (defensive, not offensive security); no evidence of use for penetration testing, red teaming, or vulnerability discovery. |
| [arcanjohacklindo/security-vulnerabilities-cli-llm](https://github.com/arcanjohacklindo/security-vulnerabilities-cli-llm) | ai-security | applicability | Analyzes vulnerabilities in LLM deployments but does not demonstrate offensive security automation, AI-powered attacks, or fuzzing. |
| [datacline/open-threat-detector](https://github.com/datacline/open-threat-detector) | ai-security | applicability | Focuses on detecting shadow AI threats in organizational environments but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [ethicxlhuman/security-automation-insights](https://github.com/ethicxlhuman/security-automation-insights) | ai-security | applicability | The repository focuses on automation and AI in security operations and compliance, but lacks explicit evidence of offensive security context such as penetration testing, red teaming, vulnerability analysis, exploit development, or malware analysis. The topics and description do not demonstrate the use of AI/automation/fuzzing for offensive security purposes. |
| [fkern4612-design/openclaw-telemetry](https://github.com/fkern4612-design/openclaw-telemetry) | ai-security | applicability | Focuses on observability, telemetry, and LLM security for defense, not offensive security or automation for offensive operations. |
| [foodman1227/awesome-ai-tools](https://github.com/foodman1227/awesome-ai-tools) | ai-security | applicability | General AI tools list; not specific to offensive security or automation for security testing. |
| [inkog-io/inkog](https://github.com/inkog-io/inkog) | ai-security | applicability | Focuses on static analysis and pre-flight checks for AI agents, but lacks explicit mention of offensive security, penetration testing, or fuzzing use cases. |
| [jenishsoftx6/ai-compliance-risk-insights](https://github.com/jenishsoftx6/ai-compliance-risk-insights) | ai-security | applicability | Repository focuses on AI for financial risk management and compliance, not on offensive security or automated security testing. |
| [labkomputerinformatika/HISSI-Policy-Concept](https://github.com/labkomputerinformatika/HISSI-Policy-Concept) | ai-security | applicability | Focuses on policy concepts for AI security in robotics and supply chain, not on offensive security or the use of AI/automation/fuzzing for security testing. |
| [loaiasd/redspecter-ai-usage-watchdog](https://github.com/loaiasd/redspecter-ai-usage-watchdog) | ai-security | applicability | Monitors AI usage on endpoints for security, but is focused on blue team/monitoring rather than offensive security or automation/fuzzing. |
| [luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock) | ai-security | applicability | Repository focuses on securing AI agents with egress proxy and integrity monitoring but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [melanynewmown790/healthcare-assistant](https://github.com/melanynewmown790/healthcare-assistant) | ai-security | applicability | Healthcare assistant with AI features, not related to offensive security or automation for penetration testing. |
| [nonamebatbai/Anti_Phishing_Email_Detector_gui](https://github.com/nonamebatbai/Anti_Phishing_Email_Detector_gui) | ai-security | applicability | Uses AI/ML for phishing detection, which is defensive rather than offensive security. |
| [ogulcanaydogan/LLM-Supply-Chain-Attestation](https://github.com/ogulcanaydogan/LLM-Supply-Chain-Attestation) | ai-security | applicability | Targets supply chain security for LLMs, not offensive security or automation for offensive purposes. |
| [peg/rampart](https://github.com/peg/rampart) | ai-security | applicability | Focuses on securing AI agents and controlling their actions, not on offensive security or automated offensive operations. |
| [rizkycsv/PromptGuard](https://github.com/rizkycsv/PromptGuard) | ai-security | applicability | Focuses on safeguarding and detecting regressions in LLMs, but does not explicitly demonstrate offensive security use or automation for offensive purposes. |
| [roynaldo1234/meta-ai-bug-bounty](https://github.com/roynaldo1234/meta-ai-bug-bounty) | ai-security | applicability | Focuses on AI security and bug bounty, but lacks explicit mention of AI/automation/fuzzing being used for offensive security tooling or automation. |
| [sairysee/aappmart](https://github.com/sairysee/aappmart) | ai-security | applicability | Mentions offensive security and automation, but description and topics suggest a general-purpose marketplace with security-related keywords, not an explicit offensive security AI/automation tool. |
| [stacklok/toolhive-studio](https://github.com/stacklok/toolhive-studio) | ai-security | applicability | Mentions AI agents but lacks explicit offensive security focus or automation for security testing. |
| [superagent-ai/brin](https://github.com/superagent-ai/brin) | ai-security | applicability | Focuses on securing package gateways and malware detection, but lacks explicit offensive security automation or AI-powered offensive tooling. |
| [HungTran733/How-AI-Detects-Rugpulls](https://github.com/HungTran733/How-AI-Detects-Rugpulls) | ai-security | credibility | No stars and no community validation; description is clear but lacks evidence of adoption. |
| [Shaurya1456/AI-Vulverability-Scanner](https://github.com/Shaurya1456/AI-Vulverability-Scanner) | ai-security | credibility | No stars and recent creation date suggest no community validation; description is clear but project may be untested or unknown. |
| [kyle122497/llamator-mcp-server](https://github.com/kyle122497/llamator-mcp-server) | ai-security | credibility | No stars and very recent update; description is clear but no community validation. |
| [vukssan/KamelionStack-OSE](https://github.com/vukssan/KamelionStack-OSE) | ai-security | credibility | No stars or community validation, but description is clear and recently updated. |
| [666Vendetta666/security-scanner](https://github.com/666Vendetta666/security-scanner) | ai-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | ai-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | ai-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | ai-security | relevance | missing_ai_keywords |
| [Ashik245-commits/LLM-Filter-Probe](https://github.com/Ashik245-commits/LLM-Filter-Probe) | ai-security | relevance | missing_ai_keywords |
| [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | ai-security | relevance | missing_ai_keywords |
| [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | ai-security | relevance | missing_ai_keywords |
| [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | ai-security | relevance | missing_ai_keywords |
| [Rizwan723/MCP-Security-Proxy](https://github.com/Rizwan723/MCP-Security-Proxy) | ai-security | relevance | missing_ai_keywords |
| [Soulreaper1188/openclaw-detect](https://github.com/Soulreaper1188/openclaw-detect) | ai-security | relevance | missing_ai_keywords |
| [andyaziz/claude-code-ultimate-guide](https://github.com/andyaziz/claude-code-ultimate-guide) | ai-security | relevance | missing_ai_keywords |
| [baagad-ai/content-wand](https://github.com/baagad-ai/content-wand) | ai-security | relevance | missing_ai_keywords |
| [chrismmt/mcp-adversarial-suite](https://github.com/chrismmt/mcp-adversarial-suite) | ai-security | relevance | missing_ai_keywords |
| [javidahmed64592/cyber-query-ai](https://github.com/javidahmed64592/cyber-query-ai) | ai-security | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | ai-security | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | ai-security | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [GaloisInc/grease](https://github.com/GaloisInc/grease) | binary-analysis | applicability | Repository is for binary analysis and symbolic execution (automation), but no explicit mention of offensive security use cases (e.g., pentesting, exploit dev, malware analysis). |
| [NebiyuSeyoum/exploring-the-true-nature-of-variable](https://github.com/NebiyuSeyoum/exploring-the-true-nature-of-variable) | binary-analysis | applicability | Repository is a learning resource about programming variables and memory, with no connection to offensive security or AI/automation/fuzzing. |
| [fhjlfer098/Malware-Analysis](https://github.com/fhjlfer098/Malware-Analysis) | binary-analysis | applicability | Focuses on manual malware analysis techniques without evidence of AI, automation, or fuzzing. |
| [than0024/ida-reach](https://github.com/than0024/ida-reach) | binary-analysis | applicability | Mentions automation but lacks explicit connection to offensive security or AI usage for security testing. |
| [11philip22/extract-shellcode](https://github.com/11philip22/extract-shellcode) | binary-analysis | relevance | missing_ai_keywords |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [CUB3D/ghidra-hexagon-sleigh](https://github.com/CUB3D/ghidra-hexagon-sleigh) | binary-analysis | relevance | missing_ai_keywords |
| [Chaoses-Ib/FormalLanguages](https://github.com/Chaoses-Ib/FormalLanguages) | binary-analysis | relevance | missing_ai_keywords |
| [Chaoses-Ib/FormalLanguages](https://github.com/Chaoses-Ib/FormalLanguages) | binary-analysis | relevance | missing_ai_keywords |
| [DynamoRIO/dynamorio](https://github.com/DynamoRIO/dynamorio) | binary-analysis | relevance | missing_ai_keywords |
| [HyperDbg/HyperDbg](https://github.com/HyperDbg/HyperDbg) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [KasperskyLab/hrtng](https://github.com/KasperskyLab/hrtng) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Morenoch26/OffsetInspect](https://github.com/Morenoch26/OffsetInspect) | binary-analysis | relevance | missing_ai_keywords |
| [Morenoch26/OffsetInspect](https://github.com/Morenoch26/OffsetInspect) | binary-analysis | relevance | missing_ai_keywords |
| [Morenoch26/OffsetInspect](https://github.com/Morenoch26/OffsetInspect) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Rych156/PEAnalyzer](https://github.com/Rych156/PEAnalyzer) | binary-analysis | relevance | missing_ai_keywords |
| [Rych156/PEAnalyzer](https://github.com/Rych156/PEAnalyzer) | binary-analysis | relevance | missing_ai_keywords |
| [Rych156/PEAnalyzer](https://github.com/Rych156/PEAnalyzer) | binary-analysis | relevance | missing_ai_keywords |
| [Rych156/PEAnalyzer](https://github.com/Rych156/PEAnalyzer) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [Vector35/binaryninja-api](https://github.com/Vector35/binaryninja-api) | binary-analysis | relevance | missing_ai_keywords |
| [Vector35/binaryninja-api](https://github.com/Vector35/binaryninja-api) | binary-analysis | relevance | missing_ai_keywords |
| [Yessi-cmd/spectra](https://github.com/Yessi-cmd/spectra) | binary-analysis | relevance | missing_ai_keywords |
| [Yessi-cmd/spectra](https://github.com/Yessi-cmd/spectra) | binary-analysis | relevance | missing_ai_keywords |
| [ZukiZero/udbg](https://github.com/ZukiZero/udbg) | binary-analysis | relevance | missing_ai_keywords |
| [ZukiZero/udbg](https://github.com/ZukiZero/udbg) | binary-analysis | relevance | missing_ai_keywords |
| [ZukiZero/udbg](https://github.com/ZukiZero/udbg) | binary-analysis | relevance | missing_ai_keywords |
| [ZukiZero/udbg](https://github.com/ZukiZero/udbg) | binary-analysis | relevance | missing_ai_keywords |
| [camilo123433/Dridex-Malware-Unpacking-Report](https://github.com/camilo123433/Dridex-Malware-Unpacking-Report) | binary-analysis | relevance | missing_ai_keywords |
| [e-m-b-a/emba](https://github.com/e-m-b-a/emba) | binary-analysis | relevance | missing_ai_keywords |
| [horsicq/DIE-engine](https://github.com/horsicq/DIE-engine) | binary-analysis | relevance | missing_ai_keywords |
| [horsicq/DIE-engine](https://github.com/horsicq/DIE-engine) | binary-analysis | relevance | missing_ai_keywords |
| [horsicq/DIE-engine](https://github.com/horsicq/DIE-engine) | binary-analysis | relevance | missing_ai_keywords |
| [horsicq/Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy) | binary-analysis | relevance | missing_ai_keywords |
| [horsicq/Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy) | binary-analysis | relevance | missing_ai_keywords |
| [kevinmuoz/pybinwalk](https://github.com/kevinmuoz/pybinwalk) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [lief-project/LIEF](https://github.com/lief-project/LIEF) | binary-analysis | relevance | missing_ai_keywords |
| [lifting-bits/sleigh](https://github.com/lifting-bits/sleigh) | binary-analysis | relevance | missing_ai_keywords |
| [mandiant/capa](https://github.com/mandiant/capa) | binary-analysis | relevance | missing_ai_keywords |
| [mandiant/capa](https://github.com/mandiant/capa) | binary-analysis | relevance | missing_ai_keywords |
| [packing-box/python-exeplot](https://github.com/packing-box/python-exeplot) | binary-analysis | relevance | missing_ai_keywords |
| [pumpkin-bit/EUVA-](https://github.com/pumpkin-bit/EUVA-) | binary-analysis | relevance | missing_ai_keywords |
| [radareorg/radare2](https://github.com/radareorg/radare2) | binary-analysis | relevance | missing_ai_keywords |
| [radareorg/radare2](https://github.com/radareorg/radare2) | binary-analysis | relevance | missing_ai_keywords |
| [radareorg/radare2](https://github.com/radareorg/radare2) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [thisarasewmina/DbgNexum](https://github.com/thisarasewmina/DbgNexum) | binary-analysis | relevance | missing_ai_keywords |
| [thisarasewmina/DbgNexum](https://github.com/thisarasewmina/DbgNexum) | binary-analysis | relevance | missing_ai_keywords |
| [thisarasewmina/DbgNexum](https://github.com/thisarasewmina/DbgNexum) | binary-analysis | relevance | missing_ai_keywords |
| [thisarasewmina/DbgNexum](https://github.com/thisarasewmina/DbgNexum) | binary-analysis | relevance | missing_ai_keywords |
| [thisarasewmina/DbgNexum](https://github.com/thisarasewmina/DbgNexum) | binary-analysis | relevance | missing_ai_keywords |
| [thisarasewmina/DbgNexum](https://github.com/thisarasewmina/DbgNexum) | binary-analysis | relevance | missing_ai_keywords |
| [thisarasewmina/DbgNexum](https://github.com/thisarasewmina/DbgNexum) | binary-analysis | relevance | missing_ai_keywords |
| [z0mb13w4r/objtools](https://github.com/z0mb13w4r/objtools) | binary-analysis | relevance | missing_ai_keywords |
| [z0mb13w4r/objtools](https://github.com/z0mb13w4r/objtools) | binary-analysis | relevance | missing_ai_keywords |
| [z0mb13w4r/objtools](https://github.com/z0mb13w4r/objtools) | binary-analysis | relevance | missing_ai_keywords |
| [DUVALL707/ExploitMaze](https://github.com/DUVALL707/ExploitMaze) | malware-analysis | applicability | Duplicate of Repository 1; lacks explicit mention of AI, automation, or fuzzing for offensive security. |
| [Jeremy344555/rat](https://github.com/Jeremy344555/rat) | malware-analysis | applicability | Repository mentions remote access, exploitation, and malware analysis, but there is no explicit mention of AI, automation, or fuzzing for offensive security. |
| [LagZeroCode/HackWire](https://github.com/LagZeroCode/HackWire) | malware-analysis | applicability | While the repository mentions offensive security topics, there is no explicit evidence of AI, automation, or fuzzing usage in the description or topics. |
| [Mr-Vitoo/lisa](https://github.com/Mr-Vitoo/lisa) | malware-analysis | applicability | Mentions malware-analysis and pwn, but project is for feature planning and interviews, not offensive security or automation for security. |
| [RealRGJ/cyber-training-resources](https://github.com/RealRGJ/cyber-training-resources) | malware-analysis | applicability | Focuses on cyber training resources and education, not on AI/automation/fuzzing for offensive security. |
| [Truong882/ReVex](https://github.com/Truong882/ReVex) | malware-analysis | applicability | While it mentions exploit-development and malware-analysis in topics, the description and content focus on a browser-based HTTP repeater for web security testing, with no explicit mention of AI, automation, or fuzzing. |
| [gaga84700/police](https://github.com/gaga84700/police) | malware-analysis | applicability | Uses AI for video analysis, but not in an offensive security context (no penetration testing, red teaming, or vulnerability/exploit focus). |
| [mrfeelssss/ObfuscationZone](https://github.com/mrfeelssss/ObfuscationZone) | malware-analysis | applicability | Focuses on code obfuscation and anti-debugging, which are relevant to security, but there is no explicit mention of AI, automation, or fuzzing being used for offensive security purposes. |
| [ocramtec-marco/suspicious](https://github.com/ocramtec-marco/suspicious) | malware-analysis | applicability | Mentions machine learning and malware analysis, but lacks explicit indication of offensive security automation or AI-driven offensive tooling. |
| [pedro00715/C3_CRT_Python](https://github.com/pedro00715/C3_CRT_Python) | malware-analysis | applicability | Mentions automation and some security topics, but no explicit mention of AI, ML, or fuzzing for offensive security. Description is vague about automation's role. |
| [penxpkj/Defensive-Security-Hub](https://github.com/penxpkj/Defensive-Security-Hub) | malware-analysis | applicability | The repository focuses on defensive security resources and lacks any mention of AI, automation, or fuzzing for offensive security. |
| [romeorone/ShellStrike](https://github.com/romeorone/ShellStrike) | malware-analysis | applicability | Focuses on shell scripting automation but lacks explicit offensive security automation or AI/ML context. |
| [timgerstel/suspicious_IPs](https://github.com/timgerstel/suspicious_IPs) | malware-analysis | applicability | While the repository involves malware analysis and penetration testing, it does not explicitly mention AI, automation, or fuzzing. |
| [zee839/APTBench](https://github.com/zee839/APTBench) | malware-analysis | applicability | Mentions LLMs and automation but focuses on software engineering and performance benchmarking, not offensive security or automated security testing. |
| [OnlyyxErika/Ciphey](https://github.com/OnlyyxErika/Ciphey) | malware-analysis | credibility | No stars and potentially a fork or duplicate; description is substantive but no community validation. |
| [gigachad80/Andro-Malstat-CLI](https://github.com/gigachad80/Andro-Malstat-CLI) | malware-analysis | credibility | No stars, but description is substantive and clear. Recently updated. No red flags for malicious intent. |
| [neelamkhalid/Ciphey](https://github.com/neelamkhalid/Ciphey) | malware-analysis | credibility | No stars and unclear maintenance, but description is substantive and relevant. |
| [Aayannaveed/GoVettersTools](https://github.com/Aayannaveed/GoVettersTools) | malware-analysis | relevance | missing_ai_keywords |
| [Abhishek-innovation/ShadowSploit](https://github.com/Abhishek-innovation/ShadowSploit) | malware-analysis | relevance | missing_ai_keywords |
| [Ahegaho/ExploitMaze](https://github.com/Ahegaho/ExploitMaze) | malware-analysis | relevance | missing_ai_keywords |
| [Ajoloid/cybersecurity-interview-boilerplate](https://github.com/Ajoloid/cybersecurity-interview-boilerplate) | malware-analysis | relevance | missing_ai_keywords |
| [Ajoloid/cybersecurity-interview-boilerplate](https://github.com/Ajoloid/cybersecurity-interview-boilerplate) | malware-analysis | relevance | missing_ai_keywords |
| [AleX-AA08/PhantomStego](https://github.com/AleX-AA08/PhantomStego) | malware-analysis | relevance | missing_ai_keywords |
| [Badasone/Cyberlivre](https://github.com/Badasone/Cyberlivre) | malware-analysis | relevance | missing_ai_keywords |
| [Badasone/Cyberlivre](https://github.com/Badasone/Cyberlivre) | malware-analysis | relevance | missing_ai_keywords |
| [CYB3RMX/Qu1cksc0pe](https://github.com/CYB3RMX/Qu1cksc0pe) | malware-analysis | relevance | missing_ai_keywords |
| [CYB3RMX/Qu1cksc0pe](https://github.com/CYB3RMX/Qu1cksc0pe) | malware-analysis | relevance | missing_ai_keywords |
| [Coursa4lyfe/NekoFlare](https://github.com/Coursa4lyfe/NekoFlare) | malware-analysis | relevance | missing_ai_keywords |
| [Coursa4lyfe/NekoFlare](https://github.com/Coursa4lyfe/NekoFlare) | malware-analysis | relevance | missing_ai_keywords |
| [Cvar1984/sussyfinder](https://github.com/Cvar1984/sussyfinder) | malware-analysis | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline](https://github.com/CybercentreCanada/assemblyline) | malware-analysis | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline-service-urldownloader](https://github.com/CybercentreCanada/assemblyline-service-urldownloader) | malware-analysis | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline-service-urldownloader](https://github.com/CybercentreCanada/assemblyline-service-urldownloader) | malware-analysis | relevance | missing_ai_keywords |
| [DeadFox55YZ/ShadowSploit](https://github.com/DeadFox55YZ/ShadowSploit) | malware-analysis | relevance | missing_ai_keywords |
| [Extenedi/DeleteShadowCopies](https://github.com/Extenedi/DeleteShadowCopies) | malware-analysis | relevance | missing_ai_keywords |
| [Extenedi/DeleteShadowCopies](https://github.com/Extenedi/DeleteShadowCopies) | malware-analysis | relevance | missing_ai_keywords |
| [Extenedi/DeleteShadowCopies](https://github.com/Extenedi/DeleteShadowCopies) | malware-analysis | relevance | missing_ai_keywords |
| [Extenedi/DeleteShadowCopies](https://github.com/Extenedi/DeleteShadowCopies) | malware-analysis | relevance | missing_ai_keywords |
| [Gobabi25/python-obfuscator-CalypsisOBF](https://github.com/Gobabi25/python-obfuscator-CalypsisOBF) | malware-analysis | relevance | missing_ai_keywords |
| [Gobabi25/python-obfuscator-CalypsisOBF](https://github.com/Gobabi25/python-obfuscator-CalypsisOBF) | malware-analysis | relevance | missing_ai_keywords |
| [Goldroger0262/PwnRM](https://github.com/Goldroger0262/PwnRM) | malware-analysis | relevance | missing_ai_keywords |
| [Jay-melly/NoBBomb](https://github.com/Jay-melly/NoBBomb) | malware-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | malware-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | malware-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | malware-analysis | relevance | missing_ai_keywords |
| [JerryJev1/image-malware-detection-model](https://github.com/JerryJev1/image-malware-detection-model) | malware-analysis | relevance | missing_ai_keywords |
| [JerryJev1/image-malware-detection-model](https://github.com/JerryJev1/image-malware-detection-model) | malware-analysis | relevance | missing_ai_keywords |
| [JerryLinLinLin/huorong-virdb-changelog](https://github.com/JerryLinLinLin/huorong-virdb-changelog) | malware-analysis | relevance | missing_ai_keywords |
| [Karthik-reddy6/aegistrace-threat-intelligence](https://github.com/Karthik-reddy6/aegistrace-threat-intelligence) | malware-analysis | relevance | missing_ai_keywords |
| [Karthik-reddy6/aegistrace-threat-intelligence](https://github.com/Karthik-reddy6/aegistrace-threat-intelligence) | malware-analysis | relevance | missing_ai_keywords |
| [KasunCSB/Live-Malware-DB](https://github.com/KasunCSB/Live-Malware-DB) | malware-analysis | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | malware-analysis | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | malware-analysis | relevance | missing_ai_keywords |
| [LFBaptista/IAmAntimalware](https://github.com/LFBaptista/IAmAntimalware) | malware-analysis | relevance | missing_ai_keywords |
| [LFBaptista/IAmAntimalware](https://github.com/LFBaptista/IAmAntimalware) | malware-analysis | relevance | missing_ai_keywords |
| [LadyPatricia/198macros-v1.4.0](https://github.com/LadyPatricia/198macros-v1.4.0) | malware-analysis | relevance | missing_ai_keywords |
| [LadyPatricia/198macros-v1.4.0](https://github.com/LadyPatricia/198macros-v1.4.0) | malware-analysis | relevance | missing_ai_keywords |
| [MARIAMSOFT/Bytecode-Truth-Not-Source](https://github.com/MARIAMSOFT/Bytecode-Truth-Not-Source) | malware-analysis | relevance | missing_ai_keywords |
| [Morenoch26/OffsetInspect](https://github.com/Morenoch26/OffsetInspect) | malware-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | malware-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | malware-analysis | relevance | missing_ai_keywords |
| [NishanthGSuryavamshi/thinksec](https://github.com/NishanthGSuryavamshi/thinksec) | malware-analysis | relevance | missing_ai_keywords |
| [Pareekshithmk/Anti-Sandbox](https://github.com/Pareekshithmk/Anti-Sandbox) | malware-analysis | relevance | missing_ai_keywords |
| [Prajwalgrathish/TotalOSINT](https://github.com/Prajwalgrathish/TotalOSINT) | malware-analysis | relevance | missing_ai_keywords |
| [Rohan17182004/SmrtiLog](https://github.com/Rohan17182004/SmrtiLog) | malware-analysis | relevance | missing_ai_keywords |
| [Rohan17182004/SmrtiLog](https://github.com/Rohan17182004/SmrtiLog) | malware-analysis | relevance | missing_ai_keywords |
| [Rych156/PEAnalyzer](https://github.com/Rych156/PEAnalyzer) | malware-analysis | relevance | missing_ai_keywords |
| [Soocile/ShadowStrike](https://github.com/Soocile/ShadowStrike) | malware-analysis | relevance | missing_ai_keywords |
| [Soocile/ShadowStrike](https://github.com/Soocile/ShadowStrike) | malware-analysis | relevance | missing_ai_keywords |
| [Threatwise/attack-rs](https://github.com/Threatwise/attack-rs) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | malware-analysis | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | malware-analysis | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | malware-analysis | relevance | missing_ai_keywords |
| [Wajihbawa/threat-intel-resources](https://github.com/Wajihbawa/threat-intel-resources) | malware-analysis | relevance | missing_ai_keywords |
| [WilliamLCardoso/ShellStrike](https://github.com/WilliamLCardoso/ShellStrike) | malware-analysis | relevance | missing_ai_keywords |
| [WilliamLCardoso/ShellStrike](https://github.com/WilliamLCardoso/ShellStrike) | malware-analysis | relevance | missing_ai_keywords |
| [anshlmalik/CustomC2ChannelTemplate](https://github.com/anshlmalik/CustomC2ChannelTemplate) | malware-analysis | relevance | missing_ai_keywords |
| [arieahXxshrek/secwexen.github.io](https://github.com/arieahXxshrek/secwexen.github.io) | malware-analysis | relevance | missing_ai_keywords |
| [awab208/CyberSecurity-Journey](https://github.com/awab208/CyberSecurity-Journey) | malware-analysis | relevance | missing_ai_keywords |
| [awab208/CyberSecurity-Journey](https://github.com/awab208/CyberSecurity-Journey) | malware-analysis | relevance | missing_ai_keywords |
| [binbi123/RedAudit-USB](https://github.com/binbi123/RedAudit-USB) | malware-analysis | relevance | missing_ai_keywords |
| [camilo123433/Dridex-Malware-Unpacking-Report](https://github.com/camilo123433/Dridex-Malware-Unpacking-Report) | malware-analysis | relevance | missing_ai_keywords |
| [dishantar/cybratix-extention](https://github.com/dishantar/cybratix-extention) | malware-analysis | relevance | missing_ai_keywords |
| [doniboyd/IOC-Checker-Pro](https://github.com/doniboyd/IOC-Checker-Pro) | malware-analysis | relevance | missing_ai_keywords |
| [enzoplaaygamemg12/gtfobinSUID](https://github.com/enzoplaaygamemg12/gtfobinSUID) | malware-analysis | relevance | missing_ai_keywords |
| [ferxxo2024/PenetrationSystem](https://github.com/ferxxo2024/PenetrationSystem) | malware-analysis | relevance | missing_ai_keywords |
| [ferxxo2024/PenetrationSystem](https://github.com/ferxxo2024/PenetrationSystem) | malware-analysis | relevance | missing_ai_keywords |
| [fhgggggggggggggggggggg/IntrudeLab](https://github.com/fhgggggggggggggggggggg/IntrudeLab) | malware-analysis | relevance | missing_ai_keywords |
| [gofokili/EDR-Freeze](https://github.com/gofokili/EDR-Freeze) | malware-analysis | relevance | missing_ai_keywords |
| [hiephoiga1166/MidnightRAT-Payload](https://github.com/hiephoiga1166/MidnightRAT-Payload) | malware-analysis | relevance | missing_ai_keywords |
| [hiephoiga1166/MidnightRAT-Payload](https://github.com/hiephoiga1166/MidnightRAT-Payload) | malware-analysis | relevance | missing_ai_keywords |
| [horsicq/Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy) | malware-analysis | relevance | missing_ai_keywords |
| [ibaneez/VirusTotalJsonDownloader](https://github.com/ibaneez/VirusTotalJsonDownloader) | malware-analysis | relevance | missing_ai_keywords |
| [ibaneez/VirusTotalJsonDownloader](https://github.com/ibaneez/VirusTotalJsonDownloader) | malware-analysis | relevance | missing_ai_keywords |
| [kal21k/HWBP-DEP-Bypass](https://github.com/kal21k/HWBP-DEP-Bypass) | malware-analysis | relevance | missing_ai_keywords |
| [kenttibusiness/scamnet](https://github.com/kenttibusiness/scamnet) | malware-analysis | relevance | missing_ai_keywords |
| [lukenixon8/CryptInject](https://github.com/lukenixon8/CryptInject) | malware-analysis | relevance | missing_ai_keywords |
| [malwaredb/malwaredb-rs](https://github.com/malwaredb/malwaredb-rs) | malware-analysis | relevance | missing_ai_keywords |
| [mreshuu/STForensicMacOS](https://github.com/mreshuu/STForensicMacOS) | malware-analysis | relevance | missing_ai_keywords |
| [mreshuu/STForensicMacOS](https://github.com/mreshuu/STForensicMacOS) | malware-analysis | relevance | missing_ai_keywords |
| [mreshuu/STForensicMacOS](https://github.com/mreshuu/STForensicMacOS) | malware-analysis | relevance | missing_ai_keywords |
| [mtysedke/security-incident-artifact-analyzer](https://github.com/mtysedke/security-incident-artifact-analyzer) | malware-analysis | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | malware-analysis | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | malware-analysis | relevance | missing_ai_keywords |
| [prateek123s/HWBP-DEP-Bypass](https://github.com/prateek123s/HWBP-DEP-Bypass) | malware-analysis | relevance | missing_ai_keywords |
| [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) | malware-analysis | relevance | missing_ai_keywords |
| [radareorg/radare2](https://github.com/radareorg/radare2) | malware-analysis | relevance | missing_ai_keywords |
| [reuteras/dfirws](https://github.com/reuteras/dfirws) | malware-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | malware-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | malware-analysis | relevance | missing_ai_keywords |
| [spontopt/StyxLoaderX-EDR-Evasion](https://github.com/spontopt/StyxLoaderX-EDR-Evasion) | malware-analysis | relevance | missing_ai_keywords |
| [spontopt/StyxLoaderX-EDR-Evasion](https://github.com/spontopt/StyxLoaderX-EDR-Evasion) | malware-analysis | relevance | missing_ai_keywords |
| [tabishcricketer/pe-signgen](https://github.com/tabishcricketer/pe-signgen) | malware-analysis | relevance | missing_ai_keywords |
| [tabishcricketer/pe-signgen](https://github.com/tabishcricketer/pe-signgen) | malware-analysis | relevance | missing_ai_keywords |
| [vmkspv/lenspect](https://github.com/vmkspv/lenspect) | malware-analysis | relevance | missing_ai_keywords |
| [KhonneyMann/nightops-drop](https://github.com/KhonneyMann/nightops-drop) | offensive-security | applicability | Describes red team payload delivery platform but no explicit mention of AI, automation, or fuzzing in description or topics. |
| [Leywkeny/WinNT-add-system-user-injector](https://github.com/Leywkeny/WinNT-add-system-user-injector) | offensive-security | applicability | Focuses on system administration and automation without offensive security context or AI usage. |
| [Maamitiana/cybersec-projects](https://github.com/Maamitiana/cybersec-projects) | offensive-security | applicability | Mentions automation scripts and AI in topics, but lacks explicit evidence that AI or automation is used for offensive security tasks (no details in description or topics). |
| [Quocton1/kali-linux-teaching-course-live](https://github.com/Quocton1/kali-linux-teaching-course-live) | offensive-security | applicability | While the repository covers penetration testing and mentions security automation, there is no explicit evidence of AI, automation, or fuzzing being used for offensive security in the description or topics. |
| [SanhitaVichare/temp-os](https://github.com/SanhitaVichare/temp-os) | offensive-security | applicability | Mentions offensive security topics but no evidence of AI, automation, or fuzzing for offensive security; focuses on Fedora installation. |
| [Sylphoraz/SharpAllowedToAct-Modify](https://github.com/Sylphoraz/SharpAllowedToAct-Modify) | offensive-security | applicability | Focuses on post-exploitation without mentioning AI, automation, or fuzzing. |
| [modifiable-japaneseiris792/r-shell](https://github.com/modifiable-japaneseiris792/r-shell) | offensive-security | applicability | Repository is focused on building an SSH client and reverse shells for remote management, with no mention of AI, automation, or fuzzing for offensive security. |
| [n3rada/toboggan](https://github.com/n3rada/toboggan) | offensive-security | applicability | Focuses on transforming RCE into shells for offensive security, but no mention of AI, automation, or fuzzing in description or topics. |
| [sairysee/aappmart](https://github.com/sairysee/aappmart) | offensive-security | applicability | Although the topics and description mention offensive security and AI/automation-related terms, there is no explicit evidence that the repository demonstrates the use of AI, automation, or fuzzing for offensive security. The description is focused on building an online marketplace. |
| [Froezens/Python-Blacklist-Breaker](https://github.com/Froezens/Python-Blacklist-Breaker) | offensive-security | credibility | No stars and no community validation; description is clear but repository is unvalidated and could be a toy project. |
| [ahmetdrak/drakben](https://github.com/ahmetdrak/drakben) | offensive-security | credibility | Very low star count (4) and future last update date suggest possible toy project or placeholder; otherwise, description is substantive. |
| [secwexen/aapp-mart](https://github.com/secwexen/aapp-mart) | offensive-security | credibility | Low stars count and outdated repository with last update in 2026, suggesting inactive maintenance. |
| [vukssan/KamelionStack-OSE](https://github.com/vukssan/KamelionStack-OSE) | offensive-security | credibility | No community validation (0 stars), but description and topics are substantive and clear. Recently updated, but lack of stars is a concern. |
| [0xsyr0/Awesome-Cybersecurity-Handbooks](https://github.com/0xsyr0/Awesome-Cybersecurity-Handbooks) | offensive-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | offensive-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | offensive-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | offensive-security | relevance | missing_ai_keywords |
| [Aviwe45/metasploit-for-beginners](https://github.com/Aviwe45/metasploit-for-beginners) | offensive-security | relevance | missing_ai_keywords |
| [Aviwe45/metasploit-for-beginners](https://github.com/Aviwe45/metasploit-for-beginners) | offensive-security | relevance | missing_ai_keywords |
| [Aviwe45/metasploit-for-beginners](https://github.com/Aviwe45/metasploit-for-beginners) | offensive-security | relevance | missing_ai_keywords |
| [Eabnfccblls/awesome-cybersecurity-tools](https://github.com/Eabnfccblls/awesome-cybersecurity-tools) | offensive-security | relevance | missing_ai_keywords |
| [Eabnfccblls/awesome-cybersecurity-tools](https://github.com/Eabnfccblls/awesome-cybersecurity-tools) | offensive-security | relevance | missing_ai_keywords |
| [Finnnwm/CloneX-Muck-security-testing-tool](https://github.com/Finnnwm/CloneX-Muck-security-testing-tool) | offensive-security | relevance | missing_ai_keywords |
| [Finnnwm/CloneX-Muck-security-testing-tool](https://github.com/Finnnwm/CloneX-Muck-security-testing-tool) | offensive-security | relevance | missing_ai_keywords |
| [Finnnwm/CloneX-Muck-security-testing-tool](https://github.com/Finnnwm/CloneX-Muck-security-testing-tool) | offensive-security | relevance | missing_ai_keywords |
| [Finnnwm/CloneX-Muck-security-testing-tool](https://github.com/Finnnwm/CloneX-Muck-security-testing-tool) | offensive-security | relevance | missing_ai_keywords |
| [Finnnwm/CloneX-Muck-security-testing-tool](https://github.com/Finnnwm/CloneX-Muck-security-testing-tool) | offensive-security | relevance | missing_ai_keywords |
| [Finnnwm/CloneX-Muck-security-testing-tool](https://github.com/Finnnwm/CloneX-Muck-security-testing-tool) | offensive-security | relevance | missing_ai_keywords |
| [Finnnwm/CloneX-Muck-security-testing-tool](https://github.com/Finnnwm/CloneX-Muck-security-testing-tool) | offensive-security | relevance | missing_ai_keywords |
| [FlameBudy/MSSQLServer-CLR-CommandKit](https://github.com/FlameBudy/MSSQLServer-CLR-CommandKit) | offensive-security | relevance | missing_ai_keywords |
| [FlameBudy/MSSQLServer-CLR-CommandKit](https://github.com/FlameBudy/MSSQLServer-CLR-CommandKit) | offensive-security | relevance | missing_ai_keywords |
| [FlameBudy/MSSQLServer-CLR-CommandKit](https://github.com/FlameBudy/MSSQLServer-CLR-CommandKit) | offensive-security | relevance | missing_ai_keywords |
| [FlameBudy/MSSQLServer-CLR-CommandKit](https://github.com/FlameBudy/MSSQLServer-CLR-CommandKit) | offensive-security | relevance | missing_ai_keywords |
| [FlameBudy/MSSQLServer-CLR-CommandKit](https://github.com/FlameBudy/MSSQLServer-CLR-CommandKit) | offensive-security | relevance | missing_ai_keywords |
| [FlameBudy/MSSQLServer-CLR-CommandKit](https://github.com/FlameBudy/MSSQLServer-CLR-CommandKit) | offensive-security | relevance | missing_ai_keywords |
| [FlameBudy/MSSQLServer-CLR-CommandKit](https://github.com/FlameBudy/MSSQLServer-CLR-CommandKit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [KvzinNcpx7/CVE-2025-9074_DAEMON_KILLER](https://github.com/KvzinNcpx7/CVE-2025-9074_DAEMON_KILLER) | offensive-security | relevance | missing_ai_keywords |
| [MaicolMoreno26/MemoryExec-Shellcode-Loader](https://github.com/MaicolMoreno26/MemoryExec-Shellcode-Loader) | offensive-security | relevance | missing_ai_keywords |
| [MiguelArmando/Bug-Bounty-Roadmap](https://github.com/MiguelArmando/Bug-Bounty-Roadmap) | offensive-security | relevance | missing_ai_keywords |
| [MiguelArmando/Bug-Bounty-Roadmap](https://github.com/MiguelArmando/Bug-Bounty-Roadmap) | offensive-security | relevance | missing_ai_keywords |
| [MiguelArmando/Bug-Bounty-Roadmap](https://github.com/MiguelArmando/Bug-Bounty-Roadmap) | offensive-security | relevance | missing_ai_keywords |
| [Morenoch26/OffsetInspect](https://github.com/Morenoch26/OffsetInspect) | offensive-security | relevance | missing_ai_keywords |
| [MuhammadSufyanSikander/emacs-tramp-rpc](https://github.com/MuhammadSufyanSikander/emacs-tramp-rpc) | offensive-security | relevance | missing_ai_keywords |
| [MuhammadSufyanSikander/emacs-tramp-rpc](https://github.com/MuhammadSufyanSikander/emacs-tramp-rpc) | offensive-security | relevance | missing_ai_keywords |
| [MuhammadSufyanSikander/emacs-tramp-rpc](https://github.com/MuhammadSufyanSikander/emacs-tramp-rpc) | offensive-security | relevance | missing_ai_keywords |
| [Ornateill/nightmare-exploit-roadmap](https://github.com/Ornateill/nightmare-exploit-roadmap) | offensive-security | relevance | missing_ai_keywords |
| [Rakum713/ColdWer](https://github.com/Rakum713/ColdWer) | offensive-security | relevance | missing_ai_keywords |
| [Rakum713/ColdWer](https://github.com/Rakum713/ColdWer) | offensive-security | relevance | missing_ai_keywords |
| [Rakum713/ColdWer](https://github.com/Rakum713/ColdWer) | offensive-security | relevance | missing_ai_keywords |
| [Ramborat1013/BreakerZero_PasswordCracker_v1.0](https://github.com/Ramborat1013/BreakerZero_PasswordCracker_v1.0) | offensive-security | relevance | missing_ai_keywords |
| [Ramborat1013/BreakerZero_PasswordCracker_v1.0](https://github.com/Ramborat1013/BreakerZero_PasswordCracker_v1.0) | offensive-security | relevance | missing_ai_keywords |
| [Relampag0/forensic-log-mcp](https://github.com/Relampag0/forensic-log-mcp) | offensive-security | relevance | missing_ai_keywords |
| [Trapsta1467/sherluck](https://github.com/Trapsta1467/sherluck) | offensive-security | relevance | missing_ai_keywords |
| [Trapsta1467/sherluck](https://github.com/Trapsta1467/sherluck) | offensive-security | relevance | missing_ai_keywords |
| [Trapsta1467/sherluck](https://github.com/Trapsta1467/sherluck) | offensive-security | relevance | missing_ai_keywords |
| [Trapsta1467/sherluck](https://github.com/Trapsta1467/sherluck) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Wanssss1/BOFs](https://github.com/Wanssss1/BOFs) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [aliwioiod/speedloader](https://github.com/aliwioiod/speedloader) | offensive-security | relevance | missing_ai_keywords |
| [aliwioiod/speedloader](https://github.com/aliwioiod/speedloader) | offensive-security | relevance | missing_ai_keywords |
| [aliwioiod/speedloader](https://github.com/aliwioiod/speedloader) | offensive-security | relevance | missing_ai_keywords |
| [aliwioiod/speedloader](https://github.com/aliwioiod/speedloader) | offensive-security | relevance | missing_ai_keywords |
| [anshlmalik/CustomC2ChannelTemplate](https://github.com/anshlmalik/CustomC2ChannelTemplate) | offensive-security | relevance | missing_ai_keywords |
| [arieahXxshrek/secwexen.github.io](https://github.com/arieahXxshrek/secwexen.github.io) | offensive-security | relevance | missing_ai_keywords |
| [beroboi/watchTowr-vs-Fortiweb-AuthBypass](https://github.com/beroboi/watchTowr-vs-Fortiweb-AuthBypass) | offensive-security | relevance | missing_ai_keywords |
| [edoardottt/secfiles](https://github.com/edoardottt/secfiles) | offensive-security | relevance | missing_ai_keywords |
| [enzoplaaygamemg12/gtfobinSUID](https://github.com/enzoplaaygamemg12/gtfobinSUID) | offensive-security | relevance | missing_ai_keywords |
| [enzoplaaygamemg12/gtfobinSUID](https://github.com/enzoplaaygamemg12/gtfobinSUID) | offensive-security | relevance | missing_ai_keywords |
| [halilkirazkaya/gecit](https://github.com/halilkirazkaya/gecit) | offensive-security | relevance | missing_ai_keywords |
| [halilkirazkaya/gecit](https://github.com/halilkirazkaya/gecit) | offensive-security | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | offensive-security | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | offensive-security | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | offensive-security | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | offensive-security | relevance | missing_ai_keywords |
| [lizxyyyc/sc-reentrancy-attack](https://github.com/lizxyyyc/sc-reentrancy-attack) | offensive-security | relevance | missing_ai_keywords |
| [nikamhritik/awesome-battery-data](https://github.com/nikamhritik/awesome-battery-data) | offensive-security | relevance | missing_ai_keywords |
| [pepitopere666/WireTapper](https://github.com/pepitopere666/WireTapper) | offensive-security | relevance | missing_ai_keywords |
| [pepitopere666/WireTapper](https://github.com/pepitopere666/WireTapper) | offensive-security | relevance | missing_ai_keywords |
| [pepitopere666/WireTapper](https://github.com/pepitopere666/WireTapper) | offensive-security | relevance | missing_ai_keywords |
| [praetorian-inc/brutus](https://github.com/praetorian-inc/brutus) | offensive-security | relevance | missing_ai_keywords |
| [praetorian-inc/brutus](https://github.com/praetorian-inc/brutus) | offensive-security | relevance | missing_ai_keywords |
| [thesp0nge/nightcrawler-mitm](https://github.com/thesp0nge/nightcrawler-mitm) | offensive-security | relevance | missing_ai_keywords |
| [unk9vvn/unk9vvn.github.io](https://github.com/unk9vvn/unk9vvn.github.io) | offensive-security | relevance | missing_ai_keywords |
| [vishalo7o1/chronix](https://github.com/vishalo7o1/chronix) | offensive-security | relevance | missing_ai_keywords |
| [vishalo7o1/chronix](https://github.com/vishalo7o1/chronix) | offensive-security | relevance | missing_ai_keywords |
| [vishalo7o1/chronix](https://github.com/vishalo7o1/chronix) | offensive-security | relevance | missing_ai_keywords |
| [voltsparx/NetLoader-X](https://github.com/voltsparx/NetLoader-X) | offensive-security | relevance | missing_ai_keywords |
| [voltsparx/NetLoader-X](https://github.com/voltsparx/NetLoader-X) | offensive-security | relevance | missing_ai_keywords |
| [voltsparx/mercury-framework](https://github.com/voltsparx/mercury-framework) | offensive-security | relevance | missing_ai_keywords |
| [xseduran/ofxpwn](https://github.com/xseduran/ofxpwn) | offensive-security | relevance | missing_ai_keywords |
| [Fishin09/GodzillaNodeJsPayload](https://github.com/Fishin09/GodzillaNodeJsPayload) | penetration-testing | applicability | Focuses on payload development for Godzilla platform but does not mention AI, automation, or fuzzing in the context of offensive security. |
| [Kasim200429/GoBypass403](https://github.com/Kasim200429/GoBypass403) | penetration-testing | applicability | The repository is a tool for bypassing 403 errors during penetration testing but does not demonstrate the use of AI, automation, or fuzzing. |
| [NINJA45FFS1/security-tools-hacking](https://github.com/NINJA45FFS1/security-tools-hacking) | penetration-testing | applicability | Manual penetration testing framework; no evidence of AI, automation, or fuzzing components. |
| [Nagaraju9550/CloudSEK-CTF-Writeup-2025](https://github.com/Nagaraju9550/CloudSEK-CTF-Writeup-2025) | penetration-testing | applicability | Repository is a collection of CTF writeups and does not provide any tools or automation related to offensive security or AI. |
| [Olivaire/Fscan-Output-POC-Parser](https://github.com/Olivaire/Fscan-Output-POC-Parser) | penetration-testing | applicability | Mentions automated vulnerability scanning, but no explicit indication of AI, ML, or advanced fuzzing techniques for offensive security. |
| [ParraX123/meta-ai-bug-bounty](https://github.com/ParraX123/meta-ai-bug-bounty) | penetration-testing | applicability | Focuses on bug bounty and vulnerability analysis in AI systems, but lacks explicit mention of automation, AI-driven tools, or fuzzing for offensive security. |
| [Quocton1/kali-linux-teaching-course-live](https://github.com/Quocton1/kali-linux-teaching-course-live) | penetration-testing | applicability | Duplicate of Repository 0. No explicit evidence of AI, automation, or fuzzing for offensive security. |
| [SafwanSaleem/Subdomain-port-scanner-passive](https://github.com/SafwanSaleem/Subdomain-port-scanner-passive) | penetration-testing | applicability | Focuses on passive reconnaissance without offensive security context or AI usage. |
| [VAZlabs/cyber-find](https://github.com/VAZlabs/cyber-find) | penetration-testing | applicability | OSINT tool for reconnaissance; no explicit mention of AI, automation, or fuzzing for offensive security. |
| [abhxhekrathore5/AI-Vibe-Check](https://github.com/abhxhekrathore5/AI-Vibe-Check) | penetration-testing | applicability | Focuses on AI for sentiment analysis and developer mood tracking, not offensive security or penetration testing automation. |
| [arqi-io/zphisher](https://github.com/arqi-io/zphisher) | penetration-testing | applicability | Automated phishing tool for security assessments, but no explicit mention of AI, ML, or fuzzing; only automation is present. |
| [bac0nnfires/wslkalisetup](https://github.com/bac0nnfires/wslkalisetup) | penetration-testing | applicability | Automates setup of Kali tools but does not mention AI, ML, or fuzzing; focuses on scripting and environment setup. |
| [belohilly/xssrecon](https://github.com/belohilly/xssrecon) | penetration-testing | applicability | Mentions automation for XSS scanning but no explicit evidence of AI, ML, or fuzzing; automation is limited to scripting, not advanced offensive security automation. |
| [dagule/blackarch-i3-kvm-setup](https://github.com/dagule/blackarch-i3-kvm-setup) | penetration-testing | applicability | Automates OS and environment setup for penetration testing, but does not automate offensive security tasks or use AI/fuzzing. |
| [elmahdy1986/RedTiger-Tools](https://github.com/elmahdy1986/RedTiger-Tools) | penetration-testing | applicability | Mentions automation and security topics, but description focuses on development workflow, not offensive security automation/AI/fuzzing. |
| [gubogushod/cyphisher](https://github.com/gubogushod/cyphisher) | penetration-testing | applicability | Framework for phishing awareness and education; no explicit mention of AI, automation, or fuzzing for offensive security. |
| [jimmyner009/Krafter](https://github.com/jimmyner009/Krafter) | penetration-testing | applicability | Mentions penetration testing and red teaming, but no explicit evidence of AI, automation, or fuzzing being used for offensive security in the description or topics. |
| [lurito3/NetShark](https://github.com/lurito3/NetShark) | penetration-testing | applicability | Describes a vulnerability scanner for penetration testing, but does not mention AI, ML, or fuzzing; automation is implied but not explicitly tied to offensive security via AI/fuzzing. |
| [melolixodocaralho/mercury-framework](https://github.com/melolixodocaralho/mercury-framework) | penetration-testing | applicability | Mentions penetration testing and machine learning, but lacks explicit evidence of AI, automation, or fuzzing being used for offensive security in the description or topics. |
| [modifiable-japaneseiris792/r-shell](https://github.com/modifiable-japaneseiris792/r-shell) | penetration-testing | applicability | Repository focuses on remote shell access and penetration testing but does not mention AI, automation, or fuzzing in its description or topics. |
| [mohamedelalfy27/argus](https://github.com/mohamedelalfy27/argus) | penetration-testing | applicability | Mentions penetration-testing and ethical-hacking, but the AI/automation component is about agent observability, not offensive security. No explicit evidence of AI/automation being used for offensive operations. |
| [romeorone/ShellStrike](https://github.com/romeorone/ShellStrike) | penetration-testing | applicability | General-purpose shell scripting toolkit; while it mentions automation and some security topics, it does not demonstrate AI, fuzzing, or offensive security automation. |
| [swathigoud/WhisperNet](https://github.com/swathigoud/WhisperNet) | penetration-testing | applicability | The repository is a password generator tool for penetration testing but does not mention AI, automation, or fuzzing explicitly. |
| [timgerstel/suspicious_IPs](https://github.com/timgerstel/suspicious_IPs) | penetration-testing | applicability | The repository focuses on collecting suspicious IPs from a honeypot but does not demonstrate the use of AI, automation, or fuzzing for offensive security. |
| [usa2692/noemvex-wayback](https://github.com/usa2692/noemvex-wayback) | penetration-testing | applicability | Focuses on passive subdomain enumeration and file discovery, with no mention of AI, automation, or fuzzing in the context of offensive security. |
| [venom4044/Web-Vulnerability-Attack-Defense-and-Patch-Experimentation-on-the-RailsGoat-Application](https://github.com/venom4044/Web-Vulnerability-Attack-Defense-and-Patch-Experimentation-on-the-RailsGoat-Application) | penetration-testing | applicability | Focuses on manual vulnerability reproduction and patching; no mention of AI, automation, or fuzzing. |
| [Wyllkirby/SimPhish](https://github.com/Wyllkirby/SimPhish) | penetration-testing | credibility | No stars, no community validation, and the description is somewhat vague about the actual AI/automation implementation. |
| [ryzecx/vulscanner](https://github.com/ryzecx/vulscanner) | penetration-testing | credibility | Very low stars and new project, but description is clear and relevant; no obvious red flags. |
| [vukssan/KamelionStack-OSE](https://github.com/vukssan/KamelionStack-OSE) | penetration-testing | credibility | No community validation (0 stars), but description and topics are substantive and clear. Recently updated, but lack of stars is a concern. |
| [zee839/APTBench](https://github.com/zee839/APTBench) | penetration-testing | credibility | Recently updated but has only 1 star and limited community validation. The description is somewhat clear but lacks detail about implementation. |
| [Abhishek-innovation/ShadowSploit](https://github.com/Abhishek-innovation/ShadowSploit) | penetration-testing | relevance | missing_ai_keywords |
| [Ajoloid/cybersecurity-interview-boilerplate](https://github.com/Ajoloid/cybersecurity-interview-boilerplate) | penetration-testing | relevance | missing_ai_keywords |
| [Alakaroud/vuln-structure](https://github.com/Alakaroud/vuln-structure) | penetration-testing | relevance | missing_ai_keywords |
| [Ancescride/Ethical-Hacking-College_Project](https://github.com/Ancescride/Ethical-Hacking-College_Project) | penetration-testing | relevance | missing_ai_keywords |
| [Ancescride/Ethical-Hacking-College_Project](https://github.com/Ancescride/Ethical-Hacking-College_Project) | penetration-testing | relevance | missing_ai_keywords |
| [Asder10/React2Shell](https://github.com/Asder10/React2Shell) | penetration-testing | relevance | missing_ai_keywords |
| [Bienfait-Mutunzi/Awesome-Hacking-Learning-Path](https://github.com/Bienfait-Mutunzi/Awesome-Hacking-Learning-Path) | penetration-testing | relevance | missing_ai_keywords |
| [Bienfait-Mutunzi/Awesome-Hacking-Learning-Path](https://github.com/Bienfait-Mutunzi/Awesome-Hacking-Learning-Path) | penetration-testing | relevance | missing_ai_keywords |
| [Cauan00O1/ADBCommandCenter](https://github.com/Cauan00O1/ADBCommandCenter) | penetration-testing | relevance | missing_ai_keywords |
| [Chrimak/AD-Privilege-Escalation-Finder](https://github.com/Chrimak/AD-Privilege-Escalation-Finder) | penetration-testing | relevance | missing_ai_keywords |
| [DEVayman20/firewall-whitelist-admin](https://github.com/DEVayman20/firewall-whitelist-admin) | penetration-testing | relevance | missing_ai_keywords |
| [DEVayman20/firewall-whitelist-admin](https://github.com/DEVayman20/firewall-whitelist-admin) | penetration-testing | relevance | missing_ai_keywords |
| [DaveBNU/cortexai](https://github.com/DaveBNU/cortexai) | penetration-testing | relevance | missing_ai_keywords |
| [DeadFox55YZ/ShadowSploit](https://github.com/DeadFox55YZ/ShadowSploit) | penetration-testing | relevance | missing_ai_keywords |
| [DrippieduckYT/Aegis_Interceptor](https://github.com/DrippieduckYT/Aegis_Interceptor) | penetration-testing | relevance | missing_ai_keywords |
| [Eunsei677383/Free-Passive](https://github.com/Eunsei677383/Free-Passive) | penetration-testing | relevance | missing_ai_keywords |
| [Eunsei677383/Free-Passive](https://github.com/Eunsei677383/Free-Passive) | penetration-testing | relevance | missing_ai_keywords |
| [FaresArgus/artaxerxes](https://github.com/FaresArgus/artaxerxes) | penetration-testing | relevance | missing_ai_keywords |
| [Giufenix/ChicomaloTools](https://github.com/Giufenix/ChicomaloTools) | penetration-testing | relevance | missing_ai_keywords |
| [Icy-Senpal/bypass-all](https://github.com/Icy-Senpal/bypass-all) | penetration-testing | relevance | missing_ai_keywords |
| [Icy-Senpal/bypass-all](https://github.com/Icy-Senpal/bypass-all) | penetration-testing | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | penetration-testing | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | penetration-testing | relevance | missing_ai_keywords |
| [LordBooming/Smart-Access-Control-Auditor](https://github.com/LordBooming/Smart-Access-Control-Auditor) | penetration-testing | relevance | missing_ai_keywords |
| [MitaTuppeu/NeonFlux](https://github.com/MitaTuppeu/NeonFlux) | penetration-testing | relevance | missing_ai_keywords |
| [Nerowmist/nullsec-flipper-suite](https://github.com/Nerowmist/nullsec-flipper-suite) | penetration-testing | relevance | missing_ai_keywords |
| [OWASP/wstg](https://github.com/OWASP/wstg) | penetration-testing | relevance | missing_ai_keywords |
| [Oluwanifemithe/ctf-writeups](https://github.com/Oluwanifemithe/ctf-writeups) | penetration-testing | relevance | missing_ai_keywords |
| [Oz134/perishable-inventory-risk-engine](https://github.com/Oz134/perishable-inventory-risk-engine) | penetration-testing | relevance | missing_ai_keywords |
| [RoshanBetediya/minecraft-account-checker](https://github.com/RoshanBetediya/minecraft-account-checker) | penetration-testing | relevance | missing_ai_keywords |
| [TahaGameDev/Offensive-Security-Forensics-Portfolio](https://github.com/TahaGameDev/Offensive-Security-Forensics-Portfolio) | penetration-testing | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | penetration-testing | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | penetration-testing | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | penetration-testing | relevance | missing_ai_keywords |
| [Vectoricks/RDP-Forensic](https://github.com/Vectoricks/RDP-Forensic) | penetration-testing | relevance | missing_ai_keywords |
| [WilliamLCardoso/ShellStrike](https://github.com/WilliamLCardoso/ShellStrike) | penetration-testing | relevance | missing_ai_keywords |
| [Yaxiswagonwheel794/AbyssForge](https://github.com/Yaxiswagonwheel794/AbyssForge) | penetration-testing | relevance | missing_ai_keywords |
| [Yudissaputra160905/Kaneki-DDoS](https://github.com/Yudissaputra160905/Kaneki-DDoS) | penetration-testing | relevance | missing_ai_keywords |
| [YuriPeixoto25/portpilot](https://github.com/YuriPeixoto25/portpilot) | penetration-testing | relevance | missing_ai_keywords |
| [aaryan-1112/SQLMap-Inject-Suite-Pro](https://github.com/aaryan-1112/SQLMap-Inject-Suite-Pro) | penetration-testing | relevance | missing_ai_keywords |
| [abbassFarhat/hacker101-CTF-Solutions](https://github.com/abbassFarhat/hacker101-CTF-Solutions) | penetration-testing | relevance | missing_ai_keywords |
| [ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors](https://github.com/ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors) | penetration-testing | relevance | missing_ai_keywords |
| [aiatagramkonnect/hacker101-CTF-Solutions](https://github.com/aiatagramkonnect/hacker101-CTF-Solutions) | penetration-testing | relevance | missing_ai_keywords |
| [aiatagramkonnect/hacker101-CTF-Solutions](https://github.com/aiatagramkonnect/hacker101-CTF-Solutions) | penetration-testing | relevance | missing_ai_keywords |
| [aidenateagain/ghostscan](https://github.com/aidenateagain/ghostscan) | penetration-testing | relevance | missing_ai_keywords |
| [arieahXxshrek/secwexen.github.io](https://github.com/arieahXxshrek/secwexen.github.io) | penetration-testing | relevance | missing_ai_keywords |
| [awab208/CyberSecurity-Journey](https://github.com/awab208/CyberSecurity-Journey) | penetration-testing | relevance | missing_ai_keywords |
| [carolinavigil/prickly](https://github.com/carolinavigil/prickly) | penetration-testing | relevance | missing_ai_keywords |
| [dedsec1121fk/DedSec](https://github.com/dedsec1121fk/DedSec) | penetration-testing | relevance | missing_ai_keywords |
| [ferxxo2024/PenetrationSystem](https://github.com/ferxxo2024/PenetrationSystem) | penetration-testing | relevance | missing_ai_keywords |
| [fhgggggggggggggggggggg/IntrudeLab](https://github.com/fhgggggggggggggggggggg/IntrudeLab) | penetration-testing | relevance | missing_ai_keywords |
| [grild/pa_task](https://github.com/grild/pa_task) | penetration-testing | relevance | missing_ai_keywords |
| [hanyshehata1510/RoboBack](https://github.com/hanyshehata1510/RoboBack) | penetration-testing | relevance | missing_ai_keywords |
| [huymini/pencall](https://github.com/huymini/pencall) | penetration-testing | relevance | missing_ai_keywords |
| [huymini/pencall](https://github.com/huymini/pencall) | penetration-testing | relevance | missing_ai_keywords |
| [ivantaktos/Secure-Port-Redirector](https://github.com/ivantaktos/Secure-Port-Redirector) | penetration-testing | relevance | missing_ai_keywords |
| [javidahmed64592/cyber-query-ai](https://github.com/javidahmed64592/cyber-query-ai) | penetration-testing | relevance | missing_ai_keywords |
| [jinsolkr/Ethical-Hacking-Course-Resources](https://github.com/jinsolkr/Ethical-Hacking-Course-Resources) | penetration-testing | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | penetration-testing | relevance | missing_ai_keywords |
| [kal21k/HWBP-DEP-Bypass](https://github.com/kal21k/HWBP-DEP-Bypass) | penetration-testing | relevance | missing_ai_keywords |
| [landoalva/jira-servicedesk-enum](https://github.com/landoalva/jira-servicedesk-enum) | penetration-testing | relevance | missing_ai_keywords |
| [landoalva/jira-servicedesk-enum](https://github.com/landoalva/jira-servicedesk-enum) | penetration-testing | relevance | missing_ai_keywords |
| [madarauchiha45/Nmap-Security-Scanner-2025](https://github.com/madarauchiha45/Nmap-Security-Scanner-2025) | penetration-testing | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | penetration-testing | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | penetration-testing | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | penetration-testing | relevance | missing_ai_keywords |
| [moikakd/Camphish-pro](https://github.com/moikakd/Camphish-pro) | penetration-testing | relevance | missing_ai_keywords |
| [niago1967/ExploitHawk](https://github.com/niago1967/ExploitHawk) | penetration-testing | relevance | missing_ai_keywords |
| [niago1967/ExploitHawk](https://github.com/niago1967/ExploitHawk) | penetration-testing | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | penetration-testing | relevance | missing_ai_keywords |
| [pbarucco/Wayback-Recon](https://github.com/pbarucco/Wayback-Recon) | penetration-testing | relevance | missing_ai_keywords |
| [pedrocruz2202/mongobleed-scanner](https://github.com/pedrocruz2202/mongobleed-scanner) | penetration-testing | relevance | missing_ai_keywords |
| [phiduong1230/kali-setup](https://github.com/phiduong1230/kali-setup) | penetration-testing | relevance | missing_ai_keywords |
| [pigeon-wings/Port-Phantom](https://github.com/pigeon-wings/Port-Phantom) | penetration-testing | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | penetration-testing | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | penetration-testing | relevance | missing_ai_keywords |
| [prateek123s/HWBP-DEP-Bypass](https://github.com/prateek123s/HWBP-DEP-Bypass) | penetration-testing | relevance | missing_ai_keywords |
| [r0zhh/ASNHunter](https://github.com/r0zhh/ASNHunter) | penetration-testing | relevance | missing_ai_keywords |
| [rix4uni/medium-writeups](https://github.com/rix4uni/medium-writeups) | penetration-testing | relevance | missing_ai_keywords |
| [rix4uni/medium-writeups](https://github.com/rix4uni/medium-writeups) | penetration-testing | relevance | missing_ai_keywords |
| [rix4uni/medium-writeups](https://github.com/rix4uni/medium-writeups) | penetration-testing | relevance | missing_ai_keywords |
| [rix4uni/resolvers](https://github.com/rix4uni/resolvers) | penetration-testing | relevance | missing_ai_keywords |
| [rix4uni/resolvers](https://github.com/rix4uni/resolvers) | penetration-testing | relevance | missing_ai_keywords |
| [rix4uni/resolvers](https://github.com/rix4uni/resolvers) | penetration-testing | relevance | missing_ai_keywords |
| [sakthivel10q/CVE-2025-14847](https://github.com/sakthivel10q/CVE-2025-14847) | penetration-testing | relevance | missing_ai_keywords |
| [setyanoegraha/hackmyvm-writeups](https://github.com/setyanoegraha/hackmyvm-writeups) | penetration-testing | relevance | missing_ai_keywords |
| [spontopt/StyxLoaderX-EDR-Evasion](https://github.com/spontopt/StyxLoaderX-EDR-Evasion) | penetration-testing | relevance | missing_ai_keywords |
| [tushuuu01/Inventory](https://github.com/tushuuu01/Inventory) | penetration-testing | relevance | missing_ai_keywords |
| [tushuuu01/Inventory](https://github.com/tushuuu01/Inventory) | penetration-testing | relevance | missing_ai_keywords |
| [viaC5real/ParamX](https://github.com/viaC5real/ParamX) | penetration-testing | relevance | missing_ai_keywords |
| [Bossthetigan/NOLO](https://github.com/Bossthetigan/NOLO) | red-team | applicability | The repository focuses on AI-powered PTZ tracking using YOLO but does not relate to offensive security or automation for security testing. |
| [KhonneyMann/nightops-drop](https://github.com/KhonneyMann/nightops-drop) | red-team | applicability | Focuses on payload delivery and red team operations, but lacks explicit mention of AI, automation, or fuzzing in description or topics. |
| [LagZeroCode/HackWire](https://github.com/LagZeroCode/HackWire) | red-team | applicability | Mentions offensive security topics but no explicit mention of AI, automation, or fuzzing in the description or topics. |
| [MASHJJS/aTerm](https://github.com/MASHJJS/aTerm) | red-team | applicability | Mentions AI tools and red-team in topics, but the description and topics indicate a general-purpose developer terminal workspace, not an offensive security tool using AI/automation. |
| [Moayd307/superpoweredcv](https://github.com/Moayd307/superpoweredcv) | red-team | applicability | Mentions red-team and AI, but context is job application tooling and prompt engineering, not offensive security automation or AI-powered security testing. |
| [OPBOY1203/redmind](https://github.com/OPBOY1203/redmind) | red-team | applicability | Mentions offensive security and machine learning, but no explicit evidence that AI/ML is used for offensive operations or automation; appears to be a collection of resources. |
| [Quocton1/kali-linux-teaching-course-live](https://github.com/Quocton1/kali-linux-teaching-course-live) | red-team | applicability | Focuses on teaching penetration testing and security automation but does not explicitly mention AI, ML, or fuzzing for offensive security. |
| [Teddiesarcosomal392/eye](https://github.com/Teddiesarcosomal392/eye) | red-team | applicability | Mentions AI models and red-team in topics, but the description and topics focus on memory preservation and conversations, not offensive security or automation/fuzzing. |
| [Zain3311/CVE-2025-49844](https://github.com/Zain3311/CVE-2025-49844) | red-team | applicability | Exploit repository for a CVE with AI/ML topics, but no explicit evidence of AI, automation, or fuzzing being used in the exploit or tooling. |
| [david3c2004/CLR-Unhook](https://github.com/david3c2004/CLR-Unhook) | red-team | applicability | Repository is related to bypassing EDR/AV for red team/offensive security, but there is no explicit mention of AI, automation, or fuzzing in its description or topics. |
| [gubogushod/cyphisher](https://github.com/gubogushod/cyphisher) | red-team | applicability | Duplicate of Repository 2; no explicit AI, automation, or fuzzing for offensive security. |
| [loaiasd/redspecter-ai-usage-watchdog](https://github.com/loaiasd/redspecter-ai-usage-watchdog) | red-team | applicability | Repository is related to monitoring AI usage for security, but it is focused on blue team/monitoring/defensive security, not offensive security or automation of offensive tasks. |
| [rabeal21/Tea](https://github.com/rabeal21/Tea) | red-team | applicability | The repository focuses on generating TEA wallet addresses and does not explicitly mention AI, automation, or fuzzing for offensive security. |
| [usa2692/noemvex-wayback](https://github.com/usa2692/noemvex-wayback) | red-team | applicability | Duplicate of Repository 2. Focuses on passive enumeration and file discovery, with no explicit AI, automation, or fuzzing for offensive security. |
| [v2lurpin/portscan-vulnerabilidades](https://github.com/v2lurpin/portscan-vulnerabilidades) | red-team | applicability | Mentions automation and vulnerability scanning for pentesting, but lacks explicit evidence of AI, advanced automation, or fuzzing in description or topics. |
| [ahmetdrak/drakben](https://github.com/ahmetdrak/drakben) | red-team | credibility | Very low star count (4) despite ambitious claims; possible toy project or early stage. However, recently updated and description is clear. |
| [Ahirshath/nmap-cheatsheet-tr](https://github.com/Ahirshath/nmap-cheatsheet-tr) | red-team | relevance | missing_ai_keywords |
| [Ahirshath/nmap-cheatsheet-tr](https://github.com/Ahirshath/nmap-cheatsheet-tr) | red-team | relevance | missing_ai_keywords |
| [Akunpubg9236/proyecto_AICAD_JPereira](https://github.com/Akunpubg9236/proyecto_AICAD_JPereira) | red-team | relevance | missing_ai_keywords |
| [AlejandroZaZ/cybersecurity-tools](https://github.com/AlejandroZaZ/cybersecurity-tools) | red-team | relevance | missing_ai_keywords |
| [AlejandroZaZ/cybersecurity-tools](https://github.com/AlejandroZaZ/cybersecurity-tools) | red-team | relevance | missing_ai_keywords |
| [Astrosp/Awesome-OSINT-For-Everything](https://github.com/Astrosp/Awesome-OSINT-For-Everything) | red-team | relevance | missing_ai_keywords |
| [BishopFox/sliver](https://github.com/BishopFox/sliver) | red-team | relevance | missing_ai_keywords |
| [BlackArch/blackarch](https://github.com/BlackArch/blackarch) | red-team | relevance | missing_ai_keywords |
| [Calla-DZ/Applied-Cybersecurity-Incident-Response-Web-Attacks-and-Secure-System-Design](https://github.com/Calla-DZ/Applied-Cybersecurity-Incident-Response-Web-Attacks-and-Secure-System-Design) | red-team | relevance | missing_ai_keywords |
| [DEVayman20/firewall-whitelist-admin](https://github.com/DEVayman20/firewall-whitelist-admin) | red-team | relevance | missing_ai_keywords |
| [DEVayman20/firewall-whitelist-admin](https://github.com/DEVayman20/firewall-whitelist-admin) | red-team | relevance | missing_ai_keywords |
| [DeepZatakiya/OpenMalleableC2](https://github.com/DeepZatakiya/OpenMalleableC2) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | red-team | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | red-team | relevance | missing_ai_keywords |
| [KvzinNcpx7/CVE-2025-9074_DAEMON_KILLER](https://github.com/KvzinNcpx7/CVE-2025-9074_DAEMON_KILLER) | red-team | relevance | missing_ai_keywords |
| [MahinTanzimSami/advanced-nmap-cli](https://github.com/MahinTanzimSami/advanced-nmap-cli) | red-team | relevance | missing_ai_keywords |
| [Mazzy-Stars/lain_c2](https://github.com/Mazzy-Stars/lain_c2) | red-team | relevance | missing_ai_keywords |
| [Mazzy-Stars/lain_c2](https://github.com/Mazzy-Stars/lain_c2) | red-team | relevance | missing_ai_keywords |
| [Mazzy-Stars/lain_c2](https://github.com/Mazzy-Stars/lain_c2) | red-team | relevance | missing_ai_keywords |
| [Michael1-dav/red-teaming](https://github.com/Michael1-dav/red-teaming) | red-team | relevance | missing_ai_keywords |
| [Michael1-dav/red-teaming](https://github.com/Michael1-dav/red-teaming) | red-team | relevance | missing_ai_keywords |
| [Michael1-dav/red-teaming](https://github.com/Michael1-dav/red-teaming) | red-team | relevance | missing_ai_keywords |
| [Nerowmist/nullsec-flipper-suite](https://github.com/Nerowmist/nullsec-flipper-suite) | red-team | relevance | missing_ai_keywords |
| [Nerowmist/nullsec-flipper-suite](https://github.com/Nerowmist/nullsec-flipper-suite) | red-team | relevance | missing_ai_keywords |
| [Nikopmpm/Fsociety-CVE-2024-0670-CheckMK-LPE](https://github.com/Nikopmpm/Fsociety-CVE-2024-0670-CheckMK-LPE) | red-team | relevance | missing_ai_keywords |
| [Rakum713/ColdWer](https://github.com/Rakum713/ColdWer) | red-team | relevance | missing_ai_keywords |
| [Rakum713/ColdWer](https://github.com/Rakum713/ColdWer) | red-team | relevance | missing_ai_keywords |
| [Ramborat1013/BreakerZero_PasswordCracker_v1.0](https://github.com/Ramborat1013/BreakerZero_PasswordCracker_v1.0) | red-team | relevance | missing_ai_keywords |
| [Renpapi/n8n-workflows](https://github.com/Renpapi/n8n-workflows) | red-team | relevance | missing_ai_keywords |
| [Rizwan723/MCP-Security-Proxy](https://github.com/Rizwan723/MCP-Security-Proxy) | red-team | relevance | missing_ai_keywords |
| [Wanssss1/BOFs](https://github.com/Wanssss1/BOFs) | red-team | relevance | missing_ai_keywords |
| [ZayaCrypt/memtap](https://github.com/ZayaCrypt/memtap) | red-team | relevance | missing_ai_keywords |
| [abckit0324-crypto/Paper_Agg](https://github.com/abckit0324-crypto/Paper_Agg) | red-team | relevance | missing_ai_keywords |
| [ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors](https://github.com/ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors) | red-team | relevance | missing_ai_keywords |
| [ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors](https://github.com/ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors) | red-team | relevance | missing_ai_keywords |
| [aidenateagain/ghostscan](https://github.com/aidenateagain/ghostscan) | red-team | relevance | missing_ai_keywords |
| [aidenateagain/ghostscan](https://github.com/aidenateagain/ghostscan) | red-team | relevance | missing_ai_keywords |
| [ali-ctf-player/HTB-reports](https://github.com/ali-ctf-player/HTB-reports) | red-team | relevance | missing_ai_keywords |
| [arieahXxshrek/secwexen.github.io](https://github.com/arieahXxshrek/secwexen.github.io) | red-team | relevance | missing_ai_keywords |
| [atulranjanz/Swatted-Webhook-Spammer](https://github.com/atulranjanz/Swatted-Webhook-Spammer) | red-team | relevance | missing_ai_keywords |
| [atulranjanz/Swatted-Webhook-Spammer](https://github.com/atulranjanz/Swatted-Webhook-Spammer) | red-team | relevance | missing_ai_keywords |
| [chrisgallenx/Interactive-MITRE-Tree](https://github.com/chrisgallenx/Interactive-MITRE-Tree) | red-team | relevance | missing_ai_keywords |
| [chrisgallenx/Interactive-MITRE-Tree](https://github.com/chrisgallenx/Interactive-MITRE-Tree) | red-team | relevance | missing_ai_keywords |
| [chrisgallenx/Interactive-MITRE-Tree](https://github.com/chrisgallenx/Interactive-MITRE-Tree) | red-team | relevance | missing_ai_keywords |
| [chrismmt/mcp-adversarial-suite](https://github.com/chrismmt/mcp-adversarial-suite) | red-team | relevance | missing_ai_keywords |
| [ferxxo2024/PenetrationSystem](https://github.com/ferxxo2024/PenetrationSystem) | red-team | relevance | missing_ai_keywords |
| [ferxxo2024/PenetrationSystem](https://github.com/ferxxo2024/PenetrationSystem) | red-team | relevance | missing_ai_keywords |
| [fhgggggggggggggggggggg/IntrudeLab](https://github.com/fhgggggggggggggggggggg/IntrudeLab) | red-team | relevance | missing_ai_keywords |
| [fhgggggggggggggggggggg/IntrudeLab](https://github.com/fhgggggggggggggggggggg/IntrudeLab) | red-team | relevance | missing_ai_keywords |
| [harshit86198800/SecureShell-Pro](https://github.com/harshit86198800/SecureShell-Pro) | red-team | relevance | missing_ai_keywords |
| [harshit86198800/SecureShell-Pro](https://github.com/harshit86198800/SecureShell-Pro) | red-team | relevance | missing_ai_keywords |
| [hiephoiga1166/MidnightRAT-Payload](https://github.com/hiephoiga1166/MidnightRAT-Payload) | red-team | relevance | missing_ai_keywords |
| [hiephoiga1166/MidnightRAT-Payload](https://github.com/hiephoiga1166/MidnightRAT-Payload) | red-team | relevance | missing_ai_keywords |
| [huymini/pencall](https://github.com/huymini/pencall) | red-team | relevance | missing_ai_keywords |
| [huymini/pencall](https://github.com/huymini/pencall) | red-team | relevance | missing_ai_keywords |
| [huymini/pencall](https://github.com/huymini/pencall) | red-team | relevance | missing_ai_keywords |
| [huymini/pencall](https://github.com/huymini/pencall) | red-team | relevance | missing_ai_keywords |
| [javidahmed64592/cyber-query-ai](https://github.com/javidahmed64592/cyber-query-ai) | red-team | relevance | missing_ai_keywords |
| [jenkinsmichpa/coconut_crab](https://github.com/jenkinsmichpa/coconut_crab) | red-team | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | red-team | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | red-team | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | red-team | relevance | missing_ai_keywords |
| [kemalyaa/webinar-session-jwt](https://github.com/kemalyaa/webinar-session-jwt) | red-team | relevance | missing_ai_keywords |
| [kronossphpp/Hardcoded-Token-Hunter](https://github.com/kronossphpp/Hardcoded-Token-Hunter) | red-team | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | red-team | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | red-team | relevance | missing_ai_keywords |
| [luq12-growagarden/Adversarial-Detection-Engineering-Framework](https://github.com/luq12-growagarden/Adversarial-Detection-Engineering-Framework) | red-team | relevance | missing_ai_keywords |
| [luq12-growagarden/Adversarial-Detection-Engineering-Framework](https://github.com/luq12-growagarden/Adversarial-Detection-Engineering-Framework) | red-team | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | red-team | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | red-team | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | red-team | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | red-team | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | red-team | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | red-team | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | red-team | relevance | missing_ai_keywords |
| [nupurgurnule/GoldMAC](https://github.com/nupurgurnule/GoldMAC) | red-team | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | red-team | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | red-team | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | red-team | relevance | missing_ai_keywords |
| [pedrocruz2202/mongobleed-scanner](https://github.com/pedrocruz2202/mongobleed-scanner) | red-team | relevance | missing_ai_keywords |
| [pepitopere666/WireTapper](https://github.com/pepitopere666/WireTapper) | red-team | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | red-team | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | red-team | relevance | missing_ai_keywords |
| [praetorian-inc/brutus](https://github.com/praetorian-inc/brutus) | red-team | relevance | missing_ai_keywords |
| [r0zhh/ASNHunter](https://github.com/r0zhh/ASNHunter) | red-team | relevance | missing_ai_keywords |
| [r0zhh/ASNHunter](https://github.com/r0zhh/ASNHunter) | red-team | relevance | missing_ai_keywords |
| [r0zhh/ASNHunter](https://github.com/r0zhh/ASNHunter) | red-team | relevance | missing_ai_keywords |
| [sakthivel10q/CVE-2025-14847](https://github.com/sakthivel10q/CVE-2025-14847) | red-team | relevance | missing_ai_keywords |
| [simar100/mft_reader](https://github.com/simar100/mft_reader) | red-team | relevance | missing_ai_keywords |
| [simar100/mft_reader](https://github.com/simar100/mft_reader) | red-team | relevance | missing_ai_keywords |
| [simar100/mft_reader](https://github.com/simar100/mft_reader) | red-team | relevance | missing_ai_keywords |
| [spontopt/StyxLoaderX-EDR-Evasion](https://github.com/spontopt/StyxLoaderX-EDR-Evasion) | red-team | relevance | missing_ai_keywords |
| [srvishal/sliver-tor-bridge](https://github.com/srvishal/sliver-tor-bridge) | red-team | relevance | missing_ai_keywords |
| [temboohms68/Flipper-Zero-IR-Signal-Generator](https://github.com/temboohms68/Flipper-Zero-IR-Signal-Generator) | red-team | relevance | missing_ai_keywords |
| [tharun27102006/Aether-C2-Framework](https://github.com/tharun27102006/Aether-C2-Framework) | red-team | relevance | missing_ai_keywords |
| [vonofdaville/adversarial-phish-forge](https://github.com/vonofdaville/adversarial-phish-forge) | red-team | relevance | missing_ai_keywords |
| [CanvizTechnologies/cloud-claw](https://github.com/CanvizTechnologies/cloud-claw) | reverse-engineering | applicability | AI assistant for workflow enhancement; no explicit connection to offensive security, automation, or fuzzing. |
| [DUVALL707/ExploitMaze](https://github.com/DUVALL707/ExploitMaze) | reverse-engineering | applicability | Focuses on vulnerability assessment and exploit development but lacks explicit mention of AI, automation, or fuzzing. |
| [JKASle/Inspector](https://github.com/JKASle/Inspector) | reverse-engineering | applicability | Transforms Google AI Studio exports for analysis; no evidence of offensive security, automation, or fuzzing. |
| [KevinC-ux/WatchGuard](https://github.com/KevinC-ux/WatchGuard) | reverse-engineering | applicability | Focuses on server/domain renewal tracking and alerting, not offensive security or AI/automation for security testing. |
| [Muzammil-Malik/esp8266-weather-clock-opensource](https://github.com/Muzammil-Malik/esp8266-weather-clock-opensource) | reverse-engineering | applicability | Focuses on reverse engineering for home automation, not offensive security or AI/automation for security testing. |
| [NebiyuSeyoum/exploring-the-true-nature-of-variable](https://github.com/NebiyuSeyoum/exploring-the-true-nature-of-variable) | reverse-engineering | applicability | Repository focuses on programming concepts, memory management, and reverse engineering, but does not mention AI, automation, or fuzzing in the context of offensive security. |
| [Olivaire/sleep-duck-eye-Detect-SleepMask](https://github.com/Olivaire/sleep-duck-eye-Detect-SleepMask) | reverse-engineering | applicability | Mentions automated security testing and malware detection, but no explicit evidence of AI, ML, or fuzzing for offensive security. Focus appears to be on detection/forensics. |
| [Richiepandey/PS2Recomp](https://github.com/Richiepandey/PS2Recomp) | reverse-engineering | applicability | Repository is about recompiling PS2 binaries, not about offensive security or AI/automation for security testing. |
| [SamruddhiS7/zasm](https://github.com/SamruddhiS7/zasm) | reverse-engineering | applicability | Repository is a cross-compilation toolchain and assembler, with some reverse engineering relevance, but no AI, automation, fuzzing, or offensive security context. |
| [SanBryanDJ21/Nintendo](https://github.com/SanBryanDJ21/Nintendo) | reverse-engineering | applicability | A JavaScript NES emulator with no explicit mention of AI, automation, or fuzzing for offensive security purposes. |
| [SantiagoRM9/ace-tool](https://github.com/SantiagoRM9/ace-tool) | reverse-engineering | applicability | Focuses on codebase indexing and AI prompt optimization, not on offensive security or automation for security testing. |
| [Truong882/ReVex](https://github.com/Truong882/ReVex) | reverse-engineering | applicability | Primarily a browser-based HTTP repeater for web security testing; no evidence of AI, automation, or fuzzing for offensive security. |
| [YamateKudashai/PHind](https://github.com/YamateKudashai/PHind) | reverse-engineering | applicability | Repository focuses on AI-powered semantic search for Laravel, not offensive security or automation/fuzzing for security testing. |
| [anto16jose/ai-chat-interface](https://github.com/anto16jose/ai-chat-interface) | reverse-engineering | applicability | Repository is an AI chat interface with no offensive security or automation for security testing context. |
| [blackgamma7/Aidyn](https://github.com/blackgamma7/Aidyn) | reverse-engineering | applicability | This is a decompilation project for a Nintendo 64 game, focused on reverse engineering but with no mention of AI, automation, or fuzzing for offensive security. |
| [by-reales/fripack](https://github.com/by-reales/fripack) | reverse-engineering | applicability | Focuses on packaging Frida scripts for reverse engineering, but does not mention AI, automation, or fuzzing for offensive security. |
| [dhesnut/gemini_gpt](https://github.com/dhesnut/gemini_gpt) | reverse-engineering | applicability | AI chat application with no explicit connection to offensive security, penetration testing, or automation for security testing. |
| [eslamfox100/AIDA](https://github.com/eslamfox100/AIDA) | reverse-engineering | applicability | Mentions AI and pentesting tools, but lacks explicit evidence of AI/automation/fuzzing being used for offensive security; description is vague about actual implementation. |
| [imamardiyanto/ts-testdoc](https://github.com/imamardiyanto/ts-testdoc) | reverse-engineering | applicability | Repository is a documentation testing tool and not related to offensive security, AI, automation, or fuzzing. |
| [kidkaitou121212/Roblox-Executor-Injector-2025](https://github.com/kidkaitou121212/Roblox-Executor-Injector-2025) | reverse-engineering | applicability | Mentions exploit and reverse-engineering, but no explicit evidence of AI, automation, or fuzzing for offensive security; appears to be a game cheat/injector. |
| [kingdenofficial/ReverseBox](https://github.com/kingdenofficial/ReverseBox) | reverse-engineering | applicability | Repository is about reversing text/data, not offensive security or AI/automation/fuzzing. |
| [mrfeelssss/ObfuscationZone](https://github.com/mrfeelssss/ObfuscationZone) | reverse-engineering | applicability | Repository is about code obfuscation and anti-debugging, which are relevant to security, but there is no explicit mention of AI, automation, or fuzzing. |
| [mulhala-100ttl/AIDA64-Network-Audit-2026](https://github.com/mulhala-100ttl/AIDA64-Network-Audit-2026) | reverse-engineering | applicability | The repository is focused on network auditing and inventory reporting without any mention of AI, automation, or fuzzing for offensive security. |
| [mwakidenis/UN-OFFICIAL-KPLC-TOKEN-HISTORY-VIEW](https://github.com/mwakidenis/UN-OFFICIAL-KPLC-TOKEN-HISTORY-VIEW) | reverse-engineering | applicability | The repository is focused on accessing token purchase history and does not involve AI, automation, or fuzzing for offensive security. |
| [mzmaaz60/unicor](https://github.com/mzmaaz60/unicor) | reverse-engineering | applicability | No evidence of offensive security or AI/automation for security. Focus is on trading and API data analysis. |
| [parroalex01/Dumper-FiveM-And-Custom-Launcher](https://github.com/parroalex01/Dumper-FiveM-And-Custom-Launcher) | reverse-engineering | applicability | Repository is about dumping resources and bypassing anti-cheat, which is a form of reverse engineering, but there is no mention of AI, automation, or fuzzing. |
| [rdnrhm92/switch](https://github.com/rdnrhm92/switch) | reverse-engineering | applicability | The repository is a feature flag management platform for enterprise applications. While it mentions AI-tools and reverse-engineering in topics, there is no explicit evidence of AI, automation, or fuzzing being used for offensive security purposes. |
| [stepanovmykola/CryptInject](https://github.com/stepanovmykola/CryptInject) | reverse-engineering | applicability | While the repository mentions penetration testing and malware analysis, there is no explicit indication of AI, automation, or fuzzing being used. |
| [viniciussantos2004/strata](https://github.com/viniciussantos2004/strata) | reverse-engineering | applicability | Repository is focused on AI initiative management and compliance, not offensive security or automation/fuzzing for security testing. |
| [yassiroz/sekaictf-2025](https://github.com/yassiroz/sekaictf-2025) | reverse-engineering | applicability | Repository contains CTF challenges and writeups related to offensive security, but there is no explicit mention of AI, automation, or fuzzing usage. |
| [yutangru1114/hwidtool](https://github.com/yutangru1114/hwidtool) | reverse-engineering | applicability | The repository is a hardware ID management tool focused on privacy and system programming; no explicit mention of AI, automation, or fuzzing for offensive security. |
| [OnlyyxErika/Ciphey](https://github.com/OnlyyxErika/Ciphey) | reverse-engineering | credibility | No stars and potentially a fork or duplicate; description is substantive but no community validation. |
| [neelamkhalid/Ciphey](https://github.com/neelamkhalid/Ciphey) | reverse-engineering | credibility | No stars and no evidence of community validation, but description is clear and substantive. |
| [Abhishek-innovation/ShadowSploit](https://github.com/Abhishek-innovation/ShadowSploit) | reverse-engineering | relevance | missing_ai_keywords |
| [Abhishek-innovation/ShadowSploit](https://github.com/Abhishek-innovation/ShadowSploit) | reverse-engineering | relevance | missing_ai_keywords |
| [Adrianmau5/Luna](https://github.com/Adrianmau5/Luna) | reverse-engineering | relevance | missing_ai_keywords |
| [Ahegaho/ExploitMaze](https://github.com/Ahegaho/ExploitMaze) | reverse-engineering | relevance | missing_ai_keywords |
| [AhmedHossam151/AspyrArchiveTool](https://github.com/AhmedHossam151/AspyrArchiveTool) | reverse-engineering | relevance | missing_ai_keywords |
| [AlYElkooptan/DiaSymbolView](https://github.com/AlYElkooptan/DiaSymbolView) | reverse-engineering | relevance | missing_ai_keywords |
| [AlessandroBonomo28/HealthyIG](https://github.com/AlessandroBonomo28/HealthyIG) | reverse-engineering | relevance | missing_ai_keywords |
| [AlessandroBonomo28/HealthyIG](https://github.com/AlessandroBonomo28/HealthyIG) | reverse-engineering | relevance | missing_ai_keywords |
| [Ali632-lgtm/mcafee-tools](https://github.com/Ali632-lgtm/mcafee-tools) | reverse-engineering | relevance | missing_ai_keywords |
| [Ali632-lgtm/mcafee-tools](https://github.com/Ali632-lgtm/mcafee-tools) | reverse-engineering | relevance | missing_ai_keywords |
| [Bienfait-Mutunzi/Awesome-Hacking-Learning-Path](https://github.com/Bienfait-Mutunzi/Awesome-Hacking-Learning-Path) | reverse-engineering | relevance | missing_ai_keywords |
| [Bienfait-Mutunzi/Awesome-Hacking-Learning-Path](https://github.com/Bienfait-Mutunzi/Awesome-Hacking-Learning-Path) | reverse-engineering | relevance | missing_ai_keywords |
| [BillyGitau/My-first-game](https://github.com/BillyGitau/My-first-game) | reverse-engineering | relevance | missing_ai_keywords |
| [Chrimakan/WinRAR-Password-Cracker-Tool](https://github.com/Chrimakan/WinRAR-Password-Cracker-Tool) | reverse-engineering | relevance | missing_ai_keywords |
| [Coconginamo/MoovitPatcher](https://github.com/Coconginamo/MoovitPatcher) | reverse-engineering | relevance | missing_ai_keywords |
| [Crossie7/WeChat-Channels-Video-File-Decryption](https://github.com/Crossie7/WeChat-Channels-Video-File-Decryption) | reverse-engineering | relevance | missing_ai_keywords |
| [DeadFox55YZ/ShadowSploit](https://github.com/DeadFox55YZ/ShadowSploit) | reverse-engineering | relevance | missing_ai_keywords |
| [DeadFox55YZ/ShadowSploit](https://github.com/DeadFox55YZ/ShadowSploit) | reverse-engineering | relevance | missing_ai_keywords |
| [Dhruvchaudhary255/reverse](https://github.com/Dhruvchaudhary255/reverse) | reverse-engineering | relevance | missing_ai_keywords |
| [GeoloeG-IsT/agents-reverse-engineer](https://github.com/GeoloeG-IsT/agents-reverse-engineer) | reverse-engineering | relevance | missing_ai_keywords |
| [Hans11609/planning-with-files](https://github.com/Hans11609/planning-with-files) | reverse-engineering | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | reverse-engineering | relevance | missing_ai_keywords |
| [Laeteth/advanced-anti-sandbox-Virtual-Machine](https://github.com/Laeteth/advanced-anti-sandbox-Virtual-Machine) | reverse-engineering | relevance | missing_ai_keywords |
| [Laeteth/advanced-anti-sandbox-Virtual-Machine](https://github.com/Laeteth/advanced-anti-sandbox-Virtual-Machine) | reverse-engineering | relevance | missing_ai_keywords |
| [Laeteth/advanced-anti-sandbox-Virtual-Machine](https://github.com/Laeteth/advanced-anti-sandbox-Virtual-Machine) | reverse-engineering | relevance | missing_ai_keywords |
| [Matteo907-boop/zyrox](https://github.com/Matteo907-boop/zyrox) | reverse-engineering | relevance | missing_ai_keywords |
| [Michelplayer/android-re-ctfs](https://github.com/Michelplayer/android-re-ctfs) | reverse-engineering | relevance | missing_ai_keywords |
| [Mighty08war/PEBLoader.h](https://github.com/Mighty08war/PEBLoader.h) | reverse-engineering | relevance | missing_ai_keywords |
| [Mighty08war/PEBLoader.h](https://github.com/Mighty08war/PEBLoader.h) | reverse-engineering | relevance | missing_ai_keywords |
| [Oluwanifemithe/ctf-writeups](https://github.com/Oluwanifemithe/ctf-writeups) | reverse-engineering | relevance | missing_ai_keywords |
| [Omkar675/ImHex](https://github.com/Omkar675/ImHex) | reverse-engineering | relevance | missing_ai_keywords |
| [Ornateill/nightmare-exploit-roadmap](https://github.com/Ornateill/nightmare-exploit-roadmap) | reverse-engineering | relevance | missing_ai_keywords |
| [Orpheashatzis/JDX_ReverseEngineeringJSONExample](https://github.com/Orpheashatzis/JDX_ReverseEngineeringJSONExample) | reverse-engineering | relevance | missing_ai_keywords |
| [Rbel12b/Lpf2](https://github.com/Rbel12b/Lpf2) | reverse-engineering | relevance | missing_ai_keywords |
| [Rych156/PEAnalyzer](https://github.com/Rych156/PEAnalyzer) | reverse-engineering | relevance | missing_ai_keywords |
| [SEPTMOON/planning-with-files](https://github.com/SEPTMOON/planning-with-files) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [Spray6T9/dexter](https://github.com/Spray6T9/dexter) | reverse-engineering | relevance | missing_ai_keywords |
| [SteamDatabase/GameTracking-Deadlock](https://github.com/SteamDatabase/GameTracking-Deadlock) | reverse-engineering | relevance | missing_ai_keywords |
| [TECHNO-SOUQ/AspyrArchiveTool](https://github.com/TECHNO-SOUQ/AspyrArchiveTool) | reverse-engineering | relevance | missing_ai_keywords |
| [Terralyp/SunloginLP-Eanalysis-tool](https://github.com/Terralyp/SunloginLP-Eanalysis-tool) | reverse-engineering | relevance | missing_ai_keywords |
| [Terralyp/UnrealDbg-VT-engine](https://github.com/Terralyp/UnrealDbg-VT-engine) | reverse-engineering | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | reverse-engineering | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | reverse-engineering | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | reverse-engineering | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | reverse-engineering | relevance | missing_ai_keywords |
| [VectorlyApp/bluebox](https://github.com/VectorlyApp/bluebox) | reverse-engineering | relevance | missing_ai_keywords |
| [Winich007/samsung-umtz0](https://github.com/Winich007/samsung-umtz0) | reverse-engineering | relevance | missing_ai_keywords |
| [Winich007/samsung-umtz0](https://github.com/Winich007/samsung-umtz0) | reverse-engineering | relevance | missing_ai_keywords |
| [ak-sports/qiling](https://github.com/ak-sports/qiling) | reverse-engineering | relevance | missing_ai_keywords |
| [alilooop/AssetRetrieval3D](https://github.com/alilooop/AssetRetrieval3D) | reverse-engineering | relevance | missing_ai_keywords |
| [arieahXxshrek/secwexen.github.io](https://github.com/arieahXxshrek/secwexen.github.io) | reverse-engineering | relevance | missing_ai_keywords |
| [bfjesso/jesso-decompiler](https://github.com/bfjesso/jesso-decompiler) | reverse-engineering | relevance | missing_ai_keywords |
| [debbie23/Anker_Prime_BLE_hacking](https://github.com/debbie23/Anker_Prime_BLE_hacking) | reverse-engineering | relevance | missing_ai_keywords |
| [debbie23/Anker_Prime_BLE_hacking](https://github.com/debbie23/Anker_Prime_BLE_hacking) | reverse-engineering | relevance | missing_ai_keywords |
| [delvinru/apk-info](https://github.com/delvinru/apk-info) | reverse-engineering | relevance | missing_ai_keywords |
| [fromgabyaaye/UniPwn](https://github.com/fromgabyaaye/UniPwn) | reverse-engineering | relevance | missing_ai_keywords |
| [jovibor/HexCtrl](https://github.com/jovibor/HexCtrl) | reverse-engineering | relevance | missing_ai_keywords |
| [kal21k/HWBP-DEP-Bypass](https://github.com/kal21k/HWBP-DEP-Bypass) | reverse-engineering | relevance | missing_ai_keywords |
| [lukenixon8/CryptInject](https://github.com/lukenixon8/CryptInject) | reverse-engineering | relevance | missing_ai_keywords |
| [lukenixon8/CryptInject](https://github.com/lukenixon8/CryptInject) | reverse-engineering | relevance | missing_ai_keywords |
| [lympdegrin919fl/AnyDesk-Ultimate-2026](https://github.com/lympdegrin919fl/AnyDesk-Ultimate-2026) | reverse-engineering | relevance | missing_ai_keywords |
| [manishvedwal2609/mips-atan2](https://github.com/manishvedwal2609/mips-atan2) | reverse-engineering | relevance | missing_ai_keywords |
| [megakiyaiscool/Smart_Plug](https://github.com/megakiyaiscool/Smart_Plug) | reverse-engineering | relevance | missing_ai_keywords |
| [megakiyaiscool/Smart_Plug](https://github.com/megakiyaiscool/Smart_Plug) | reverse-engineering | relevance | missing_ai_keywords |
| [namanONcode/Anchor-pq](https://github.com/namanONcode/Anchor-pq) | reverse-engineering | relevance | missing_ai_keywords |
| [nebil175/lcu_dumper](https://github.com/nebil175/lcu_dumper) | reverse-engineering | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | reverse-engineering | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | reverse-engineering | relevance | missing_ai_keywords |
| [prateek123s/HWBP-DEP-Bypass](https://github.com/prateek123s/HWBP-DEP-Bypass) | reverse-engineering | relevance | missing_ai_keywords |
| [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) | reverse-engineering | relevance | missing_ai_keywords |
| [radareorg/radare2](https://github.com/radareorg/radare2) | reverse-engineering | relevance | missing_ai_keywords |
| [rashmiranjanp/frida-reversing-lab](https://github.com/rashmiranjanp/frida-reversing-lab) | reverse-engineering | relevance | missing_ai_keywords |
| [rizinorg/rz-libdemangle](https://github.com/rizinorg/rz-libdemangle) | reverse-engineering | relevance | missing_ai_keywords |
| [snaku/Persona3-FES-Decompilation](https://github.com/snaku/Persona3-FES-Decompilation) | reverse-engineering | relevance | missing_ai_keywords |
| [usethesource/rascal](https://github.com/usethesource/rascal) | reverse-engineering | relevance | missing_ai_keywords |
| [vascodavid/PICO8-Extractor](https://github.com/vascodavid/PICO8-Extractor) | reverse-engineering | relevance | missing_ai_keywords |
| [vascodavid/PICO8-Extractor](https://github.com/vascodavid/PICO8-Extractor) | reverse-engineering | relevance | missing_ai_keywords |
| [vascodavid/PICO8-Extractor](https://github.com/vascodavid/PICO8-Extractor) | reverse-engineering | relevance | missing_ai_keywords |
| [wisamna84/ps5-app-dumper](https://github.com/wisamna84/ps5-app-dumper) | reverse-engineering | relevance | missing_ai_keywords |
| [wowemulation-dev/cascette-py](https://github.com/wowemulation-dev/cascette-py) | reverse-engineering | relevance | missing_ai_keywords |
| [wowemulation-dev/cascette-rs](https://github.com/wowemulation-dev/cascette-rs) | reverse-engineering | relevance | missing_ai_keywords |
| [wowemulation-dev/cascette-rs](https://github.com/wowemulation-dev/cascette-rs) | reverse-engineering | relevance | missing_ai_keywords |
| [wowemulation-dev/warcraft-rs](https://github.com/wowemulation-dev/warcraft-rs) | reverse-engineering | relevance | missing_ai_keywords |
| [Ajithkumar8/Dependency-Confusion-Hunter](https://github.com/Ajithkumar8/Dependency-Confusion-Hunter) | security-automation | applicability | Automates vulnerability detection but does not explicitly mention AI, ML, or fuzzing; focus is on dependency scanning, not offensive operations. |
| [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content) | security-automation | applicability | Repository focuses on security automation for compliance and hardening, not offensive security or AI-driven tools. |
| [Frog456-dev/secwexen-arsenal](https://github.com/Frog456-dev/secwexen-arsenal) | security-automation | applicability | Curates offensive and automation tools, but does not explicitly demonstrate the use of AI, automation, or fuzzing for offensive security in the description or topics. |
| [GhostkillerMMIX/enterprise-soc-blueprint](https://github.com/GhostkillerMMIX/enterprise-soc-blueprint) | security-automation | applicability | Focus is on SOC, SIEM, and security automation for defense, not offensive security. No evidence of AI/automation for offensive operations. |
| [Invertebrate-cankerweed632/awesome-devsecops](https://github.com/Invertebrate-cankerweed632/awesome-devsecops) | security-automation | applicability | Repository is a DevSecOps tools list, with no explicit mention of offensive security or AI/automation/fuzzing usage for offensive operations. |
| [Mirai8888/ThreatMouth](https://github.com/Mirai8888/ThreatMouth) | security-automation | applicability | Automates threat intelligence feed collection but not related to offensive security or AI/fuzzing for offensive use. |
| [Quocton1/kali-linux-teaching-course-live](https://github.com/Quocton1/kali-linux-teaching-course-live) | security-automation | applicability | Repository focuses on teaching Kali Linux and penetration testing, but lacks explicit evidence of AI, automation, or fuzzing usage for offensive security in description or topics. |
| [Thenguyenvn/rsync-backup-solution](https://github.com/Thenguyenvn/rsync-backup-solution) | security-automation | applicability | Repository is about automated backups and data protection, not about offensive security or the use of AI/automation/fuzzing for security testing. |
| [TypicalShot/zenmap](https://github.com/TypicalShot/zenmap) | security-automation | applicability | Despite offensive security keywords, the repository is a memory-mapped file library and does not mention AI, automation, or fuzzing for security. |
| [ValiantKaka/Phishing-Email-Analysis](https://github.com/ValiantKaka/Phishing-Email-Analysis) | security-automation | applicability | The repository focuses on analyzing phishing emails and provides actionable insights for healthcare organizations, which is defensive security. While it mentions 'security-automation' and related topics, there is no explicit evidence of AI, automation, or fuzzing being used for offensive security purposes such as penetration testing, red teaming, vulnerability detection, exploit development, or automated malware analysis. |
| [Yjaballi/cybersecurity_roadmap](https://github.com/Yjaballi/cybersecurity_roadmap) | security-automation | applicability | Focuses on cybersecurity career development and education, not on AI/automation/fuzzing for offensive security. |
| [akutemmanuel/StormSec](https://github.com/akutemmanuel/StormSec) | security-automation | applicability | The repository mentions offensive security keywords such as penetration-testing, malware-analysis, and security-automation, but lacks explicit evidence of AI, automation, or fuzzing being used for offensive security purposes in the description or topics. |
| [anubis01sk/splunk-detection-engineer-agent](https://github.com/anubis01sk/splunk-detection-engineer-agent) | security-automation | applicability | Repository uses AI for generating Splunk SPL queries for security analytics and detection engineering, but does not explicitly mention offensive security, penetration testing, or red team automation. |
| [ar157209/soc-roadmap-2026](https://github.com/ar157209/soc-roadmap-2026) | security-automation | applicability | The repository focuses on SOC analyst training, automation, and machine learning, but its topics and description are centered on blue-team (defensive) operations rather than offensive security. There is no explicit evidence of AI/automation/fuzzing being used for offensive security purposes such as penetration testing, red teaming, or exploit/malware analysis. |
| [bznbnn/Code-Reviewer-AI](https://github.com/bznbnn/Code-Reviewer-AI) | security-automation | applicability | The repository focuses on AI-driven code review and coding assistance, but does not explicitly mention offensive security, penetration testing, vulnerability detection, exploit development, or malware analysis. The 'security-automation' topic is present, but context is generic and not tied to offensive security. |
| [designershount/astra](https://github.com/designershount/astra) | security-automation | applicability | Mentions penetration-testing-framework and security-automation, but description and topics focus on AI agent environments, not offensive security or automation for security testing. |
| [mikehubers/Awesome-AI-For-Security](https://github.com/mikehubers/Awesome-AI-For-Security) | security-automation | applicability | Curated list of resources; not a tool or implementation, and does not demonstrate the use of AI/automation/fuzzing for offensive security. |
| [yud1takata/security-ops-blueprint](https://github.com/yud1takata/security-ops-blueprint) | security-automation | applicability | Focuses on security operations and automation, but lacks explicit mention of offensive security activities or AI/fuzzing for offensive use. |
| [zricethezav/h1domains](https://github.com/zricethezav/h1domains) | security-automation | applicability | Repository provides a list of domains for HackerOne but does not involve AI, automation, or fuzzing for offensive security. |
| [sairysee/aappmart](https://github.com/sairysee/aappmart) | security-automation | credibility | No stars, but recently updated and description is clear and relevant. No red flags for malicious intent. |
| [three2hot/cyber-agent](https://github.com/three2hot/cyber-agent) | security-automation | credibility | No stars or community validation yet, but description is clear and relevant; recently updated. |
| [CybercentreCanada/assemblyline](https://github.com/CybercentreCanada/assemblyline) | security-automation | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline](https://github.com/CybercentreCanada/assemblyline) | security-automation | relevance | missing_ai_keywords |
| [DefectDojo/django-DefectDojo](https://github.com/DefectDojo/django-DefectDojo) | security-automation | relevance | missing_ai_keywords |
| [Fireresistive-bottleneck299/aws-jit-access](https://github.com/Fireresistive-bottleneck299/aws-jit-access) | security-automation | relevance | missing_ai_keywords |
| [Fireresistive-bottleneck299/aws-jit-access](https://github.com/Fireresistive-bottleneck299/aws-jit-access) | security-automation | relevance | missing_ai_keywords |
| [Fireresistive-bottleneck299/aws-jit-access](https://github.com/Fireresistive-bottleneck299/aws-jit-access) | security-automation | relevance | missing_ai_keywords |
| [Gberegbe/infrastructure-security-automation](https://github.com/Gberegbe/infrastructure-security-automation) | security-automation | relevance | missing_ai_keywords |
| [Gervis123212/azure-sentinel-honeypot](https://github.com/Gervis123212/azure-sentinel-honeypot) | security-automation | relevance | missing_ai_keywords |
| [Gervis123212/azure-sentinel-honeypot](https://github.com/Gervis123212/azure-sentinel-honeypot) | security-automation | relevance | missing_ai_keywords |
| [Gervis123212/azure-sentinel-honeypot](https://github.com/Gervis123212/azure-sentinel-honeypot) | security-automation | relevance | missing_ai_keywords |
| [Ivan55555555555/Pentest-Clink-Completions](https://github.com/Ivan55555555555/Pentest-Clink-Completions) | security-automation | relevance | missing_ai_keywords |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [Lmgsd-2024/skill-security-scan](https://github.com/Lmgsd-2024/skill-security-scan) | security-automation | relevance | missing_ai_keywords |
| [Munem-1/File-Integrity-Checker-Cybersecurity-Tool](https://github.com/Munem-1/File-Integrity-Checker-Cybersecurity-Tool) | security-automation | relevance | missing_ai_keywords |
| [Ramyachand/ezbio-username-checker](https://github.com/Ramyachand/ezbio-username-checker) | security-automation | relevance | missing_ai_keywords |
| [SecObserve/SecObserve](https://github.com/SecObserve/SecObserve) | security-automation | relevance | missing_ai_keywords |
| [SecObserve/SecObserve](https://github.com/SecObserve/SecObserve) | security-automation | relevance | missing_ai_keywords |
| [Shubh2-0/Spring_Security](https://github.com/Shubh2-0/Spring_Security) | security-automation | relevance | missing_ai_keywords |
| [Shubh2-0/Spring_Security](https://github.com/Shubh2-0/Spring_Security) | security-automation | relevance | missing_ai_keywords |
| [TianTheHacker/cloudflare-auto-protection](https://github.com/TianTheHacker/cloudflare-auto-protection) | security-automation | relevance | missing_ai_keywords |
| [TianTheHacker/cloudflare-auto-protection](https://github.com/TianTheHacker/cloudflare-auto-protection) | security-automation | relevance | missing_ai_keywords |
| [TianTheHacker/cloudflare-auto-protection](https://github.com/TianTheHacker/cloudflare-auto-protection) | security-automation | relevance | missing_ai_keywords |
| [WhyN0tTh0/enterprise-attack-simulator](https://github.com/WhyN0tTh0/enterprise-attack-simulator) | security-automation | relevance | missing_ai_keywords |
| [WhyN0tTh0/enterprise-attack-simulator](https://github.com/WhyN0tTh0/enterprise-attack-simulator) | security-automation | relevance | missing_ai_keywords |
| [WhyN0tTh0/enterprise-attack-simulator](https://github.com/WhyN0tTh0/enterprise-attack-simulator) | security-automation | relevance | missing_ai_keywords |
| [hitq11/AdaPol](https://github.com/hitq11/AdaPol) | security-automation | relevance | missing_ai_keywords |
| [hitq11/AdaPol](https://github.com/hitq11/AdaPol) | security-automation | relevance | missing_ai_keywords |
| [hitq11/AdaPol](https://github.com/hitq11/AdaPol) | security-automation | relevance | missing_ai_keywords |
| [hitq11/AdaPol](https://github.com/hitq11/AdaPol) | security-automation | relevance | missing_ai_keywords |
| [kynaan5353/cargo-recon](https://github.com/kynaan5353/cargo-recon) | security-automation | relevance | missing_ai_keywords |
| [kynaan5353/cargo-recon](https://github.com/kynaan5353/cargo-recon) | security-automation | relevance | missing_ai_keywords |
| [kynaan5353/cargo-recon](https://github.com/kynaan5353/cargo-recon) | security-automation | relevance | missing_ai_keywords |
| [kynaan5353/cargo-recon](https://github.com/kynaan5353/cargo-recon) | security-automation | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | security-automation | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | security-automation | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | security-automation | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | security-automation | relevance | missing_ai_keywords |
| [nancy12341/husky-image-guard](https://github.com/nancy12341/husky-image-guard) | security-automation | relevance | missing_ai_keywords |
| [octivi/update-securitytxt-expires](https://github.com/octivi/update-securitytxt-expires) | security-automation | relevance | missing_ai_keywords |
| [octivi/update-securitytxt-expires](https://github.com/octivi/update-securitytxt-expires) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [quinntrys/devsecops](https://github.com/quinntrys/devsecops) | security-automation | relevance | missing_ai_keywords |
| [quinntrys/devsecops](https://github.com/quinntrys/devsecops) | security-automation | relevance | missing_ai_keywords |
| [quinntrys/devsecops](https://github.com/quinntrys/devsecops) | security-automation | relevance | missing_ai_keywords |
| [secureCodeBox/secureCodeBox](https://github.com/secureCodeBox/secureCodeBox) | security-automation | relevance | missing_ai_keywords |
| [securego/gosec](https://github.com/securego/gosec) | security-automation | relevance | missing_ai_keywords |
| [securego/gosec](https://github.com/securego/gosec) | security-automation | relevance | missing_ai_keywords |
| [securego/gosec](https://github.com/securego/gosec) | security-automation | relevance | missing_ai_keywords |
| [wazuh/wazuh](https://github.com/wazuh/wazuh) | security-automation | relevance | missing_ai_keywords |
| [wazuh/wazuh](https://github.com/wazuh/wazuh) | security-automation | relevance | missing_ai_keywords |
| [wazuh/wazuh](https://github.com/wazuh/wazuh) | security-automation | relevance | missing_ai_keywords |
| [&#x26;#xa;AI-Powered Knowledge Graph Generator &#x26; APTs, (Thu, Feb 12th)](https://isc.sans.edu/diary/rss/32712) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [260K+ Chrome Users Duped by Fake AI Browser Extensions](https://www.darkreading.com/cyber-risk/chrome-fake-ai-browser-extensions) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [8-Minute Access: AI Accelerates Breach of AWS Environment](https://www.darkreading.com/cloud-security/8-minute-access-ai-aws-environment-breach) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [80% of Fortune 500 use active AI Agents: Observability, governance, and security shape the new frontier](https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [A Content-Based Framework for Cybersecurity Refusal Decisions in Large Language Models](https://arxiv.org/abs/2602.15689) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [A Content-Based Framework for Cybersecurity Refusal Decisions in Large Language Models](https://arxiv.org/abs/2602.15689) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [A Scalable Approach to Solving Simulation-Based Network Security Games](https://arxiv.org/abs/2602.16564) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [A one-prompt attack that breaks LLM safety alignment](https://www.microsoft.com/en-us/security/blog/2026/02/09/prompt-attack-breaks-llm-safety/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models](https://arxiv.org/abs/2602.06771) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [AI Agents 'Swarm,' Security Complexity Follows Suit](https://www.darkreading.com/cloud-security/ai-agents-swarm-security-complexity) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [AI Malware: Hype vs. Reality](https://www.recordedfuture.com/blog/ai-malware-hype-vs-reality) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [AI May Supplant Pen Testers, But Oversight &amp; Trust Are Not There Yet](https://www.darkreading.com/cybersecurity-operations/ai-supplant-pen-testers-oversight-trust-not-there-yet) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [AI Rising: Do We Know Enough About the Data Populating It?](https://www.darkreading.com/data-privacy/do-we-know-enough-about-data-populating-ai) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [AI-Generated Text and the Detection Arms Race](https://www.schneier.com/blog/archives/2026/02/the-ai-generated-text-arms-race.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Abstractive Red-Teaming of Language Model Character](https://arxiv.org/abs/2602.12318) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Agentic AI Security: Threats, Defenses, Evaluation, and Open Challenges](https://arxiv.org/abs/2510.23883) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Agentic AI Site 'Moltbook' Is Riddled With Security Risks](https://www.darkreading.com/cyber-risk/agentic-ai-moltbook-security-risks) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Agentic AI for Cybersecurity: A Meta-Cognitive Architecture for Governable Autonomy](https://arxiv.org/abs/2602.11897) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Agentic AI for Cybersecurity: A Meta-Cognitive Architecture for Governable Autonomy](https://arxiv.org/abs/2602.11897) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [All gas, no brakes: Time to come to AI church](https://blog.talosintelligence.com/all-gas-no-brakes-time-to-come-to-ai-church/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Autonomous Threat Operations in action: Real results from Recorded Future’s own SOC team | Recorded Future](https://www.recordedfuture.com/blog/autonomous-threat-operations-in-action) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Backdoor Attacks on Contrastive Continual Learning for IoT Systems](https://arxiv.org/abs/2602.13062) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System](https://arxiv.org/abs/2602.10915) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [CP-uniGuard: A Unified, Probability-Agnostic, and Adaptive Framework for Malicious Agent Detection and Defense in Multi-Agent Embodied Perception Systems](https://arxiv.org/abs/2506.22890) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Can chatbots craft correct code?](https://blog.trailofbits.com/2025/12/19/can-chatbots-craft-correct-code/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Claude LLM artifacts abused to push Mac infostealers in ClickFix attack](https://www.bleepingcomputer.com/news/security/claude-llm-artifacts-abused-to-push-mac-infostealers-in-clickfix-attack/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [ClawSec: Hardening OpenClaw Agents from the Inside Out](https://www.sentinelone.com/blog/clawsec-hardening-openclaw-agents-from-the-inside-out/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [ClickFix added nslookup commands to its arsenal for downloading RATs](https://www.malwarebytes.com/blog/news/2026/02/clickfix-added-nslookup-commands-to-its-arsenal-for-downloading-rats) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Closing the Distribution Gap in Adversarial Training for LLMs](https://arxiv.org/abs/2602.15238) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Collaborative Zone-Adaptive Zero-Day Intrusion Detection for IoBT](https://arxiv.org/abs/2602.16098) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Collaborative Zone-Adaptive Zero-Day Intrusion Detection for IoBT](https://arxiv.org/abs/2602.16098) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Community-powered security with AI: an open source framework for security research](https://github.blog/security/community-powered-security-with-ai-an-open-source-framework-for-security-research/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Consistency of Large Reasoning Models Under Multi-Turn Attacks](https://arxiv.org/abs/2602.13093) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Copilot Studio agent security: Top 10 risks you can detect and prevent](https://www.microsoft.com/en-us/security/blog/2026/02/12/copilot-studio-agent-security-top-10-risks-detect-prevent/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Criminals are using AI website builders to clone major brands](https://www.malwarebytes.com/blog/news/2026/02/criminals-are-using-ai-website-builders-to-clone-major-brands) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Cybersecurity 2026 | The Year Ahead in AI, Adversaries, and Global Change](https://www.sentinelone.com/blog/cybersecurity-2026-the-year-ahead-in-ai-adversaries-and-global-change/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Datadog uses Codex for system-level code review](https://openai.com/index/datadog) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Deep Learning for Contextualized NetFlow-Based Network Intrusion Detection: Methods, Data, Evaluation and Deployment](https://arxiv.org/abs/2602.05594) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Detecting Object Tracking Failure via Sequential Hypothesis Testing](https://arxiv.org/abs/2602.12983) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Detecting backdoored language models at scale](https://www.microsoft.com/en-us/security/blog/2026/02/04/detecting-backdoored-language-models-at-scale/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Drift-Aware Variational Autoencoder-based Anomaly Detection with Two-level Ensembling](https://arxiv.org/abs/2602.12976) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Efficient Semi-Supervised Adversarial Training via Latent Clustering-Based Data Reduction](https://arxiv.org/abs/2501.10466) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [EnCase Driver Weaponized as EDR Killers Persist](https://www.darkreading.com/threat-intelligence/encase-driver-weaponized-edr-killers-persist) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Exploiting Layer-Specific Vulnerabilities to Backdoor Attack in Federated Learning](https://arxiv.org/abs/2602.15161) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Exploiting Layer-Specific Vulnerabilities to Backdoor Attack in Federated Learning](https://arxiv.org/abs/2602.15161) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Exploiting Layer-Specific Vulnerabilities to Backdoor Attack in Federated Learning](https://arxiv.org/abs/2602.15161) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Federated Graph AGI for Cross-Border Insider Threat Intelligence in Government Financial Schemes](https://arxiv.org/abs/2602.16109) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Four Seconds to Botnet - Analyzing a Self Propagating SSH Worm with Cryptographically Signed C2 &#x5b;Guest Diary&#x5d;, (Wed, Feb 11th)](https://isc.sans.edu/diary/rss/32708) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [From 27 Steps to 5: How Recorded Future Reimagined Threat Hunting with Autonomous Threat Operations](https://www.recordedfuture.com/blog/threat-hunting-27-steps-to-5) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [From Prompts to Protection: Large Language Model-Enabled In-Context Learning for Smart Public Safety UAV](https://arxiv.org/abs/2506.02649) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [GPTZero: Robust Detection of LLM-Generated Texts](https://arxiv.org/abs/2602.13042) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Hobby coder accidentally creates vacuum robot army](https://www.malwarebytes.com/blog/news/2026/02/hobby-coder-accidentally-creates-vacuum-robot-army) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [How to Scale SOC Automation with Falcon Fusion SOAR](https://www.crowdstrike.com/en-us/blog/how-to-scale-soc-automation-with-falcon-fusion-soar/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [I scan, you scan, we all scan for...  knowledge?](https://blog.talosintelligence.com/i-scan-you-scan-we-all-scan-for-knowledge/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach](https://arxiv.org/abs/2602.13156) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach](https://arxiv.org/abs/2602.13156) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Infostealer Steals OpenClaw AI Agent Configuration Files and Gateway Tokens](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Inside the CopyCop Playbook: How to Fight Back in the Age of Synthetic Media](https://www.recordedfuture.com/blog/inside-the-copycop-playbook) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Inside the Human-AI Feedback Loop Powering CrowdStrike&rsquo;s Agentic Security](https://www.crowdstrike.com/en-us/blog/inside-the-human-ai-feedback-loop-powering-crowdstrike-agentic-security/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Intent-Driven Smart Manufacturing Integrating Knowledge Graphs and Large Language Models](https://arxiv.org/abs/2602.12419) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Introducing &quot;AI Unlocked: Decoding Prompt Injection,&quot; a New Interactive Challenge](https://www.crowdstrike.com/en-us/blog/introducing-ai-unlocked-interactive-prompt-injection-challenge/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Keeping your data safe when an AI agent clicks a link](https://openai.com/index/ai-agent-link-safety) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [MASPRM: Multi-Agent System Process Reward Model](https://arxiv.org/abs/2510.24803) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Manipulating AI memory for profit: The rise of AI Recommendation Poisoning](https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Membership and Dataset Inference Attacks on Large Audio Generative Models](https://arxiv.org/abs/2512.09654) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Memory Injection Attacks on LLM Agents via Query-Only Interaction](https://arxiv.org/abs/2503.03704) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Metasploit Wrap-Up 02/06/2026](https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-02-06-2026) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Metasploit Wrap-Up 02/13/2026](https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-02-13-2026) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Microsoft Finds “Summarize with AI” Prompts Manipulating Chatbot Recommendations](https://thehackernews.com/2026/02/microsoft-finds-summarize-with-ai.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [North Korea's UNC1069 Hammers Crypto Firms With AI](https://www.darkreading.com/threat-intelligence/north-koreas-unc1069-hammers-crypto-firms) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [North Korea-Linked UNC1069 Uses AI Lures to Attack Cryptocurrency Organizations](https://thehackernews.com/2026/02/north-korea-linked-unc1069-uses-ai.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [OneClaw: Discovery and Observability for the Agentic Era](https://www.sentinelone.com/blog/oneclaw-discovery-and-observability-for-the-agentic-era/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection](https://arxiv.org/abs/2602.11247) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Pixel-Based Similarities as an Alternative to Neural Data for Improving Convolutional Neural Network Adversarial Robustness](https://arxiv.org/abs/2410.03952) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Policy Compiler for Secure Agentic Systems](https://arxiv.org/abs/2602.16708) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [RMM Abuse Explodes as Hackers Ditch Malware](https://www.darkreading.com/application-security/rmm-abuse-explodes-hackers-ditch-malware) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Recursive language models for jailbreak detection: a procedural defense for tool-augmented agents](https://arxiv.org/abs/2602.16520) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Recursive language models for jailbreak detection: a procedural defense for tool-augmented agents](https://arxiv.org/abs/2602.16520) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Revisiting Backdoor Threat in Federated Instruction Tuning from a Signal Aggregation Perspective](https://arxiv.org/abs/2602.15671) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Robust Deep Reinforcement Learning against Adversarial Behavior Manipulation](https://arxiv.org/abs/2406.03862) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Robust Deep Reinforcement Learning against Adversarial Behavior Manipulation](https://arxiv.org/abs/2406.03862) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [RobustBlack: Challenging Black-Box Adversarial Attacks on State-of-the-Art Defenses](https://arxiv.org/abs/2412.20987) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [SPARC: Scenario Planning and Reasoning for Automated C Unit Test Generation](https://arxiv.org/abs/2602.16671) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Safe and Inclusive E‑Society: How Lithuania Is Bracing for AI‑Driven Cyber Fraud](https://thehackernews.com/2026/02/safe-and-inclusive-esociety-how.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Sample-Specific Noise Injection For Diffusion-Based Adversarial Purification](https://arxiv.org/abs/2506.06027) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation](https://arxiv.org/abs/2602.12544) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Scammers use fake “Gemini” AI chatbot to sell fake “Google Coin”](https://www.malwarebytes.com/blog/ai/2026/02/scammers-use-fake-gemini-ai-chatbot-to-sell-fake-google-coin) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Secure AI with CrowdStrike: Real-World Stories of Protecting AI Workloads and Data](https://www.crowdstrike.com/en-us/blog/how-three-companies-secure-ai-with-crowdstrike/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://arxiv.org/abs/2602.12405) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Sequential Membership Inference Attacks](https://arxiv.org/abs/2602.16596) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Shadow Agents: How SentinelOne Secures the AI Tools That Act Like Users](https://www.sentinelone.com/blog/how-sentinelone-secures-the-ai-tools-that-act-like-users/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Side-Channel Attacks Against LLMs](https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [SmartGuard: Leveraging Large Language Models for Network Attack Detection through Audit Log Analysis and Summarization](https://arxiv.org/abs/2506.16981) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Sparse Autoencoders are Capable LLM Jailbreak Mitigators](https://arxiv.org/abs/2602.12418) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [SpecterOps Launches BloodHound Scentry to Accelerate the Practice of Identity Attack Path Management](https://www.darkreading.com/identity-access-management-security/specterops-launches-bloodhound-scentry) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [TCRL: Temporal-Coupled Adversarial Training for Robust Constrained Reinforcement Learning in Worst-Case Scenarios](https://arxiv.org/abs/2602.13040) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [TeamPCP Turns Cloud Infrastructure Into Crime Bots](https://www.darkreading.com/cloud-security/teampcp-cloud-infrastructure-crime-bots) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [The Buyer’s Guide to AI Usage Control](https://thehackernews.com/2026/02/the-buyers-guide-to-ai-usage-control.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [The strategic SIEM buyer’s guide: Choosing an AI-ready platform for the agentic era](https://www.microsoft.com/en-us/security/blog/2026/02/11/the-strategic-siem-buyers-guide-choosing-an-ai-ready-platform-for-the-agentic-era/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Those 'Summarize With AI' Buttons May Be Lying to You](https://www.darkreading.com/cyber-risk/summarize-ai-buttons-may-be-lying) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Threat Intelligence Automation](https://www.recordedfuture.com/blog/threat-intelligence-automation) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [ThreatsDay Bulletin: Codespaces RCE, AsyncRAT C2, BYOVD Abuse, AI Cloud Intrusions & 15+ Stories](https://thehackernews.com/2026/02/threatsday-bulletin-codespaces-rce.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Visual Memory Injection Attacks for Multi-Turn Conversations](https://arxiv.org/abs/2602.15927) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Webinar: How Modern SOC Teams Use AI and Context to Investigate Cloud Breaches Faster](https://thehackernews.com/2026/02/cloud-forensics-webinar-learn-how-ai.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Weekly Recap: Outlook Add-Ins Hijack, 0-Day Patches, Wormable Botnet & AI Malware](https://thehackernews.com/2026/02/weekly-recap-outlook-add-ins-hijack-0.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Weight space Detection of Backdoors in LoRA Adapters](https://arxiv.org/abs/2602.15195) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Weight space Detection of Backdoors in LoRA Adapters](https://arxiv.org/abs/2602.15195) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [When Your AI Coding Plugin Starts Picking Your Dependencies: Marketplace Skills and Dependency Hijack in Claude Code](https://www.sentinelone.com/blog/marketplace-skills-and-dependency-hijack-in-claude-code/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [X-MAP: eXplainable Misclassification Analysis and Profiling for Spam and Phishing Detection](https://arxiv.org/abs/2602.15298) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [ZAST.AI Raises $6M Pre-A to Scale "Zero False Positive" AI-Powered Code Security](https://thehackernews.com/2026/02/zastai-raises-6m-pre-to-scale-zero.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections](https://arxiv.org/abs/2602.15654) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections](https://arxiv.org/abs/2602.15654) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [⚡ Weekly Recap: AI Skill Malware, 31Tbps DDoS, Notepad++ Hack, LLM Backdoors and More](https://thehackernews.com/2026/02/weekly-recap-ai-skill-malware-31tbps.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |

---

[← Back to Index](index.md)
