income = input("Enter monthly income:")
expenses = input("Enter monthly expenses:")

income = float(income)
expenses = float(expenses)

savings = income - expenses

if savings >= 0:
    print("Savings: ", savings)
else:
    print("Deflicit: ", savings)