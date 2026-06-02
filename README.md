# 💰 Smart Expense Manager

## Overview

Smart Expense Manager is a Streamlit-powered expense tracker that helps users record, view, update, and delete daily expenses using a local SQLite database.

## Features

* Add new expenses with date, category, amount, and description
* View expenses in a sortable table
* Filter expenses by category
* See total, average, and transaction count metrics
* View the latest expense in a summary card
* Update expenses by ID
* Delete expenses by ID
* Category-wise expense summary

## Technologies

* Python 3.11+
* Streamlit
* SQLite
* Pandas

## Project Structure

SmartExpenseManager/

├── app.py          # Streamlit app UI and workflow
├── database.py     # SQLite helpers and CRUD operations
├── expenses.db     # Local SQLite database file (ignored by Git)
├── requirements.txt
├── .gitignore
└── README.md

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/rubinisk/Smart-Expense-Tracker.git
```

2. Navigate into the project folder:

```bash
cd SmartExpenseManager
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

5. Open the URL shown in the terminal (usually http://localhost:8501).

## Usage

1. Fill in the expense form with a date, category, amount, and description.
2. Click **Add Expense** to save the entry.
3. Use the category filter to narrow expense results.
4. Update or delete expenses by entering the expense ID displayed in the table.
5. Review summary metrics and category totals on the dashboard.

## Database Schema

The app uses a SQLite table named `expenses` with the following columns:

| Column      | Type                |
| ----------- | ------------------- |
| id          | INTEGER PRIMARY KEY AUTOINCREMENT |
| date        | TEXT                |
| category    | TEXT                |
| amount      | REAL                |
| description | TEXT                |

## Notes

* The app stores data locally in `expenses.db`.
* `expenses.db` is excluded from Git via `.gitignore` so database state is not pushed.
* If you want a fresh database, delete `expenses.db` and restart the app.

## Author

Built by Rubin as a personal Smart Expense Manager project.

