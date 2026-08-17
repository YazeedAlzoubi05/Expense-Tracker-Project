# Expense Tracker

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Interface](https://img.shields.io/badge/Interface-Command%20Line-0E7490)](#menu-options)
[![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-14B8A6)](#requirements)

A menu-driven Python command-line application for recording expenses, updating and deleting entries, and reviewing overall or category-level spending. Expense records are validated and saved locally so they remain available between runs.

## Features

- Create expenses with a name, quantity, category, and unit price
- View every saved expense and its calculated line total
- Update an existing expense by ID
- Delete an expense by ID
- Calculate total spending across all records
- Calculate spending grouped by category
- Validate names, numeric values, IDs, and menu selections
- Persist data in a local text file

## Requirements

- Python 3.10 or newer
- No third-party packages

## Run the application

Clone the repository and run the script from its root directory:

```bash
git clone https://github.com/YazeedAlzoubi05/Expense-Tracker-Project.git
cd Expense-Tracker-Project
python IntershipTrackerProject.py
```

The existing filename is `IntershipTrackerProject.py`, so use that spelling when running the program.

## Menu options

```text
1. Enter a new expense
2. View all expenses
3. Update an expense
4. Delete an expense
5. Calculate total spent
6. Calculate spent by category
0. Exit
```

## Expense record

Each record contains:

| Field | Description |
|---|---|
| ID | Automatically generated unique integer |
| Name | Human-readable expense name |
| Amount | Quantity purchased |
| Category | Spending category |
| Unit price | Price for one unit |
| Line total | Calculated as `amount × unit price` |

## Data persistence

The application creates `test.txt` in the working directory and stores one record per line:

```text
id|name|amount|category|unit_price
```

The file is loaded when an operation needs the latest records and rewritten after changes. It is excluded from Git so personal expense data is not committed accidentally.

## Validation behavior

- Names and categories must contain letters and be at least two characters long.
- Amounts must be positive integers.
- Unit prices must be positive numbers.
- Update and delete operations verify that the requested ID exists.
- Invalid file rows are handled without stopping the complete application.

## Project structure

```text
.
├── IntershipTrackerProject.py  # Complete command-line application
├── README.md                   # Project documentation
└── .gitignore                  # Local Python and expense-data exclusions
```

## Limitations and possible extensions

- Data is stored in a local text file rather than a database.
- Records do not currently include transaction dates or currencies.
- Future versions could add CSV export, monthly budgets, recurring expenses, and automated tests.

## Author

**Yazeed Alzoubi** — [GitHub profile](https://github.com/YazeedAlzoubi05)

