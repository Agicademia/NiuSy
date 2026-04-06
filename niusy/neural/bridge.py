import json
from typing import List, Dict, Any, Union

class ConceptExtractor:
    """Bridges Natural Language text to Symbolic Facts using an LLM."""
    def __init__(self, model_interface: Any = None):
        self.model = model_interface

    def get_prompt(self, text: str, target_concepts: List[str]) -> str:
        """Generate a prompt for the LLM to extract concept probabilities."""
        concepts_str = ", ".join(target_concepts)
        return (
            f"Analyze the following text and determine the probability (0.0 to 1.0) "
            f"for each of these concepts: {concepts_str}.\n"
            f"Return ONLY a JSON object like: {{'concept_name': probability}}\n\n"
            f"Text: \"{text}\""
        )

    def extract(self, text: str, target_concepts: List[str]) -> Dict[str, float]:
        """Extract probabilities for concepts from text (Mocked for demonstration)."""
        if not self.model:
            mock_results = {}
            text_lower = text.lower()
            for concept in target_concepts:
                # Better keyword extraction for the demo
                keywords = ['violence', 'blood', 'sword', 'attack'] if 'violence' in concept else \
                           (['hate', 'toxic', 'insult'] if 'hate' in concept else [])
                
                if any(k in text_lower for k in keywords):
                    mock_results[concept] = 0.85
                else:
                    mock_results[concept] = 0.05
            return mock_results
        return {}

