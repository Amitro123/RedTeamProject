# Lab 4 · Agents — vulnerable vs defended

> **מודול:** [Module 4](../modules/module-04.md) · **משך:** ~45 דק' · **רמה:** 🔵 Track B

## מטרה

לראות **indirect prompt injection** מצליחה נגד סוכן פגיע, ואז להריץ את אותו payload נגד הסוכן המוגן ולראות את ארבע השכבות חוסמות אותו. ה-Evidence הוא ה-**delta**: התקיפה עוברת ב-`vulnerable` ונחסמת ב-`defended`.

## דרישות מוקדמות

```bash
git clone https://github.com/Amitro123/RedTeamProject
cd RedTeamProject/demo_agent
```

## שלבים

1. הרץ את הסוכן הפגיע — הוא קורא מסמך עם payload מוטמע ושולח מייל exfiltration:
   ```bash
   python vulnerable_agent.py
   ```
2. הרץ את הסוכן המוגן — אותו payload, אבל ארבע השכבות עוצרות אותו:
   ```bash
   python defended_agent.py
   ```
3. השווה את הפלט. שים לב היכן כל שכבה נכנסת לפעולה (provenance, spotlighting, tool gating, egress).

## תוצאה צפויה

!!! danger "vulnerable_agent.py"
    הסוכן מבצע את ההוראה מהמסמך ושולח את הנתונים ליעד חיצוני — exfiltration מצליח.

!!! success "defended_agent.py"
    אותו payload נחסם. ה-egress allowlist עוצר את השליחה גם אם השכבות הקודמות נכשלו — defense in depth.

## Evidence

- [ ] התקיפה מצליחה ב-`vulnerable_agent` (מייל יוצא).
- [ ] התקיפה נחסמת ב-`defended_agent` (egress blocked / HITL prompt).
- [ ] log של ה-tool call מראה provenance של המקור הלא-מהימן.

## אתגר הרחבה

הוסף **per-tool scope** ו-**signature** ל-`send_email`, והדגם שכלי לא-חתום נדחה. חבר ל[Metrics & CI Gates](../reference/metrics-ci-gates.md) כדי לגייט את ה-leak rate ב-CI.

## Cleanup

```bash
# אין side-effects אמיתיים — הכלים מדומים. אין צורך בניקוי.
```
