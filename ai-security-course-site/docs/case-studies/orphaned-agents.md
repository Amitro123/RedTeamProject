# Orphaned AI Agents { #orphaned-agents }

> **סוג:** Excessive Agency + Identity Governance gap · **OWASP:** LLM06 · **מודול:** [6](../modules/module-06.md)

## מה קרה

תופעה רוחבית: **סוכנים יתומים** (נשארים פעילים אחרי שיוצרם עזב) ו-**standing privileges** (גישה קבועה לא-נחוצה). בלתי-נראים ל-IAM מסורתי, נוצרים דרך Shadow AI. כ-70% מהארגונים כבר מריצים סוכנים בפרודקשן.

## למה זה עבד

!!! danger "המנגנון"
    סוכן הוא **non-human identity (NHI)** עם credentials. בלי lifecycle ו-ownership, הוא backdoor קבוע ועמיד — שפועל עם זהות והרשאות לגיטימיות, ולכן שום כלי אבטחה מסורתי לא מזהה.

## ההגנה / איך מתמודדים

!!! success "Control"
    רישום ובעלות (owner) לכל סוכן; **deprovisioning בעת עזיבת עובד**; ניטור standing privileges; least privilege; הכללת NHI ב-IAM/governance.

## השיעור לקורס

[Module 6a](../modules/module-06.md) — אבטחת סוכנים היא **ניהול זהויות לא-אנושיות**, לא ניהול משתמשים. הלקח מ-Pinchy: phishing על סוכנים לא נפתר בהדרכה אלא בהגבלת יכולות.

## מקורות

- [Orphaned AI Agents — The Hacker News](https://thehackernews.com/2026/06/orphaned-ai-agents-how-to-find-hidden.html)
