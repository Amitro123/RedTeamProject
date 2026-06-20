# Module 6 · Governance & Scale { #module-6 }

> **OWASP:** LLM03 + LLM09 + LLM10 · **משך:** ~60 דק'

## Overview

כל מה שמסביב למודל. מפוצל לשני תת-חלקים: **6a Governance, Ownership & Lifecycle** ו-**6b Scale, Cost, Abuse & Loops**.

## 6a · Governance, Ownership & Lifecycle

=== "🟢 Track A — מנהלי"

    - **Attack surface:** סוכן/prompt/tool בלי owner הוא backdoor (orphaned agents).
    - **"המודל מסרב" אינו control:** governance הוא תהליך אנושי-טכני.
    - **אחריות ארגונית:** RACI מלא לכל נכס.

=== "🔵 Track B — טכני"

    **Lab:** רישום כל סוכן כ-NHI; approval workflow ל-side-effect; audit log.

**רכיבים:** owner ל-prompts/tools/memory/RAG/eval corpus/CI gates · RACI לכל מודול · policy enforcement, audit trails, approval workflows · ניהול NHI ו-lifecycle (auth, rotation, deprovisioning).

## 6b · Scale, Cost, Abuse, Loops & Denial-of-Wallet

=== "🟢 Track A — מנהלי"

    - **Attack surface:** כל קריאת מודל היא עלות; לולאות מגדילות אותה.
    - **"המודל מסרב" אינו control:** denial-of-wallet לא דורש תוכן זדוני.
    - **אחריות ארגונית:** מי בעל התקציב ומי מגדיר quotas.

=== "🔵 Track B — טכני"

    **Lab:** token/loop budgets + timeout; CI gate עם `--ci --max-leak-rate`.

## Threat / Control / Evidence

!!! danger "Threat model"
    standing privileges וסוכנים יתומים; token-flood, לולאות, supply-chain מורעל.
!!! success "Control"
    ownership + lifecycle + deprovisioning; rate/loop/token limits; pinning + verify; CI gate.
!!! info "Evidence"
    0 סוכנים ללא owner; audit trail על side-effects; build נכשל על רגרסיית leak-rate.

## RACI

| נכס | Owner | Accountable | Responsible | Consulted | Informed |
| --- | --- | --- | --- | --- | --- |
| Governance | CISO/Architect | CISO | Eng Lead | Security | Management |
| CI gate | Eng Lead | Eng Lead | Dev | Security/Finance | Management |

## Outcomes

- 🟢 **Track A:** מגדיר תקציב, quotas, ומפת supply chain.
- 🔵 **Track B:** מטמיע budgets, rate limits, ו-CI gate; רושם NHI עם owner.

## Lab

NHI registry + approval workflow; budgets + CI gate.
