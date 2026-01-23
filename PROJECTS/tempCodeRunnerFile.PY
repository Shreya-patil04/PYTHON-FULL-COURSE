# Program: Mini Expense Tracker
# Author: Shreya Patil 

# Declaring and initializing expense variables (in Indian rupees)
food_expense = 2500
travel_expense = 1250
books_expense = 1350
entertainment_expense = 1700
rental_expense = 20000

# Concatenating for display
category = "Monthly Expenses"

# Calculating total and average
total_monthly_expense = food_expense + travel_expense + books_expense + entertainment_expense + rental_expense
average_expense_per_week = total_monthly_expense / 4

# Displaying results
print("---- " + category + " ----")
print("Food: ₹" + str(food_expense))
print("Travel: ₹" + str(travel_expense))
print("Books: ₹" + str(books_expense))
print("Entertainment: ₹" + str(entertainment_expense))
print("----------------------------")
print("Total Monthly Expense = ₹" + str(total_monthly_expense))
print("Average Expense per week = ₹" + str(round(average_expense_per_week, 2)))
print("Great job tracking your spending!")



