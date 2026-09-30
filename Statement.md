#Problem Statement: Pocket Money Tracker

##The problem

Most students get a fixed amount of money at the start of the month, and most of us have no clear idea where it goes. Spending happens in small pieces, like a snack, a recharge, a bus fare, and it's hard to see the bigger picture until the money is already gone. Paper notes get lost, and opening a full spreadsheet for a ₹40 expense feels like too much effort.

So the real question is: **how can a student quickly record their spending and always know whether they're on track for the month?**

##What I wanted to build

A lightweight program that runs in the terminal and does the boring bookkeeping for me. It should:

1. Let me set a monthly budget.
2. Let me log each expense under a category.
3. Warn me before I overspend, not after.
4. Show me where my money is going in a clear summary.
5. Tell me how much I can spend per day for the rest of the month.
6. Let me fix mistakes without restarting everything.

##Who it's for

Students living on a monthly allowance, especially hostel students, who want a simple way to stay aware of their spending without installing an app or learning new software.

##How the program solves it

| Need | How the program handles it |
|------|---------------------------|
| Know my limit | Option 1 stores the monthly budget |
| Record spending | Option 2 adds amounts to a category, creating new categories automatically |
| Avoid overspending | After every expense, it warns at 80% of the budget and again when the budget is exceeded |
| Understand my habits | Option 3 shows each category's percentage share, the total, and the highest expense |
| Plan the rest of the month | It divides the remaining budget by the days left to give a safe daily limit |
| Fix typing mistakes | Option 4 undoes the last entry, and can be repeated |

##Approach and design choices

- **Dictionary for totals:** Expenses are stored as `category -> total amount`, so repeated spending in "Food" simply adds up and is easy to summarise.
- **List for history:** Every entry is also stored as a `(category, amount)` pair in a list. This works like a stack, so the newest entry is the first one removed when undoing.
- **Validation loop for categories:** The program keeps asking until the category contains only letters, which keeps the summary clean.
- **Cleanup on undo:** If undoing an entry brings a category down to zero, that category is removed so it doesn't show up as an empty line in the summary.
- **Guard against bad input:** Days left must be greater than zero, which avoids a division by zero error.
- **Small human touch:** The confirmation message after setting a budget is picked randomly, so the program doesn't feel completely robotic.

##Inputs and outputs

**Inputs:** menu choice, monthly budget, category name, expense amount, days left in the month.

**Outputs:** confirmation messages, budget warnings, a spending summary with percentages, total spent, highest expense category, remaining budget, and a safe daily spending limit.

##Limitations

- Data is not saved after the program closes.
- Entering non-numeric text for a number field causes an error.
- Expense amounts must be whole numbers.
- It tracks a single month at a time.

##What I learned

Building this showed me how much cleaner a program becomes when the data structure fits the problem. Using a dictionary for totals and a list for history made both the summary and the undo feature much simpler than I expected. I also learned that handling user input carefully takes as much thought as the main logic, and that's something I want to improve next.

##Possible improvements

- Save and load data from a file.
- Add `try/except` blocks so wrong input never crashes the program.
- Support decimal expense amounts.
- Keep records across multiple months for comparison.
