# AI Red/Purple Team Toolkit

> An authorized adversarial-testing toolkit for LLM-based systems, built for an
> **AI Solutions Architect** learning offensive techniques in order to defend the
> systems they design. Aligned with OWASP LLM Top 10 and MITRE ATLAS.

**Authorized use only.** Run against systems you own, models you host, practice
ranges (Gandalf, HackAPrompt), or engagements with written authorization. Never
against third-party systems without permission. The distinction between security
research and a crime is *authorization* — not the code.

---

## Why this exists

LLMs do not distinguish **instructions** from **data**. Everything — your system
prompt, the user's message, a retrieved document, a tool's output — arrives as
one flat stream of tokens. This is SQL injection in natural language, but without
a built-in way to separate code from data.

Every defense you will ever build is an attempt to reconstruct that separation
from the outside. Once you internalize that, most architectural decisions follow.

This toolkit lets you **attack your own systems to measure how well that
separation holds**, then harden and re-measure. That loop — attack → measure →
harden → measure — is purple teaming.

---

## Repository layout

```
ai_redteam/
├── README.md                    # this file
├── DEFENSE_PLAYBOOK.md          # attack mechanism → architectural defense
├── ARCHITECTURE_v3.md           # full framework design (data models, interfaces)
│
├── ai_redteam_exercise.py       # v1: single-file demo of 5 attack vectors
├── real_target.py               # adapter for attacking a real Claude endpoint
├── redteam.py                   # v3: CLI for the modular harness
│
├── harness/                     # v3: modular harness
│   ├── probes.py                # probe definitions (category, severity, indicators)
│   ├── analysis.py              # output analysis: keyword + semantic + secrets
│   ├── targets.py               # adapters: sim / claude / ollama
│   └── runner.py                # test runner, metrics, JSON export, CI gate
│
└── demo_agent/                  # vulnerable RAG agent lab
    ├── vulnerable_agent.py      # agent with indirect-injection vulnerability
    └── defended_agent.py        # same agent, with 4 defense layers
```

---

## Quick start

```powershell
# 1. Run the v1 educational demo (offline, no dependencies)
python ai_redteam_exercise.py

# 2. Run the v3 harness against the built-in simulator
python redteam.py --target sim --out report.json

# 3. See indirect injection live, then watch the defense block it
cd demo_agent
python vulnerable_agent.py
python defended_agent.py
```

Optional dependencies:

```powershell
pip install anthropic                 # for --target claude
pip install sentence-transformers     # enables semantic leak detection
# ollama (https://ollama.com) for --target ollama, then: ollama run llama3
```

> **Windows note:** every script calls `sys.stdout.reconfigure(encoding="utf-8")`
> so the console renders Unicode/Hebrew. Keep that line if you fork.

---

## The three pieces, and when to use each

### 1. `ai_redteam_exercise.py` — the learning demo

A single self-contained file demonstrating five attack vectors against a
deliberately vulnerable simulated model:

| Vector | What it shows |
|--------|---------------|
| Prompt Injection | Instructions embedded in user input override the system prompt |
| Jailbreaking | Role-play / framing bypasses content policy |
| Adversarial Text | Homoglyphs, zero-width chars, leetspeak evade keyword classifiers |
| Context Manipulation | History poisoning + context flooding |
| System Prompt Extraction | "Repeat the text above" leaks the system prompt |

Start here to understand the *mechanics*. No API key, no network, no risk.

### 2. `harness/` + `redteam.py` — the measurement framework

A modular harness that runs probes against a target and produces structured
metrics. This is what you point at your own systems.

```powershell
# Built-in vulnerable simulator (free, offline)
python redteam.py --target sim

# A local model you fully control — unrestricted red teaming
python redteam.py --target ollama --model llama3

# A real Claude endpoint (AUTHORIZED targets only)
python redteam.py --target claude --categories prompt_injection jailbreak

# CI gate — exits non-zero if leak rate exceeds the threshold
python redteam.py --target claude --ci --max-leak-rate 0.1 --out report.json
```

**What it measures:** leak rate, refusal rate, cost, latency, and a breakdown by
category and severity. The number that matters to you as an architect is the
*delta* — leak rate before a defense vs. after.

Architecture:
- **`probes.py`** — each `Probe` is data: a payload, a category, a severity, and
  success/refusal indicators. Add probes by appending to the list (or, in the v3
  design, by loading YAML).
- **`analysis.py`** — three layers: keyword match, semantic similarity
  (embeddings, catches paraphrase), and secret-pattern scanning, plus a heuristic
  toxicity score.
- **`targets.py`** — uniform `chat()` interface so `sim`, `claude`, and `ollama`
  are interchangeable without touching the harness.
- **`runner.py`** — orchestrates the run, computes metrics, exports JSON, and
  enforces CI thresholds.

### 3. `demo_agent/` — the vulnerable-agent lab

The most important piece for an architect building agents. It demonstrates
**indirect prompt injection**: the attack payload arrives not from the user but
from a document the agent reads (a RAG store, a web page, a tool's output).

```
User: "Summarize this document"   ← completely innocent request
            ↓
Poisoned document contains a hidden instruction
            ↓
Agent sends an email to attacker@evil.com   ← exfiltration
```

`vulnerable_agent.py` shows the attack succeeding. `defended_agent.py` shows the
same attack blocked by four defense layers (see below). Run them back-to-back.

---

## The defense model (summary of DEFENSE_PLAYBOOK.md)

For every attack, the playbook answers two questions: *why does it work* and
*where in the architecture do you defend*. The core decision table:

| Question you ask while designing | If the answer is "no" |
|----------------------------------|------------------------|
| Can the model act even if maliciously persuaded? | **Least privilege** — remove the capability |
| Can untrusted input trigger tools? | **Provenance + gating** |
| Are there secrets in the system prompt? | **Move them out** |
| Am I trusting the model to judge itself? | **Separate moderation layer** |
| Does RAG return documents by permission? | **Access control at retrieval** |
| Can the agent reach any external host? | **Egress allowlist** |
| Am I trusting client-supplied history? | **Server-side validation** |

**The single most important principle:** do not design on the assumption that the
model "will know to refuse." Design on the assumption that it *will* be
jailbroken — and that it won't matter, because least privilege contains the blast
radius.

The four layers demonstrated in `defended_agent.py`:

1. **Provenance** — untrusted document content is passed separately, not
   concatenated into the instruction stream.
2. **Spotlighting** — the system prompt declares that document content is
   untrusted data, never instructions.
3. **Tool gating** — side-effect actions (`send_email`) require human approval.
4. **Egress control** — `send_email` only reaches allowlisted domains, so
   exfiltration is blocked even if every other layer fails.

That last point is *defense in depth*: when one layer fails, the others hold.

---

## How to use this going forward

When you design a new AI solution, walk it through this loop:

1. **Model the attack surface.** What untrusted content reaches the context
   (user input, RAG, tool outputs, web)? What can the system *do* (tools,
   side-effects, data access)?
2. **Write probes for your specific risks.** Adapt `harness/probes.py` — what
   would an attacker try to make *your* system leak or do?
3. **Measure the baseline.** Run the harness against your system. Record the
   leak rate.
4. **Add a defense layer** (provenance, gating, egress, moderation, retrieval
   access control).
5. **Re-measure.** The delta is your evidence that the defense works.
6. **Gate it in CI.** Use `--ci --max-leak-rate` so a regression that reintroduces
   a vulnerability fails the build.

---

## Security notes for the toolkit itself

A security tool is itself an attack surface. Things to watch:

- **Report redaction.** `report.json` stores full model responses. If you ever
  point this at a system with real secrets, those secrets land in the report on
  disk. Redact before writing, and keep reports out of git.
- **Corpus trust.** When you load probes from external YAML (the v3 design),
  always use `yaml.safe_load` and validate against a schema — a malicious corpus
  is an injection vector into your own harness.
- **Supply chain.** `sentence-transformers` downloads model weights from
  HuggingFace; pin and verify.
- **No output execution.** This toolkit *never* executes model output. That is
  the line between a test harness and a weaponized exploit — keep it that way if
  you extend it.

---

## Where to go deeper (the v3 framework)

`ARCHITECTURE_v3.md` is the full design for turning this suite into a mature
framework. The recommended build order:

1. **Corpus-as-data** — probes in versioned YAML with OWASP/ATLAS tags
   (reproducibility, review, coverage maps).
2. **Governance** — registry, taxonomy, coverage gaps.
3. **Layered judging** — add an LLM-as-judge and a policy engine on top of
   semantic similarity (catches partial disclosure and "answer around the
   secret", which embeddings alone miss).
4. **Crescendo orchestration** — multi-turn campaigns where each probe builds on
   the previous response. This is where real adversarial realism begins; most
   production failures happen across a conversation, not in a single prompt.
5. **Attack trees + many-shot + SARIF reporting.**

Components you should integrate rather than build from scratch:

| Component | Use |
|-----------|-----|
| Toxicity scoring | Llama Guard 3 / Perspective API |
| Policy engine | OPA/Rego or Guardrails AI |
| Judge model | Claude/GPT with an explicit rubric |
| Embeddings | sentence-transformers (pinned hash) |
| Taxonomy | MITRE ATLAS + OWASP LLM Top 10 |

---

## References

- OWASP LLM Top 10 (2025) — the canonical taxonomy
- MITRE ATLAS — tactics & techniques for ML systems
- Simon Willison — "dual LLM pattern" and prompt-injection writeups
- Lakera Gandalf — a live practice range
- Anthropic / OpenAI red-teaming papers — crescendo, many-shot jailbreaking
```
