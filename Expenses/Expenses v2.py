total = 0
expenses = []

num_of_expenses = int(input("Enter the number of expenses: "))

for i in range(num_of_expenses):
    expenses.append(float(input("Enter an expense: ")))

print("Total spent $", sum(expenses), sep='')
