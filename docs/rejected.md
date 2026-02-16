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

Total rejected articles: **74**

| Title | Topic | Rejection Type | Rejection Reason |
|-------|-------|----------------|------------------|
| [CloudDefenseAI/secure-agents-md](https://github.com/CloudDefenseAI/secure-agents-md) | ai-security | applicability | Focuses on governance and secure coding practices for AI agents but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [Luxvil/ai-coding-rules](https://github.com/Luxvil/ai-coding-rules) | ai-security | applicability | Repository focuses on enhancing AI coding assistants but lacks any explicit connection to offensive security or automation/fuzzing for security purposes. |
| [Rul1an/assay](https://github.com/Rul1an/assay) | ai-security | applicability | Repository focuses on runtime security and policy enforcement for AI agents but lacks explicit evidence of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [Yosuraki/claude4-audit-recon](https://github.com/Yosuraki/claude4-audit-recon) | ai-security | applicability | Focuses on ethical auditing and introspection of AI models without offensive security or automation context. |
| [datacline/open-threat-detector](https://github.com/datacline/open-threat-detector) | ai-security | applicability | Focuses on detecting shadow AI threats in organizational environments but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock) | ai-security | applicability | Repository focuses on securing AI agents with egress proxy and integrity monitoring but lacks explicit mention of offensive security or AI-driven automation for penetration testing or vulnerability detection. |
| [stacklok/toolhive-studio](https://github.com/stacklok/toolhive-studio) | ai-security | applicability | Mentions AI agents but lacks explicit offensive security focus or automation for security testing. |
| [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) | ai-security | relevance | missing_ai_keywords |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | ai-security | relevance | missing_ai_keywords |
| [fhjlfer098/Malware-Analysis](https://github.com/fhjlfer098/Malware-Analysis) | binary-analysis | applicability | Focuses on manual malware analysis techniques without evidence of AI, automation, or fuzzing. |
| [than0024/ida-reach](https://github.com/than0024/ida-reach) | binary-analysis | applicability | Mentions automation but lacks explicit connection to offensive security or AI usage for security testing. |
| [Andepzaiiii/semantic-copycat-binarysniffer](https://github.com/Andepzaiiii/semantic-copycat-binarysniffer) | binary-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | binary-analysis | relevance | missing_ai_keywords |
| [Krix77/IDAFind](https://github.com/Krix77/IDAFind) | binary-analysis | relevance | missing_ai_keywords |
| [Natikverma/C_BitPacking](https://github.com/Natikverma/C_BitPacking) | binary-analysis | relevance | missing_ai_keywords |
| [SenSeiSGS/ida-structor](https://github.com/SenSeiSGS/ida-structor) | binary-analysis | relevance | missing_ai_keywords |
| [krauzermaster1/GTI](https://github.com/krauzermaster1/GTI) | binary-analysis | relevance | missing_ai_keywords |
| [senaMizo/assembly-reverse-engineering](https://github.com/senaMizo/assembly-reverse-engineering) | binary-analysis | relevance | missing_ai_keywords |
| [thisarasewmina/DbgNexum](https://github.com/thisarasewmina/DbgNexum) | binary-analysis | relevance | missing_ai_keywords |
| [penxpkj/Defensive-Security-Hub](https://github.com/penxpkj/Defensive-Security-Hub) | malware-analysis | applicability | The repository focuses on defensive security resources and lacks any mention of AI, automation, or fuzzing for offensive security. |
| [timgerstel/suspicious_IPs](https://github.com/timgerstel/suspicious_IPs) | malware-analysis | applicability | While the repository involves malware analysis and penetration testing, it does not explicitly mention AI, automation, or fuzzing. |
| [CYB3RMX/Qu1cksc0pe](https://github.com/CYB3RMX/Qu1cksc0pe) | malware-analysis | relevance | missing_ai_keywords |
| [CybercentreCanada/assemblyline-service-urldownloader](https://github.com/CybercentreCanada/assemblyline-service-urldownloader) | malware-analysis | relevance | missing_ai_keywords |
| [Jazeredz/DLL-Hijacking-Vulnerability-Scanner](https://github.com/Jazeredz/DLL-Hijacking-Vulnerability-Scanner) | malware-analysis | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | malware-analysis | relevance | missing_ai_keywords |
| [hiephoiga1166/MidnightRAT-Payload](https://github.com/hiephoiga1166/MidnightRAT-Payload) | malware-analysis | relevance | missing_ai_keywords |
| [mreshuu/STForensicMacOS](https://github.com/mreshuu/STForensicMacOS) | malware-analysis | relevance | missing_ai_keywords |
| [reuteras/dfirws](https://github.com/reuteras/dfirws) | malware-analysis | relevance | missing_ai_keywords |
| [Leywkeny/WinNT-add-system-user-injector](https://github.com/Leywkeny/WinNT-add-system-user-injector) | offensive-security | applicability | Focuses on system administration and automation without offensive security context or AI usage. |
| [Sylphoraz/SharpAllowedToAct-Modify](https://github.com/Sylphoraz/SharpAllowedToAct-Modify) | offensive-security | applicability | Focuses on post-exploitation without mentioning AI, automation, or fuzzing. |
| [secwexen/aapp-mart](https://github.com/secwexen/aapp-mart) | offensive-security | credibility | Low stars count and outdated repository with last update in 2026, suggesting inactive maintenance. |
| [Finnnwm/CloneX-Muck-security-testing-tool](https://github.com/Finnnwm/CloneX-Muck-security-testing-tool) | offensive-security | relevance | missing_ai_keywords |
| [FlameBudy/MSSQLServer-CLR-CommandKit](https://github.com/FlameBudy/MSSQLServer-CLR-CommandKit) | offensive-security | relevance | missing_ai_keywords |
| [Karararam/SpringBoot-Exploit-Toolkit](https://github.com/Karararam/SpringBoot-Exploit-Toolkit) | offensive-security | relevance | missing_ai_keywords |
| [Ylxmy/Windows-Shellcode-Generator-Loader](https://github.com/Ylxmy/Windows-Shellcode-Generator-Loader) | offensive-security | relevance | missing_ai_keywords |
| [aliwioiod/speedloader](https://github.com/aliwioiod/speedloader) | offensive-security | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | offensive-security | relevance | missing_ai_keywords |
| [praetorian-inc/brutus](https://github.com/praetorian-inc/brutus) | offensive-security | relevance | missing_ai_keywords |
| [Kasim200429/GoBypass403](https://github.com/Kasim200429/GoBypass403) | penetration-testing | applicability | The repository is a tool for bypassing 403 errors during penetration testing but does not demonstrate the use of AI, automation, or fuzzing. |
| [SafwanSaleem/Subdomain-port-scanner-passive](https://github.com/SafwanSaleem/Subdomain-port-scanner-passive) | penetration-testing | applicability | Focuses on passive reconnaissance without offensive security context or AI usage. |
| [swathigoud/WhisperNet](https://github.com/swathigoud/WhisperNet) | penetration-testing | applicability | The repository is a password generator tool for penetration testing but does not mention AI, automation, or fuzzing explicitly. |
| [timgerstel/suspicious_IPs](https://github.com/timgerstel/suspicious_IPs) | penetration-testing | applicability | The repository focuses on collecting suspicious IPs from a honeypot but does not demonstrate the use of AI, automation, or fuzzing for offensive security. |
| [FaresArgus/artaxerxes](https://github.com/FaresArgus/artaxerxes) | penetration-testing | relevance | missing_ai_keywords |
| [abbassFarhat/hacker101-CTF-Solutions](https://github.com/abbassFarhat/hacker101-CTF-Solutions) | penetration-testing | relevance | missing_ai_keywords |
| [hanyshehata1510/RoboBack](https://github.com/hanyshehata1510/RoboBack) | penetration-testing | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | penetration-testing | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | penetration-testing | relevance | missing_ai_keywords |
| [Bossthetigan/NOLO](https://github.com/Bossthetigan/NOLO) | red-team | applicability | The repository focuses on AI-powered PTZ tracking using YOLO but does not relate to offensive security or automation for security testing. |
| [rabeal21/Tea](https://github.com/rabeal21/Tea) | red-team | applicability | The repository focuses on generating TEA wallet addresses and does not explicitly mention AI, automation, or fuzzing for offensive security. |
| [AlejandroZaZ/cybersecurity-tools](https://github.com/AlejandroZaZ/cybersecurity-tools) | red-team | relevance | missing_ai_keywords |
| [Jancarow/BypassNeo-reGeorg](https://github.com/Jancarow/BypassNeo-reGeorg) | red-team | relevance | missing_ai_keywords |
| [atulranjanz/Swatted-Webhook-Spammer](https://github.com/atulranjanz/Swatted-Webhook-Spammer) | red-team | relevance | missing_ai_keywords |
| [hiephoiga1166/MidnightRAT-Payload](https://github.com/hiephoiga1166/MidnightRAT-Payload) | red-team | relevance | missing_ai_keywords |
| [jm7knz/CVE-2025-54253-Exploit-Demo](https://github.com/jm7knz/CVE-2025-54253-Exploit-Demo) | red-team | relevance | missing_ai_keywords |
| [otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit](https://github.com/otuhsgcasg/Cooolis-ms-C2-Loader-Metasploit) | red-team | relevance | missing_ai_keywords |
| [praetorian-inc/brutus](https://github.com/praetorian-inc/brutus) | red-team | relevance | missing_ai_keywords |
| [mulhala-100ttl/AIDA64-Network-Audit-2026](https://github.com/mulhala-100ttl/AIDA64-Network-Audit-2026) | reverse-engineering | applicability | The repository is focused on network auditing and inventory reporting without any mention of AI, automation, or fuzzing for offensive security. |
| [mwakidenis/UN-OFFICIAL-KPLC-TOKEN-HISTORY-VIEW](https://github.com/mwakidenis/UN-OFFICIAL-KPLC-TOKEN-HISTORY-VIEW) | reverse-engineering | applicability | The repository is focused on accessing token purchase history and does not involve AI, automation, or fuzzing for offensive security. |
| [AlessandroBonomo28/HealthyIG](https://github.com/AlessandroBonomo28/HealthyIG) | reverse-engineering | relevance | missing_ai_keywords |
| [Ali632-lgtm/mcafee-tools](https://github.com/Ali632-lgtm/mcafee-tools) | reverse-engineering | relevance | missing_ai_keywords |
| [Laeteth/advanced-anti-sandbox-Virtual-Machine](https://github.com/Laeteth/advanced-anti-sandbox-Virtual-Machine) | reverse-engineering | relevance | missing_ai_keywords |
| [SoWeBegin/ToyBattlesHQ](https://github.com/SoWeBegin/ToyBattlesHQ) | reverse-engineering | relevance | missing_ai_keywords |
| [Terralyp/SunloginLP-Eanalysis-tool](https://github.com/Terralyp/SunloginLP-Eanalysis-tool) | reverse-engineering | relevance | missing_ai_keywords |
| [Trivexion/iMonitor-System-Activity-Monitor](https://github.com/Trivexion/iMonitor-System-Activity-Monitor) | reverse-engineering | relevance | missing_ai_keywords |
| [lympdegrin919fl/AnyDesk-Ultimate-2026](https://github.com/lympdegrin919fl/AnyDesk-Ultimate-2026) | reverse-engineering | relevance | missing_ai_keywords |
| [megakiyaiscool/Smart_Plug](https://github.com/megakiyaiscool/Smart_Plug) | reverse-engineering | relevance | missing_ai_keywords |
| [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content) | security-automation | applicability | Repository focuses on security automation for compliance and hardening, not offensive security or AI-driven tools. |
| [zricethezav/h1domains](https://github.com/zricethezav/h1domains) | security-automation | applicability | Repository provides a list of domains for HackerOne but does not involve AI, automation, or fuzzing for offensive security. |
| [JulesJujuu/wpaudit](https://github.com/JulesJujuu/wpaudit) | security-automation | relevance | missing_ai_keywords |
| [hitq11/AdaPol](https://github.com/hitq11/AdaPol) | security-automation | relevance | missing_ai_keywords |
| [kynaan5353/cargo-recon](https://github.com/kynaan5353/cargo-recon) | security-automation | relevance | missing_ai_keywords |
| [osamahamad/payout-targets-data](https://github.com/osamahamad/payout-targets-data) | security-automation | relevance | missing_ai_keywords |
| [securego/gosec](https://github.com/securego/gosec) | security-automation | relevance | missing_ai_keywords |
| [wazuh/wazuh](https://github.com/wazuh/wazuh) | security-automation | relevance | missing_ai_keywords |

---

[← Back to Index](index.md)
