import os
from niusy.agents.agent import ReasoningAgent

def main():
    # Path to the JSON configuration
    config_path = os.path.join('examples', 'medical_rules.json')
    
    # Initialize Agent directly from JSON
    agent = ReasoningAgent.from_config(config_path, name="NiuMedical")
    print(f"--- {agent.name} Initialized from {config_path} ---")

    # Scenario: High risk patient with symptoms
    observation = {
        'has_fever': 0.9,
        'has_cough': 1.0,
        'high_risk_patient': 1.0
    }
    
    agent.process_observation(observation)
    
    # Reasoning
    result, explanation = agent.act(explain=True)
    
    print("\n[Decision]")
    print(result)
    
    print("\n[Reasoning Trace]")
    print(explanation)

if __name__ == "__main__":
    main()
