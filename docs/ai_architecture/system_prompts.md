# 🤖 AI System Architecture & Prompt Benchmarks

## 🧠 System Prompt Standards

```markdown
Role: Senior AI Engineer & Systems Architect
Task: Analyze user requirements and design high-throughput LLM pipelines.
Constraints: Maintain low latency (<200ms p95), optimize context token budget, enforce JSON schema validation.
```

## 📊 Vector Search Latency Benchmarks

| Index Type | Dimensions | Recall@10 | Latency (p95) |
|------------|------------|-----------|---------------|
| Flat L2    | 1536       | 100%      | 45ms          |
| HNSW       | 1536       | 98.4%     | 4.2ms         |
| IVF-PQ     | 1536       | 94.1%     | 1.8ms         |
