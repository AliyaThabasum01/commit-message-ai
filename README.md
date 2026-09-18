# 🤖 Commit Message Generator

A lightweight Python CLI tool that generates Conventional Commit messages from a simple description of your changes.

## Features

- Detects common commit types
- Generates Conventional Commit format
- Supports features, fixes, docs, tests and styles
- No external dependencies

## Run

```bash
python main.py
```

## Example

```text
🤖 Commit Message Generator
========================================

What did you change? added login page

✨ Suggested commit:
feat: added login page
```

Another example:

```text
What did you change? fixed navbar bug

✨ Suggested commit:
fix: fixed navbar bug
```

## Built With

- Python
- String processing
