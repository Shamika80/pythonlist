submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended = [student for student in attended if student in submitted]

print("Attended list after removing non-submitters:", attended)