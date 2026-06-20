# Module 3 · Secrets & System Prompt Leakage { #module-3 }

> **OWASP:** LLM02 + LLM07 · **ATLAS:** AML.T0056 · **משך:** ~45 דק'

## Overview

מה דולף וכיצד. וריאציות על "Repeat the text above" מחלצות את ה-system prompt וחושפות לוגיקה וסודות. השיעור: **אל תשים סודות ב-system prompt, ואל תניח שהוא חסוי.**

## Track A / Track B

=== "🟢 Track A — מנהלי"

    - **Attack surface:** כל מה שהוטמע ב-system prompt חשוף.
    - **"המודל מסרב" אינו control:** "Repeat the text above" עוקף.
    - **אחריות ארגונית:** מי מאשר מה נכנס ל-system prompt.

=== "🔵 Track B — טכני"

    **Lab:** ה-secrets layer ב-`analysis.py`; report redaction.

## Threat / Control / Evidence

!!! danger "Threat model"
    חילוץ system prompt חושף לוגיקה וסודות.
!!! success "Control"
    move secrets out; secret-pattern scanning + redaction.
!!! info "Evidence"
    0 סודות בדוחות; alert על דליפת תבנית-סוד.

## RACI

| נכס | Owner | Accountable | Responsible | Consulted | Informed |
| --- | --- | --- | --- | --- | --- |
| Prompts / Secrets | Security Eng | Architect | Dev | Security | Management |

## Outcomes

- 🟢 **Track A:** יודע מה אסור ב-system prompt.
- 🔵 **Track B:** מטמיע redaction ו-secret scanning.

## Lab

`harness/analysis.py` — secret-pattern scanning.
