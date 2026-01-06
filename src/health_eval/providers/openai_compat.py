"""OpenAI-compatible API provider."""
from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class OpenAICompatProvider(BaseModel):
    """OpenAI-compatible API provider."""
    api_base: str = "http://localhost:8000/v1"
    api_key: str = "dummy-key"
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1024
    
    def generate(self, prompt: str) -> str:
        """Generate response for prompt."""
        return f"OpenAI-compat response for: {prompt[:50]}"
    
    def batch_generate(self, prompts: List[str]) -> List[str]:
        """Generate responses for multiple prompts."""
        return [self.generate(prompt) for prompt in prompts]
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """Generate chat completion."""
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens
        last_message = messages[-1]["content"] if messages else ""
        return f"Chat response (temp={temp}, max_tokens={tokens}): {last_message[:50]}"


def create_provider(config: Dict[str, Any]) -> OpenAICompatProvider:
    """Create OpenAI-compatible provider instance."""
    return OpenAICompatProvider(
        api_base=config.get("api_base", "http://localhost:8000/v1"),
        api_key=config.get("api_key", "dummy-key"),
        model=config.get("model", "gpt-3.5-turbo"),
        temperature=config.get("temperature", 0.7),
        max_tokens=config.get("max_tokens", 1024)
    )
