marks = []
n = int(input("Enter number of subjects: "))


for i in range(n):
    while True:
        m = float(input(f"Enter marks for subject {i+1}: "))
        if 0 <= m <= 100:
            marks.append(m)
            break
        else:
            print("Invalid input. Enter between 0 and 100.")


print(marks)