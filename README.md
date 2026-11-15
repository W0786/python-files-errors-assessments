<p align="center">
  <img src="images/banner.svg" alt="Python Files & Errors Assessment banner" width="100%">
</p>

# Python Files & Errors Assessment

Two small management tools for a training institute, built with Python's **file handling**, **exception handling**, **sets** and **list comprehensions**. Only the standard library is used (Python 3.8+).

---

## 1. Overview

| Program | Purpose |
|---------|---------|
| `expense_tracker.py` | **Expense Tracking System.** Records daily operational expenses (stationery, internet bills, refreshments, transport) in `expenses.csv`, shows them, and totals them by category. |
| `attendance_cleaner.py` | **Attendance Management System.** Cleans the messy `attendance.txt` (repeated names, wrong capitalisation, extra spaces), removes duplicates and generates a clean, sorted `attendance_clean.csv`. |

## 2. Project structure

```
python-files-errors-assessment/
├── expense_tracker.py
├── attendance_cleaner.py
├── attendance.txt
├── README.md
└── images/            <- SVG diagrams used in this README only
```

`expenses.csv` and `attendance_clean.csv` are created automatically when the programs run.

![Project structure and data flow](images/structure.svg)

---

## 3. Requirements checklist

### Task 1: `expense_tracker.py`

| # | Requirement | Status | Where in code |
|---|-------------|:------:|---------------|
| 1 | **Save expenses in `expenses.csv` with columns `date,item,category,amount`** | ✅ | `FIELDS` (line 9), `save_expenses()` |
| 2 | **Load saved expenses on start; catch `FileNotFoundError` and start with an empty list** | ✅ | `load_expenses()`, `except FileNotFoundError` (line 25) |
| 3 | **Menu: 1. Add New Expense, 2. Show All Expenses, 3. Calculate Total Expenses by Category, 4. Exit** | ✅ | `main()` (lines 119-122) |
| 4 | **User enters date, item name, category and amount** | ✅ | `add_expense()` |
| 5 | **Catch `ValueError` for an invalid amount and ask again** | ✅ | `ask_amount()`, `except ValueError` (line 65) |
| 6 | **Use a `set` to display all unique categories** | ✅ | `show_all()` (line 97), `total_by_category()` (line 105) |
| 7 | **New expenses are saved to the CSV so they remain after restart** | ✅ | `save_expenses()` is called inside `add_expense()` |

### Task 2: `attendance_cleaner.py`

| # | Requirement | Status | Where in code |
|---|-------------|:------:|---------------|
| 1 | **Read names from `attendance.txt` (one name per line)** | ✅ | `open(INPUT_FILE)` (line 15) |
| 2 | **Clean names with `strip()` and `title()` using a list comprehension** | ✅ | line 21 |
| 3 | **Use a `set` to find unique students and count them** | ✅ | `set(cleaned)` (line 23) |
| 4 | **Sort the cleaned names alphabetically** | ✅ | `sorted(...)` (line 24) |
| 5 | **Save the cleaned, sorted list to `attendance_clean.csv`** | ✅ | `csv.writer` block |
| 6 | **Display original record count, unique student count and cleaned list** | ✅ | final `print` statements |

### Repository / README

| Requirement | Status |
|-------------|:------:|
| **Public GitHub repo named `python-files-errors-assessment` with the 4 files above** | ✅ |
| **README: overview of both apps** | ✅ Section 1 |
| **README: how to run each program** | ✅ Section 4 |
| **README: errors handled and why** | ✅ Section 5 |
| **README: how sets and list comprehensions are used** | ✅ Section 6 |
| **README: sample run showing data saved and loaded again** | ✅ Section 7 |
| **Test cases** | ✅ Section 8 |
| **SVG banner, structure diagram and flowcharts** | ✅ Sections 2, 4 and 6 |

---

## 4. How to run

Open a terminal in the project folder, then:

```
python expense_tracker.py
python attendance_cleaner.py
```

(Use `python3` on Mac/Linux or `py` on Windows if `python` is not recognised.)

### Expense Tracker menu
1. **Add New Expense**: enter date (`YYYY-MM-DD`, or press Enter for today), item, category and amount
2. **Show All Expenses**: table of all records plus the unique categories
3. **Calculate Total Expenses by Category**
4. **Exit**

Every new expense is written to `expenses.csv` immediately, and the file is loaded again the next time the program starts.

#### Expense Tracker flowchart

![Expense tracker flowchart](images/expense_flowchart.svg)

### Attendance Cleaner
Reads `attendance.txt`, cleans it, prints the **original number of records**, the **unique student count** and the **cleaned list**, and saves the sorted unique names to `attendance_clean.csv`. No input is needed.

#### Attendance Cleaner flowchart

![Attendance cleaner flowchart](images/attendance_flowchart.svg)

---

## 5. Errors handled and why

| Error | Where | Why it is handled |
|-------|-------|-------------------|
| **`FileNotFoundError`** | Expense tracker, at start-up | On the first run `expenses.csv` does not exist yet. The program starts with an empty list instead of crashing. |
| **`ValueError` (amount)** | Expense tracker, amount input | `float("abc")` fails. The user is told what went wrong and is asked again until a valid number is entered. |
| `ValueError` (date) | Expense tracker, date input | A wrong date such as `2026-13-45` is rejected and the user is asked again, so only valid dates are stored. |
| `ValueError` / `TypeError` / `KeyError` | Expense tracker, loading rows | A damaged row in the CSV is skipped so the rest of the data still loads. |
| `FileNotFoundError` | Attendance cleaner | If `attendance.txt` is missing, a clear message is shown instead of a traceback. |

Extra input checks: negative amounts, empty item/category and invalid menu choices are rejected with a message.

---

## 6. How sets and list comprehensions are used

![Cleaning pipeline: list comprehension, set, sorted](images/sets_and_comprehension.svg)

### Sets (store only unique values)
- `expense_tracker.py`: `{e["category"] for e in expenses}` gives **each category once**, even if it was used many times. It is used to display the unique categories and to calculate totals.
- `attendance_cleaner.py`: `set(cleaned)` **removes repeated student names**, and `len()` of the set is the unique student count.

### List comprehension (cleans every line in one expression)
```python
cleaned = [line.strip().title() for line in lines if line.strip()]
```
- `strip()` removes extra spaces
- `title()` fixes capitalisation (`"  ali RAZA "` becomes `"Ali Raza"`)
- `if line.strip()` skips blank lines

The cleaned list is turned into a set and passed to `sorted()` to get the final alphabetical list.

---

## 7. Sample run: data saved and loaded again

**Run 1** (no `expenses.csv` yet)
```
expenses.csv not found. Starting with an empty expense list.
Choose an option (1-4): 1
Date (YYYY-MM-DD, Enter for today): 2026-11-10
Item name: A4 Paper
Category: stationery
Amount: abc
Invalid amount. Please enter a number (e.g. 1500 or 99.5).
Amount: 1850
Expense saved.
Choose an option (1-4): 1
Date (YYYY-MM-DD, Enter for today): 2026-13-45
Invalid date. Use the format YYYY-MM-DD (e.g. 2026-11-14).
Date (YYYY-MM-DD, Enter for today): 2026-11-11
Item name: WiFi Bill
Category: internet
Amount: 4500.50
Expense saved.
... (two more expenses added) ...
Choose an option (1-4): 3

Total expenses by category:
  Internet           4500.50
  Refreshments        700.00
  Stationery         2800.00
  GRAND TOTAL        8000.50
Choose an option (1-4): 4
Goodbye!
```

`expenses.csv` after Run 1:
```
date,item,category,amount
2026-11-10,A4 Paper,Stationery,1850.0
2026-11-11,WiFi Bill,Internet,4500.5
2026-11-14,Tea & Biscuits,Refreshments,700.0
2026-11-12,Paper Ream,Stationery,950.0
```

**Run 2** (program restarted, data loaded again)
```
Loaded 4 expense(s) from expenses.csv.
Choose an option (1-4): 2

Date        Item                  Category            Amount
------------------------------------------------------------
2026-11-10  A4 Paper              Stationery         1850.00
2026-11-11  WiFi Bill             Internet           4500.50
2026-11-14  Tea & Biscuits        Refreshments        700.00
2026-11-12  Paper Ream            Stationery          950.00

Unique categories: Internet, Refreshments, Stationery
```

**Attendance cleaner**
```
Original number of records : 10
(Blank lines skipped       : 1)
Unique students            : 5

Cleaned attendance list:
  1. Ahmed
  2. Ali Raza
  3. Bilal Ahmed
  4. Sara Khan
  5. Zainab Fatima

Saved to attendance_clean.csv
```

`attendance_clean.csv`:
```
name
Ahmed
Ali Raza
Bilal Ahmed
Sara Khan
Zainab Fatima
```

---

## 8. Test cases

All test cases below were run and **passed (27/27)**. To repeat them manually, run the program and enter the input shown.

### Expense Tracker

| ID | Test | Input / Action | Expected result | Result |
|----|------|----------------|-----------------|:------:|
| E1 | No file on first run | Delete `expenses.csv`, run program | "Starting with an empty expense list" (`FileNotFoundError` handled) | ✅ |
| E2 | Show all when empty | Option 2 | "No expenses recorded yet" | ✅ |
| E3 | Totals when empty | Option 3 | "No expenses recorded yet" | ✅ |
| E4 | Invalid amount | Amount = `abc` | "Invalid amount", asked again; `1850` then accepted | ✅ |
| E5 | Empty amount | Amount = (just Enter) | "Invalid amount", asked again | ✅ |
| E6 | Negative amount | Amount = `-5` | "Amount cannot be negative", asked again | ✅ |
| E7 | Invalid date | Date = `2026-13-45` | "Invalid date", asked again | ✅ |
| E8 | Blank date | Date = (just Enter) | Today's date is saved | ✅ |
| E9 | CSV header | Open `expenses.csv` | First line is `date,item,category,amount` | ✅ |
| E10 | Expense saved to CSV | Add `WiFi Bill`, `internet`, `4500.50` | Row `2026-11-11,WiFi Bill,Internet,4500.5` in file | ✅ |
| E11 | Data loaded again | Exit, run again | "Loaded 3 expense(s) from expenses.csv" | ✅ |
| E12 | Loaded data shown | Option 2 after restart | Old expenses are listed | ✅ |
| E13 | Unique categories (set) | Add `stationery` and `STATIONERY` | Category appears once: `Internet, Stationery` | ✅ |
| E14 | Category total | Stationery 1850 + 20 + 950 | `2820.00` | ✅ |
| E15 | Grand total | Option 3 | `7320.50` | ✅ |
| E16 | Invalid menu choice | Enter `9` or `abc` | "Invalid choice", menu shown again | ✅ |
| E17 | Exit | Option 4 | "Goodbye!" and program ends | ✅ |
| E18 | Damaged CSV row | Row with amount `xyz` in CSV | Row skipped, valid rows still loaded | ✅ |

### Attendance Cleaner

| ID | Test | Input / Action | Expected result | Result |
|----|------|----------------|-----------------|:------:|
| A1 | Original record count | Provided `attendance.txt` | `Original number of records : 10` | ✅ |
| A2 | Unique count (set) | Same file | `Unique students : 5` | ✅ |
| A3 | Cleaned list shown | Same file | Numbered, alphabetical list printed | ✅ |
| A4 | CSV sorted | Open `attendance_clean.csv` | `Ahmed, Ali Raza, Bilal Ahmed, Sara Khan, Zainab Fatima` | ✅ |
| A5 | Blank line | File contains an empty line | Skipped and reported | ✅ |
| A6 | strip + title + dedupe | `"  zed  "`, `"ZED"`, `"  amy lee"` | `Amy Lee`, `Zed` | ✅ |
| A7 | Empty file | `attendance.txt` is empty | `Unique students : 0`, no crash | ✅ |
| A8 | Missing file | Delete `attendance.txt` | "attendance.txt not found" (`FileNotFoundError` handled) | ✅ |
