# Spec-Checker
PyPI package for checking specs using users own custom rules

# 📦 spec-checker

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spec-checker)
![PyPI](https://img.shields.io/pypi/v/spec-checker)
![License](https://img.shields.io/github/license/Yuvi369/Spec-Checker)
![Issues](https://img.shields.io/github/issues/Yuvi369/Spec-Checker)

> **A Universal Spec Validator** for validating laptops, mobiles, and other electronics from CSV/JSON using CLI or Web UI (Streamlit).

## 🚀 Features

- ✅ Validate structured specs using pre-defined or custom rules  
- ✅ Supports both **CSV** and **JSON** formats  
- ✅ Built-in **Streamlit Web UI** for easy visual validation  
- ✅ Easy to install via `pip`  
- ✅ Extendable to any product type: laptop, mobile, monitor, etc.

## 🖥️ Installation

```bash
pip install spec-checker

🔧 Usage
CLI
bashspec-checker path/to/data.csv --type laptop
Optional flags:
--config    Custom rules JSON path
--report    Output HTML report

Examples:
bash# Validate laptops and generate HTML report
spec-checker data/laptops.csv --type laptop --report out.html

# Launch web interface
spec-checker --web
🧪 Supported Products

💻 Laptops
📱 Mobiles
🖥️ Monitors

🛠️ Developer Setup
bashgit clone https://github.com/yuvaraj-dev/spec-checker
cd spec-checker
pip install -e .

📁 Project Structure

spec_checker/
├── __init__.py
├── cli.py
├── validator.py
├── rules/
└── web.py

🤝 Contributing
PRs are welcome! Please open an issue first for major changes.
💬 Feedback & Suggestions
We'd love to hear from you! Help us improve spec-checker by sharing your suggestions, reporting bugs, or proposing new features.
📬 Submit your feedback here:
👉 https://forms.cloud.microsoft/r/LucPyefjm8
The form is quick to fill out — just a few questions to help us make this tool better for developers like you.

📄 License
This project is licensed under the MIT License.

Authored by Yuvaraj S S
LinkedIn - https://www.linkedin.com/in/yuvaraj24/
Github - https://github.com/Yuvi369
