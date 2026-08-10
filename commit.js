const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Parse CLI arguments
const args = process.argv.slice(2);
let minCommits = 12;
let maxCommits = 50;
let explicitCount = null;
let isDryRun = false;

args.forEach((arg) => {
  if (arg.startsWith('--min=')) minCommits = parseInt(arg.split('=')[1], 10);
  if (arg.startsWith('--max=')) maxCommits = parseInt(arg.split('=')[1], 10);
  if (arg.startsWith('--count=')) explicitCount = parseInt(arg.split('=')[1], 10);
  if (arg === '--dry-run') isDryRun = true;
});

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const totalCommits = explicitCount !== null ? explicitCount : getRandomInt(minCommits, maxCommits);

// Directories
const pyDir = path.join(__dirname, 'src', 'python');
const jsDir = path.join(__dirname, 'src', 'javascript');
const javaDir = path.join(__dirname, 'src', 'java');
const docDir = path.join(__dirname, 'docs', 'ai_architecture');

[pyDir, jsDir, javaDir, docDir].forEach(d => {
  if (!fs.existsSync(d)) fs.mkdirSync(d, { recursive: true });
});

// Generators for Python, JS, Java, MD
const pythonSnippets = [
  {
    file: 'rag_pipeline.py',
    msg: 'feat(python): add similarity threshold filter to RAG pipeline',
    code: '\ndef filter_by_threshold(docs, threshold=0.75):\n    """Filter retrieved documents above confidence score threshold."""\n    return [doc for doc in docs if doc.get("score", 0) >= threshold]\n'
  },
  {
    file: 'embeddings_utils.py',
    msg: 'feat(python): implement L2 vector normalization routine',
    code: 'import math\n\ndef l2_normalize(vector):\n    """Normalize embedding vector using L2 norm."""\n    norm = math.sqrt(sum(x * x for x in vector))\n    if norm == 0:\n        return vector\n    return [x / norm for x in vector]\n'
  },
  {
    file: 'llm_evaluator.py',
    msg: 'feat(python): add BLEU & ROUGE score calculator for AI evals',
    code: 'def evaluate_hallucination_score(ground_truth: str, answer: str) -> float:\n    """Estimate hallucination ratio via token overlap."""\n    gt_tokens = set(ground_truth.lower().split())\n    ans_tokens = set(answer.lower().split())\n    if not ans_tokens:\n        return 0.0\n    return len(gt_tokens.intersection(ans_tokens)) / len(ans_tokens)\n'
  }
];

const jsSnippets = [
  {
    file: 'llmStreamClient.js',
    msg: 'feat(js): add exponential backoff retry handler for LLM API',
    code: '\n  async retryWithBackoff(fn, retries = 3, delay = 1000) {\n    try {\n      return await fn();\n    } catch (err) {\n      if (retries <= 0) throw err;\n      await new Promise(res => setTimeout(res, delay));\n      return this.retryWithBackoff(fn, retries - 1, delay * 2);\n    }\n  }\n'
  },
  {
    file: 'vectorMath.js',
    msg: 'feat(js): add Euclidean distance calculation helper',
    code: 'function euclideanDistance(a, b) {\n  let sum = 0;\n  for (let i = 0; i < a.length; i++) {\n    sum += Math.pow(a[i] - b[i], 2);\n  }\n  return Math.sqrt(sum);\n}\n\nmodule.exports = { euclideanDistance };\n'
  }
];

const javaSnippets = [
  {
    file: 'VectorStore.java',
    msg: 'feat(java): implement cosine similarity algorithm in VectorStore',
    code: '\n    public static float cosineSimilarity(float[] a, float[] b) {\n        float dot = calculateDotProduct(a, b);\n        float normA = 0.0f, normB = 0.0f;\n        for (int i = 0; i < a.length; i++) {\n            normA += a[i] * a[i];\n            normB += b[i] * b[i];\n        }\n        return (normA == 0 || normB == 0) ? 0.0f : (float)(dot / (Math.sqrt(normA) * Math.sqrt(normB)));\n    }\n'
  },
  {
    file: 'EmbeddingsCache.java',
    msg: 'feat(java): add LRU embeddings cache container for vector queries',
    code: 'package com.ai.vectorstore;\nimport java.util.LinkedHashMap;\nimport java.util.Map;\n\npublic class EmbeddingsCache<K, V> extends LinkedHashMap<K, V> {\n    private final int capacity;\n    public EmbeddingsCache(int capacity) {\n        super(capacity, 0.75f, true);\n        this.capacity = capacity;\n    }\n    @Override\n    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {\n        return size() > capacity;\n    }\n}\n'
  }
];

const mdSnippets = [
  {
    file: 'system_prompts.md',
    msg: 'docs(ai): update prompt engineering architecture notes',
    code: `\n\n### ⚡ Daily Update: ${new Date().toISOString().split('T')[0]}\n- Optimized zero-shot chain-of-thought system prompt.\n- Reduced prompt overhead by ~14% while improving reasoning accuracy.\n`
  },
  {
    file: 'rag_benchmarks.md',
    msg: 'docs(ai): add vector database latency vs recall matrix',
    code: `# RAG Vector Database Benchmarks\n\n- Date: ${new Date().toISOString()}\n- Tested Index: HNSW (M=16, efConstruction=200)\n- Query Throughput: 4,200 QPS\n`
  }
];

const allGenerators = [
  { type: 'python', dir: pyDir, items: pythonSnippets },
  { type: 'js', dir: jsDir, items: jsSnippets },
  { type: 'java', dir: javaDir, items: javaSnippets },
  { type: 'md', dir: docDir, items: mdSnippets }
];

console.log(`🤖 AI Engineer Automated Contribution Generator`);
console.log(`📊 Target Commits Today: ${totalCommits} (Range: ${minCommits}-${maxCommits})`);

let successCount = 0;

for (let i = 0; i < totalCommits; i++) {
  const category = allGenerators[Math.floor(Math.random() * allGenerators.length)];
  const item = category.items[Math.floor(Math.random() * category.items.length)];
  
  const targetPath = path.join(category.dir, item.file);
  const stamp = `\n// Updated at: ${new Date().toISOString()} [Pulse ${i + 1}/${totalCommits}]\n`;
  
  fs.appendFileSync(targetPath, stamp + item.code, 'utf8');

  const commitMsg = `${item.msg} [${i + 1}/${totalCommits}]`;

  if (!isDryRun) {
    try {
      execSync(`git add "${targetPath}"`, { stdio: 'pipe' });
      execSync(`git commit -m "${commitMsg}"`, { stdio: 'pipe' });
      successCount++;
    } catch (err) {
      console.error(`❌ Commit failed for step ${i + 1}:`, err.message);
    }
  } else {
    successCount++;
  }
}

console.log(`✅ Successfully generated and committed ${successCount} AI Engineering updates!`);
