submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

present_in_both = set(submitted) & set(attended)

print("Students who submitted and attended:", list(present_in_both))