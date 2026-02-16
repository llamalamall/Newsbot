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

Total rejected articles: **594**

| Title | Topic | Rejection Type | Rejection Reason |
|-------|-------|----------------|------------------|
| [AakarshakKaushal00/guardrail-layer](https://github.com/AakarshakKaushal00/guardrail-layer) | ai-security | applicability | Focuses on data privacy and access control using AI, not offensive security or automated offensive tooling. |
| [Carricacha/local-rag-system](https://github.com/Carricacha/local-rag-system) | ai-security | applicability | Repository is about Retrieval-Augmented Generation (RAG) for private AI memory, not offensive security or automated security testing. |
| [CloudDefenseAI/secure-agents-md](https://github.com/CloudDefenseAI/secure-agents-md) | ai-security | applicability | Focuses on governance and secure coding practices for AI agents but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [CtacPyc/AI-Home-Guardian](https://github.com/CtacPyc/AI-Home-Guardian) | ai-security | applicability | Repository focuses on home security and AI-driven surveillance, not offensive security or penetration testing. No evidence of AI/automation for offensive security. |
| [JohannFreddyLoayzaHuana/awesome-ai-coding-tools](https://github.com/JohannFreddyLoayzaHuana/awesome-ai-coding-tools) | ai-security | applicability | Repository is a curated list of AI coding tools, not focused on offensive security or automation for security testing. |
| [LoonMORTI/promptshield](https://github.com/LoonMORTI/promptshield) | ai-security | applicability | Focuses on protecting LLM applications from prompt injection and jailbreaks, which is defensive security, not offensive. No evidence of AI/automation being used for offensive security. |
| [Luxvil/ai-coding-rules](https://github.com/Luxvil/ai-coding-rules) | ai-security | applicability | Repository focuses on enhancing AI coding assistants but lacks any explicit connection to offensive security or automation/fuzzing for security purposes. |
| [ParraX123/meta-ai-bug-bounty](https://github.com/ParraX123/meta-ai-bug-bounty) | ai-security | applicability | Focuses on analyzing vulnerabilities in Meta AI's group chat but does not explicitly mention use of AI, automation, or fuzzing for offensive security; appears to be a manual or research-focused project. |
| [Rul1an/assay](https://github.com/Rul1an/assay) | ai-security | applicability | Repository focuses on runtime security and policy enforcement for AI agents but lacks explicit evidence of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [Sarb-jot/system-prompt-research](https://github.com/Sarb-jot/system-prompt-research) | ai-security | applicability | Researches prompt engineering and LLM security, but does not demonstrate offensive security tooling or automated attack/defense. |
| [Yosuraki/claude4-audit-recon](https://github.com/Yosuraki/claude4-audit-recon) | ai-security | applicability | Focuses on ethical auditing and introspection of AI models without offensive security or automation context. |
| [Zain3311/CVE-2025-49844](https://github.com/Zain3311/CVE-2025-49844) | ai-security | applicability | Repository is an exploit PoC for a Redis vulnerability with offensive security context, but there is no explicit evidence of AI, automation, or fuzzing being used in the exploit or its description. |
| [datacline/open-threat-detector](https://github.com/datacline/open-threat-detector) | ai-security | applicability | Focuses on detecting shadow AI threats in organizational environments but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [ethicxlhuman/security-automation-insights](https://github.com/ethicxlhuman/security-automation-insights) | ai-security | applicability | The repository focuses on automation and AI in security operations and compliance, but lacks explicit evidence of offensive security context such as penetration testing, red teaming, vulnerability analysis, exploit development, or malware analysis. The topics and description do not demonstrate the use of AI/automation/fuzzing for offensive security purposes. |
| [inkog-io/inkog](https://github.com/inkog-io/inkog) | ai-security | applicability | Focuses on static analysis and pre-flight checks for AI agents, but lacks explicit mention of offensive security, penetration testing, or fuzzing use cases. |
| [jenishsoftx6/ai-compliance-risk-insights](https://github.com/jenishsoftx6/ai-compliance-risk-insights) | ai-security | applicability | Repository focuses on AI for financial risk management and compliance, not on offensive security or automated security testing. |
| [labkomputerinformatika/HISSI-Policy-Concept](https://github.com/labkomputerinformatika/HISSI-Policy-Concept) | ai-security | applicability | Focuses on policy concepts for AI security in robotics and supply chain, not on offensive security or the use of AI/automation/fuzzing for security testing. |
| [luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock) | ai-security | applicability | Repository focuses on securing AI agents with egress proxy and integrity monitoring but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [melanynewmown790/healthcare-assistant](https://github.com/melanynewmown790/healthcare-assistant) | ai-security | applicability | Healthcare assistant with AI features, not related to offensive security or automation for penetration testing. |
| [rizkycsv/PromptGuard](https://github.com/rizkycsv/PromptGuard) | ai-security | applicability | Focuses on safeguarding and detecting regressions in LLMs, but does not explicitly demonstrate offensive security use or automation for offensive purposes. |
| [roynaldo1234/meta-ai-bug-bounty](https://github.com/roynaldo1234/meta-ai-bug-bounty) | ai-security | applicability | Focuses on AI security and bug bounty, but lacks explicit mention of AI/automation/fuzzing being used for offensive security tooling or automation. |
| [sairysee/aappmart](https://github.com/sairysee/aappmart) | ai-security | applicability | Mentions offensive security and automation, but description and topics suggest a general-purpose marketplace with security-related keywords, not an explicit offensive security AI/automation tool. |
| [stacklok/toolhive-studio](https://github.com/stacklok/toolhive-studio) | ai-security | applicability | Mentions AI agents but lacks explicit offensive security focus or automation for security testing. |
| [superagent-ai/brin](https://github.com/superagent-ai/brin) | ai-security | applicability | Focuses on securing package gateways and malware detection, but lacks explicit offensive security automation or AI-powered offensive tooling. |
| [Shaurya1456/AI-Vulverability-Scanner](https://github.com/Shaurya1456/AI-Vulverability-Scanner) | ai-security | credibility | No stars and recent creation date suggest no community validation; description is clear but project may be untested or unknown. |
| [kyle122497/llamator-mcp-server](https://github.com/kyle122497/llamator-mcp-server) | ai-security | credibility | No stars and very recent update; description is clear but no community validation. |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | ai-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | ai-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | ai-security | relevance | missing_ai_keywords |
| [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | ai-security | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | ai-security | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | ai-security | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
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
| [DynamoRIO/dynamorio](https://github.com/DynamoRIO/dynamorio) | binary-analysis | relevance | missing_ai_keywords |
| [HyperDbg/HyperDbg](https://github.com/HyperDbg/HyperDbg) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Morenoch26/OffsetInspect](https://github.com/Morenoch26/OffsetInspect) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [Rych156/PEAnalyzer](https://github.com/Rych156/PEAnalyzer) | binary-analysis | relevance | missing_ai_keywords |
| [Rych156/PEAnalyzer](https://github.com/Rych156/PEAnalyzer) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [ZukiZero/udbg](https://github.com/ZukiZero/udbg) | binary-analysis | relevance | missing_ai_keywords |
| [ZukiZero/udbg](https://github.com/ZukiZero/udbg) | binary-analysis | relevance | missing_ai_keywords |
| [camilo123433/Dridex-Malware-Unpacking-Report](https://github.com/camilo123433/Dridex-Malware-Unpacking-Report) | binary-analysis | relevance | missing_ai_keywords |
| [e-m-b-a/emba](https://github.com/e-m-b-a/emba) | binary-analysis | relevance | missing_ai_keywords |
| [horsicq/DIE-engine](https://github.com/horsicq/DIE-engine) | binary-analysis | relevance | missing_ai_keywords |
| [kevinmuoz/pybinwalk](https://github.com/kevinmuoz/pybinwalk) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [lief-project/LIEF](https://github.com/lief-project/LIEF) | binary-analysis | relevance | missing_ai_keywords |
| [packing-box/python-exeplot](https://github.com/packing-box/python-exeplot) | binary-analysis | relevance | missing_ai_keywords |
| [radareorg/radare2](https://github.com/radareorg/radare2) | binary-analysis | relevance | missing_ai_keywords |
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
| [z0mb13w4r/objtools](https://github.com/z0mb13w4r/objtools) | binary-analysis | relevance | missing_ai_keywords |
| [DUVALL707/ExploitMaze](https://github.com/DUVALL707/ExploitMaze) | malware-analysis | applicability | Duplicate of Repository 1; lacks explicit mention of AI, automation, or fuzzing for offensive security. |
| [Jeremy344555/rat](https://github.com/Jeremy344555/rat) | malware-analysis | applicability | Repository mentions remote access, exploitation, and malware analysis, but there is no explicit mention of AI, automation, or fuzzing for offensive security. |
| [LagZeroCode/HackWire](https://github.com/LagZeroCode/HackWire) | malware-analysis | applicability | While the repository mentions offensive security topics, there is no explicit evidence of AI, automation, or fuzzing usage in the description or topics. |
| [Truong882/ReVex](https://github.com/Truong882/ReVex) | malware-analysis | applicability | While it mentions exploit-development and malware-analysis in topics, the description and content focus on a browser-based HTTP repeater for web security testing, with no explicit mention of AI, automation, or fuzzing. |
| [mrfeelssss/ObfuscationZone](https://github.com/mrfeelssss/ObfuscationZone) | malware-analysis | applicability | Focuses on code obfuscation and anti-debugging, which are relevant to security, but there is no explicit mention of AI, automation, or fuzzing being used for offensive security purposes. |
| [ocramtec-marco/suspicious](https://github.com/ocramtec-marco/suspicious) | malware-analysis | applicability | Mentions machine learning and malware analysis, but lacks explicit indication of offensive security automation or AI-driven offensive tooling. |
| [pedro00715/C3_CRT_Python](https://github.com/pedro00715/C3_CRT_Python) | malware-analysis | applicability | Mentions automation and some security topics, but no explicit mention of AI, ML, or fuzzing for offensive security. Description is vague about automation's role. |
| [penxpkj/Defensive-Security-Hub](https://github.com/penxpkj/Defensive-Security-Hub) | malware-analysis | applicability | The repository focuses on defensive security resources and lacks any mention of AI, automation, or fuzzing for offensive security. |
| [romeorone/ShellStrike](https://github.com/romeorone/ShellStrike) | malware-analysis | applicability | Focuses on shell scripting automation but lacks explicit offensive security automation or AI/ML context. |
| [timgerstel/suspicious_IPs](https://github.com/timgerstel/suspicious_IPs) | malware-analysis | applicability | While the repository involves malware analysis and penetration testing, it does not explicitly mention AI, automation, or fuzzing. |
| [zee839/APTBench](https://github.com/zee839/APTBench) | malware-analysis | applicability | Mentions LLMs and automation but focuses on software engineering and performance benchmarking, not offensive security or automated security testing. |
| [OnlyyxErika/Ciphey](https://github.com/OnlyyxErika/Ciphey) | malware-analysis | credibility | No stars and potentially a fork or duplicate; description is substantive but no community validation. |
| [neelamkhalid/Ciphey](https://github.com/neelamkhalid/Ciphey) | malware-analysis | credibility | No stars and unclear maintenance, but description is substantive and relevant. |
| [Abhishek-innovation/ShadowSploit](https://github.com/Abhishek-innovation/ShadowSploit) | malware-analysis | relevance | missing_ai_keywords |
| [Ahegaho/ExploitMaze](https://github.com/Ahegaho/ExploitMaze) | malware-analysis | relevance | missing_ai_keywords |
| [Ajoloid/cybersecurity-interview-boilerplate](https://github.com/Ajoloid/cybersecurity-interview-boilerplate) | malware-analysis | relevance | missing_ai_keywords |
| [Badasone/Cyberlivre](https://github.com/Badasone/Cyberlivre) | malware-analysis | relevance | missing_ai_keywords |
| [CYB3RMX/Qu1cksc0pe](https://github.com/CYB3RMX/Qu1cksc0pe) | malware-analysis | relevance | missing_ai_keywords |
| [CYB3RMX/Qu1cksc0pe](https://github.com/CYB3RMX/Qu1cksc0pe) | malware-analysis | relevance | missing_ai_keywords |
| [Coursa4lyfe/NekoFlare](https://github.com/Coursa4lyfe/NekoFlare) | malware-analysis | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline](https://github.com/CybercentreCanada/assemblyline) | malware-analysis | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline-service-urldownloader](https://github.com/CybercentreCanada/assemblyline-service-urldownloader) | malware-analysis | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline-service-urldownloader](https://github.com/CybercentreCanada/assemblyline-service-urldownloader) | malware-analysis | relevance | missing_ai_keywords |
| [DeadFox55YZ/ShadowSploit](https://github.com/DeadFox55YZ/ShadowSploit) | malware-analysis | relevance | missing_ai_keywords |
| [Extenedi/DeleteShadowCopies](https://github.com/Extenedi/DeleteShadowCopies) | malware-analysis | relevance | missing_ai_keywords |
| [Extenedi/DeleteShadowCopies](https://github.com/Extenedi/DeleteShadowCopies) | malware-analysis | relevance | missing_ai_keywords |
| [Gobabi25/python-obfuscator-CalypsisOBF](https://github.com/Gobabi25/python-obfuscator-CalypsisOBF) | malware-analysis | relevance | missing_ai_keywords |
| [Gobabi25/python-obfuscator-CalypsisOBF](https://github.com/Gobabi25/python-obfuscator-CalypsisOBF) | malware-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | malware-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | malware-analysis | relevance | missing_ai_keywords |
| [JerryJev1/image-malware-detection-model](https://github.com/JerryJev1/image-malware-detection-model) | malware-analysis | relevance | missing_ai_keywords |
| [JerryJev1/image-malware-detection-model](https://github.com/JerryJev1/image-malware-detection-model) | malware-analysis | relevance | missing_ai_keywords |
| [JerryLinLinLin/huorong-virdb-changelog](https://github.com/JerryLinLinLin/huorong-virdb-changelog) | malware-analysis | relevance | missing_ai_keywords |
| [Karthik-reddy6/aegistrace-threat-intelligence](https://github.com/Karthik-reddy6/aegistrace-threat-intelligence) | malware-analysis | relevance | missing_ai_keywords |
| [KasunCSB/Live-Malware-DB](https://github.com/KasunCSB/Live-Malware-DB) | malware-analysis | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | malware-analysis | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | malware-analysis | relevance | missing_ai_keywords |
| [LFBaptista/IAmAntimalware](https://github.com/LFBaptista/IAmAntimalware) | malware-analysis | relevance | missing_ai_keywords |
| [LFBaptista/IAmAntimalware](https://github.com/LFBaptista/IAmAntimalware) | malware-analysis | relevance | missing_ai_keywords |
| [LadyPatricia/198macros-v1.4.0](https://github.com/LadyPatricia/198macros-v1.4.0) | malware-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | malware-analysis | relevance | missing_ai_keywords |
| [Rohan17182004/SmrtiLog](https://github.com/Rohan17182004/SmrtiLog) | malware-analysis | relevance | missing_ai_keywords |
| [Soocile/ShadowStrike](https://github.com/Soocile/ShadowStrike) | malware-analysis | relevance | missing_ai_keywords |
| [Soocile/ShadowStrike](https://github.com/Soocile/ShadowStrike) | malware-analysis | relevance | missing_ai_keywords |
| [Threatwise/attack-rs](https://github.com/Threatwise/attack-rs) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | malware-analysis | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | malware-analysis | relevance | missing_ai_keywords |
| [WilliamLCardoso/ShellStrike](https://github.com/WilliamLCardoso/ShellStrike) | malware-analysis | relevance | missing_ai_keywords |
| [WilliamLCardoso/ShellStrike](https://github.com/WilliamLCardoso/ShellStrike) | malware-analysis | relevance | missing_ai_keywords |
| [camilo123433/Dridex-Malware-Unpacking-Report](https://github.com/camilo123433/Dridex-Malware-Unpacking-Report) | malware-analysis | relevance | missing_ai_keywords |
| [enzoplaaygamemg12/gtfobinSUID](https://github.com/enzoplaaygamemg12/gtfobinSUID) | malware-analysis | relevance | missing_ai_keywords |
| [ferxxo2024/PenetrationSystem](https://github.com/ferxxo2024/PenetrationSystem) | malware-analysis | relevance | missing_ai_keywords |
| [ferxxo2024/PenetrationSystem](https://github.com/ferxxo2024/PenetrationSystem) | malware-analysis | relevance | missing_ai_keywords |
| [fhgggggggggggggggggggg/IntrudeLab](https://github.com/fhgggggggggggggggggggg/IntrudeLab) | malware-analysis | relevance | missing_ai_keywords |
| [gofokili/EDR-Freeze](https://github.com/gofokili/EDR-Freeze) | malware-analysis | relevance | missing_ai_keywords |
| [hiephoiga1166/MidnightRAT-Payload](https://github.com/hiephoiga1166/MidnightRAT-Payload) | malware-analysis | relevance | missing_ai_keywords |
| [hiephoiga1166/MidnightRAT-Payload](https://github.com/hiephoiga1166/MidnightRAT-Payload) | malware-analysis | relevance | missing_ai_keywords |
| [ibaneez/VirusTotalJsonDownloader](https://github.com/ibaneez/VirusTotalJsonDownloader) | malware-analysis | relevance | missing_ai_keywords |
| [kal21k/HWBP-DEP-Bypass](https://github.com/kal21k/HWBP-DEP-Bypass) | malware-analysis | relevance | missing_ai_keywords |
| [kenttibusiness/scamnet](https://github.com/kenttibusiness/scamnet) | malware-analysis | relevance | missing_ai_keywords |
| [lukenixon8/CryptInject](https://github.com/lukenixon8/CryptInject) | malware-analysis | relevance | missing_ai_keywords |
| [malwaredb/malwaredb-rs](https://github.com/malwaredb/malwaredb-rs) | malware-analysis | relevance | missing_ai_keywords |
| [mreshuu/STForensicMacOS](https://github.com/mreshuu/STForensicMacOS) | malware-analysis | relevance | missing_ai_keywords |
| [mreshuu/STForensicMacOS](https://github.com/mreshuu/STForensicMacOS) | malware-analysis | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | malware-analysis | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | malware-analysis | relevance | missing_ai_keywords |
| [prateek123s/HWBP-DEP-Bypass](https://github.com/prateek123s/HWBP-DEP-Bypass) | malware-analysis | relevance | missing_ai_keywords |
| [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) | malware-analysis | relevance | missing_ai_keywords |
| [radareorg/radare2](https://github.com/radareorg/radare2) | malware-analysis | relevance | missing_ai_keywords |
| [reuteras/dfirws](https://github.com/reuteras/dfirws) | malware-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | malware-analysis | relevance | missing_ai_keywords |
| [spontopt/StyxLoaderX-EDR-Evasion](https://github.com/spontopt/StyxLoaderX-EDR-Evasion) | malware-analysis | relevance | missing_ai_keywords |
| [vmkspv/lenspect](https://github.com/vmkspv/lenspect) | malware-analysis | relevance | missing_ai_keywords |
| [Leywkeny/WinNT-add-system-user-injector](https://github.com/Leywkeny/WinNT-add-system-user-injector) | offensive-security | applicability | Focuses on system administration and automation without offensive security context or AI usage. |
| [Maamitiana/cybersec-projects](https://github.com/Maamitiana/cybersec-projects) | offensive-security | applicability | Mentions automation scripts and AI in topics, but lacks explicit evidence that AI or automation is used for offensive security tasks (no details in description or topics). |
| [Quocton1/kali-linux-teaching-course-live](https://github.com/Quocton1/kali-linux-teaching-course-live) | offensive-security | applicability | While the repository covers penetration testing and mentions security automation, there is no explicit evidence of AI, automation, or fuzzing being used for offensive security in the description or topics. |
| [SanhitaVichare/temp-os](https://github.com/SanhitaVichare/temp-os) | offensive-security | applicability | Mentions offensive security topics but no evidence of AI, automation, or fuzzing for offensive security; focuses on Fedora installation. |
| [Sylphoraz/SharpAllowedToAct-Modify](https://github.com/Sylphoraz/SharpAllowedToAct-Modify) | offensive-security | applicability | Focuses on post-exploitation without mentioning AI, automation, or fuzzing. |
| [modifiable-japaneseiris792/r-shell](https://github.com/modifiable-japaneseiris792/r-shell) | offensive-security | applicability | Repository is focused on building an SSH client and reverse shells for remote management, with no mention of AI, automation, or fuzzing for offensive security. |
| [sairysee/aappmart](https://github.com/sairysee/aappmart) | offensive-security | applicability | Although the topics and description mention offensive security and AI/automation-related terms, there is no explicit evidence that the repository demonstrates the use of AI, automation, or fuzzing for offensive security. The description is focused on building an online marketplace. |
| [Froezens/Python-Blacklist-Breaker](https://github.com/Froezens/Python-Blacklist-Breaker) | offensive-security | credibility | No stars and no community validation; description is clear but repository is unvalidated and could be a toy project. |
| [ahmetdrak/drakben](https://github.com/ahmetdrak/drakben) | offensive-security | credibility | Very low star count (4) and future last update date suggest possible toy project or placeholder; otherwise, description is substantive. |
| [secwexen/aapp-mart](https://github.com/secwexen/aapp-mart) | offensive-security | credibility | Low stars count and outdated repository with last update in 2026, suggesting inactive maintenance. |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | offensive-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | offensive-security | relevance | missing_ai_keywords |
| [AKURHULA/LLMSecurityGuide](https://github.com/AKURHULA/LLMSecurityGuide) | offensive-security | relevance | missing_ai_keywords |
| [Aviwe45/metasploit-for-beginners](https://github.com/Aviwe45/metasploit-for-beginners) | offensive-security | relevance | missing_ai_keywords |
| [Aviwe45/metasploit-for-beginners](https://github.com/Aviwe45/metasploit-for-beginners) | offensive-security | relevance | missing_ai_keywords |
| [Eabnfccblls/awesome-cybersecurity-tools](https://github.com/Eabnfccblls/awesome-cybersecurity-tools) | offensive-security | relevance | missing_ai_keywords |
| [Eabnfccblls/awesome-cybersecurity-tools](https://github.com/Eabnfccblls/awesome-cybersecurity-tools) | offensive-security | relevance | missing_ai_keywords |
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
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [MiguelArmando/Bug-Bounty-Roadmap](https://github.com/MiguelArmando/Bug-Bounty-Roadmap) | offensive-security | relevance | missing_ai_keywords |
| [MiguelArmando/Bug-Bounty-Roadmap](https://github.com/MiguelArmando/Bug-Bounty-Roadmap) | offensive-security | relevance | missing_ai_keywords |
| [MuhammadSufyanSikander/emacs-tramp-rpc](https://github.com/MuhammadSufyanSikander/emacs-tramp-rpc) | offensive-security | relevance | missing_ai_keywords |
| [MuhammadSufyanSikander/emacs-tramp-rpc](https://github.com/MuhammadSufyanSikander/emacs-tramp-rpc) | offensive-security | relevance | missing_ai_keywords |
| [Rakum713/ColdWer](https://github.com/Rakum713/ColdWer) | offensive-security | relevance | missing_ai_keywords |
| [Rakum713/ColdWer](https://github.com/Rakum713/ColdWer) | offensive-security | relevance | missing_ai_keywords |
| [Ramborat1013/BreakerZero_PasswordCracker_v1.0](https://github.com/Ramborat1013/BreakerZero_PasswordCracker_v1.0) | offensive-security | relevance | missing_ai_keywords |
| [Trapsta1467/sherluck](https://github.com/Trapsta1467/sherluck) | offensive-security | relevance | missing_ai_keywords |
| [Trapsta1467/sherluck](https://github.com/Trapsta1467/sherluck) | offensive-security | relevance | missing_ai_keywords |
| [Trapsta1467/sherluck](https://github.com/Trapsta1467/sherluck) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [aliwioiod/speedloader](https://github.com/aliwioiod/speedloader) | offensive-security | relevance | missing_ai_keywords |
| [aliwioiod/speedloader](https://github.com/aliwioiod/speedloader) | offensive-security | relevance | missing_ai_keywords |
| [aliwioiod/speedloader](https://github.com/aliwioiod/speedloader) | offensive-security | relevance | missing_ai_keywords |
| [enzoplaaygamemg12/gtfobinSUID](https://github.com/enzoplaaygamemg12/gtfobinSUID) | offensive-security | relevance | missing_ai_keywords |
| [halilkirazkaya/gecit](https://github.com/halilkirazkaya/gecit) | offensive-security | relevance | missing_ai_keywords |
| [halilkirazkaya/gecit](https://github.com/halilkirazkaya/gecit) | offensive-security | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | offensive-security | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | offensive-security | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | offensive-security | relevance | missing_ai_keywords |
| [lizxyyyc/sc-reentrancy-attack](https://github.com/lizxyyyc/sc-reentrancy-attack) | offensive-security | relevance | missing_ai_keywords |
| [pepitopere666/WireTapper](https://github.com/pepitopere666/WireTapper) | offensive-security | relevance | missing_ai_keywords |
| [pepitopere666/WireTapper](https://github.com/pepitopere666/WireTapper) | offensive-security | relevance | missing_ai_keywords |
| [praetorian-inc/brutus](https://github.com/praetorian-inc/brutus) | offensive-security | relevance | missing_ai_keywords |
| [praetorian-inc/brutus](https://github.com/praetorian-inc/brutus) | offensive-security | relevance | missing_ai_keywords |
| [vishalo7o1/chronix](https://github.com/vishalo7o1/chronix) | offensive-security | relevance | missing_ai_keywords |
| [vishalo7o1/chronix](https://github.com/vishalo7o1/chronix) | offensive-security | relevance | missing_ai_keywords |
| [voltsparx/NetLoader-X](https://github.com/voltsparx/NetLoader-X) | offensive-security | relevance | missing_ai_keywords |
| [voltsparx/NetLoader-X](https://github.com/voltsparx/NetLoader-X) | offensive-security | relevance | missing_ai_keywords |
| [Kasim200429/GoBypass403](https://github.com/Kasim200429/GoBypass403) | penetration-testing | applicability | The repository is a tool for bypassing 403 errors during penetration testing but does not demonstrate the use of AI, automation, or fuzzing. |
| [NINJA45FFS1/security-tools-hacking](https://github.com/NINJA45FFS1/security-tools-hacking) | penetration-testing | applicability | Manual penetration testing framework; no evidence of AI, automation, or fuzzing components. |
| [Olivaire/Fscan-Output-POC-Parser](https://github.com/Olivaire/Fscan-Output-POC-Parser) | penetration-testing | applicability | Mentions automated vulnerability scanning, but no explicit indication of AI, ML, or advanced fuzzing techniques for offensive security. |
| [ParraX123/meta-ai-bug-bounty](https://github.com/ParraX123/meta-ai-bug-bounty) | penetration-testing | applicability | Focuses on bug bounty and vulnerability analysis in AI systems, but lacks explicit mention of automation, AI-driven tools, or fuzzing for offensive security. |
| [Quocton1/kali-linux-teaching-course-live](https://github.com/Quocton1/kali-linux-teaching-course-live) | penetration-testing | applicability | Duplicate of Repository 0. No explicit evidence of AI, automation, or fuzzing for offensive security. |
| [SafwanSaleem/Subdomain-port-scanner-passive](https://github.com/SafwanSaleem/Subdomain-port-scanner-passive) | penetration-testing | applicability | Focuses on passive reconnaissance without offensive security context or AI usage. |
| [VAZlabs/cyber-find](https://github.com/VAZlabs/cyber-find) | penetration-testing | applicability | OSINT tool for reconnaissance; no explicit mention of AI, automation, or fuzzing for offensive security. |
| [arqi-io/zphisher](https://github.com/arqi-io/zphisher) | penetration-testing | applicability | Automated phishing tool for security assessments, but no explicit mention of AI, ML, or fuzzing; only automation is present. |
| [bac0nnfires/wslkalisetup](https://github.com/bac0nnfires/wslkalisetup) | penetration-testing | applicability | Automates setup of Kali tools but does not mention AI, ML, or fuzzing; focuses on scripting and environment setup. |
| [dagule/blackarch-i3-kvm-setup](https://github.com/dagule/blackarch-i3-kvm-setup) | penetration-testing | applicability | Automates OS and environment setup for penetration testing, but does not automate offensive security tasks or use AI/fuzzing. |
| [gubogushod/cyphisher](https://github.com/gubogushod/cyphisher) | penetration-testing | applicability | Framework for phishing awareness and education; no explicit mention of AI, automation, or fuzzing for offensive security. |
| [jimmyner009/Krafter](https://github.com/jimmyner009/Krafter) | penetration-testing | applicability | Mentions penetration testing and red teaming, but no explicit evidence of AI, automation, or fuzzing being used for offensive security in the description or topics. |
| [modifiable-japaneseiris792/r-shell](https://github.com/modifiable-japaneseiris792/r-shell) | penetration-testing | applicability | Repository focuses on remote shell access and penetration testing but does not mention AI, automation, or fuzzing in its description or topics. |
| [mohamedelalfy27/argus](https://github.com/mohamedelalfy27/argus) | penetration-testing | applicability | Mentions penetration-testing and ethical-hacking, but the AI/automation component is about agent observability, not offensive security. No explicit evidence of AI/automation being used for offensive operations. |
| [romeorone/ShellStrike](https://github.com/romeorone/ShellStrike) | penetration-testing | applicability | General-purpose shell scripting toolkit; while it mentions automation and some security topics, it does not demonstrate AI, fuzzing, or offensive security automation. |
| [swathigoud/WhisperNet](https://github.com/swathigoud/WhisperNet) | penetration-testing | applicability | The repository is a password generator tool for penetration testing but does not mention AI, automation, or fuzzing explicitly. |
| [timgerstel/suspicious_IPs](https://github.com/timgerstel/suspicious_IPs) | penetration-testing | applicability | The repository focuses on collecting suspicious IPs from a honeypot but does not demonstrate the use of AI, automation, or fuzzing for offensive security. |
| [usa2692/noemvex-wayback](https://github.com/usa2692/noemvex-wayback) | penetration-testing | applicability | Focuses on passive subdomain enumeration and file discovery, with no mention of AI, automation, or fuzzing in the context of offensive security. |
| [venom4044/Web-Vulnerability-Attack-Defense-and-Patch-Experimentation-on-the-RailsGoat-Application](https://github.com/venom4044/Web-Vulnerability-Attack-Defense-and-Patch-Experimentation-on-the-RailsGoat-Application) | penetration-testing | applicability | Focuses on manual vulnerability reproduction and patching; no mention of AI, automation, or fuzzing. |
| [ryzecx/vulscanner](https://github.com/ryzecx/vulscanner) | penetration-testing | credibility | Very low stars and new project, but description is clear and relevant; no obvious red flags. |
| [zee839/APTBench](https://github.com/zee839/APTBench) | penetration-testing | credibility | Recently updated but has only 1 star and limited community validation. The description is somewhat clear but lacks detail about implementation. |
| [Abhishek-innovation/ShadowSploit](https://github.com/Abhishek-innovation/ShadowSploit) | penetration-testing | relevance | missing_ai_keywords |
| [Ancescride/Ethical-Hacking-College_Project](https://github.com/Ancescride/Ethical-Hacking-College_Project) | penetration-testing | relevance | missing_ai_keywords |
| [Bienfait-Mutunzi/Awesome-Hacking-Learning-Path](https://github.com/Bienfait-Mutunzi/Awesome-Hacking-Learning-Path) | penetration-testing | relevance | missing_ai_keywords |
| [Chrimak/AD-Privilege-Escalation-Finder](https://github.com/Chrimak/AD-Privilege-Escalation-Finder) | penetration-testing | relevance | missing_ai_keywords |
| [DEVayman20/firewall-whitelist-admin](https://github.com/DEVayman20/firewall-whitelist-admin) | penetration-testing | relevance | missing_ai_keywords |
| [DEVayman20/firewall-whitelist-admin](https://github.com/DEVayman20/firewall-whitelist-admin) | penetration-testing | relevance | missing_ai_keywords |
| [DaveBNU/cortexai](https://github.com/DaveBNU/cortexai) | penetration-testing | relevance | missing_ai_keywords |
| [DeadFox55YZ/ShadowSploit](https://github.com/DeadFox55YZ/ShadowSploit) | penetration-testing | relevance | missing_ai_keywords |
| [Eunsei677383/Free-Passive](https://github.com/Eunsei677383/Free-Passive) | penetration-testing | relevance | missing_ai_keywords |
| [FaresArgus/artaxerxes](https://github.com/FaresArgus/artaxerxes) | penetration-testing | relevance | missing_ai_keywords |
| [Giufenix/ChicomaloTools](https://github.com/Giufenix/ChicomaloTools) | penetration-testing | relevance | missing_ai_keywords |
| [Icy-Senpal/bypass-all](https://github.com/Icy-Senpal/bypass-all) | penetration-testing | relevance | missing_ai_keywords |
| [Icy-Senpal/bypass-all](https://github.com/Icy-Senpal/bypass-all) | penetration-testing | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | penetration-testing | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | penetration-testing | relevance | missing_ai_keywords |
| [LordBooming/Smart-Access-Control-Auditor](https://github.com/LordBooming/Smart-Access-Control-Auditor) | penetration-testing | relevance | missing_ai_keywords |
| [Nerowmist/nullsec-flipper-suite](https://github.com/Nerowmist/nullsec-flipper-suite) | penetration-testing | relevance | missing_ai_keywords |
| [OWASP/wstg](https://github.com/OWASP/wstg) | penetration-testing | relevance | missing_ai_keywords |
| [Oz134/perishable-inventory-risk-engine](https://github.com/Oz134/perishable-inventory-risk-engine) | penetration-testing | relevance | missing_ai_keywords |
| [RoshanBetediya/minecraft-account-checker](https://github.com/RoshanBetediya/minecraft-account-checker) | penetration-testing | relevance | missing_ai_keywords |
| [TahaGameDev/Offensive-Security-Forensics-Portfolio](https://github.com/TahaGameDev/Offensive-Security-Forensics-Portfolio) | penetration-testing | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | penetration-testing | relevance | missing_ai_keywords |
| [Trimamkash/SqlKnife](https://github.com/Trimamkash/SqlKnife) | penetration-testing | relevance | missing_ai_keywords |
| [WilliamLCardoso/ShellStrike](https://github.com/WilliamLCardoso/ShellStrike) | penetration-testing | relevance | missing_ai_keywords |
| [Yaxiswagonwheel794/AbyssForge](https://github.com/Yaxiswagonwheel794/AbyssForge) | penetration-testing | relevance | missing_ai_keywords |
| [aaryan-1112/SQLMap-Inject-Suite-Pro](https://github.com/aaryan-1112/SQLMap-Inject-Suite-Pro) | penetration-testing | relevance | missing_ai_keywords |
| [abbassFarhat/hacker101-CTF-Solutions](https://github.com/abbassFarhat/hacker101-CTF-Solutions) | penetration-testing | relevance | missing_ai_keywords |
| [ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors](https://github.com/ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors) | penetration-testing | relevance | missing_ai_keywords |
| [aiatagramkonnect/hacker101-CTF-Solutions](https://github.com/aiatagramkonnect/hacker101-CTF-Solutions) | penetration-testing | relevance | missing_ai_keywords |
| [aidenateagain/ghostscan](https://github.com/aidenateagain/ghostscan) | penetration-testing | relevance | missing_ai_keywords |
| [carolinavigil/prickly](https://github.com/carolinavigil/prickly) | penetration-testing | relevance | missing_ai_keywords |
| [ferxxo2024/PenetrationSystem](https://github.com/ferxxo2024/PenetrationSystem) | penetration-testing | relevance | missing_ai_keywords |
| [fhgggggggggggggggggggg/IntrudeLab](https://github.com/fhgggggggggggggggggggg/IntrudeLab) | penetration-testing | relevance | missing_ai_keywords |
| [hanyshehata1510/RoboBack](https://github.com/hanyshehata1510/RoboBack) | penetration-testing | relevance | missing_ai_keywords |
| [huymini/pencall](https://github.com/huymini/pencall) | penetration-testing | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | penetration-testing | relevance | missing_ai_keywords |
| [kal21k/HWBP-DEP-Bypass](https://github.com/kal21k/HWBP-DEP-Bypass) | penetration-testing | relevance | missing_ai_keywords |
| [landoalva/jira-servicedesk-enum](https://github.com/landoalva/jira-servicedesk-enum) | penetration-testing | relevance | missing_ai_keywords |
| [landoalva/jira-servicedesk-enum](https://github.com/landoalva/jira-servicedesk-enum) | penetration-testing | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | penetration-testing | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | penetration-testing | relevance | missing_ai_keywords |
| [niago1967/ExploitHawk](https://github.com/niago1967/ExploitHawk) | penetration-testing | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | penetration-testing | relevance | missing_ai_keywords |
| [phiduong1230/kali-setup](https://github.com/phiduong1230/kali-setup) | penetration-testing | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | penetration-testing | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | penetration-testing | relevance | missing_ai_keywords |
| [prateek123s/HWBP-DEP-Bypass](https://github.com/prateek123s/HWBP-DEP-Bypass) | penetration-testing | relevance | missing_ai_keywords |
| [rix4uni/medium-writeups](https://github.com/rix4uni/medium-writeups) | penetration-testing | relevance | missing_ai_keywords |
| [rix4uni/resolvers](https://github.com/rix4uni/resolvers) | penetration-testing | relevance | missing_ai_keywords |
| [setyanoegraha/hackmyvm-writeups](https://github.com/setyanoegraha/hackmyvm-writeups) | penetration-testing | relevance | missing_ai_keywords |
| [spontopt/StyxLoaderX-EDR-Evasion](https://github.com/spontopt/StyxLoaderX-EDR-Evasion) | penetration-testing | relevance | missing_ai_keywords |
| [tushuuu01/Inventory](https://github.com/tushuuu01/Inventory) | penetration-testing | relevance | missing_ai_keywords |
| [tushuuu01/Inventory](https://github.com/tushuuu01/Inventory) | penetration-testing | relevance | missing_ai_keywords |
| [Bossthetigan/NOLO](https://github.com/Bossthetigan/NOLO) | red-team | applicability | The repository focuses on AI-powered PTZ tracking using YOLO but does not relate to offensive security or automation for security testing. |
| [LagZeroCode/HackWire](https://github.com/LagZeroCode/HackWire) | red-team | applicability | Mentions offensive security topics but no explicit mention of AI, automation, or fuzzing in the description or topics. |
| [MASHJJS/aTerm](https://github.com/MASHJJS/aTerm) | red-team | applicability | Mentions AI tools and red-team in topics, but the description and topics indicate a general-purpose developer terminal workspace, not an offensive security tool using AI/automation. |
| [OPBOY1203/redmind](https://github.com/OPBOY1203/redmind) | red-team | applicability | Mentions offensive security and machine learning, but no explicit evidence that AI/ML is used for offensive operations or automation; appears to be a collection of resources. |
| [Quocton1/kali-linux-teaching-course-live](https://github.com/Quocton1/kali-linux-teaching-course-live) | red-team | applicability | Focuses on teaching penetration testing and security automation but does not explicitly mention AI, ML, or fuzzing for offensive security. |
| [Teddiesarcosomal392/eye](https://github.com/Teddiesarcosomal392/eye) | red-team | applicability | Mentions AI models and red-team in topics, but the description and topics focus on memory preservation and conversations, not offensive security or automation/fuzzing. |
| [Zain3311/CVE-2025-49844](https://github.com/Zain3311/CVE-2025-49844) | red-team | applicability | Exploit repository for a CVE with AI/ML topics, but no explicit evidence of AI, automation, or fuzzing being used in the exploit or tooling. |
| [gubogushod/cyphisher](https://github.com/gubogushod/cyphisher) | red-team | applicability | Duplicate of Repository 2; no explicit AI, automation, or fuzzing for offensive security. |
| [rabeal21/Tea](https://github.com/rabeal21/Tea) | red-team | applicability | The repository focuses on generating TEA wallet addresses and does not explicitly mention AI, automation, or fuzzing for offensive security. |
| [usa2692/noemvex-wayback](https://github.com/usa2692/noemvex-wayback) | red-team | applicability | Duplicate of Repository 2. Focuses on passive enumeration and file discovery, with no explicit AI, automation, or fuzzing for offensive security. |
| [ahmetdrak/drakben](https://github.com/ahmetdrak/drakben) | red-team | credibility | Very low star count (4) despite ambitious claims; possible toy project or early stage. However, recently updated and description is clear. |
| [Ahirshath/nmap-cheatsheet-tr](https://github.com/Ahirshath/nmap-cheatsheet-tr) | red-team | relevance | missing_ai_keywords |
| [Akunpubg9236/proyecto_AICAD_JPereira](https://github.com/Akunpubg9236/proyecto_AICAD_JPereira) | red-team | relevance | missing_ai_keywords |
| [AlejandroZaZ/cybersecurity-tools](https://github.com/AlejandroZaZ/cybersecurity-tools) | red-team | relevance | missing_ai_keywords |
| [Astrosp/Awesome-OSINT-For-Everything](https://github.com/Astrosp/Awesome-OSINT-For-Everything) | red-team | relevance | missing_ai_keywords |
| [BishopFox/sliver](https://github.com/BishopFox/sliver) | red-team | relevance | missing_ai_keywords |
| [DEVayman20/firewall-whitelist-admin](https://github.com/DEVayman20/firewall-whitelist-admin) | red-team | relevance | missing_ai_keywords |
| [DEVayman20/firewall-whitelist-admin](https://github.com/DEVayman20/firewall-whitelist-admin) | red-team | relevance | missing_ai_keywords |
| [DeepZatakiya/OpenMalleableC2](https://github.com/DeepZatakiya/OpenMalleableC2) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | red-team | relevance | missing_ai_keywords |
| [Krizx6/IntrudeLab](https://github.com/Krizx6/IntrudeLab) | red-team | relevance | missing_ai_keywords |
| [Mazzy-Stars/lain_c2](https://github.com/Mazzy-Stars/lain_c2) | red-team | relevance | missing_ai_keywords |
| [Mazzy-Stars/lain_c2](https://github.com/Mazzy-Stars/lain_c2) | red-team | relevance | missing_ai_keywords |
| [Michael1-dav/red-teaming](https://github.com/Michael1-dav/red-teaming) | red-team | relevance | missing_ai_keywords |
| [Michael1-dav/red-teaming](https://github.com/Michael1-dav/red-teaming) | red-team | relevance | missing_ai_keywords |
| [Nerowmist/nullsec-flipper-suite](https://github.com/Nerowmist/nullsec-flipper-suite) | red-team | relevance | missing_ai_keywords |
| [Rakum713/ColdWer](https://github.com/Rakum713/ColdWer) | red-team | relevance | missing_ai_keywords |
| [ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors](https://github.com/ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors) | red-team | relevance | missing_ai_keywords |
| [ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors](https://github.com/ahmedawad22/Offense-to-Defense-A-Kali-Linux-Guide-to-Reverse-Shells-and-Backdoors) | red-team | relevance | missing_ai_keywords |
| [aidenateagain/ghostscan](https://github.com/aidenateagain/ghostscan) | red-team | relevance | missing_ai_keywords |
| [aidenateagain/ghostscan](https://github.com/aidenateagain/ghostscan) | red-team | relevance | missing_ai_keywords |
| [ali-ctf-player/HTB-reports](https://github.com/ali-ctf-player/HTB-reports) | red-team | relevance | missing_ai_keywords |
| [atulranjanz/Swatted-Webhook-Spammer](https://github.com/atulranjanz/Swatted-Webhook-Spammer) | red-team | relevance | missing_ai_keywords |
| [chrisgallenx/Interactive-MITRE-Tree](https://github.com/chrisgallenx/Interactive-MITRE-Tree) | red-team | relevance | missing_ai_keywords |
| [chrisgallenx/Interactive-MITRE-Tree](https://github.com/chrisgallenx/Interactive-MITRE-Tree) | red-team | relevance | missing_ai_keywords |
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
| [jenkinsmichpa/coconut_crab](https://github.com/jenkinsmichpa/coconut_crab) | red-team | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | red-team | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | red-team | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | red-team | relevance | missing_ai_keywords |
| [ksnnd32/redis_exploit](https://github.com/ksnnd32/redis_exploit) | red-team | relevance | missing_ai_keywords |
| [luq12-growagarden/Adversarial-Detection-Engineering-Framework](https://github.com/luq12-growagarden/Adversarial-Detection-Engineering-Framework) | red-team | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | red-team | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | red-team | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | red-team | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | red-team | relevance | missing_ai_keywords |
| [mods20hh/ZeroLogon-PoC-DC-Pwn](https://github.com/mods20hh/ZeroLogon-PoC-DC-Pwn) | red-team | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | red-team | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | red-team | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | red-team | relevance | missing_ai_keywords |
| [pepitopere666/WireTapper](https://github.com/pepitopere666/WireTapper) | red-team | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | red-team | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | red-team | relevance | missing_ai_keywords |
| [praetorian-inc/brutus](https://github.com/praetorian-inc/brutus) | red-team | relevance | missing_ai_keywords |
| [r0zhh/ASNHunter](https://github.com/r0zhh/ASNHunter) | red-team | relevance | missing_ai_keywords |
| [r0zhh/ASNHunter](https://github.com/r0zhh/ASNHunter) | red-team | relevance | missing_ai_keywords |
| [simar100/mft_reader](https://github.com/simar100/mft_reader) | red-team | relevance | missing_ai_keywords |
| [simar100/mft_reader](https://github.com/simar100/mft_reader) | red-team | relevance | missing_ai_keywords |
| [spontopt/StyxLoaderX-EDR-Evasion](https://github.com/spontopt/StyxLoaderX-EDR-Evasion) | red-team | relevance | missing_ai_keywords |
| [temboohms68/Flipper-Zero-IR-Signal-Generator](https://github.com/temboohms68/Flipper-Zero-IR-Signal-Generator) | red-team | relevance | missing_ai_keywords |
| [CanvizTechnologies/cloud-claw](https://github.com/CanvizTechnologies/cloud-claw) | reverse-engineering | applicability | AI assistant for workflow enhancement; no explicit connection to offensive security, automation, or fuzzing. |
| [DUVALL707/ExploitMaze](https://github.com/DUVALL707/ExploitMaze) | reverse-engineering | applicability | Focuses on vulnerability assessment and exploit development but lacks explicit mention of AI, automation, or fuzzing. |
| [JKASle/Inspector](https://github.com/JKASle/Inspector) | reverse-engineering | applicability | Transforms Google AI Studio exports for analysis; no evidence of offensive security, automation, or fuzzing. |
| [NebiyuSeyoum/exploring-the-true-nature-of-variable](https://github.com/NebiyuSeyoum/exploring-the-true-nature-of-variable) | reverse-engineering | applicability | Repository focuses on programming concepts, memory management, and reverse engineering, but does not mention AI, automation, or fuzzing in the context of offensive security. |
| [Olivaire/sleep-duck-eye-Detect-SleepMask](https://github.com/Olivaire/sleep-duck-eye-Detect-SleepMask) | reverse-engineering | applicability | Mentions automated security testing and malware detection, but no explicit evidence of AI, ML, or fuzzing for offensive security. Focus appears to be on detection/forensics. |
| [Truong882/ReVex](https://github.com/Truong882/ReVex) | reverse-engineering | applicability | Primarily a browser-based HTTP repeater for web security testing; no evidence of AI, automation, or fuzzing for offensive security. |
| [YamateKudashai/PHind](https://github.com/YamateKudashai/PHind) | reverse-engineering | applicability | Repository focuses on AI-powered semantic search for Laravel, not offensive security or automation/fuzzing for security testing. |
| [anto16jose/ai-chat-interface](https://github.com/anto16jose/ai-chat-interface) | reverse-engineering | applicability | Repository is an AI chat interface with no offensive security or automation for security testing context. |
| [by-reales/fripack](https://github.com/by-reales/fripack) | reverse-engineering | applicability | Focuses on packaging Frida scripts for reverse engineering, but does not mention AI, automation, or fuzzing for offensive security. |
| [dhesnut/gemini_gpt](https://github.com/dhesnut/gemini_gpt) | reverse-engineering | applicability | AI chat application with no explicit connection to offensive security, penetration testing, or automation for security testing. |
| [eslamfox100/AIDA](https://github.com/eslamfox100/AIDA) | reverse-engineering | applicability | Mentions AI and pentesting tools, but lacks explicit evidence of AI/automation/fuzzing being used for offensive security; description is vague about actual implementation. |
| [kingdenofficial/ReverseBox](https://github.com/kingdenofficial/ReverseBox) | reverse-engineering | applicability | Repository is about reversing text/data, not offensive security or AI/automation/fuzzing. |
| [mrfeelssss/ObfuscationZone](https://github.com/mrfeelssss/ObfuscationZone) | reverse-engineering | applicability | Repository is about code obfuscation and anti-debugging, which are relevant to security, but there is no explicit mention of AI, automation, or fuzzing. |
| [mulhala-100ttl/AIDA64-Network-Audit-2026](https://github.com/mulhala-100ttl/AIDA64-Network-Audit-2026) | reverse-engineering | applicability | The repository is focused on network auditing and inventory reporting without any mention of AI, automation, or fuzzing for offensive security. |
| [mwakidenis/UN-OFFICIAL-KPLC-TOKEN-HISTORY-VIEW](https://github.com/mwakidenis/UN-OFFICIAL-KPLC-TOKEN-HISTORY-VIEW) | reverse-engineering | applicability | The repository is focused on accessing token purchase history and does not involve AI, automation, or fuzzing for offensive security. |
| [mzmaaz60/unicor](https://github.com/mzmaaz60/unicor) | reverse-engineering | applicability | No evidence of offensive security or AI/automation for security. Focus is on trading and API data analysis. |
| [rdnrhm92/switch](https://github.com/rdnrhm92/switch) | reverse-engineering | applicability | The repository is a feature flag management platform for enterprise applications. While it mentions AI-tools and reverse-engineering in topics, there is no explicit evidence of AI, automation, or fuzzing being used for offensive security purposes. |
| [stepanovmykola/CryptInject](https://github.com/stepanovmykola/CryptInject) | reverse-engineering | applicability | While the repository mentions penetration testing and malware analysis, there is no explicit indication of AI, automation, or fuzzing being used. |
| [yassiroz/sekaictf-2025](https://github.com/yassiroz/sekaictf-2025) | reverse-engineering | applicability | Repository contains CTF challenges and writeups related to offensive security, but there is no explicit mention of AI, automation, or fuzzing usage. |
| [OnlyyxErika/Ciphey](https://github.com/OnlyyxErika/Ciphey) | reverse-engineering | credibility | No stars and potentially a fork or duplicate; description is substantive but no community validation. |
| [neelamkhalid/Ciphey](https://github.com/neelamkhalid/Ciphey) | reverse-engineering | credibility | No stars and no evidence of community validation, but description is clear and substantive. |
| [Abhishek-innovation/ShadowSploit](https://github.com/Abhishek-innovation/ShadowSploit) | reverse-engineering | relevance | missing_ai_keywords |
| [Abhishek-innovation/ShadowSploit](https://github.com/Abhishek-innovation/ShadowSploit) | reverse-engineering | relevance | missing_ai_keywords |
| [Ahegaho/ExploitMaze](https://github.com/Ahegaho/ExploitMaze) | reverse-engineering | relevance | missing_ai_keywords |
| [AlYElkooptan/DiaSymbolView](https://github.com/AlYElkooptan/DiaSymbolView) | reverse-engineering | relevance | missing_ai_keywords |
| [AlessandroBonomo28/HealthyIG](https://github.com/AlessandroBonomo28/HealthyIG) | reverse-engineering | relevance | missing_ai_keywords |
| [AlessandroBonomo28/HealthyIG](https://github.com/AlessandroBonomo28/HealthyIG) | reverse-engineering | relevance | missing_ai_keywords |
| [Ali632-lgtm/mcafee-tools](https://github.com/Ali632-lgtm/mcafee-tools) | reverse-engineering | relevance | missing_ai_keywords |
| [Bienfait-Mutunzi/Awesome-Hacking-Learning-Path](https://github.com/Bienfait-Mutunzi/Awesome-Hacking-Learning-Path) | reverse-engineering | relevance | missing_ai_keywords |
| [Crossie7/WeChat-Channels-Video-File-Decryption](https://github.com/Crossie7/WeChat-Channels-Video-File-Decryption) | reverse-engineering | relevance | missing_ai_keywords |
| [DeadFox55YZ/ShadowSploit](https://github.com/DeadFox55YZ/ShadowSploit) | reverse-engineering | relevance | missing_ai_keywords |
| [DeadFox55YZ/ShadowSploit](https://github.com/DeadFox55YZ/ShadowSploit) | reverse-engineering | relevance | missing_ai_keywords |
| [Dhruvchaudhary255/reverse](https://github.com/Dhruvchaudhary255/reverse) | reverse-engineering | relevance | missing_ai_keywords |
| [GeoloeG-IsT/agents-reverse-engineer](https://github.com/GeoloeG-IsT/agents-reverse-engineer) | reverse-engineering | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | reverse-engineering | relevance | missing_ai_keywords |
| [Laeteth/advanced-anti-sandbox-Virtual-Machine](https://github.com/Laeteth/advanced-anti-sandbox-Virtual-Machine) | reverse-engineering | relevance | missing_ai_keywords |
| [Laeteth/advanced-anti-sandbox-Virtual-Machine](https://github.com/Laeteth/advanced-anti-sandbox-Virtual-Machine) | reverse-engineering | relevance | missing_ai_keywords |
| [Laeteth/advanced-anti-sandbox-Virtual-Machine](https://github.com/Laeteth/advanced-anti-sandbox-Virtual-Machine) | reverse-engineering | relevance | missing_ai_keywords |
| [Mighty08war/PEBLoader.h](https://github.com/Mighty08war/PEBLoader.h) | reverse-engineering | relevance | missing_ai_keywords |
| [Omkar675/ImHex](https://github.com/Omkar675/ImHex) | reverse-engineering | relevance | missing_ai_keywords |
| [Rbel12b/Lpf2](https://github.com/Rbel12b/Lpf2) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [Spray6T9/dexter](https://github.com/Spray6T9/dexter) | reverse-engineering | relevance | missing_ai_keywords |
| [SteamDatabase/GameTracking-Deadlock](https://github.com/SteamDatabase/GameTracking-Deadlock) | reverse-engineering | relevance | missing_ai_keywords |
| [Terralyp/SunloginLP-Eanalysis-tool](https://github.com/Terralyp/SunloginLP-Eanalysis-tool) | reverse-engineering | relevance | missing_ai_keywords |
| [Terralyp/UnrealDbg-VT-engine](https://github.com/Terralyp/UnrealDbg-VT-engine) | reverse-engineering | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | reverse-engineering | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | reverse-engineering | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | reverse-engineering | relevance | missing_ai_keywords |
| [Ujwaldahal/dexdumper](https://github.com/Ujwaldahal/dexdumper) | reverse-engineering | relevance | missing_ai_keywords |
| [VectorlyApp/bluebox](https://github.com/VectorlyApp/bluebox) | reverse-engineering | relevance | missing_ai_keywords |
| [Winich007/samsung-umtz0](https://github.com/Winich007/samsung-umtz0) | reverse-engineering | relevance | missing_ai_keywords |
| [Winich007/samsung-umtz0](https://github.com/Winich007/samsung-umtz0) | reverse-engineering | relevance | missing_ai_keywords |
| [bfjesso/jesso-decompiler](https://github.com/bfjesso/jesso-decompiler) | reverse-engineering | relevance | missing_ai_keywords |
| [debbie23/Anker_Prime_BLE_hacking](https://github.com/debbie23/Anker_Prime_BLE_hacking) | reverse-engineering | relevance | missing_ai_keywords |
| [fromgabyaaye/UniPwn](https://github.com/fromgabyaaye/UniPwn) | reverse-engineering | relevance | missing_ai_keywords |
| [kal21k/HWBP-DEP-Bypass](https://github.com/kal21k/HWBP-DEP-Bypass) | reverse-engineering | relevance | missing_ai_keywords |
| [lukenixon8/CryptInject](https://github.com/lukenixon8/CryptInject) | reverse-engineering | relevance | missing_ai_keywords |
| [lukenixon8/CryptInject](https://github.com/lukenixon8/CryptInject) | reverse-engineering | relevance | missing_ai_keywords |
| [lympdegrin919fl/AnyDesk-Ultimate-2026](https://github.com/lympdegrin919fl/AnyDesk-Ultimate-2026) | reverse-engineering | relevance | missing_ai_keywords |
| [megakiyaiscool/Smart_Plug](https://github.com/megakiyaiscool/Smart_Plug) | reverse-engineering | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | reverse-engineering | relevance | missing_ai_keywords |
| [plichycode/DLL-Injection-Engine](https://github.com/plichycode/DLL-Injection-Engine) | reverse-engineering | relevance | missing_ai_keywords |
| [prateek123s/HWBP-DEP-Bypass](https://github.com/prateek123s/HWBP-DEP-Bypass) | reverse-engineering | relevance | missing_ai_keywords |
| [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) | reverse-engineering | relevance | missing_ai_keywords |
| [radareorg/radare2](https://github.com/radareorg/radare2) | reverse-engineering | relevance | missing_ai_keywords |
| [rizinorg/rz-libdemangle](https://github.com/rizinorg/rz-libdemangle) | reverse-engineering | relevance | missing_ai_keywords |
| [vascodavid/PICO8-Extractor](https://github.com/vascodavid/PICO8-Extractor) | reverse-engineering | relevance | missing_ai_keywords |
| [vascodavid/PICO8-Extractor](https://github.com/vascodavid/PICO8-Extractor) | reverse-engineering | relevance | missing_ai_keywords |
| [wisamna84/ps5-app-dumper](https://github.com/wisamna84/ps5-app-dumper) | reverse-engineering | relevance | missing_ai_keywords |
| [wowemulation-dev/cascette-py](https://github.com/wowemulation-dev/cascette-py) | reverse-engineering | relevance | missing_ai_keywords |
| [wowemulation-dev/cascette-rs](https://github.com/wowemulation-dev/cascette-rs) | reverse-engineering | relevance | missing_ai_keywords |
| [wowemulation-dev/cascette-rs](https://github.com/wowemulation-dev/cascette-rs) | reverse-engineering | relevance | missing_ai_keywords |
| [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content) | security-automation | applicability | Repository focuses on security automation for compliance and hardening, not offensive security or AI-driven tools. |
| [Frog456-dev/secwexen-arsenal](https://github.com/Frog456-dev/secwexen-arsenal) | security-automation | applicability | Curates offensive and automation tools, but does not explicitly demonstrate the use of AI, automation, or fuzzing for offensive security in the description or topics. |
| [GhostkillerMMIX/enterprise-soc-blueprint](https://github.com/GhostkillerMMIX/enterprise-soc-blueprint) | security-automation | applicability | Focus is on SOC, SIEM, and security automation for defense, not offensive security. No evidence of AI/automation for offensive operations. |
| [Invertebrate-cankerweed632/awesome-devsecops](https://github.com/Invertebrate-cankerweed632/awesome-devsecops) | security-automation | applicability | Repository is a DevSecOps tools list, with no explicit mention of offensive security or AI/automation/fuzzing usage for offensive operations. |
| [Quocton1/kali-linux-teaching-course-live](https://github.com/Quocton1/kali-linux-teaching-course-live) | security-automation | applicability | Repository focuses on teaching Kali Linux and penetration testing, but lacks explicit evidence of AI, automation, or fuzzing usage for offensive security in description or topics. |
| [Thenguyenvn/rsync-backup-solution](https://github.com/Thenguyenvn/rsync-backup-solution) | security-automation | applicability | Repository is about automated backups and data protection, not about offensive security or the use of AI/automation/fuzzing for security testing. |
| [ValiantKaka/Phishing-Email-Analysis](https://github.com/ValiantKaka/Phishing-Email-Analysis) | security-automation | applicability | The repository focuses on analyzing phishing emails and provides actionable insights for healthcare organizations, which is defensive security. While it mentions 'security-automation' and related topics, there is no explicit evidence of AI, automation, or fuzzing being used for offensive security purposes such as penetration testing, red teaming, vulnerability detection, exploit development, or automated malware analysis. |
| [Yjaballi/cybersecurity_roadmap](https://github.com/Yjaballi/cybersecurity_roadmap) | security-automation | applicability | Focuses on cybersecurity career development and education, not on AI/automation/fuzzing for offensive security. |
| [akutemmanuel/StormSec](https://github.com/akutemmanuel/StormSec) | security-automation | applicability | The repository mentions offensive security keywords such as penetration-testing, malware-analysis, and security-automation, but lacks explicit evidence of AI, automation, or fuzzing being used for offensive security purposes in the description or topics. |
| [anubis01sk/splunk-detection-engineer-agent](https://github.com/anubis01sk/splunk-detection-engineer-agent) | security-automation | applicability | Repository uses AI for generating Splunk SPL queries for security analytics and detection engineering, but does not explicitly mention offensive security, penetration testing, or red team automation. |
| [ar157209/soc-roadmap-2026](https://github.com/ar157209/soc-roadmap-2026) | security-automation | applicability | The repository focuses on SOC analyst training, automation, and machine learning, but its topics and description are centered on blue-team (defensive) operations rather than offensive security. There is no explicit evidence of AI/automation/fuzzing being used for offensive security purposes such as penetration testing, red teaming, or exploit/malware analysis. |
| [bznbnn/Code-Reviewer-AI](https://github.com/bznbnn/Code-Reviewer-AI) | security-automation | applicability | The repository focuses on AI-driven code review and coding assistance, but does not explicitly mention offensive security, penetration testing, vulnerability detection, exploit development, or malware analysis. The 'security-automation' topic is present, but context is generic and not tied to offensive security. |
| [designershount/astra](https://github.com/designershount/astra) | security-automation | applicability | Mentions penetration-testing-framework and security-automation, but description and topics focus on AI agent environments, not offensive security or automation for security testing. |
| [mikehubers/Awesome-AI-For-Security](https://github.com/mikehubers/Awesome-AI-For-Security) | security-automation | applicability | Curated list of resources; not a tool or implementation, and does not demonstrate the use of AI/automation/fuzzing for offensive security. |
| [zricethezav/h1domains](https://github.com/zricethezav/h1domains) | security-automation | applicability | Repository provides a list of domains for HackerOne but does not involve AI, automation, or fuzzing for offensive security. |
| [sairysee/aappmart](https://github.com/sairysee/aappmart) | security-automation | credibility | No stars, but recently updated and description is clear and relevant. No red flags for malicious intent. |
| [CybercentreCanada/assemblyline](https://github.com/CybercentreCanada/assemblyline) | security-automation | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline](https://github.com/CybercentreCanada/assemblyline) | security-automation | relevance | missing_ai_keywords |
| [DefectDojo/django-DefectDojo](https://github.com/DefectDojo/django-DefectDojo) | security-automation | relevance | missing_ai_keywords |
| [Fireresistive-bottleneck299/aws-jit-access](https://github.com/Fireresistive-bottleneck299/aws-jit-access) | security-automation | relevance | missing_ai_keywords |
| [Fireresistive-bottleneck299/aws-jit-access](https://github.com/Fireresistive-bottleneck299/aws-jit-access) | security-automation | relevance | missing_ai_keywords |
| [Gervis123212/azure-sentinel-honeypot](https://github.com/Gervis123212/azure-sentinel-honeypot) | security-automation | relevance | missing_ai_keywords |
| [Gervis123212/azure-sentinel-honeypot](https://github.com/Gervis123212/azure-sentinel-honeypot) | security-automation | relevance | missing_ai_keywords |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [SecObserve/SecObserve](https://github.com/SecObserve/SecObserve) | security-automation | relevance | missing_ai_keywords |
| [Shubh2-0/Spring_Security](https://github.com/Shubh2-0/Spring_Security) | security-automation | relevance | missing_ai_keywords |
| [Shubh2-0/Spring_Security](https://github.com/Shubh2-0/Spring_Security) | security-automation | relevance | missing_ai_keywords |
| [TianTheHacker/cloudflare-auto-protection](https://github.com/TianTheHacker/cloudflare-auto-protection) | security-automation | relevance | missing_ai_keywords |
| [WhyN0tTh0/enterprise-attack-simulator](https://github.com/WhyN0tTh0/enterprise-attack-simulator) | security-automation | relevance | missing_ai_keywords |
| [hitq11/AdaPol](https://github.com/hitq11/AdaPol) | security-automation | relevance | missing_ai_keywords |
| [hitq11/AdaPol](https://github.com/hitq11/AdaPol) | security-automation | relevance | missing_ai_keywords |
| [hitq11/AdaPol](https://github.com/hitq11/AdaPol) | security-automation | relevance | missing_ai_keywords |
| [kynaan5353/cargo-recon](https://github.com/kynaan5353/cargo-recon) | security-automation | relevance | missing_ai_keywords |
| [kynaan5353/cargo-recon](https://github.com/kynaan5353/cargo-recon) | security-automation | relevance | missing_ai_keywords |
| [kynaan5353/cargo-recon](https://github.com/kynaan5353/cargo-recon) | security-automation | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | security-automation | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | security-automation | relevance | missing_ai_keywords |
| [mahaishu/n8n-CyberSecurity-Workflows](https://github.com/mahaishu/n8n-CyberSecurity-Workflows) | security-automation | relevance | missing_ai_keywords |
| [octivi/update-securitytxt-expires](https://github.com/octivi/update-securitytxt-expires) | security-automation | relevance | missing_ai_keywords |
| [octivi/update-securitytxt-expires](https://github.com/octivi/update-securitytxt-expires) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [quinntrys/devsecops](https://github.com/quinntrys/devsecops) | security-automation | relevance | missing_ai_keywords |
| [quinntrys/devsecops](https://github.com/quinntrys/devsecops) | security-automation | relevance | missing_ai_keywords |
| [securego/gosec](https://github.com/securego/gosec) | security-automation | relevance | missing_ai_keywords |
| [securego/gosec](https://github.com/securego/gosec) | security-automation | relevance | missing_ai_keywords |
| [securego/gosec](https://github.com/securego/gosec) | security-automation | relevance | missing_ai_keywords |
| [wazuh/wazuh](https://github.com/wazuh/wazuh) | security-automation | relevance | missing_ai_keywords |
| [wazuh/wazuh](https://github.com/wazuh/wazuh) | security-automation | relevance | missing_ai_keywords |
| [&#x26;#xa;AI-Powered Knowledge Graph Generator &#x26; APTs, (Thu, Feb 12th)](https://isc.sans.edu/diary/rss/32712) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [260K+ Chrome Users Duped by Fake AI Browser Extensions](https://www.darkreading.com/cyber-risk/chrome-fake-ai-browser-extensions) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [8-Minute Access: AI Accelerates Breach of AWS Environment](https://www.darkreading.com/cloud-security/8-minute-access-ai-aws-environment-breach) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [80% of Fortune 500 use active AI Agents: Observability, governance, and security shape the new frontier](https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
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
| [Autonomous Threat Operations in action: Real results from Recorded Future’s own SOC team | Recorded Future](https://www.recordedfuture.com/blog/autonomous-threat-operations-in-action) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Backdoor Attacks on Contrastive Continual Learning for IoT Systems](https://arxiv.org/abs/2602.13062) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System](https://arxiv.org/abs/2602.10915) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [CP-uniGuard: A Unified, Probability-Agnostic, and Adaptive Framework for Malicious Agent Detection and Defense in Multi-Agent Embodied Perception Systems](https://arxiv.org/abs/2506.22890) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Claude LLM artifacts abused to push Mac infostealers in ClickFix attack](https://www.bleepingcomputer.com/news/security/claude-llm-artifacts-abused-to-push-mac-infostealers-in-clickfix-attack/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [ClickFix added nslookup commands to its arsenal for downloading RATs](https://www.malwarebytes.com/blog/news/2026/02/clickfix-added-nslookup-commands-to-its-arsenal-for-downloading-rats) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
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
| [EnCase Driver Weaponized as EDR Killers Persist](https://www.darkreading.com/threat-intelligence/encase-driver-weaponized-edr-killers-persist) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Four Seconds to Botnet - Analyzing a Self Propagating SSH Worm with Cryptographically Signed C2 &#x5b;Guest Diary&#x5d;, (Wed, Feb 11th)](https://isc.sans.edu/diary/rss/32708) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [From 27 Steps to 5: How Recorded Future Reimagined Threat Hunting with Autonomous Threat Operations](https://www.recordedfuture.com/blog/threat-hunting-27-steps-to-5) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [GPTZero: Robust Detection of LLM-Generated Texts](https://arxiv.org/abs/2602.13042) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [How to Scale SOC Automation with Falcon Fusion SOAR](https://www.crowdstrike.com/en-us/blog/how-to-scale-soc-automation-with-falcon-fusion-soar/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach](https://arxiv.org/abs/2602.13156) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach](https://arxiv.org/abs/2602.13156) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Inside the Human-AI Feedback Loop Powering CrowdStrike&rsquo;s Agentic Security](https://www.crowdstrike.com/en-us/blog/inside-the-human-ai-feedback-loop-powering-crowdstrike-agentic-security/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Intent-Driven Smart Manufacturing Integrating Knowledge Graphs and Large Language Models](https://arxiv.org/abs/2602.12419) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Keeping your data safe when an AI agent clicks a link](https://openai.com/index/ai-agent-link-safety) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [MASPRM: Multi-Agent System Process Reward Model](https://arxiv.org/abs/2510.24803) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Manipulating AI memory for profit: The rise of AI Recommendation Poisoning](https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Membership and Dataset Inference Attacks on Large Audio Generative Models](https://arxiv.org/abs/2512.09654) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Memory Injection Attacks on LLM Agents via Query-Only Interaction](https://arxiv.org/abs/2503.03704) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Metasploit Wrap-Up 02/13/2026](https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-02-13-2026) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [North Korea's UNC1069 Hammers Crypto Firms With AI](https://www.darkreading.com/threat-intelligence/north-koreas-unc1069-hammers-crypto-firms) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Peak + Accumulation: A Proxy-Level Scoring Formula for Multi-Turn LLM Attack Detection](https://arxiv.org/abs/2602.11247) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Pixel-Based Similarities as an Alternative to Neural Data for Improving Convolutional Neural Network Adversarial Robustness](https://arxiv.org/abs/2410.03952) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Sample-Specific Noise Injection For Diffusion-Based Adversarial Purification](https://arxiv.org/abs/2506.06027) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation](https://arxiv.org/abs/2602.12544) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://arxiv.org/abs/2602.12405) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
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
| [Weekly Recap: Outlook Add-Ins Hijack, 0-Day Patches, Wormable Botnet & AI Malware](https://thehackernews.com/2026/02/weekly-recap-outlook-add-ins-hijack-0.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [ZAST.AI Raises $6M Pre-A to Scale "Zero False Positive" AI-Powered Code Security](https://thehackernews.com/2026/02/zastai-raises-6m-pre-to-scale-zero.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |
| [⚡ Weekly Recap: AI Skill Malware, 31Tbps DDoS, Notepad++ Hack, LLM Backdoors and More](https://thehackernews.com/2026/02/weekly-recap-ai-skill-malware-31tbps.html) | N/A | relevance | llm_applicability_below_threshold (threshold: 0.6) |

---

[← Back to Index](index.md)
