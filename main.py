
# Gym Management System
# First Version - 1.0

members = []

def add_member():
    print("\n--- Add New Member ---")

    name = input("Enter member name: ")
    age = input("Enter member age: ")
    phone = input("Enter phone number: ")

    member = {
        "name": name,
        "age": age,
        "phone": phone
    }

    members.append(member)
    print("\nMember added successfully!")


def view_members():
    print("\n--- Gym Members ---")

    if not members:
        print("No members registered yet.")
        return

    for i, member in enumerate(members, start=1):
        print(f"\nMember {i}")
        print("Name:", member["name"])
        print("Age:", member["age"])
        print("Phone:", member["phone"])


def main():
    while True:
        print("\n==============================")
        print("    GYM MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Member")
        print("2. View Members")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
