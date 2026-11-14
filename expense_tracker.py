"""Institute Expense Tracker
Records daily operational expenses in expenses.csv (date,item,category,amount).
"""

import csv
from datetime import date, datetime

FILENAME = "expenses.csv"
FIELDS = ["date", "item", "category", "amount"]


def load_expenses():
    """Load saved expenses. If the file does not exist, start with an empty list."""
    expenses = []
    try:
        with open(FILENAME, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    row["amount"] = float(row["amount"])
                except (ValueError, TypeError, KeyError):
                    print(f"Skipping damaged row: {row}")
                    continue
                expenses.append(row)
        print(f"Loaded {len(expenses)} expense(s) from {FILENAME}.")
    except FileNotFoundError:
        print(f"{FILENAME} not found. Starting with an empty expense list.")
    return expenses


def save_expenses(expenses):
    """Write all expenses to the CSV file (header + rows)."""
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


def ask_date():
    """Ask for a date (YYYY-MM-DD). Press Enter to use today's date."""
    while True:
        text = input("Date (YYYY-MM-DD, Enter for today): ").strip()
        if text == "":
            return date.today().isoformat()
        try:
            return datetime.strptime(text, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("Invalid date. Use the format YYYY-MM-DD (e.g. 2026-11-14).")


def ask_text(prompt):
    """Ask for a non-empty text value."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty.")


def ask_amount():
    """Keep asking until the user enters a valid, non-negative number."""
    while True:
        text = input("Amount: ").strip()
        try:
            amount = float(text)
        except ValueError:
            print("Invalid amount. Please enter a number (e.g. 1500 or 99.5).")
            continue
        if amount < 0:
            print("Amount cannot be negative.")
            continue
        return amount


def add_expense(expenses):
    expense_date = ask_date()
    item = ask_text("Item name: ")
    category = ask_text("Category (e.g. Stationery, Internet, Refreshments, Transport): ").title()
    amount = ask_amount()
    expenses.append({
        "date": expense_date,
        "item": item,
        "category": category,
        "amount": amount,
    })
    save_expenses(expenses)  # saved immediately so it survives restarts
    print("Expense saved.")


def show_all(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"\n{'Date':<12}{'Item':<22}{'Category':<16}{'Amount':>10}")
    print("-" * 60)
    for e in expenses:
        print(f"{e['date']:<12}{e['item']:<22}{e['category']:<16}{e['amount']:>10.2f}")
    unique_categories = {e["category"] for e in expenses}  # set of unique categories
    print("\nUnique categories:", ", ".join(sorted(unique_categories)))


def total_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    categories = {e["category"] for e in expenses}  # set of unique categories
    print("\nTotal expenses by category:")
    grand_total = 0
    for cat in sorted(categories):
        total = sum(e["amount"] for e in expenses if e["category"] == cat)
        grand_total += total
        print(f"  {cat:<16}{total:>10.2f}")
    print(f"  {'GRAND TOTAL':<16}{grand_total:>10.2f}")


def main():
    expenses = load_expenses()
    while True:
        print("\n=== Institute Expense Tracker ===")
        print("1. Add New Expense")
        print("2. Show All Expenses")
        print("3. Calculate Total Expenses by Category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_all(expenses)
        elif choice == "3":
            total_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
