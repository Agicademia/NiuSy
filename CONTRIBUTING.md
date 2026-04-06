# Contributing to NiuSy

We are thrilled that you want to contribute to **NiuSy**! We want to make it as easy and transparent as possible to contribute to the future of Neuro-Symbolic AI.

## 🚀 How to Contribute

### 1. Feature Requests & Bug Reports
Please open an issue for any feature request or bug report. Provide as much detail as possible, including code snippets and expectations.

### 2. Pull Requests (PRs)
1. Fork the repository and create your feature branch.
2. Ensure your code follows the established coding style (no emojis in source code).
3. Ensure $NiuSy$ passes all existing tests.
4. Add tests for your new features.
5. Provide a clear description in your PR of what you've added or fixed.

## ⚖️ Code of Conduct
We expect all contributors to adhere to a high professional standard. 
- Be respectful and inclusive.
- Keep the library's "Agicademia" philosophy in mind (General AGI + Safe AI).
- **Pro Tip**: Keep the codebase clean and avoid AI-tell-tale signs (like inappropriate emojis).

## 🧩 Modularity First
NiuSy is designed to be an "umbrella" framework. If you are adding a domain-specific rule set (e.g., Medical, Finance), please place it under `niusy/domains/`.

---

## 🛠️ Developer Setup
```bash
git clone https://github.com/Agicademia/NiuSy.git
cd NiuSy
pip install -e .
pytest tests/
```
