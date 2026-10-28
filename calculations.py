
from expenses import expenses


def calculate_balances():
    """Calculate each user's net balance."""

    balances = {}

    for expense in expenses:
        payer = expense["paid_by"]
        amount = expense["amount"]

        # The person who paid receives credit for the full amount.
        balances[payer] = balances.get(payer, 0) + amount

        # Each participant owes their assigned share.
        for user, share in expense["shares"].items():
            balances[user] = balances.get(user, 0) - share

    # Round balances to two decimal places.
    return {
        user: round(balance, 2)
        for user, balance in balances.items()
    }


def display_balances():
    balances = calculate_balances()

    if not balances:
        print("No balances to display yet.")
        return

    print("\n===== USER BALANCES =====")

    for user, balance in balances.items():
        if balance > 0:
            print(f"{user} should receive: Rs. {balance:.2f}")
        elif balance < 0:
            print(f"{user} owes: Rs. {abs(balance):.2f}")
        else:
            print(f"{user} is settled.")

    print("=========================")
