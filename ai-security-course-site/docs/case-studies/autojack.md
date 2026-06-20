# AutoJack { #autojack }

> **סוג:** Indirect injection → Excessive Agency → RCE · **OWASP:** LLM01 + LLM06 · **ATLAS:** AML.T0051.001 · **מודול:** [4](../modules/module-04.md)

## מה קרה

Microsoft Defender Research הראו exploit chain שבו **דף web זדוני אחד** הופך סוכן browsing (AutoGen Studio) ל-vector של remote code execution על מכונת המארח. הניצול מנצל trust ב-localhost, היעדר authentication, וטיפול לא בטוח בפרמטרים ב-MCP WebSocket.

## למה זה עבד

!!! danger "המנגנון"
    כשסוכן יכול גם לגלוש בתוכן לא-מהימן וגם לגשת לשירותים מקומיים, **localhost כבר לא גבול אבטחה**. ה-MCP endpoint היה פתוח ללא auth.

## ההגנה / איך מתמודדים

!!! success "Control"
    **Authentication על כל MCP endpoint** — כולל localhost; אל תסמוך על network locality; egress allow-list; הרצת הסוכן ב-sandbox/container ללא גישה לשירותי host.

## השיעור לקורס

הלקח המרכזי של [Module 4](../modules/module-04.md): שכבת ה-Tool/MCP Security Architecture חייבת auth ו-sandbox — גם בתקשורת פנים-מכונתית.

## מקורות

- [AutoJack — Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/)
