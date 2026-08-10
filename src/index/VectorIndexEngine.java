package com.company.ai.index;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

/**
 * High-Performance Vector Similarity Index
 * Author: Junior AI Engineer
 */
public class VectorIndexEngine {
    private final List<DocumentVector> index = new ArrayList<>();

    public static class DocumentVector {
        public final String id;
        public final float[] vector;

        public DocumentVector(String id, float[] vector) {
            this.id = id;
            this.vector = vector;
        }
    }

    public static class SearchResult {
        public final String id;
        public final float score;

        public SearchResult(String id, float score) {
            this.id = id;
            this.score = score;
        }
    }

    public synchronized void addVector(String id, float[] vector) {
        index.add(new DocumentVector(id, vector));
    }

    public List<SearchResult> searchTopK(float[] queryVector, int topK) {
        PriorityQueue<SearchResult> pq = new PriorityQueue<>(Comparator.comparingDouble(a -> a.score));

        for (DocumentVector doc : index) {
            float similarity = cosineSimilarity(queryVector, doc.vector);
            if (pq.size() < topK) {
                pq.add(new SearchResult(doc.id, similarity));
            } else if (pq.peek() != null && similarity > pq.peek().score) {
                pq.poll();
                pq.add(new SearchResult(doc.id, similarity));
            }
        }

        List<SearchResult> results = new ArrayList<>(pq);
        results.sort((a, b) -> Float.compare(b.score, a.score));
        return results;
    }

    public static float cosineSimilarity(float[] a, float[] b) {
        if (a.length != b.length) return 0.0f;
        float dot = 0.0f, normA = 0.0f, normB = 0.0f;
        for (int i = 0; i < a.length; i++) {
            dot += a[i] * b[i];
            normA += a[i] * a[i];
            normB += b[i] * b[i];
        }
        return (normA == 0 || normB == 0) ? 0.0f : (float) (dot / (Math.sqrt(normA) * Math.sqrt(normB)));
    }
}

    public synchronized void addBatchVectors(List<DocumentVector> docs) {
        this.index.addAll(docs);
    }

    public synchronized void addBatchVectors(List<DocumentVector> docs) {
        this.index.addAll(docs);
    }

    public synchronized void addBatchVectors(List<DocumentVector> docs) {
        this.index.addAll(docs);
    }
