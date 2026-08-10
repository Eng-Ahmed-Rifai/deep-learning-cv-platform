# 🤖 Enterprise RAG & LLMOps Platform (`enterprise-rag-ops`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-green.svg)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)](https://typescriptlang.org)
[![Java 17+](https://img.shields.io/badge/Java-17+-orange.svg)](https://oracle.com/java)

Production-grade **Retrieval-Augmented Generation (RAG)** platform featuring hybrid search (Dense Embeddings + BM25), Reciprocal Rank Fusion (RRF), automated faithfulness evaluation metrics, and streaming LLM API client architecture.

---

## 🏛️ System Architecture

```text
enterprise-rag-ops/
├── configs/                  # YAML configurations (LLM parameters, vector DB thresholds)
├── prompts/                  # Version-controlled prompt templates & Jinja2 schemas
├── src/
│   ├── ingestion/            # Document loaders, token-aware text splitters
│   ├── retrieval/            # Vector DB adapters, dense embeddings, BM25 reranking
│   ├── generation/           # Streaming LLM API client (OpenAI / Anthropic)
│   └── index/                # Java high-performance vector search engine
├── evals/                    # Evaluation harness (faithfulness, hallucination, RAGAS metrics)
├── tests/                    # Unit & integration test suites
└── docs/                     # RAG architecture specs, latency benchmarks
```

---

## ⚡ Core Features

- **Hybrid Vector Search**: Combines dense vector similarity with sparse BM25 keyword matching via Reciprocal Rank Fusion (RRF).
- **Faithfulness & Groundedness Metrics**: Automated hallucination audit harness measuring document context overlap before output dispatch.
- **Streaming Response Client**: Real-time SSE token reader for low-latency user interfaces.
- **High-Performance Java Index**: Sub-10ms vector similarity distance calculations for large document collections.

---

## 🧪 Quickstart & Testing

```bash
# Run evaluation suite
python -m unittest discover evals

# Run retrieval unit tests
python -m unittest discover tests
```

---

## 📄 License
MIT License - Built by **Junior AI Engineer**
