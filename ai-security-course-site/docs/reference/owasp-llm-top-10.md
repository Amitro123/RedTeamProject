# OWASP LLM Top 10 (2025) — מיפוי לקורס

הטקסונומיה הקנונית. כל סיכון ממופה למודול בקורס ולמיקום בריפו.

| # | סיכון | מודול | מכוסה בריפו? |
| --- | --- | --- | --- |
| **LLM01** | Prompt Injection | [2](../modules/module-02.md), [4](../modules/module-04.md) | ✅ direct + indirect |
| **LLM02** | Sensitive Information Disclosure | [3](../modules/module-03.md) | ✅ system prompt extraction |
| **LLM03** | Supply Chain | [6](../modules/module-06.md) | ⚠️ security notes |
| **LLM04** | Data & Model Poisoning | [5](../modules/module-05.md) | ⚠️ corpus trust |
| **LLM05** | Improper Output Handling | [4](../modules/module-04.md) | ✅ "no output execution" |
| **LLM06** | Excessive Agency | [4](../modules/module-04.md) | ✅ tool gating + egress |
| **LLM07** | System Prompt Leakage | [3](../modules/module-03.md) | ✅ extraction probe |
| **LLM08** | Vector & Embedding Weaknesses | [5](../modules/module-05.md) | ✅ RAG lab |
| **LLM09** | Misinformation | [6](../modules/module-06.md) | ➖ להרחבה |
| **LLM10** | Unbounded Consumption | [6](../modules/module-06.md) | ➖ להרחבה |

!!! note "Agentic AI"
    OWASP מתחזקת גם רשימת איומים ל-**Agentic AI** (memory poisoning, tool misuse, identity/privilege, cascading agent failures) — רלוונטית למודולים [4](../modules/module-04.md), [5](../modules/module-05.md), ו-[6](../modules/module-06.md).

## מקורות

- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)
