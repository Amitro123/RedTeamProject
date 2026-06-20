# Module 2 · Prompt Injection & Jailbreaking { #module-2 }

> **OWASP:** LLM01 · **ATLAS:** AML.T0051 / T0054 / T0043 · **משך:** ~60 דק'

## Overview

התקיפה מס' 1 ב-OWASP, שנתיים ברציפות. שלושה סוגים קשורים: **direct injection**, **jailbreaking** (role-play / many-shot / crescendo), ו-**adversarial text** (homoglyphs, zero-width, leetspeak).

## Track A / Track B

=== "🟢 Track A — מנהלי"

    - **Attack surface:** כל שדה טקסט חופשי שמגיע למודל.
    - **"המודל מסרב" אינו control:** many-shot ו-crescendo עוקפים סירוב.
    - **אחריות ארגונית:** מי מגדיר מדיניות תוכן ומי מנטר ניסיונות.

=== "🔵 Track B — טכני"

    **Lab:** הדגמה ב-[Gandalf](https://gandalf.lakera.ai/); הוספת probe חדש ל-`probes.py`.

## Threat / Control / Evidence

!!! danger "Threat model"
    הוראות מוטמעות ב-input גוברות על ה-system prompt.
!!! success "Control"
    normalization + זיהוי סמנטי + moderation layer נפרד.
!!! info "Evidence"
    ירידה ב-leak rate על probes של injection/jailbreak.

## RACI

| נכס | Owner | Accountable | Responsible | Consulted | Informed |
| --- | --- | --- | --- | --- | --- |
| Prompts | Architect | Eng Lead | Dev | Security | Product |

## Outcomes

- 🟢 **Track A:** מזהה ומסווג ניסיון injection.
- 🔵 **Track B:** כותב probe ומודד אותו.

## Lab

[Gandalf](https://gandalf.lakera.ai/) + `harness/probes.py`.
