# Module 0 · Foundations { #module-0 }

> **משך:** ~45 דק' · **Lab:** offline, ללא תלויות

## Overview

למה אבטחת AI שונה מאבטחה רגילה. העיקרון המכונן: מודל לא מבדיל בין **instructions** ל-**data** — הכול מגיע כזרם טוקנים אחד, כמו הזרקת SQL בשפה טבעית. כל הגנה היא ניסיון לשחזר את ההפרדה מבחוץ.

## Track A / Track B

=== "🟢 Track A — מנהלי"

    - **Attack surface:** כל קלט (user, RAG, tool, web) הוא וקטור פוטנציאלי.
    - **"המודל מסרב" אינו control:** סירוב הוא התנהגות הסתברותית, לא גבול אכיף.
    - **אחריות ארגונית:** מי מגדיר מה נכנס למערכת ומה היא רשאית לעשות.

=== "🔵 Track B — טכני"

    **Lab:** `python ai_redteam_exercise.py` (offline) — לראות את 5 הווקטורים חיים.

## Threat / Control / Evidence

!!! danger "Threat model"
    תוכן לא-מהימן מכל מקור מתפרש כהוראה.
!!! success "Control"
    spotlighting + least privilege כבר משלב התכנון.
!!! info "Evidence"
    מפת attack-surface חתומה לכל מערכת חדשה.

## RACI

| נכס | Owner | Accountable | Responsible | Consulted | Informed |
| --- | --- | --- | --- | --- | --- |
| Attack-surface map | Architect | Eng Lead | Dev | Security | Product |

## Outcomes

- 🟢 **Track A:** מסביר למה אין הפרדה קוד-נתונים וממפה attack surface.
- 🔵 **Track B:** מריץ את ה-exercise ומסווג את חמשת הווקטורים.

## Lab

`python ai_redteam_exercise.py` — ראה [סקציית המעבדות](../labs/index.md).
