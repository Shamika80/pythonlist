students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

student_records = list(zip(students, grades, activities))

filtered_records = [record for record in student_records if record[1] >= 80]

for name, grade, activity in filtered_records:
  print(name, grade, activity)