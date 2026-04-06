from typing import List, Dict, Any
from ..core.logic import Fact, Rule
from ..reasoning.engine import ReasoningEngine

class FairnessAuditor:
    """A symbolic auditor that checks for bias using probabilistic logic rules."""
    def __init__(self):
        # Default Fairness Rules with Weights
        self.rules = [
            # Disparate Impact has high weight
            Rule(premises=['is_protected_group', 'is_rejected', 'has_high_score'], 
                 conclusion_name='PotentialBias', 
                 weight=1.0),
            # Inconsistent decision has moderate weight
            Rule(premises=['has_high_score', 'is_rejected'], 
                 conclusion_name='InconsistentDecision', 
                 weight=0.8)
        ]
        self.engine = ReasoningEngine(self.rules)

    def audit_record(self, record_data: Dict[str, Any]) -> Dict[str, float]:
        """Audit a record and return a dictionary of alerts and their confidence scores."""
        # Convert dictionary to Facts (supporting both flags and probabilities)
        facts = set()
        for k, v in record_data.items():
            if isinstance(v, (float, int)):
                facts.add(Fact(k, True, score=float(v)))
            elif isinstance(v, bool) and v is True:
                facts.add(Fact(k, True, score=1.0))

        inferred = self.engine.infer(facts)
        
        # Extract specific alerts and their scores
        results = {f.name: f.score for f in inferred 
                   if f.name in ['PotentialBias', 'InconsistentDecision']}
        return results

    def __repr__(self):
        return f"FairnessAuditor(rules_count={len(self.rules)})"

