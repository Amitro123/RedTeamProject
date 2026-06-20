# AI Security Course — Site (MkDocs Material)

אתר הקורס "AI Security for Solutions Architects". בנוי ב-**MkDocs Material**, מתפרסם ל-**GitHub Pages** דרך **GitHub Actions**.

---

## המלצה מנומקת: MkDocs Material מול Quartz

**הבחירה: MkDocs Material.** למרות שאתה עובד ב-Obsidian (ש-Quartz מתוכנן עבורו), לקורס *מובנה* היתרון של Material מובהק:

| קריטריון | MkDocs Material | Quartz |
| --- | --- | --- |
| התאמה לקורס מובנה (nav, sections, פרקים) | ✅ מצוין — nav ידני, tabs, sections | ⚠️ מכוון ל-digital garden / wikilinks |
| חיפוש מובנה | ✅ מהיר, offline, תומך עברית | ✅ יש, אך פחות מכוון |
| Callouts / admonitions | ✅ נטיבי (note/warning/tip + collapsible) | ⚠️ דרך plugins |
| Tabs ל-Track A/B | ✅ `pymdownx.tabbed` נטיבי | ❌ אין מקבילה נקייה |
| Code highlighting + copy | ✅ מצוין | ✅ בסיסי |
| Diagrams (Mermaid) | ✅ נטיבי ב-superfences | ✅ יש |
| Dark mode | ✅ toggle מובנה | ✅ יש |
| RTL לעברית | ✅ `language: he` נותן RTL מלא | ⚠️ דורש התאמות |
| בגרות + תיעוד + קהילה | ✅ מהבשלים בתעשייה | ⚠️ צעיר יותר |
| Deploy ל-GitHub Pages | ✅ Action רשמי, שורה אחת | ✅ יש |

**מתי כן Quartz?** אם המטרה העיקרית היא לפרסם את ה-Vault *כמו שהוא* עם `[[wikilinks]]`, backlinks, וגרף — בלי לתחזק nav ידני. זה מצוין ל-knowledge garden, פחות לקורס עם מבנה פדגוגי קשיח של מודולים, tabs, ו-labs.

**ה-workflow מול Obsidian נשמר:** אפשר להמשיך לכתוב ב-Obsidian — פשוט פתח את Obsidian על תיקיית `docs/` (או כתוב ב-Vault והעתק לתוך `docs/`). הסינטקס כמעט זהה; ההבדל היחיד הוא ש-`[[wikilinks]]` הופכים ל-`[טקסט](path.md)`.

---

## מבנה תיקיות

```
ai-security-course-site/
├── mkdocs.yml                 # קונפיגורציה + navigation tree
├── requirements.txt           # mkdocs-material
├── README.md                  # הקובץ הזה
├── .github/workflows/
│   └── deploy.yml             # GitHub Actions → GitHub Pages
└── docs/
    ├── index.md               # homepage (grid cards + mermaid)
    ├── stylesheets/
    │   └── extra.css          # brand: teal=הגנה, red=תקיפה, RTL, dark
    ├── modules/
    │   ├── index.md           # עמוד נחיתה לסקציית המודולים
    │   ├── _TEMPLATE.md        # תבנית אחידה לעמוד מודול
    │   ├── module-00.md … module-07.md
    ├── labs/
    │   ├── index.md
    │   ├── _TEMPLATE.md        # תבנית עמוד Lab
    │   └── lab-04-agents.md    # דוגמה ממומשת
    ├── reference/
    │   ├── owasp-llm-top-10.md
    │   ├── mitre-atlas.md
    │   ├── metrics-ci-gates.md
    │   └── glossary.md
    └── case-studies/
        ├── index.md
        ├── _TEMPLATE.md
        └── echoleak.md
```

---

## הרצה מקומית

```bash
cd ai-security-course-site
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve        # http://127.0.0.1:8000
```

---

## Checklist לפרסום ב-GitHub Pages

- [ ] העתק את התיקייה `ai-security-course-site/` לשורש ריפו `RedTeamProject` (או לריפו ייעודי).
- [ ] ודא ש-`site_url` ו-`repo_url` ב-`mkdocs.yml` נכונים.
- [ ] בריפו: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
- [ ] commit + push ל-`main` (כל שינוי תחת `ai-security-course-site/**` מפעיל deploy).
- [ ] עקוב אחרי ה-run תחת לשונית **Actions**; בסיום הירוק האתר עולה.
- [ ] בדוק את הכתובת: `https://amitro123.github.io/RedTeamProject/`.
- [ ] (אופציונלי) domain מותאם: **Settings → Pages → Custom domain** + רשומת DNS.
- [ ] ודא שה-build עובר `--strict` מקומית לפני push (תופס לינקים שבורים).

---

## Roadmap — העברת הסילבוס הקיים לאתר

1. **שלד (בוצע).** `mkdocs.yml`, homepage, תבניות, ועמוד מודול 4 + lab + EchoLeak ממומשים.
2. **מילוי מודולים 0–3, 5–7.** העתק את התוכן מ-`Syllabus v2 — AI Security Course.md`, מודול-לעמוד, לפי `modules/_TEMPLATE.md`. כל סקשן בסילבוס כבר ממופה לשדות התבנית (Overview, Track A/B, Threat/Control/Evidence, RACI, Outcomes, Lab).
3. **מילוי reference.** הרחב את `owasp-llm-top-10.md` ו-`mitre-atlas.md` מתוך מפת התקיפות (`01_attack_map.md`); ה-Glossary כבר מאוכלס.
4. **Case studies.** צור עמוד לכל אירוע (EchoLeak בוצע) מתוך הנספח (`04_2026_incidents_and_defenses.md`): Agentjacking, AutoJack, SearchLeak, LangGraph, LiteLLM, JetBrains, Orphaned Agents.
5. **Labs.** עמוד Lab לכל מודול עם Track B lab; חבר ל-`demo_agent` / `harness` בריפו.
6. **מדיה.** הטמע את הדיאגרמות (`index.html`) ואת לינקי הפודקאסט של NotebookLM בעמודי המודול הרלוונטיים.
7. **ליטוש.** logo/favicon, custom domain, ובדיקת `mkdocs build --strict` ב-CI.

> טיפ: שלבים 2–4 הם מכניים. אפשר לג'נרט את כל עמודי המודול מהסילבוס בבת אחת — ראה את `modules/module-04.md` כדוגמת-ייחוס מלאה.
