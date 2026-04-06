from typing import Any, List, Set, Protocol, Union, Dict

class Fact:
    """A single piece of knowledge in the NiuSy ecosystem with a confidence score."""
    def __init__(self, name: str, value: Any = True, score: float = 1.0):
        self.name = name
        self.value = value
        self.score = score

    def __repr__(self):
        return f"Fact({self.name}={self.value}, score={self.score:.2f})"

    def __eq__(self, other):
        if not isinstance(other, Fact):
            return False
        return self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash((self.name, self.value))

class Rule:
    """A symbolic constraint or implication with an associated weight."""
    def __init__(self, premises: List[str], conclusion_name: str, weight: float = 1.0):
        self.premises = set(premises)
        self.conclusion_name = conclusion_name
        self.weight = weight

    def __repr__(self):
        return f"Rule({' & '.join(self.premises)} -> {self.conclusion_name} [w={self.weight}])"

    def evaluate(self, facts: Set[Fact]) -> Union[Fact, None]:
        """Checks if the rule is satisfied and returns the conclusion with a calculated score."""
        relevant_facts = {f.name: f.score for f in facts if f.value}
        
        if self.premises.issubset(relevant_facts.keys()):
            # Fuzzy Logic: P(Conclusion) = min(P(Premises)) * Rule_Weight
            min_premise_score = min(relevant_facts[p] for p in self.premises)
            return Fact(self.conclusion_name, True, score=min_premise_score * self.weight)
        
        return None

