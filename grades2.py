grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

sorted_grades = sorted(grades, reverse=True)

total_grades = sum(grades)
average_grade = total_grades / len(grades)

print("Average grade:", average_grade)