# Changelog

Snapshots are immutable; `data/latest.*` always points at the newest one.
Versions use the snapshot date (`YYYY.MM.DD`).

## 2026.06.18

- Data refresh. 300 source-derived rows across 39 represented providers.
- Broader catalog now tracks 5,277 models / 145 providers (4,901 with pricing).
- Evidence grades (source-derived rows): A+ = 204, A = 85, C = 10, D = 1.
- `data/latest.*` now points at `snapshots/2026-06-18/`; 2026-06-14 retained.

## 2026.06.14

- Initial public release.
- 300 source-derived pricing rows across 39 represented providers.
- Derived from a ByteCosts catalog tracking 5,261 models / 145 providers
  (4,888 with pricing) as of 2026-06-14.
- Files: `data/latest.json`, `data/latest.csv`,
  `snapshots/2026-06-14/` (with `checksums.txt`).
