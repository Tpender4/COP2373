# Description: Program that prompts user to enter monthly expenses and then displays the total of expenses,
# the highest expense listed and the lowest expense listed.

# imports reduce method
from functools import reduce

def main():
    # list to keep track of expenses the user enters
    expenses = []

    # Prompts user to enter the number of expenses they have
    expenses_number = int(input("Enter the number of expenses you have: "))

    # loop for collecting the expenses
    for i in range(expenses_number):
        expense_name = input("Enter expense name: ")
        amount = float(input(f"Enter amount for {expense_name}: "))
        expenses.append([expense_name, amount])
