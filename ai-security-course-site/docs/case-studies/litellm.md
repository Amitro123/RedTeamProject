# LiteLLM Chain — AI Gateway Takeover { #litellm }

> **סוג:** Authz bypass + Privesc + Sandbox escape · **OWASP:** LLM03 + LLM06 · **מודול:** [6](../modules/module-06.md) · **CVSS:** 9.9

## מה קרה

Obsidian Security: שרשרת של 3 CVEs שמעלה חשבון low-privilege ב-LiteLLM proxy ל-root על ה-host:

- **CVE-2026-47101** — authz bypass.
- **CVE-2026-47102** — privesc ל-`proxy_admin`.
- **CVE-2026-40217** — sandbox escape דרך `exec()` ב-**Custom Code Guardrail**.

התוצאה: master key + DB creds → **כל מפתח API שה-proxy מחזיק נקרא**. בנוסף **CVE-2026-42271** (RCE) נוצל בטבע ונכנס ל-CISA KEV.

## למה זה עבד

!!! danger "המנגנון"
    ה-gateway הוא control plane — נקודת ריכוז של כל ה-secrets. כשל בו = exfiltration של כל המפתחות. אירוניה: הבריחה הייתה דרך פונקציה ששימשה דווקא את ה-Guardrail.

## ההגנה / איך מתמודדים

!!! success "Control"
    patch ל-`v1.83.14-stable`+; least privilege על חשבונות proxy; rotation של master key/DB creds; **אל תריץ `exec()` על input**.

## השיעור לקורס

[Module 6b](../modules/module-06.md) — פגיעה ב-orchestrator/proxy מסוכנת עשרות מונים מפגיעה במודל בודד: מ-"תוכן" ל-"קיומי".

## מקורות

- [LiteLLM Vulnerability Chain — The Hacker News](https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html)
