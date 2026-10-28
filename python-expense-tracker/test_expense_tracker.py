"""Unit tests for the expense tracker."""

import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from expense_tracker import (
    ExpenseError,
    load_expenses,
    save_expense,
    summarize_expenses,
    validate_expense,
)


class ExpenseTrackerTests(unittest.TestCase):
    def test_valid_expense_is_normalized(self):
        record = validate_expense("12.5", " Food ", " Lunch ")
        self.assertEqual(record["amount"], "12.50")
        self.assertEqual(record["category"], "Food")
        self.assertEqual(record["description"], "Lunch")
        self.assertIn("date", record)

    def test_invalid_amount_is_rejected(self):
        for amount in ("0", "-1", "not-a-number", "NaN", "Infinity"):
            with self.subTest(amount=amount):
                with self.assertRaises(ExpenseError):
                    validate_expense(amount, "Food", "Lunch")

    def test_empty_text_is_rejected(self):
        with self.assertRaises(ExpenseError):
            validate_expense("10", "   ", "Lunch")
        with self.assertRaises(ExpenseError):
            validate_expense("10", "Food", " ")

    def test_missing_file_means_empty_list(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load_expenses(Path(folder) / "missing.json"), [])

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nested" / "expenses.json"
            record = validate_expense("19.99", "Books", "Notebook")
            save_expense(path, record)
            self.assertEqual(load_expenses(path), [record])

    def test_summary_totals_by_category(self):
        records = [
            {"amount": "10.00", "category": "Food"},
            {"amount": "4.25", "category": "Travel"},
            {"amount": "2.50", "category": "Food"},
        ]
        total, categories = summarize_expenses(records)
        self.assertEqual(total, Decimal("16.75"))
        self.assertEqual(categories["Food"], Decimal("12.50"))
        self.assertEqual(categories["Travel"], Decimal("4.25"))

    def test_invalid_json_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "expenses.json"
            path.write_text("{", encoding="utf-8")
            with self.assertRaises(ExpenseError):
                load_expenses(path)


if __name__ == "__main__":
    unittest.main()
