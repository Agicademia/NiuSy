from typing import List
from ...core.logic import Rule

def get_agi_alignment_rules() -> List[Rule]:
    """Provides a foundational set of AGI alignment and safety rules."""
    return [
        # 🛡️ Fundamental Alignment: Action must be safe and help the user
        Rule(premises=['helps_user', 'is_safe'], conclusion_name='GoodAction', weight=1.0),
        
        # 🏁 Goal Pursuit: Action should advance the current goal
        Rule(premises=['advances_goal', 'is_safe'], conclusion_name='ExecuteAction', weight=0.9),
        
        # ⚠️ Safety Override: If unsafe, then NoAction
        Rule(premises=['is_unsafe'], conclusion_name='NoAction', weight=1.0),
        
        # 🔗 Constraint: If Deny, then NoAction
        Rule(premises=['Deny'], conclusion_name='NoAction', weight=1.0)
    ]

def get_autonomous_behavior_rules() -> List[Rule]:
    """Rules for exploration and learning behavior in AGI agents."""
    return [
        # Curiosity: If (NewEnvironment) AND (NoSafetyViolation) -> Explore
        Rule(premises=['new_environment', 'is_safe'], conclusion_name='Explore', weight=0.7),
        
        # Optimization: If (HasAction) AND (ActionReliability < 0.5) -> Retrain
        Rule(premises=['has_action', 'low_reliability'], conclusion_name='OptimizeModel', weight=0.8)
    ]
