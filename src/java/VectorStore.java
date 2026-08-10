package com.ai.vectorstore;

import java.util.ArrayList;
import java.util.List;

/**
 * High-performance Java Vector Store Interface
 * Author: AI Engineer Portfolio
 */
public class VectorStore {
    private final List<VectorEntry> store = new ArrayList<>();

    public static class VectorEntry {
        public String id;
        public float[] embedding;

        public VectorEntry(String id, float[] embedding) {
            this.id = id;
            this.embedding = embedding;
        }
    }

    public void addVector(String id, float[] embedding) {
        store.add(new VectorEntry(id, embedding));
    }

    public static float calculateDotProduct(float[] a, float[] b) {
        if (a.length != b.length) return 0.0f;
        float sum = 0.0f;
        for (int i = 0; i < a.length; i++) {
            sum += a[i] * b[i];
        }
        return sum;
    }

    public int getStoreSize() {
        return store.size();
    }
}

// Updated at: 2026-08-10T20:18:33.497Z [Pulse 12/24]

    public static float cosineSimilarity(float[] a, float[] b) {
        float dot = calculateDotProduct(a, b);
        float normA = 0.0f, normB = 0.0f;
        for (int i = 0; i < a.length; i++) {
            normA += a[i] * a[i];
            normB += b[i] * b[i];
        }
        return (normA == 0 || normB == 0) ? 0.0f : (float)(dot / (Math.sqrt(normA) * Math.sqrt(normB)));
    }

// Updated at: 2026-08-10T20:18:33.527Z [Pulse 15/24]

    public static float cosineSimilarity(float[] a, float[] b) {
        float dot = calculateDotProduct(a, b);
        float normA = 0.0f, normB = 0.0f;
        for (int i = 0; i < a.length; i++) {
            normA += a[i] * a[i];
            normB += b[i] * b[i];
        }
        return (normA == 0 || normB == 0) ? 0.0f : (float)(dot / (Math.sqrt(normA) * Math.sqrt(normB)));
    }

// Updated at: 2026-08-10T20:18:33.537Z [Pulse 16/24]

    public static float cosineSimilarity(float[] a, float[] b) {
        float dot = calculateDotProduct(a, b);
        float normA = 0.0f, normB = 0.0f;
        for (int i = 0; i < a.length; i++) {
            normA += a[i] * a[i];
            normB += b[i] * b[i];
        }
        return (normA == 0 || normB == 0) ? 0.0f : (float)(dot / (Math.sqrt(normA) * Math.sqrt(normB)));
    }

// Updated at: 2026-08-10T20:18:33.547Z [Pulse 17/24]

    public static float cosineSimilarity(float[] a, float[] b) {
        float dot = calculateDotProduct(a, b);
        float normA = 0.0f, normB = 0.0f;
        for (int i = 0; i < a.length; i++) {
            normA += a[i] * a[i];
            normB += b[i] * b[i];
        }
        return (normA == 0 || normB == 0) ? 0.0f : (float)(dot / (Math.sqrt(normA) * Math.sqrt(normB)));
    }

// Updated at: 2026-08-10T20:18:33.581Z [Pulse 20/24]

    public static float cosineSimilarity(float[] a, float[] b) {
        float dot = calculateDotProduct(a, b);
        float normA = 0.0f, normB = 0.0f;
        for (int i = 0; i < a.length; i++) {
            normA += a[i] * a[i];
            normB += b[i] * b[i];
        }
        return (normA == 0 || normB == 0) ? 0.0f : (float)(dot / (Math.sqrt(normA) * Math.sqrt(normB)));
    }
