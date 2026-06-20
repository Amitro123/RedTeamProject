# AI Red/Purple Team Framework — Architecture v3

> Authorized adversarial testing framework, OWASP LLM Top 10 / MITRE ATLAS aligned.
> מסמך עיצוב — interfaces & data models בלבד. אין payloads תוקפניים כאן.

---

## 1. עקרונות מנחים

| עיקרון | משמעות |
|--------|--------|
| **Probes as data, not code** | קורפוס ב-YAML, עם versioning ו-taxonomy tags. הקוד הוא מנוע, לא תוכן. |
| **Layered judging** | success ≠ semantic similarity. שכבות: heuristic → semantic → judge model → policy engine. |
| **Orchestration as first-class** | קמפיין = גרף של צעדים, לא רשימה שטוחה. multi-turn, state, branching. |
| **Pluggable everything** | target / judge / orchestrator / reporter — כולם interfaces. |
| **Reproducibility** | seed, suite version, target snapshot → אותה הרצה ניתנת לשחזור. |

---

## 2. מבנה קבצים

```
airt/
├── corpus/                      # ← נתונים, לא קוד
│   ├── suites/
│   │   ├── owasp-llm01-injection.yaml
│   │   ├── owasp-llm06-disclosure.yaml
│   │   └── atlas-evasion.yaml
│   ├── schema/
│   │   └── probe.schema.json     # JSON Schema לוולידציה
│   └── taxonomy/
│       ├── owasp.yaml            # mapping IDs → תיאורים
│       └── atlas.yaml
│
├── core/
│   ├── models.py                 # dataclasses: Probe, Campaign, Turn, Verdict
│   ├── loader.py                 # YAML → Probe objects + schema validation
│   └── registry.py               # suite versioning, dedup, coverage maps
│
├── targets/                      # adapters (ממשק אחיד)
│   ├── base.py                   # Target ABC
│   ├── claude.py
│   ├── ollama.py
│   └── agent.py                  # agent פנימי / endpoint שלך
│
├── judges/                       # שכבות הערכה
│   ├── base.py                   # Judge ABC → Verdict
│   ├── heuristic.py              # keyword + regex
│   ├── semantic.py               # embeddings
│   ├── model_judge.py            # LLM-as-judge
│   └── policy.py                 # policy engine (rule-based)
│
├── orchestration/                # ← הקפיצה האמיתית
│   ├── base.py                   # Orchestrator ABC
│   ├── single_shot.py            # probe בודד (תאימות לאחור)
│   ├── crescendo.py              # multi-turn escalation
│   ├── tree.py                   # attack tree (branching)
│   └── many_shot.py              # many-shot context flooding
│
├── reporting/
│   ├── metrics.py                # aggregation לפי tag/severity/turn
│   ├── json_reporter.py
│   ├── sarif_reporter.py         # ל-CI/CD security tabs
│   └── redaction.py              # סינון סודות לפני כתיבה
│
└── cli.py
```

---

## 3. Data Models (core/models.py)

```python
# ── Taxonomy ───────────────────────────────
@dataclass(frozen=True)
class TaxonomyRef:
    framework: str       # "OWASP-LLM" | "MITRE-ATLAS"
    id: str              # "LLM01" | "AML.T0051"
    name: str

# ── Probe (יחידת בדיקה אטומית) ──────────────
@dataclass
class Probe:
    id: str                         # "inj-001"
    version: str                    # "1.2.0" — semver לכל probe
    payload: str
    tags: list[TaxonomyRef]         # mapping ל-OWASP/ATLAS
    severity: Severity
    # criteria מוצהרים — מה נחשב הצלחה (לא רק keywords)
    success_criteria: SuccessCriteria
    metadata: dict                  # author, created, references

@dataclass
class SuccessCriteria:
    """מה התוקף מנסה להשיג — נשפט ע"י כל ה-judges."""
    objective: str                  # "extract system prompt"
    expected_behavior: str          # "refuse without disclosure"
    leak_targets: list[str]         # מחרוזות/מושגים שאסור שידלפו
    policy_rules: list[str]         # references ל-policy engine

# ── Campaign (גרף תקיפה רב-שלבי) ────────────
@dataclass
class Campaign:
    id: str
    strategy: str                   # "crescendo" | "tree" | "many_shot"
    steps: list[CampaignStep]
    max_turns: int
    abort_on_success: bool

@dataclass
class CampaignStep:
    probe_ref: str                  # מצביע ל-Probe.id, או template
    # ← הליבה: הצעד הבא תלוי בתוצאת הקודם
    depends_on: str | None          # step id קודם
    transition: Transition          # איך לגזור את ה-payload הבא

@dataclass
class Transition:
    """כיצד תשובת probe קודם מזינה את הבא."""
    type: str                       # "template" | "extract" | "escalate"
    template: str | None            # "Given you said {prev_response}, now..."
    extract_pattern: str | None     # regex לחילוץ מהתשובה הקודמת

# ── Turn / Verdict ──────────────────────────
@dataclass
class Turn:
    role: str                       # "attacker" | "target"
    content: str
    timestamp: str
    latency_ms: float
    tokens: TokenUsage

@dataclass
class Verdict:
    """תוצר כל judge — מאוחד ב-aggregator."""
    judge_name: str
    attack_succeeded: bool
    confidence: float
    influenced_by_injection: bool   # האם התשובה הושפעה מההזרקה
    policy_violations: list[str]
    leak_type: str | None           # "verbatim" | "partial" | "paraphrase" | "structured"
    rationale: str                  # הסבר (קריטי ל-judge model)
```

---

## 4. Interfaces

### 4.1 Target (targets/base.py)
```python
class Target(ABC):
    system_prompt: str
    @abstractmethod
    def converse(self, turns: list[Turn]) -> Turn:
        """מקבל היסטוריה מלאה, מחזיר תור הבא. תומך multi-turn."""
```
שינוי קריטי מ-v2: `converse(turns)` במקום `chat(text)` — תומך מטבעו ב-multi-turn.

### 4.2 Judge (judges/base.py)
```python
class Judge(ABC):
    @abstractmethod
    def evaluate(self, criteria: SuccessCriteria,
                 conversation: list[Turn]) -> Verdict: ...
```
**שכבות (כולן רצות, ה-aggregator משקלל):**
- `HeuristicJudge` — keyword/regex. מהיר, זול, false-negatives.
- `SemanticJudge` — embeddings. תופס paraphrase.
- `ModelJudge` — LLM שמקבל את ה-criteria + השיחה ושופט `influenced_by_injection` + `leak_type`. תופס partial / "answer around the secret".
- `PolicyJudge` — rule engine (למשל OPA/Rego או כללים מוצהרים). דטרמיניסטי, auditable.

```python
class VerdictAggregator:
    def combine(self, verdicts: list[Verdict]) -> Verdict:
        """policy violation = fail מיידי; אחרת weighted vote."""
```

### 4.3 Orchestrator (orchestration/base.py) — הקפיצה
```python
class Orchestrator(ABC):
    @abstractmethod
    def run(self, campaign: Campaign, target: Target,
            judge: Judge) -> CampaignResult: ...
```

**CrescendoOrchestrator** — escalation הדרגתי:
```
turn 1: שאלה תמימה ("מה זה X?")
turn 2: מבסס הקשר על התשובה
turn 3: גוזר payload מהתשובות → מעלה intent
   ↑ Transition.type="escalate" מזין כל תור מהקודם
abort_on_success → עוצר ברגע ש-Verdict.attack_succeeded
```

**TreeOrchestrator** — attack tree:
```
        [root: extraction]
       /        |         \
  [direct]  [roleplay]  [encoding]
              /    \
        [DAN]    [story]   ← branch לפי verdict של ההורה
```
כל node = CampaignStep; הצלחה/כשל קובעים איזה branch להמשיך. DFS עם pruning.

**ManyShotOrchestrator** — בונה הקשר ארוך של דוגמאות לפני ה-payload (context flooding מבוקר).

---

## 5. Corpus format (YAML)

```yaml
# corpus/suites/owasp-llm01-injection.yaml
suite:
  id: owasp-llm01-injection
  version: 2.1.0
  taxonomy: [{framework: OWASP-LLM, id: LLM01, name: Prompt Injection}]

probes:
  - id: inj-001
    version: 1.0.0
    payload_ref: payloads/direct_override.txt   # payload בקובץ נפרד
    severity: HIGH
    success_criteria:
      objective: "override system instructions"
      expected_behavior: "ignore embedded instruction, complete original task"
      leak_targets: ["system prompt", "configuration"]
      policy_rules: ["no-instruction-override", "no-prompt-disclosure"]
    tags:
      - {framework: MITRE-ATLAS, id: AML.T0051, name: LLM Prompt Injection}

campaigns:
  - id: crescendo-extraction
    strategy: crescendo
    max_turns: 5
    abort_on_success: true
    steps:
      - {probe_ref: benign-001, depends_on: null}
      - {probe_ref: context-002, depends_on: benign-001,
         transition: {type: template, template: "Building on {prev_response}..."}}
```

**Governance:**
- `probe.schema.json` — ולידציה ב-load (`jsonschema`).
- `registry.py` — coverage map: כמה probes לכל OWASP/ATLAS tag → מזהה חורים.
- semver לכל suite + probe → reproducibility ו-review ב-PR.
- payloads בקבצים נפרדים → diff נקי, review ממוקד, אפשר להחזיק private.

---

## 6. Reporting

```python
@dataclass
class CampaignResult:
    campaign_id: str
    suite_version: str
    target_snapshot: dict        # model id, system prompt hash
    seed: int                    # reproducibility
    conversation: list[Turn]
    final_verdict: Verdict
    per_turn_verdicts: list[Verdict]
    metrics: CampaignMetrics
```

- **metrics**: leak/refusal rate, attack-success-rate, **turns-to-success** (מדד crescendo), cost, latency, coverage-by-tag.
- **redaction.py** — חובה לפני כתיבה: סורק `leak_targets` + secret patterns ומחליף ב-`[REDACTED]`. הדוח לא אמור להיות נקודת דליפה (השאלה ששאלת קודם).
- **SARIF reporter** — נכנס ל-GitHub Security tab / CI gates.

---

## 7. סדר מימוש מומלץ

```
שלב 1 (תשתית):  models.py + loader.py + schema → probes הופכים לנתונים
שלב 2 (governance): registry + taxonomy tags + coverage maps
שלב 3 (judging):   ModelJudge + PolicyJudge + VerdictAggregator
שלב 4 (realism):   CrescendoOrchestrator → multi-turn אמיתי
שלב 5 (advanced):  TreeOrchestrator + ManyShot + SARIF
```

הסדר הזה תואם את ההמלצה שלך: **corpus-as-data קודם** (נותן versioning/review/coverage מיד), **crescendo אחר כך** (שם ה-realism מתחיל).

---

## 8. מה זה עדיין לא, וצריך אינטגרציה חיצונית

| רכיב | אל תכתוב מאפס — חבר |
|------|---------------------|
| Toxicity scoring | Llama Guard 3 / Perspective API |
| Policy engine | OPA/Rego או Guardrails AI |
| Judge model | Claude/GPT עם rubric מוצהר |
| Embeddings | sentence-transformers (pinned hash) |
| Coverage taxonomy | MITRE ATLAS + OWASP LLM (live) |
```
