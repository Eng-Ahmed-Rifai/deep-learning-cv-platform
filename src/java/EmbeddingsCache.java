
// Updated at: 2026-08-10T20:18:33.652Z [Pulse 24/24]
package com.ai.vectorstore;
import java.util.LinkedHashMap;
import java.util.Map;

public class EmbeddingsCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    public EmbeddingsCache(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }
}

// Updated at: 2026-08-10T20:19:03.600Z [Pulse 2/21]
package com.ai.vectorstore;
import java.util.LinkedHashMap;
import java.util.Map;

public class EmbeddingsCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    public EmbeddingsCache(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }
}

// Updated at: 2026-08-10T20:19:03.803Z [Pulse 11/21]
package com.ai.vectorstore;
import java.util.LinkedHashMap;
import java.util.Map;

public class EmbeddingsCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    public EmbeddingsCache(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }
}

// Updated at: 2026-08-10T20:19:03.883Z [Pulse 20/21]
package com.ai.vectorstore;
import java.util.LinkedHashMap;
import java.util.Map;

public class EmbeddingsCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    public EmbeddingsCache(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }
}
