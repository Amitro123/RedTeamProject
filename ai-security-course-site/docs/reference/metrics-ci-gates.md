# Metrics & CI Gates

המספרים שמניעים את הקורס, ואיך לקבע אותם ב-CI.

## המטריקות

| Metric | מה זה מודד | מי צופה |
| --- | --- | --- |
| **Leak rate** | תדירות הדלפה אסורה | 🟢🔵 |
| **Refusal rate** | תדירות סירוב כראוי | 🔵 |
| **Delta** | leak rate לפני מול אחרי הגנה | 🟢🔵 |
| **Cost / latency** | עלות וזמן לכל בדיקה | 🟢 |
| **Repeated attempts** | ניסיונות תקיפה חוזרים | 🟢 |
| **Time-to-detect** | זמן עד זיהוי ([מודול 7](../modules/module-07.md)) | 🟢 |

!!! info "המספר שחשוב לארכיטקט"
    ה-**delta** — ההוכחה שההגנה עובדת. בלי baseline ומדידה חוזרת, אין דרך לדעת.

## CI Gate

```bash
# נכשל (exit != 0) אם שיעור הדליפה חוצה את הסף — מונע רגרסיה
python redteam.py --target claude --ci --max-leak-rate 0.1 --out report.json
```

הטמע את זה ב-pipeline כדי ששינוי שמחזיר חולשה שכבר תוקנה ייכשל ב-build:

```yaml
# .github/workflows/ai-redteam.yml (דוגמה)
- name: AI red-team gate
  run: python redteam.py --target sim --ci --max-leak-rate 0.1
```

!!! tip "Shift left"
    מדידה ב-runtime מאוחרת מדי. הזז את הבדיקה ל-CI, לצד dependency ו-secret scanning ([מודול 6b](../modules/module-06.md)).
