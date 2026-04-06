from niusy.agents.agent import ReasoningAgent
from niusy.core.logic import Rule
from niusy.neural.bridge import ConceptExtractor

def main():
    # 📚 1. Knowledge Engineer: Define Rules for a "Safe Content" Agent
    rules = [
        # Explicit content leads to a safety violation
        Rule(premises=['contains_violence'], conclusion_name='SafetyViolation'),
        Rule(premises=['contains_hate_speech'], conclusion_name='SafetyViolation'),
        # Safety Violation leads to a 'Deny'
        Rule(premises=['SafetyViolation'], conclusion_name='Deny', weight=1.0)
    ]

    # 🤝 2. Neural Bridge: Setup the Concept Extractor
    # In a real app, you'd pass a litellm/openai client here.
    bridge = ConceptExtractor()
    
    # 🤖 3. The NeSy Agent: Combine Neural Perception and Symbolic Reasoning
    agent = ReasoningAgent(rules=rules, name="NiuSafe")

    # --- SIMULATING A TASK ---
    raw_user_input = "The warrior swung his sword and caused blood to spill everywhere."
    print(f"User Input: \"{raw_user_input}\"")

    # Neural Stage: Process the text to extract concepts
    # We ask the LLM specifically for the symbols we care about
    neural_observations = bridge.extract(raw_user_input, ['contains_violence', 'contains_hate_speech'])
    print(f"Perceived Confidence: {neural_observations}")

    # Symbolic Stage: Update beliefs and make a goal-driven decision
    agent.process_observation(neural_observations)
    
    # GOAL: Prove if we should 'Deny' (Backward Chaining)
    result, explanation = agent.act(goal='Deny', explain=True)

    print("\n[Decision Engine Result]")
    print(result)

    print("\n[The Explainable Proof]")
    print(explanation)

if __name__ == "__main__":
    main()
