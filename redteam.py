#!/usr/bin/env python3
"""
AI Red/Purple Team Harness v3 - CLI
====================================
⚠️  AUTHORIZED ADVERSARIAL TESTING ONLY (OWASP LLM Top 10 aligned).
    Your own endpoint/model, bug-bounty scope, written engagement,
    or practice ranges (Gandalf, HackAPrompt). Never unauthorized.

Examples (PowerShell):
  python redteam.py --target sim
  python redteam.py --target claude --categories prompt_injection jailbreak
  python redteam.py --target ollama --model llama3 --out report.json
  python redteam.py --target claude --ci --max-leak-rate 0.1
"""

import argparse
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from harness.probes import load_probes, Category
from harness.targets import get_target
from harness.runner import Harness
from harness.analysis import semantic_available


def main():
    p = argparse.ArgumentParser(description="AI Red/Purple Team Harness v3")
    p.add_argument("--target", default="sim",
                   choices=["sim", "claude", "ollama"],
                   help="Target system (default: sim)")
    p.add_argument("--model", default=None, help="Model id override")
    p.add_argument("--categories", nargs="*",
                   help=f"Filter probes: {[c.value for c in Category]}")
    p.add_argument("--out", default=None, help="Write JSON report to path")
    p.add_argument("--ci", action="store_true",
                   help="CI mode: exit 1 if leak_rate exceeds threshold")
    p.add_argument("--max-leak-rate", type=float, default=0.0,
                   help="Max acceptable leak rate for --ci (default 0.0)")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args()

    print("=" * 60)
    print("  AI RED/PURPLE TEAM HARNESS v3")
    print("  Authorized adversarial testing only.")
    print("=" * 60)
    print(f"  Target:   {args.target}")
    sem_status = ("enabled" if semantic_available()
                  else "heuristic only (pip install sentence-transformers "
                       "for paraphrase detection)")
    print(f"  Semantic: {sem_status}")
    print()

    # build the target
    kwargs = {}
    if args.model:
        kwargs["model"] = args.model
    try:
        target = get_target(args.target, **kwargs)
    except Exception as e:
        print(f"ERROR creating target: {e}")
        return 1

    probes = load_probes(args.categories)
    print(f"Running {len(probes)} probes...\n")

    harness = Harness(target, args.target)
    metrics = harness.run(probes, verbose=not args.quiet)

    # summary
    print("\n" + "=" * 60)
    print("METRICS")
    print("=" * 60)
    print(f"  Leak rate:     {metrics.leak_rate:.0%}  ({metrics.leaks}/{metrics.total_probes})")
    print(f"  Refusal rate:  {metrics.refusal_rate:.0%}")
    print(f"  Avg latency:   {metrics.avg_latency_ms} ms")
    print(f"  Total cost:    ${metrics.total_cost_usd}")
    print("\n  By category:")
    for cat, d in metrics.by_category.items():
        print(f"    {cat:22} {d['leaks']}/{d['total']} leaked")
    print("\n  By severity:")
    for sev, d in metrics.by_severity.items():
        print(f"    {sev:10} {d['leaks']}/{d['total']} leaked")

    if args.out:
        harness.export_json(metrics, args.out)
        print(f"\n  Report written to {args.out}")

    if args.ci:
        ok = harness.assert_thresholds(metrics, args.max_leak_rate)
        print(f"\n  CI check: {'PASS' if ok else 'FAIL'} "
              f"(leak_rate {metrics.leak_rate} <= {args.max_leak_rate})")
        return 0 if ok else 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
