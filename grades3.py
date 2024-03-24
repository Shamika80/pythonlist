grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Modify grades below 80 to "Failed" using list comprehension
modified_grades = [grade if grade >= 80 else "Failed" for grade in grades]

print("Grades after replacing failing grades:", modified_grades)