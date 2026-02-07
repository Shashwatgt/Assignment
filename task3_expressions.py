
assignment = float(input("Enter assignment score: "))
lab = float(input("Enter lab score: "))
exam = float(input("Enter exam score: "))

# Weighted formula: assignment 30%, lab 20%, exam 50%
final_score = (assignment * 0.3) + (lab * 0.2) + (exam * 0.5)

print(f"Final Score: {final_score:.2f}")