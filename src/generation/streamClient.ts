/**
 * Streaming Response Handler for LLM Provider API
 * Author: Junior AI Engineer
 */

export interface LLMMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export class StreamingLLMClient {
  private baseUrl: string;
  private apiKey: string;

  constructor(baseUrl: string = 'https://api.openai.com/v1', apiKey: string) {
    this.baseUrl = baseUrl;
    this.apiKey = apiKey;
  }

  public async parseServerSentEvents(responseBody: ReadableStream<Uint8Array>, onToken: (token: string) => void): Promise<void> {
    const reader = responseBody.getReader();
    const decoder = new TextDecoder('utf-8');
    let buffer = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split('\n');
      buffer = lines.pop() || '';

      for (const line of lines) {
        const trimmed = line.trim();
        if (trimmed.startsWith('data: ') && trimmed !== 'data: [DONE]') {
          const jsonStr = trimmed.substring(6);
          try {
            const parsed = JSON.parse(jsonStr);
            const token = parsed.choices?.[0]?.delta?.content || '';
            if (token) onToken(token);
          } catch (e) {
            // Ignore partial chunk parse errors
          }
        }
      }
    }
  }
}

  public countTotalTokens(prompt: string, completion: string): number {
    return Math.ceil((prompt.length + completion.length) / 4.0);
  }

  public countTotalTokens(prompt: string, completion: string): number {
    return Math.ceil((prompt.length + completion.length) / 4.0);
  }
