
import pandas as pd

# Store all expense records
expenses = []


def add_expense(description, amount, paid_by, participants, split_type="equal",
                custom_shares=None):
    """Add an expense and calculate each participant's share."""

    if not description.strip():
        print("Description cannot be empty.")
        return False

    if amount <= 0:
        print("Amount must be greater than zero.")
        return False

    if not participants:
        print("At least one participant is required.")
        return False

    if paid_by not in participants:
        print("The person who paid must be a participant.")
        return False

    if split_type == "equal":
        share = round(amount / len(participants), 2)
        shares = {user: share for user in participants}

        # Correct rounding differences so shares total the expense.
        difference = round(amount - sum(shares.values()), 2)
        first_user = participants[0]
        shares[first_user] = round(shares[first_user] + difference, 2)

    elif split_type == "custom":
        if custom_shares is None:
            print("Custom shares are required.")
            return False

        if set(custom_shares) != set(participants):
            print("Provide a share for every participant.")
            return False

        if any(value < 0 for value in custom_shares.values()):
            print("Shares cannot be negative.")
            return False

        if round(sum(custom_shares.values()), 2) != round(amount, 2):
            print("Custom shares must add up to the total expense.")
            return False

        shares = {
            user: round(value, 2)
            for user, value in custom_shares.items()
        }

    else:
        print("Invalid split type.")
        return False

    expenses.append({
        "description": description.strip(),
        "amount": round(amount, 2),
        "paid_by": paid_by,
        "participants": participants.copy(),
        "split_type": split_type,
        "shares": shares
    })

    print("Expense added successfully!")
    return True


def display_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    df = pd.DataFrame([
        {
            "Description": expense["description"],
            "Amount": expense["amount"],
            "Paid By": expense["paid_by"],
            "Split Type": expense["split_type"]
        }
        for expense in expenses
    ])

    print("\nTransaction History:")
    print(df.to_string(index=False))
