expenses = []
def get_category():
    while True:
        category = input("Enter expense category: ").strip()

        if category == "":
            print("Category is required.")
        else:
            return category


def get_amount():
    while True:
        amount_input = input("Enter expense amount: ").strip()

        if amount_input == "":
            print("Amount is required.")
            continue

        try:
            amount = float(amount_input)

            if amount < 0:
                print("Amount cannot be negative.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")


def add_expense():

    category = get_category()
    amount = get_amount()

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def total_spent():

    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print("Total amount spent:", total)


def highest_expense():

    if not expenses:
        print("No expenses recorded.")
        return

    highest = max(expenses, key=lambda x: x["amount"])

    print("Highest Expense:")
    print("Category:", highest["category"])
    print("Amount:", highest["amount"])


def view_by_category():

    category = get_category()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(expense)
            found = True

    if not found:
        print("No expenses found for this category.")


def show_menu():

    print("\n====== Personal Expense Tracker ======")
    print("1. Add Expense")
    print("2. Total Spent")
    print("3. Highest Expense")
    print("4. View by Category")
    print("5. Exit")


def main():

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            total_spent()

        elif choice == "3":
            highest_expense()

        elif choice == "4":
            view_by_category()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


main()