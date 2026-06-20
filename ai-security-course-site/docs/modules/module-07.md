# Module 7 · Detection & Response { #module-7 }

> **מודול חדש** · **משך:** ~50 דק'

## Overview

איך מזהים, מדווחים, ואחראים על תקיפות AI בזמן אמת — השלמת הלולאה מ-`harden` ל-`detect → respond`. בעולם של 2026, חלק מהתקיפות יעברו; השאלה היא כמה מהר תזהה ותבין מה קרה.

## Track A / Track B

=== "🟢 Track A — מנהלי"

    - **Attack surface:** בלי telemetry, תקיפה שעברה היא בלתי-נראית.
    - **"המודל מסרב" אינו control:** detection הוא שכבה חיצונית ובלתי-תלויה במודל.
    - **אחריות ארגונית:** מי מקבל את הדיווח ומי מוביל incident response.

    **מה מציגים להנהלה:** leak rate · repeated attempts · **time-to-detect**.

=== "🔵 Track B — טכני"

    **Lab:** בניית detector פשוט + alert rule אחד (זיהוי ניסיון injection על tool call), והדמיית התרעה.

**רכיבים:** monitoring & logging (OpenTelemetry: trace/log/metrics) · anomaly detection על prompts/tool calls/outputs · alerting patterns (injection, policy violations, secrets leakage, tool abuse) · incident response flow (triage → containment → forensics → remediation) · blue team exercises.

## Threat / Control / Evidence

!!! danger "Threat model"
    תקיפה שעוברת את ההגנות נשארת ללא זיהוי.
!!! success "Control"
    telemetry מלא + anomaly detection + alert rules + IR flow.
!!! info "Evidence"
    time-to-detect נמדד; alert נורה בסימולציה; reconstruction מלא של אירוע.

## RACI

| נכס | Owner | Accountable | Responsible | Consulted | Informed |
| --- | --- | --- | --- | --- | --- |
| Logs / Detection | Security Eng | CISO | SOC/Dev | Architect | Management |

## Outcomes

- 🟢 **Track A:** יודע איזה 3 metrics לראות בדיוור ולהוביל review.
- 🔵 **Track B:** מטמיע detector, alert rule, logging pipeline, ומריץ סימולציית blue team.

## Lab

detector + alert rule + logging pipeline (OpenTelemetry).
