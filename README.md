# NiuSy: A Generic Probabilistic Neuro-Symbolic AI Library

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![Org: Agicademia](https://img.shields.io/badge/Org-Agicademia-red)](https://github.com/Agicademia)

**NiuSy** (Neuro-v-Symbolic) is a high-performance, Pythonic library for bridging neural perception and symbolic reasoning.
 It allows developers to build AI agents that combine the robust learning of Deep Learning with the transparency and formal reasoning of Symbolic Logic.

---

## Key Features

- **Probabilistic Logic Engine**: Handles uncertainty by assigning confidence scores to facts and rules.
- **Bi-Directional Reasoning**: Supports both Forward Chaining (data-driven) and Backward Chaining (goal-driven) for agentic decision making.
- **Explainable AI (XAI)**: Generates human-readable "Proof Traces" for every decision.
- **Neural Bridge**: Interfaces with LLMs to extract symbolic predicates from natural language.
- **Zero-Code Config**: Load entire symbolic rule sets from external JSON/YAML configuration files.
- **Domain Modules**: Built-in modules for **Responsible AI (RAI)** audits and **AGI Behavior** alignment.

---

## Quickstart

### 1. Installation
```bash
git clone https://github.com/Agicademia/NiuSy.git
cd NiuSy
pip install -r requirements.txt
```

### 2. A Simple Reasoning Agent
```python
from niusy.agents.agent import ReasoningAgent
from niusy.core.logic import Rule

# Define rules
rules = [
    Rule(premises=['has_fever', 'has_cough'], conclusion_name='is_sick', weight=0.8)
]

# Initialize agent
agent = ReasoningAgent(rules=rules)
agent.process_observation({'has_fever': 0.9, 'has_cough': 1.0})

# Get decision and explanation
result, explanation = agent.act(explain=True)
print(result)
```

---

## 📁 Project Structure
- `niusy/core`: Symbolic primitives (Facts, Rules, Constraints).
- `niusy/reasoning`: Inference engines (Forward/Backward chaining).
- `niusy/neural`: Neural bridges (Concept extractors, LLM wrappers).
- `niusy/audit`: Tools for Responsible AI and fairness auditing.
- `niusy/domains`: Domain-specific rule modules (AGI, Legal, etc.).

---

## License
NiuSy is licensed under the Apache License 2.0. See the `LICENSE` file for more details.

## Contributing
We welcome contributions! Please see `CONTRIBUTING.md` for guidelines.
