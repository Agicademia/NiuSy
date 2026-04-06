from typing import Set, List, Dict, Optional, Tuple, Union
from ..core.logic import Fact, Rule

class ReasoningEngine:
    """The processes facts through symbolic rules with probabilistic merging, proof tracking, and bi-directional search."""
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.proofs: Dict[str, Tuple[Rule, Set[Fact]]] = {} 

    def infer(self, initial_facts: Set[Fact]) -> Set[Fact]:
        """Forward chaining engine that maintains confidence and proof paths."""
        fact_registry: Dict[str, Fact] = {f.name: f for f in initial_facts}
        self.proofs = {} 
        
        added_new = True
        while added_new:
            added_new = False
            for rule in self.rules:
                premises_in_registry = {f for f in fact_registry.values() if f.name in rule.premises}
                conclusion = rule.evaluate(premises_in_registry)
                
                if conclusion:
                    current = fact_registry.get(conclusion.name)
                    if not current or conclusion.score > current.score:
                        fact_registry[conclusion.name] = conclusion
                        self.proofs[conclusion.name] = (rule, premises_in_registry)
                        added_new = True
                        
        return set(fact_registry.values())

    def prove(self, goal_name: str, initial_facts: Set[Fact]) -> Optional[Fact]:
        """Backward chaining engine: Tries to prove a specific goal."""
        # 1. Check if the goal is already in initial facts
        fact_registry = {f.name: f for f in initial_facts}
        if goal_name in fact_registry:
            return fact_registry[goal_name]

        # 2. Find rules that conclude the goal
        relevant_rules = [r for r in self.rules if r.conclusion_name == goal_name]
        
        best_fact = None
        for rule in relevant_rules:
            # 3. Recursively try to prove all premises of the rule
            premise_facts = set()
            possible = True
            for premise in rule.premises:
                p_fact = self.prove(premise, initial_facts)
                if p_fact:
                    premise_facts.add(p_fact)
                else:
                    possible = False
                    break
            
            if possible:
                # 4. Evaluate the rule with proven premises
                conclusion = rule.evaluate(premise_facts)
                if conclusion:
                    if not best_fact or conclusion.score > best_fact.score:
                        best_fact = conclusion
                        self.proofs[goal_name] = (rule, premise_facts)
        
        return best_fact



