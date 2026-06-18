// Load the ByteCosts AI Pricing Index and estimate a token-workload cost.
// No dependencies. Run: node examples/javascript.mjs
import { readFile } from 'node:fs/promises';

const { rows, generatedAt } = JSON.parse(
  await readFile(new URL('../data/latest.json', import.meta.url), 'utf8')
);

const norm = (s) => String(s).toLowerCase().trim();
const getModel = (q) =>
  rows.find((r) => norm(r.model) === norm(q) || norm(`${r.provider}/${r.model}`) === norm(q));

// Rows are USD per 1M tokens.
function estimateCost(model, { inputTokens = 0, outputTokens = 0 } = {}) {
  const r = typeof model === 'string' ? getModel(model) : model;
  if (!r) return null;
  const input = (inputTokens / 1e6) * (r.input ?? 0);
  const output = (outputTokens / 1e6) * (r.output ?? 0);
  return { input, output, total: input + output, currency: r.currency, source: r.sourceUrl };
}

console.log(`snapshot ${generatedAt} — ${rows.length} rows`);
const sample = rows[0];
console.log('first row:', sample.provider, sample.model, sample.input, '/', sample.output);
console.log('cost for 2M in + 0.5M out:', estimateCost(sample.model, { inputTokens: 2e6, outputTokens: 5e5 }));

// Data: ByteCosts AI Pricing Index — https://bytecosts.com/data/ai-pricing-dataset/
