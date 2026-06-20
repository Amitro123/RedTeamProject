# SearchLeak (CVE-2026-42824) { #searchleak }

> **סוג:** Parameter-to-Prompt injection + SSRF · **OWASP:** LLM01 + LLM02 + LLM05 · **מודול:** [3](../modules/module-03.md), [4](../modules/module-04.md) · **one-click**

## מה קרה

Varonis שרשרו שלושה באגים ל-one-click data leak מ-Microsoft 365 Copilot Enterprise Search: (1) **Parameter-to-Prompt injection** — פרמטר ה-`q` ב-URL נקרא כהוראות; (2) **race condition** ב-rendering — תג `<img>` מוזרק נורה לפני שה-sanitizer רץ; (3) **CSP bypass** — Bing "Search by Image" (מותר ב-allowlist) משמש כ-SSRF proxy ל-exfiltration. הקורבן רק לוחץ על לינק microsoft.com לגיטימי.

## למה זה עבד

!!! danger "המנגנון"
    אותו דפוס כמו EchoLeak — באגי web ישנים (SSRF, sanitizer race) נעשים נגישים מחדש דרך ה-prompt injection. הלינק על דומיין אמין → anti-phishing לא תופס.

## ההגנה / איך מתמודדים

!!! success "Control"
    **Data-access governance** שמצמצם מה ש-Copilot מאנדקס (מקטין blast radius); ניטור URLs עם payload מקודד בפרמטר `q`; ניטור outbound לא-רגיל ל-Bing image endpoints. (Microsoft תיקנה ב-backend.)

## השיעור לקורס

מחבר בין [Module 3](../modules/module-03.md) (leakage) ל-[Module 4](../modules/module-04.md): ה-output handling וה-egress הם הגבול האחרון.

## מקורות

- [One-Click M365 Copilot Flaw — The Hacker News](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html)
