# 🔐 Password Strength Analyzer with Custom Wordlist Generator

A Python CLI tool that analyzes password strength and generates a custom wordlist based on user info.

## 📦 Features
- Password strength analysis using `zxcvbn`
- Custom wordlist generation using name, DOB, pet
- Leetspeak variants + number suffixes
- Outputs to `custom_wordlist.txt`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py --password "Hello123" --name "pritesh" --dob "01012000" --pet "shera"
