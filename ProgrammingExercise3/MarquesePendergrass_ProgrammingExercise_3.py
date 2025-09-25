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

    # gets the total amount of expenses using lamba function with reduce and takes a running total of x any y with
    # y[1] for expenses starting at 0
    total = reduce(lambda x, y: x + y[1], expenses, 0)

    # assigns highest and lowest variables to the max expenses within the lamba key and associates it with the proper
    # index within the highest or lowest values
    highest = max(expenses, key=lambda x: x[1])
    lowest = min(expenses, key=lambda x: x[1])

    # prints the total amount of expenses, highest expense, and lowest expense
    print("Total expenses: ", total)
    print("Highest expenses: ", highest[0], 'at', highest[1])
    print("Lowest expenses: ", lowest[0], 'at', lowest[1])

if __name__ == "__main__":
    main()