# Python Learning Lab & Portfolio

A practical repository for Python fundamentals, problem-solving, and SQL interview preparation. It keeps earlier Python assignments while adding small projects that can be run, tested, explained, and improved.

## Projects

### Python Expense Tracker
A command-line app that records expenses in a local JSON file, lists transactions, and summarizes spending by category. Uses Python's standard library and includes unit tests.

Concepts: functions, input validation, modules, JSON persistence, command-line arguments, Decimal arithmetic, and testing.

### SQL Interview Lab
A PostgreSQL practice schema with six related tables, synthetic data, and 30 interview-style challenges covering filtering, joins, aggregation, and subqueries.

## Quick start

Python 3.11+ recommended.

\`\`\`bash
python python-expense-tracker/expense_tracker.py --help
python -m unittest discover -s python-expense-tracker -p "test_*.py" -v
\`\`\`

Run sql-interview-lab/schema.sql followed by sql-interview-lab/seed.sql in PostgreSQL.

## Engineering principles

- Prefer small, testable increments over unsupported claims.
- Validate inputs and handle errors clearly.
- Document setup, trade-offs, and limitations.
- Improve the projects incrementally as skills grow.

## Status

These are learning projects, not production systems. The expense tracker stores data locally and does not include authentication, encryption, or concurrent-write protection. The SQL lab uses synthetic sample data.

Built as part of my journey toward backend, cloud, and DevOps engineering.
