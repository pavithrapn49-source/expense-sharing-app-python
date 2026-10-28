
users = []


def add_user(name):
    name = name.strip()

    if not name:
        print("Name cannot be empty.")
        return False

    if name in users:
        print("User already exists.")
        return False

    users.append(name)
    print(f"User '{name}' added successfully.")
    return True


def list_users():
    if not users:
        print("No users added yet.")
        return

    print("\nRegistered Users:")
    for number, name in enumerate(users, start=1):
        print(f"{number}. {name}")
