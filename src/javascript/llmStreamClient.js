/**
 * LLM Streaming API Client & Token Utility
 * Author: AI Engineer Portfolio
 */

class LLMStreamClient {
  constructor(apiBaseUrl, apiKey) {
    this.apiBaseUrl = apiBaseUrl || 'https://api.openai.com/v1';
    this.apiKey = apiKey;
  }

  /**
   * Estimate token count (rough heuristic: ~4 chars per token)
   */
  estimateTokenCount(text) {
    if (!text) return 0;
    return Math.ceil(text.length / 4);
  }

  /**
   * Formats prompt with system instructions
   */
  formatSystemPrompt(systemPrompt, userQuery) {
    return [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: userQuery }
    ];
  }
}

module.exports = { LLMStreamClient };

// Updated at: 2026-08-10T20:18:33.507Z [Pulse 13/24]

  async retryWithBackoff(fn, retries = 3, delay = 1000) {
    try {
      return await fn();
    } catch (err) {
      if (retries <= 0) throw err;
      await new Promise(res => setTimeout(res, delay));
      return this.retryWithBackoff(fn, retries - 1, delay * 2);
    }
  }
