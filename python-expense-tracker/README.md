# Python Expense Tracker

A command-line expense tracker built with Python's standard library. It stores transactions in a local JSON file, lists saved expenses, and summarizes spending by category.

## Features

- Add an expense with amount, category, and description.
- List saved transactions.
- Summarize total spending and per-category spending.
- Store amounts as decimal strings to avoid JSON floating-point rounding issues.
- Validate positive amounts and required text.
- Test core behavior with Python's built-in unittest framework.

## Requirements

- Python 3.11+
- No third-party dependencies

## Usage

Run from the repository root:

\`\`\`bash
python python-expense-tracker/expense_tracker.py add --amount 249.50 --category Food --description "Lunch"
python python-expense-tracker/expense_tracker.py list
python python-expense-tracker/expense_tracker.py summary
\`\`\`

The program writes to expenses.json in the current working directory. Pass --data-file path/to/file.json to use a different file.

## Tests

\`\`\`bash
python -m unittest discover -s python-expense-tracker -p "test_*.py" -v
\`\`\`

## Limitations

This is a learning tool. It does not provide accounts, encryption, bank integration, or concurrent-write protection. Keep backups of the JSON file if the records matter.
