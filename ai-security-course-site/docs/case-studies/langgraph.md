# LangGraph RCE Chain { #langgraph }

> **סוג:** SQLi + Unsafe Deserialization בתוך agent framework · **OWASP:** LLM03 + LLM05 · **מודול:** [6](../modules/module-06.md)

## מה קרה

Check Point: שלושה CVEs ב-LangGraph (self-hosted), שניים מהם משורשרים ל-RCE:

- **CVE-2025-67644** — SQL injection ב-SQLite checkpointer דרך metadata filter.
- **CVE-2026-28277** — unsafe **msgpack deserialization** → הרצת קוד.
- **CVE-2026-27022** — RediSearch query injection.

ה-SQLi מחזיר checkpoint מזויף → ה-deserialization מריצה את ה-payload. LangSmith המנוהל לא מושפע.

## למה זה עבד

!!! danger "המנגנון"
    "vuln classes ישנים נעשים חזקים יותר כשהם בתוך framework של סוכן שנושא הרשאות ו-trust מוגברים."

## ההגנה / איך מתמודדים

!!! success "Control"
    patch; **authentication על שרתי LangGraph self-hosted**; הימנעות מ-secrets סטטיים ארוכי-חיים; network segmentation; **התייחסות לסוכנים כ-privileged identities**; least privilege על ה-footprint.

## השיעור לקורס

[Module 6a](../modules/module-06.md) — אבטחת ה-infrastructure של הסוכן היא חלק מהאחריות הארכיטקטונית, לא רק ה-prompt.

## מקורות

- [LangGraph Flaw Chain — The Hacker News](https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html)
