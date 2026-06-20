# Module 5 · RAG, Poisoning, Embeddings & Memory Security { #module-5 }

> **OWASP:** LLM04 + LLM08 · **משך:** ~55 דק'

## Overview

תקיפות על שכבת הידע: **data/model poisoning** ו-**vector/embedding weaknesses**, עם תת-מודול **Memory Security**. ה-corpus וה-memory הם קלט *מתמשך*, לא חד-פעמי.

## Track A / Track B

=== "🟢 Track A — מנהלי"

    - **Attack surface:** ה-RAG corpus וה-memory הם קלט מתמשך.
    - **"המודל מסרב" אינו control:** מסמך/זיכרון מורעל לא מפעיל סירוב.
    - **אחריות ארגונית:** מי הבעלים של ה-corpus ושל ה-memory לכל משתמש.

=== "🔵 Track B — טכני"

    **Lab:** הקשחת RAG (`yaml.safe_load` + schema validation); `demo_agent` שיוצר memory poisoning ומדגים detection.

### Memory Security (תת-מודול)

!!! defense "דפוסי הגנה על memory"
    - **Session isolation** ו-**per-user namespace**.
    - **TTL**, **redaction**, ו-**audit logging**.
    - **Integrity checks** ו-**hash verification** למניעת שינוי שקט.
    - דפוסי הגנה מפני **memory poisoning** (session / user / persistent).

## Threat / Control / Evidence

!!! danger "Threat model"
    הרעלת corpus/embeddings/memory, או דליפה בין tenants.
!!! success "Control"
    access control באחזור, tenant isolation, namespace + TTL + integrity על memory.
!!! info "Evidence"
    alert על memory mismatch (hash); test שמראה בידוד בין משתמשים.

## RACI

| נכס | Owner | Accountable | Responsible | Consulted | Informed |
| --- | --- | --- | --- | --- | --- |
| RAG corpus | Data Eng | Eng Lead | Dev | Security | Management |
| Memory | Architect | Eng Lead | Dev | Security | Management |

## Outcomes

- 🟢 **Track A:** מבין למה memory = attack surface ומה האחריות.
- 🔵 **Track B:** מטמיע namespace + redaction + integrity, ומדגים detection ל-poisoning.

## Lab

`demo_agent/` — RAG hardening + memory poisoning detection.
