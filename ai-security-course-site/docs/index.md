---
hide:
  - navigation
  - toc
---

# AI Security for Solutions Architects

> בנה אותו כדי לתקוף — כדי שתדע להגן. קורס מודולרי לאבטחת מערכות **LLM** ו-**Agents**, ממופה ל-**OWASP LLM Top 10 (2025)** ול-**MITRE ATLAS**, ומבוסס על [RedTeamProject](https://github.com/Amitro123/RedTeamProject).

<div class="grid cards" markdown>

-   :material-target:{ .lg .middle } __העיקרון המכונן__

    ---

    מודל לא מבדיל בין **instructions** ל-**data**. הכול מגיע כזרם טוקנים אחד — זו הזרקת SQL בשפה טבעית. כל הגנה היא ניסיון לשחזר את ההפרדה מבחוץ.

-   :material-recycle:{ .lg .middle } __הלולאה__

    ---

    `attack → measure → harden → measure → detect → respond`. ה-**delta** (leak rate לפני/אחרי) הוא המספר שחשוב לארכיטקט.

-   :material-account-tie:{ .lg .middle } __שני מסלולים__

    ---

    <span class="track-a">🟢 Track A</span> — מנהלי/לא-טכני: סיכון, אחריות, החלטות.
    <span class="track-b">🔵 Track B</span> — ארכיטקטים/מפתחים: קוד, labs, harness.

-   :material-shield-lock:{ .lg .middle } __8 מודולים__

    ---

    מיסודות, דרך injection, agents ו-RAG, ועד governance ו-**Detection & Response**.

</div>

## מסלול הלמידה

```mermaid
flowchart LR
  M0[0 · Foundations] --> M1[1 · Measurement]
  M1 --> M2[2 · Injection]
  M2 --> M3[3 · Secrets]
  M3 --> M4[4 · Agents & Tool/MCP]
  M4 --> M5[5 · RAG & Memory]
  M5 --> M6[6 · Governance & Scale]
  M6 --> M7[7 · Detection & Response]
```

## מאיפה להתחיל

<div class="grid cards" markdown>

-   __חדש כאן?__ התחל ב-[מודול 0 · Foundations](modules/module-00.md)
-   __ארכיטקט?__ קפוץ ל-[מודול 4 · Agents & Tool/MCP](modules/module-04.md)
-   __מנהל?__ קרא את העדשה הניהולית (Track A) בכל מודול
-   __רוצה לתרגל?__ פתח את [המעבדות](labs/index.md)

</div>

## מסגרת קבועה בכל מודול

כל עמוד מודול בנוי על אותו שלד: **Overview** · **Track A / Track B** · **Threat / Control / Evidence** · **RACI** · **Outcomes** · **Lab**.

!!! tip "חומרי עזר"
    [OWASP LLM Top 10](reference/owasp-llm-top-10.md) · [MITRE ATLAS](reference/mitre-atlas.md) · [Metrics & CI Gates](reference/metrics-ci-gates.md) · [Glossary](reference/glossary.md) · [Case Studies](case-studies/index.md)
