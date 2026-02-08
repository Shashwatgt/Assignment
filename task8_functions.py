def calculate_average(marks):
    return sum(marks)/len(marks)




def determine_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"




def format_output(name, avg, grade):
    return f"Student: {name}, Average: {avg:.2f}, Grade: {grade}"




marks = [70, 80, 90]
avg = calculate_average(marks)
grade = determine_grade(avg)
result = format_output("Shashwat", avg, grade)
print(result)