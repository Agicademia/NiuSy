import json
from typing import List
from ..core.logic import Rule

class RuleLoader:
    """Handles loading and saving of NiuSy rule sets."""
    
    @staticmethod
    def from_json(file_path: str) -> List[Rule]:
        """Load a set of rules from a JSON file."""
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        rules = []
        for item in data:
            rules.append(Rule(
                premises=item['premises'],
                conclusion_name=item['conclusion'],
                weight=item.get('weight', 1.0)
            ))
        return rules

    @staticmethod
    def to_json(rules: List[Rule], file_path: str):
        """Save a set of rules to a JSON file."""
        serializable = []
        for rule in rules:
            serializable.append({
                'premises': list(rule.premises),
                'conclusion': rule.conclusion_name,
                'weight': rule.weight
            })
        
        with open(file_path, 'w') as f:
            json.dump(serializable, f, indent=4)
