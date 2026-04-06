from niusy.core.logic import Fact, Rule
from niusy.agents.agent import ReasoningAgent

def main():
    # Defining the 'Symbolic Domain' (A simple security guard agent)
    rules = [
        # Rule 1: If (Action is 'Restricted') AND (User is NOT 'Admin') -> Deny
        Rule(premises=['is_restricted_action', 'is_not_admin'], conclusion_name='Deny'),
        # Rule 2: If (Action is NOT 'Restricted') -> Allow
        Rule(premises=['is_not_restricted_action'], conclusion_name='Allow'),
        # Rule 3: If (User IS 'Admin') -> Allow
        Rule(premises=['is_admin'], conclusion_name='Allow')
    ]

    agent = ReasoningAgent(rules=rules, name="NiuGuard")
    print(f"--- {agent.name} Initialized ---")

    # Scenario A: Restricted action by a non-admin (Triggered by a neural perception)
    # Scenario: LLM said 'The user wants to access the root folder and doesn't have an admin badge.'
    observation_A = {'is_restricted_action': True, 'is_not_admin': True, 'is_admin': False}
    agent.process_observation(observation_A)
    print(f"\nScenario A (Restricted Action, No Admin Role): {agent.act()}")

    # Scenario B: Non-restricted action by same user
    observation_B = {'is_not_restricted_action': True, 'is_not_admin': True}
    agent.process_observation(observation_B)
    print(f"Scenario B (Generic Action, No Admin Role): {agent.act()}")

    # Scenario C: Restricted action by an admin
    observation_C = {'is_restricted_action': True, 'is_admin': True}
    agent.process_observation(observation_C)
    print(f"Scenario C (Restricted Action, Admin Role): {agent.act()}")

if __name__ == "__main__":
    main()

