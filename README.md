#Pocket Money Tracker

A small command-line program I built in Python to keep track of where my pocket money goes each month. It's simple on purpose: no libraries to install, no files to set up, just run it and start typing.

##Why I made this

As a hostel student, money disappears faster than you'd think. A chai here, an auto there, and suddenly the month still has ten days left and the wallet is empty. I wanted something quick that could tell me three things: how much I've spent, where it went, and how much I can safely spend per day for the rest of the month.

##What it can do

- **Set a monthly budget** so the program knows your limit.
- **Add expenses by category** (Food, Travel, Snacks, whatever you like). Spending in the same category keeps adding up.
- **Warn you** when you cross 80% of your budget, and again when you go over it.
- **Show a summary** with each category's share of your spending, the total, your biggest expense, and what's left of your budget.
- **Suggest a safe daily limit** based on how many days remain in the month.
- **Undo your last entry** if you typed something wrong. You can undo several times in a row.

##How to run it

You only need Python 3 installed.

1. Save the file as `Pocket_Money_Tracker.py`.
2. Open a terminal in that folder.
3. Run:

   ```
   python Pocket_Money_Tracker.py
   ```

##How to use it

When the program starts you'll see this menu:

```
1. Set budget for this Month
2. Add your expenses
3. View summary
4. Undo last entry
5. Exit
```

Type a number and press Enter. A typical session looks like this:

1. Choose `1` and enter your budget, for example `5000`.
2. Choose `2`, enter a category like `Food`, then the amount, like `250`.
3. Repeat as you spend money through the month.
4. Choose `3` any time to see the breakdown. It will ask how many days are left in the month so it can work out your daily limit.

###Example summary

```
--- Spending Summary ---
Food 62.5 %
Travel 37.5 %
------------------------------
Total Spent: Rs. 800
Highest Expense: Food (Rs. 500)
Remaining budget: Rs. 4200.0
Safe daily spending limit: Rs. 140.0
```

##A few things to know

- Category names accept **letters and spaces only**. If you type numbers or symbols, it asks again.
- Data lives in memory only. **Closing the program clears everything**, so it's meant for one sitting or a quick check-in, not permanent storage.
- Amounts for expenses are whole numbers (no paise). The budget can have decimals.
- The summary only asks for "days left" when a budget has been set.
- Typing text where a number is expected (for example `abc` as an amount) will crash the program. I haven't added that protection yet.

##Ideas for the future

- Save data to a file so it survives after closing.
- Handle invalid number input without crashing.
- Allow decimal amounts for expenses.
- Add a monthly history so I can compare one month to the next.

##Concepts used

This project was a good way to practise what we've learned in the Python course: `while` loops, `if/elif/else` branching, dictionaries, lists, tuples, string methods, the `random` module, and basic input validation.

##Author

Piyush, B.Tech CSE, VIT Bhopal
Course: CSE1021 (Introduction to Problem Solving and Programming)
