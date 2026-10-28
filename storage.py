
import json
from pathlib import Path

import pandas as pd

from expenses import expenses
from users import users


DATA_DIR = Path(__file__).parent / "data"
USERS_FILE = DATA_DIR / "users.csv"
EXPENSES_FILE = DATA_DIR / "expenses.csv"


def save_data():
    """Save users and expenses to CSV files."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    users_df = pd.DataFrame({"name": users})
    users_df.to_csv(USERS_FILE, index=False)

    # Store lists and dictionaries as JSON text inside CSV cells.
    expense_records = []

    for expense in expenses:
        expense_records.append({
            "description": expense["description"],
            "amount": expense["amount"],
            "paid_by": expense["paid_by"],
            "participants": json.dumps(expense["participants"]),
            "split_type": expense["split_type"],
            "shares": json.dumps(expense["shares"])
        })

    expenses_df = pd.DataFrame(
        expense_records,
        columns=[
            "description", "amount", "paid_by",
            "participants", "split_type", "shares"
        ]
    )
    expenses_df.to_csv(EXPENSES_FILE, index=False)

    print("Data saved successfully!")


def load_data():
    """Load saved users and expenses from CSV files."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if USERS_FILE.exists():
        users_df = pd.read_csv(USERS_FILE)
        users.clear()
        users.extend(users_df["name"].dropna().astype(str).tolist())

    if EXPENSES_FILE.exists():
        expenses_df = pd.read_csv(EXPENSES_FILE)

        expenses.clear()

        for _, row in expenses_df.iterrows():
            expenses.append({
                "description": str(row["description"]),
                "amount": float(row["amount"]),
                "paid_by": str(row["paid_by"]),
                "participants": json.loads(row["participants"]),
                "split_type": str(row["split_type"]),
                "shares": json.loads(row["shares"])
            })

    print("Saved data loaded successfully.")
