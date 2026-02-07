n= int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

print("Total:", sum(marks))
print("Average:", sum(marks)/n)
print("Highest:", max(marks))
print("Lowest:", min(marks))