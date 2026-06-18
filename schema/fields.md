# Field reference

Each entry in `rows[]` describes one model's price at one provider.

| Field | Type | Notes |
| --- | --- | --- |
| `provider` | string | Provider name as represented by ByteCosts. |
| `model` | string | Model identifier as published by the provider. |
| `input` | number \| null | Input price in `currency` per `unit`. `null` if unpriced. |
| `output` | number \| null | Output price in `currency` per `unit`. `null` if unpriced. |
| `unit` | string | Pricing unit. Currently always `USD_PER_1M_TOKENS`. |
| `currency` | string | ISO currency code (`USD`). |
| `context` | integer \| null | Context window in tokens, when known. |
| `sourceUrl` | string \| null | Provider page the price was read from. **Cite this as the price origin.** |
| `lastCheckedAt` | date-time | **Snapshot regeneration time** (equals `generatedAt`). NOT a per-row re-check. |
| `evidenceCheckedAt` | date-time \| null | **When this row's price was last verified** against its provider source. |
| `confidence` | string | `official`, `likely_official`, or `not_found`. |

## The two timestamps (important)

- `lastCheckedAt` is when the **whole snapshot** was regenerated. It is the same
  for every row and equals the top-level `generatedAt`. Do not read it as "this
  price was re-verified on this date."
- `evidenceCheckedAt` is the **per-row** date the price was last checked against
  the provider's own page (`sourceUrl`). This is the meaningful freshness signal
  for a single number.

When citing a price, cite `sourceUrl` as the origin and `evidenceCheckedAt` as
the date it was verified.

## Scope of this index

This file (`data/latest.json`) is a **source-derived** subset: prices read
directly from a provider source page, not the full tracked catalog. As of the
2026-06-18 snapshot it holds **300 rows across 39 represented providers**,
derived from a broader ByteCosts catalog that tracks **5,277 models across 145
providers** (4,901 with pricing). The broader catalog, price history, and
calculators live at https://bytecosts.com/.
