from niusy.core.logic import Fact, Rule
from niusy.agents.agent import ReasoningAgent

def main():
    # Defining rules for a complex decision
    rules = [
        # If user is under 18 -> minor
        Rule(premises=['age_under_18'], conclusion_name='is_minor'),
        # If minor AND no_guardian -> restricted
        Rule(premises=['is_minor', 'no_guardian'], conclusion_name='Deny', weight=0.9),
        # If adult -> allowed
        Rule(premises=['is_adult'], conclusion_name='Allow')
    ]

    agent = ReasoningAgent(rules=rules, name="NiuExplain")

    # Scenario: A minor with no guardian
    observation = {
        'age_under_18': 0.95, # High confidence observation
        'no_guardian': 1.0
    }
    
    agent.process_observation(observation)
    
    # Get action and explanation
    result, explanation = agent.act(explain=True)
    
    print("--- Decision ---")
    print(result)
    print("\n--- Reasoning Trace ---")
    print(explanation)

if __name__ == "__main__":
    main()
