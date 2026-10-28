
from users import users, add_user, list_users
from expenses import expenses, add_expense, display_expenses
from calculations import display_balances
from storage import save_data, load_data


def choose_participants():
    """Select users who share an expense."""

    if not users:
        print("Please add users first.")
        return []

    list_users()
    names = input(
        "Enter participant names separated by commas: "
    )

    participants = [name.strip() for name in names.split(",") if name.strip()]

    if not participants:
        print("No participants selected.")
        return []

    if len(set(participants)) != len(participants):
        print("Duplicate participants are not allowed.")
        return []

    unknown = [name for name in participants if name not in users]

    if unknown:
        print("Unknown users:", ", ".join(unknown))
        return []

    return participants


def handle_add_expense():
    """Collect expense details from the user."""

    if not users:
        print("Please add users before recording expenses.")
        return

    description = input("Enter expense description: ").strip()

    try:
        amount = round(float(input("Enter total amount (Rs.): ")), 2)
    except ValueError:
        print("Please enter a valid number.")
        return

    list_users()
    paid_by = input("Who paid? Enter the exact name: ").strip()

    if paid_by not in users:
        print("That user does not exist.")
        return

    participants = choose_participants()

    if not participants:
        return

    print("\n1. Equal split")
    print("2. Custom split")

    split_choice = input("Choose split type: ").strip()

    if split_choice == "1":
        split_type = "equal"
        custom_shares = None

    elif split_choice == "2":
        split_type = "custom"
        custom_shares = {}

        for person in participants:
            try:
                share = round(
                    float(input(f"Enter {person}'s share (Rs.): ")),
                    2
                )
            except ValueError:
                print("Invalid share. Expense cancelled.")
                return

            custom_shares[person] = share

    else:
        print("Invalid split choice.")
        return

    added = add_expense(
        description,
        amount,
        paid_by,
        participants,
        split_type,
        custom_shares
    )

    if added:
        save_data()


def main():
    """Run the Expense Sharing App."""

    load_data()

    while True:
        print("\n===== EXPENSE SHARING APP =====")
        print("1. Add user")
        print("2. View users")
        print("3. Add expense")
        print("4. View transaction history")
        print("5. View balances")
        print("6. Save data")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            name = input("Enter user's name: ")
            if add_user(name):
                save_data()

        elif choice == "2":
            list_users()

        elif choice == "3":
            handle_add_expense()

        elif choice == "4":
            display_expenses()

        elif choice == "5":
            display_balances()

        elif choice == "6":
            save_data()

        elif choice == "7":
            save_data()
            print("Thank you for using Expense Sharing App!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()

