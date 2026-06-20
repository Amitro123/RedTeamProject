# JetBrains Marketplace — Malicious Plugins { #jetbrains-plugins }

> **סוג:** Supply Chain — malicious plugin · **OWASP:** LLM03 · **ATLAS:** AML.T0010 · **מודול:** [6](../modules/module-06.md)

## מה קרה

15 plugins ב-JetBrains Marketplace (פורסמו מאוקטובר 2025, ~70K התקנות) התחזו לכלי AI coding ו-**exfiltrated מפתחות OpenAI/DeepSeek/SiliconFlow ב-plaintext** לשרת התוקף. JetBrains הסירו וחסמו ביוני 2026.

## למה זה עבד

!!! danger "המנגנון"
    ה-IDE/plugin ecosystem הוא supply chain מלא. plugin הוא קוד שרץ בהרשאות המפתח — כולל גישה למפתחות שהוזנו ב-settings.

## ההגנה / איך מתמודדים

!!! success "Control"
    vetting של plugins (publisher, reviews, permissions); **revoke מיידי** של כל מפתח שהוזן ב-plugin חשוד; secrets ב-vault ולא ב-plugin settings; allow-list ארגוני של plugins מאושרים.

## השיעור לקורס

[Module 6a](../modules/module-06.md) — supply chain של כלי הפיתוח עצמם הוא חלק ממשטח התקיפה.

## מקורות

- [Malicious JetBrains Plugins — The Hacker News](https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html)
