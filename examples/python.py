"""Load the ByteCosts AI Pricing Index and estimate a token-workload cost.

No dependencies. Run: python examples/python.py
"""
import json
from pathlib import Path

data = json.loads((Path(__file__).parent.parent / "data" / "latest.json").read_text("utf-8"))
rows = data["rows"]


def _norm(s):
    return str(s).lower().strip()


def get_model(query):
    for r in rows:
        if _norm(r["model"]) == _norm(query) or _norm(f'{r["provider"]}/{r["model"]}') == _norm(query):
            return r
    return None


def estimate_cost(model, input_tokens=0, output_tokens=0):
    r = get_model(model) if isinstance(model, str) else model
    if not r:
        return None
    inp = (input_tokens / 1_000_000) * (r.get("input") or 0)  # rows are USD per 1M tokens
    out = (output_tokens / 1_000_000) * (r.get("output") or 0)
    return {"input": inp, "output": out, "total": inp + out, "currency": r["currency"], "source": r["sourceUrl"]}


if __name__ == "__main__":
    print(f'snapshot {data["generatedAt"]} — {len(rows)} rows')
    s = rows[0]
    print("first row:", s["provider"], s["model"], s["input"], "/", s["output"])
    print("cost for 2M in + 0.5M out:", estimate_cost(s["model"], input_tokens=2_000_000, output_tokens=500_000))

# Data: ByteCosts AI Pricing Index — https://bytecosts.com/data/ai-pricing-dataset/
