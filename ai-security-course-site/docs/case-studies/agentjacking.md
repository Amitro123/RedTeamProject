# Agentjacking { #agentjacking }

> **סוג:** Indirect injection דרך MCP tool-output · **OWASP:** LLM01 + LLM06 · **ATLAS:** AML.T0051.001 · **מודול:** [4](../modules/module-04.md) · **היקף:** 85% הצלחה · 2,388 ארגונים חשופים

## מה קרה

תוקף שולח **error event מזויף** ל-Sentry דרך DSN ציבורי שמוטמע באתרים, עם markdown מעוצב שנראה כמו "Resolution" לגיטימי. כשמפתח מבקש מ-Claude Code / Cursor "fix unresolved Sentry issues", ה-MCP server מחזיר את האירוע כ-**trusted system output**, והסוכן מריץ את הפקודה בהרשאות המפתח.

## למה זה עבד

!!! danger "המנגנון"
    הסוכן לא מבדיל בין error אמיתי ל-error מוזרק. "Every action in the chain is authorized" — לכן EDR/WAF/IAM לא תופסים. Sentry הגדירו את זה כ-"technically not defensible" בשכבת המוצר.

## ההגנה / איך מתמודדים

!!! success "Control"
    **Provenance/spotlighting** על פלט MCP (סמן אותו כ-data); **human approval לפני הרצת קוד** שמקורו בכלי חיצוני; least privilege לסוכן ה-coding; הגבלת חשיפת DSN.

## השיעור לקורס

מקביל ישיר ל-`vulnerable_agent` שלך — רק שה-payload מגיע מ-Sentry במקום ממסמך RAG. מחזק את הכלל: **כל פלט MCP הוא untrusted data**.

## מקורות

- [Agentjacking — The Hacker News](https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html)
