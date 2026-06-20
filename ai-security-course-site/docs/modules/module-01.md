# Module 1 · The Measurement Mindset { #module-1 }

> **משך:** ~50 דק' · **Lab:** harness

## Overview

Purple teaming כלולאת מדידה: `attack → measure → harden → measure`. ה-**delta** (leak rate לפני מול אחרי הגנה) הוא המספר היחיד שבאמת חשוב לארכיטקט.

## Track A / Track B

=== "🟢 Track A — מנהלי"

    - **Attack surface:** בלי baseline אי אפשר לדעת אם שטח התקיפה גדל או קטן.
    - **"המודל מסרב" אינו control:** refusal rate הוא metric, לא הבטחה.
    - **אחריות ארגונית:** מי מחזיק את ה-baseline ומי מאשר רגרסיה.

=== "🔵 Track B — טכני"

    **Lab:** `python redteam.py --target sim --out report.json`; קריאת `runner.py` ו-`analysis.py`.

## Threat / Control / Evidence

!!! danger "Threat model"
    הגנה שלא נמדדת נשחקת בשקט.
!!! success "Control"
    baseline + מדידה חוזרת אחרי כל שינוי.
!!! info "Evidence"
    leak-rate delta (לפני/אחרי) ב-`report.json`.

## RACI

| נכס | Owner | Accountable | Responsible | Consulted | Informed |
| --- | --- | --- | --- | --- | --- |
| Eval corpus | Security Eng | Eng Lead | Dev | Architect | Management |

## Outcomes

- 🟢 **Track A:** מגדיר 3 metrics ומציגם להנהלה.
- 🔵 **Track B:** מריץ harness, מפיק baseline, ומפרש delta.

## Lab

ראה [Metrics & CI Gates](../reference/metrics-ci-gates.md).
