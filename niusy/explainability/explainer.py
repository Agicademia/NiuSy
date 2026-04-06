from typing import List, Dict, Set
from ..reasoning.engine import ReasoningEngine

class ProofExplainer:
    """Provides human-readable explanations for symbolic decisions."""
    def __init__(self, engine: ReasoningEngine):
        self.engine = engine

    def explain(self, fact_name: str, depth: int = 0) -> List[str]:
        """Explain how a specific fact was derived."""
        explanation = []
        indent = "  " * depth
        
        if fact_name not in self.engine.proofs:
            explanation.append(f"{indent}- {fact_name} was provided as an initial observation.")
            return explanation

        rule, premises = self.engine.proofs[fact_name]
        explanation.append(f"{indent}- Derived '{fact_name}' because of rule: {rule}")
        explanation.append(f"{indent}  Based on premises:")
        
        for premise in premises:
            explanation.extend(self.explain(premise.name, depth + 2))
            
        return explanation

    def get_full_report(self, fact_name: str) -> str:
        """Get a formatted string explanation for a fact."""
        lines = self.explain(fact_name)
        return "\n".join(lines)
