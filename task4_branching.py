attendance = float(input("Enter attendance % = "))
marks = float(input("Enter total marks= "))

if attendance >= 75 and marks >= 40:
    print("Eligible for exam")
else:
    print("Not eligible for exam")

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)



#Scholarship checker
cgpa = float(input("Enter CGPA: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance %: "))


if cgpa >= 3.5 and income < 300000 and attendance >= 80:  #must meet all condition
    print("Scholarship Eligible")
else:
    print("Not Eligible for Scholarship")
