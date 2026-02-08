
student = {}
marks = []




def enter_details():
    student["name"] = input("Enter name: ")
    student["age"] = int(input("Enter age: "))




def enter_marks():
    marks.clear()
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        marks.append(float(input(f"Enter marks {i+1}: ")))




def view_summary():
    if not student or not marks:
        print("Data incomplete")
        return
    avg = sum(marks)/len(marks)
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Average:", avg)




while True:
    print("\n1. Enter student details")
    print("2. Enter marks")
    print("3. View result summary")
    print("4. Exit")

    choice = input("Enter choice: ")


    if choice == "1":
        enter_details()
    elif choice == "2":
        enter_marks()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        break
    else:
        print("Invalid choice")