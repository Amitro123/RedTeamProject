# Diagrams / דיאגרמות

דיאגרמות ליבה של הקורס. נבנו כתוכן נייטיב (טקסט אמיתי + SVG) — searchable, עם dark mode.

## 1 · Traditional AppSec vs. AI-Specific Defense

לכל בקרת אבטחה מסורתית יש מקבילה — אבל מערכות AI דורשות שכבה נוספת. העמודה השמאלית היא מה ש**חדש** שצריך להוסיף.

| תחום בקרה | Traditional AppSec | מה ש-AI מוסיף (AI-Specific) |
| --- | --- | --- |
| **Input Validation** | סכמה ו-sanitization | **Spotlighting** — קלט = `data`; זיהוי סמנטי |
| **Injection** | בריחת SQLi/XSS בקידוד | **Prompt Injection** — אין הפרדה קוד/נתונים; ישיר+עקיף |
| **AuthZ / Access** | RBAC ברמת המשתמש | **Access control באחזור** (RAG) + בידוד tenants |
| **Output Handling** | קידוד פלט נגד XSS | **פלט מודל = untrusted** — לא להריץ; egress allowlist |
| **Secrets Mgmt** | Vaults ומשתני סביבה | **אל תשים סודות ב-system prompt** |
| **Supply Chain** | SCA / SBOM | **Provenance למודל/dataset/plugin**; pin משקלים |
| **Least Privilege** | הרשאות מינימום לתהליך | **Tool gating + HITL**; הכלת blast radius |
| **Identity** | זהויות אנוש ושירות | **סוכן = NHI** עם lifecycle ובעלות |
| **Monitoring / IR** | SIEM ולוגים | **Telemetry על tool/MCP calls**; שחזור פעילות AI |
| **Availability** | Rate limiting | **תקציבי token/loop**; מניעת denial-of-wallet |

## 2 · אנטומיה של תקיפות סוכנים

מקור לא-מהימן מתחזה ל-`trusted system output` דרך ה-MCP, והסוכן פועל לפיו עם ההרשאות שלו. הזרימה מימין לשמאל.

<div markdown="0" style="overflow-x:auto">
<svg viewBox="0 0 1000 270" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;display:block;margin:0 auto" role="img" aria-label="Agent attack anatomy">
  <defs>
    <marker id="arrL" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#F0544F"/></marker>
  </defs>
  <rect x="790" y="70" width="190" height="120" rx="10" fill="#231722" stroke="#F0544F" stroke-width="1.6"/>
  <text x="885" y="116" text-anchor="middle" fill="#F0544F" font-size="16" font-weight="700">External</text>
  <text x="885" y="138" text-anchor="middle" fill="#F0544F" font-size="16" font-weight="700">Untrusted Source</text>
  <text x="885" y="164" text-anchor="middle" fill="#9AA7BC" font-size="12">מסמך · web · Sentry · plugin</text>
  <line x1="786" y1="130" x2="676" y2="130" stroke="#F0544F" stroke-width="2.4" marker-end="url(#arrL)"/>
  <rect x="500" y="60" width="172" height="140" rx="10" fill="#2a2410" stroke="#F3C24B" stroke-width="1.6"/>
  <text x="586" y="100" text-anchor="middle" fill="#F3C24B" font-size="15" font-weight="700">MCP boundary</text>
  <text x="586" y="128" text-anchor="middle" fill="#EAEEF6" font-size="12">מתחזה ל-</text>
  <text x="586" y="148" text-anchor="middle" fill="#EAEEF6" font-size="12">"trusted output"</text>
  <text x="586" y="182" text-anchor="middle" fill="#9AA7BC" font-size="11">אין auth / provenance</text>
  <line x1="496" y1="130" x2="396" y2="130" stroke="#F0544F" stroke-width="2.4" marker-end="url(#arrL)"/>
  <rect x="236" y="70" width="158" height="120" rx="10" fill="#10302c" stroke="#2DD4BF" stroke-width="1.6"/>
  <text x="315" y="124" text-anchor="middle" fill="#2DD4BF" font-size="17" font-weight="700">AI Agent</text>
  <text x="315" y="150" text-anchor="middle" fill="#9AA7BC" font-size="12">בהרשאות המפתח</text>
  <line x1="232" y1="105" x2="150" y2="70" stroke="#F0544F" stroke-width="2.4" marker-end="url(#arrL)"/>
  <line x1="232" y1="155" x2="150" y2="190" stroke="#F0544F" stroke-width="2.4" marker-end="url(#arrL)"/>
  <rect x="14" y="36" width="130" height="62" rx="9" fill="#231722" stroke="#F0544F" stroke-width="1.4"/>
  <text x="79" y="62" text-anchor="middle" fill="#F0544F" font-size="14" font-weight="700">Host RCE</text>
  <text x="79" y="82" text-anchor="middle" fill="#9AA7BC" font-size="11">הרצת קוד על המארח</text>
  <rect x="14" y="162" width="130" height="62" rx="9" fill="#231722" stroke="#F0544F" stroke-width="1.4"/>
  <text x="79" y="188" text-anchor="middle" fill="#F0544F" font-size="14" font-weight="700">Exfiltration</text>
  <text x="79" y="208" text-anchor="middle" fill="#9AA7BC" font-size="11">דליפת מידע / מפתחות</text>
</svg>
</div>

!!! danger "התובנה"
    כל פלט של MCP הוא **untrusted data**, לא system output. ראה [Module 4](../modules/module-04.md) ו-[Case Studies](../case-studies/index.md): EchoLeak, Agentjacking, AutoJack.
