"""Stub provider for testing."""
from typing import List, Dict, Any
from pydantic import BaseModel


class StubProvider(BaseModel):
    """Stub LLM provider for testing."""
    model: str = "stub-model"
    responses: List[str] = []
    
    def generate(self, prompt: str) -> str:
        """Generate response for prompt."""
        if self.responses:
            return self.responses.pop(0)
        return f"stub response for: {prompt[:50]}"
    
    def batch_generate(self, prompts: List[str]) -> List[str]:
        """Generate responses for multiple prompts."""
        return [self.generate(prompt) for prompt in prompts]


def create_provider(config: Dict[str, Any]) -> StubProvider:
    """Create stub provider instance."""
    return StubProvider(
        model=config.get("model", "stub-model"),
        responses=config.get("responses", [])
    )
