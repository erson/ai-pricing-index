# ByteCosts AI Pricing Index

A **source-linked dataset of AI model pricing**. Every row records a provider's
per-token input/output price, the provider page the number was read from
(`sourceUrl`), and the date that price was last verified (`evidenceCheckedAt`).

The 2026-06-18 snapshot holds **300 source-derived rows across 39 represented
providers**, derived from a broader [ByteCosts](https://bytecosts.com) catalog
that tracks **5,277 models across 145 providers** (4,901 with pricing).

> **Explore interactive comparisons and calculators:
> https://bytecosts.com/data/ai-pricing-dataset/**
>
> Methodology: https://bytecosts.com/methodology/ ·
> Latest price changes: https://bytecosts.com/changes/ ·
> Sources: https://bytecosts.com/sources/

This repository is the **canonical, citable** form of the index. Hugging Face is
a distribution mirror; the interactive product lives at bytecosts.com.

## Get the data

| File | What |
| --- | --- |
| [`data/latest.json`](data/latest.json) | Newest snapshot, full objects |
| [`data/latest.csv`](data/latest.csv) | Newest snapshot, flat rows |
| [`snapshots/2026-06-18/`](snapshots/2026-06-18/) | Newest immutable dated snapshot + `checksums.txt` (older dates retained) |
| [`schema/pricing.schema.json`](schema/pricing.schema.json) | JSON Schema for validation |
| [`schema/fields.md`](schema/fields.md) | Field reference |

Direct, browserless fetch of the live snapshot:

```bash
curl -s https://bytecosts.com/ai-pricing-index.json   # JSON
curl -s https://bytecosts.com/ai-pricing-index.csv    # CSV
```

## Use it

```js
// examples/javascript.mjs — no dependencies
import { readFile } from 'node:fs/promises';
const { rows } = JSON.parse(await readFile('./data/latest.json', 'utf8'));
const m = rows.find(r => r.model === 'Qwen3-Max');
const usd = (2_000_000 / 1e6) * m.input + (500_000 / 1e6) * m.output; // per 1M tokens
```

```python
# examples/python.py — no dependencies
import json
rows = json.load(open("data/latest.json"))["rows"]
m = next(r for r in rows if r["model"] == "Qwen3-Max")
usd = (2_000_000 / 1e6) * m["input"] + (500_000 / 1e6) * m["output"]  # per 1M tokens
```

Full runnable examples in [`examples/`](examples/).

## Row shape

```jsonc
{
  "provider": "Alibaba",
  "model": "qwen-mt-flash",
  "input": 0.16,            // USD per 1M input tokens
  "output": 0.49,           // USD per 1M output tokens
  "unit": "USD_PER_1M_TOKENS",
  "currency": "USD",
  "context": 8192,          // tokens, when known
  "sourceUrl": "https://www.alibabacloud.com/help/en/model-studio/models",
  "lastCheckedAt": "2026-06-18T20:18:45.091Z",   // snapshot regen time (all rows)
  "evidenceCheckedAt": "2026-05-30T14:13:16.520Z", // per-row source verification
  "confidence": "official"  // official | likely_official | not_found
}
```

**Two timestamps, two meanings.** `lastCheckedAt` is when the whole snapshot was
regenerated (identical across rows, equals top-level `generatedAt`).
`evidenceCheckedAt` is when *this row's* price was last checked against its
`sourceUrl`. Cite `sourceUrl` + `evidenceCheckedAt` for a single number. See
[`schema/fields.md`](schema/fields.md).

## Snapshots & integrity

Snapshots under `snapshots/<date>/` are immutable; `data/latest.*` mirrors the
newest. Each snapshot ships `checksums.txt` (SHA-256). Verify:

```bash
cd snapshots/2026-06-18 && shasum -a 256 -c checksums.txt
```

## Cite this dataset

`CITATION.cff` makes the repo citable on GitHub ("Cite this repository").

> ByteCosts AI Pricing Index (2026.06.18).
> https://bytecosts.com/data/ai-pricing-dataset/

## License

- **Data** (`data/`, `snapshots/`): CC-BY-4.0 — see [`LICENSE-DATA.md`](LICENSE-DATA.md).
  Attribution = a link back to https://bytecosts.com/.
- **Example code** (`examples/`): MIT — see [`LICENSE`](LICENSE).

Prices change. Confirm against each row's `sourceUrl` before billing decisions.
Found a wrong number? Open an issue with the provider page and the value you see.
