"""A small JSON-backed command-line expense tracker."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any


class ExpenseError(ValueError):
    """Raised when expense data is invalid."""


def validate_expense(amount: str, category: str, description: str) -> dict[str, str]:
    """Validate expense fields and return a normalized record."""
    try:
        value = Decimal(amount)
    except (InvalidOperation, TypeError) as exc:
        raise ExpenseError("Amount must be a valid number.") from exc

    if not value.is_finite() or value <= 0:
        raise ExpenseError("Amount must be greater than zero.")
    if not category.strip():
        raise ExpenseError("Category cannot be empty.")
    if not description.strip():
        raise ExpenseError("Description cannot be empty.")

    return {
        "amount": format(value.quantize(Decimal("0.01")), "f"),
        "category": category.strip(),
        "description": description.strip(),
        "date": date.today().isoformat(),
    }


def load_expenses(path: Path) -> list[dict[str, Any]]:
    """Read expenses; a missing file means no records yet."""
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ExpenseError(f"Data file is not valid JSON: {path}") from exc
    if not isinstance(data, list):
        raise ExpenseError("Data file must contain a JSON list.")
    return data


def save_expense(path: Path, record: dict[str, str]) -> None:
    """Append one record and write the full JSON document."""
    records = load_expenses(path)
    records.append(record)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")


def format_amount(amount: str) -> str:
    return f"{Decimal(amount):.2f}"


def summarize_expenses(records: list[dict[str, Any]]) -> tuple[Decimal, dict[str, Decimal]]:
    total = Decimal("0.00")
    category_totals: dict[str, Decimal] = defaultdict(lambda: Decimal("0.00"))
    for record in records:
        amount = Decimal(str(record["amount"]))
        total += amount
        category_totals[str(record["category"])] += amount
    return total, dict(sorted(category_totals.items(), key=lambda item: item[0].lower()))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track expenses in a local JSON file.")
    parser.add_argument(
        "--data-file",
        default="expenses.json",
        help="Path to the JSON data file (default: expenses.json)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Record a new expense.")
    add_parser.add_argument("--amount", required=True, help="Positive amount, e.g. 125.50")
    add_parser.add_argument("--category", required=True, help="Category, e.g. Food")
    add_parser.add_argument("--description", required=True, help="What the expense was for")

    subparsers.add_parser("list", help="List saved expenses.")
    subparsers.add_parser("summary", help="Summarize total and category spending.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    path = Path(args.data_file)

    try:
        if args.command == "add":
            record = validate_expense(args.amount, args.category, args.description)
            save_expense(path, record)
            print("Expense saved.")
        elif args.command == "list":
            records = load_expenses(path)
            if not records:
                print("No expenses recorded yet.")
            for index, item in enumerate(records, start=1):
                print(
                    f"{index}. {item['date']} | {item['category']} | "
                    f"{format_amount(str(item['amount']))} | {item['description']}"
                )
        elif args.command == "summary":
            total, categories = summarize_expenses(load_expenses(path))
            print(f"Total spent: {format_amount(str(total))}")
            if not categories:
                print("No expenses recorded yet.")
            for category, amount in categories.items():
                print(f"{category}: {format_amount(str(amount))}")
    except (ExpenseError, OSError, KeyError, InvalidOperation) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
