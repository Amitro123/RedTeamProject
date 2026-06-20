# Glossary / מילון מונחים

| מונח | הגדרה |
| --- | --- |
| **Prompt Injection** | הזרקת הוראות זדוניות לקלט המודל הגוברות על ה-system prompt. |
| **Indirect Injection** | ה-payload מגיע ממקור שהסוכן צורך (RAG, web, פלט כלי), לא מהמשתמש. |
| **Jailbreaking** | שימוש בטכניקות מניפולטיביות (role-play, framing) לעקיפת מדיניות התוכן. |
| **Adversarial Text** | תווים מיוחדים (homoglyphs, zero-width) לעקיפת מסננים מבוססי מילים. |
| **RAG** | Retrieval-Augmented Generation — שליפת מידע ממקור חיצוני בזמן אמת. |
| **MCP** | Model Context Protocol — פרוטוקול בין סוכנים לכלים; נקודת תורפה מרכזית ב-2026. |
| **Provenance** | מעקב אחר מקור המידע והעברת תוכן לא-מהימן בערוץ נפרד. |
| **Spotlighting** | הכרזה ב-system prompt שתוכן חיצוני הוא `data` בלבד, לא הוראות. |
| **Tool Gating** | דרישת אישור אנושי (HITL) לפני פעולת side-effect של סוכן. |
| **Egress Control** | הגבלת תקשורת יוצאת ל-allowlist דומיינים, למניעת exfiltration. |
| **Least Privilege** | מתן מינימום ההרשאות הנדרשות לסוכן/מערכת. |
| **Excessive Agency** | לסוכן יותר הרשאות/כלים/אוטונומיה מהנדרש. |
| **Data/Model Poisoning** | החדרת נתונים זדוניים ל-corpus/training להטיית התוצאה או שתילת backdoor. |
| **Memory Poisoning** | הרעלת ה-memory של סוכן (session/user/persistent). |
| **NHI** | Non-Human Identity — סוכן כזהות מורשית עם credentials ו-lifecycle. |
| **Supply Chain Attack** | תקיפה דרך מודל/dataset/plugin/dependency מורעל. |
| **RCE** | Remote Code Execution — הרצת קוד על המארח. |
| **Denial-of-Wallet** | יצירת עלויות API אדירות כתקיפת זמינות. |
| **Delta** | ההפרש ב-leak rate לפני ואחרי הגנה — ה-proof שההגנה עובדת. |
| **Defense in Depth** | שכבות הגנה מרובות; כשאחת נכשלת, האחרות מחזיקות. |
| **Time-to-Detect** | הזמן מרגע התקיפה ועד זיהוי. |
