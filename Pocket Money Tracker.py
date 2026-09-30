import random

# ---------- Data ----------
monthly_budget = 0
expenses = {}          # category -> total amount spent
history = []           # list of (category, amount), used for undo

print("\n--- Pocket Money Tracker ---")

while True:
    # ---------- Menu ----------
    print("\n1. Set budget for this Month")
    print("2. Add your expenses")
    print("3. View summary")
    print("4. Undo last entry")
    print("5. Exit")
    choice = input("\nChoose an option (1-5): ")

    # ---------- 1. Set budget ----------
    if choice == "1":
        monthly_budget = float(input("Enter your monthly budget: Rs. "))
        print(random.choice(["Budget saved!", "Got it!", "Updated successfully."]))

    # ---------- 2. Add expense ----------
    elif choice == "2":
        # Keep asking until the category contains only letters (spaces allowed)
        while True:
            category = input("Enter category (e.g. Food, Travel): ").strip()
            if category.replace(" ", "").isalpha():
                break
            print("Invalid category. Please enter letters only (no numbers or symbols).")

        amount = int(input("Amount spent on " + category + ": Rs. "))

        # Add to the existing category, or create it if it is new
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        history.append((category, amount))
        print("Added Rs.", amount, "to", category)

        # Budget warnings
        if monthly_budget > 0:
            total_spent = sum(expenses.values())
            if total_spent > monthly_budget:
                print("Warning: Over budget!")
                print("You are over budget by Rs.", total_spent - monthly_budget)
            elif total_spent > (monthly_budget * 0.8):
                print("Warning: You've used over 80% of your budget...")

    # ---------- 3. View summary ----------
    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
            continue

        total_spent = sum(expenses.values())
        print("\n--- Spending Summary ---")
        for category, amount in expenses.items():
            percentage = round((amount / total_spent) * 100, 1)
            print(category, percentage, "%")

        print("-" * 30)
        print("Total Spent: Rs.", total_spent)

        top_category = max(expenses, key=expenses.get)
        print("Highest Expense:", top_category, "(Rs.", expenses[top_category], ")")

        if monthly_budget > 0:
            remaining = monthly_budget - total_spent
            if remaining < 0:
                print("Over budget by: Rs.", abs(remaining))
            else:
                print("Remaining budget: Rs.", remaining)

            days_left = int(input("\nHow many days left in the month? "))
            if days_left <= 0:
                print("Days left must be greater than 0.")
            else:
                print("Safe daily spending limit: Rs.", remaining / days_left)

    # ---------- 4. Undo last entry ----------
    elif choice == "4":
        if len(history) == 0:
            print("Nothing to undo.")
        else:
            last_category, last_amount = history.pop()
            if last_category in expenses:
                expenses[last_category] -= last_amount

                # Remove the category completely if nothing is left in it
                if expenses[last_category] == 0:
                    del expenses[last_category]

            print("Undid last entry: Removed Rs.", last_amount, "from", last_category)

    # ---------- 5. Exit ----------
    elif choice == "5":
        print("Catch you later! Keep saving.")
        break

    else:
        print("Invalid choice. Please choose a number from 1 to 5.")
