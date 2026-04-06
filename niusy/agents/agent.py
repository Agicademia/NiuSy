from typing import Set, List, Dict, Union, Tuple, Optional
from ..core.logic import Fact, Rule
from ..reasoning.engine import ReasoningEngine
from ..explainability.explainer import ProofExplainer
from ..io.loader import RuleLoader

class ReasoningAgent:
    """A symbolic agent that uses probabilistic logic with support for external config files."""
    def __init__(self, rules: List[Rule], name: str = 'NiuAgent'):
        self.name = name
        self.engine = ReasoningEngine(rules)
        self.explainer = ProofExplainer(self.engine)
        self.beliefs: Set[Fact] = set()

    @staticmethod
    def from_config(config_path: str, name: str = 'NiuConfigAgent') -> 'ReasoningAgent':
        """Create an agent directly from a JSON rules configuration file."""
        rules = RuleLoader.from_json(config_path)
        return ReasoningAgent(rules=rules, name=name)

    def process_observation(self, observation: Dict[str, Union[bool, float]]):
        """Convert a neural/dict observation into probabilistic facts."""
        self.beliefs = set()
        for name, value in observation.items():
            if isinstance(value, (float, int)):
                self.beliefs.add(Fact(name, True, score=float(value)))
            elif isinstance(value, bool) and value is True:
                self.beliefs.add(Fact(name, True, score=1.0))

    def act(self, goal: Optional[str] = None, explain: bool = False) -> Union[str, Tuple[str, str]]:
        """The agent's decision based on its rules, using either Forward or Backward Chaining."""
        
        if goal:
            # Backward Chaining: Try to specifically prove one thing
            result_fact = self.engine.prove(goal, self.beliefs)
            inferred_facts = {result_fact.name: result_fact.score} if result_fact else {}
            action_key = goal if result_fact else None
        else:
            # Forward Chaining: Find everything possible
            all_inferred = self.engine.infer(self.beliefs)
            inferred_facts = {f.name: f.score for f in all_inferred if f.value}
            # Pick a default action based on priority
            action_key = 'Deny' if 'Deny' in inferred_facts else ('Allow' if 'Allow' in inferred_facts else None)

        action_result = f"[{self.name}] No specific action found."
        
        if action_key and action_key in inferred_facts:
            score = inferred_facts[action_key]
            status = "Denied" if action_key == 'Deny' else ("Granted" if action_key == 'Allow' else action_key)
            action_result = f"[{self.name}] {status} (Confidence: {score:.2f})."

        if explain and action_key:
            explanation = self.explainer.get_full_report(action_key)
            return action_result, explanation
        
        return action_result


    def __repr__(self):
        return f"ReasoningAgent(name={self.name}, rules_count={len(self.engine.rules)})"




