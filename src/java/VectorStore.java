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
