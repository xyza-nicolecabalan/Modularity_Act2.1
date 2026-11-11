#Array
# Adds every letter of a last name into an array, then removes them until empty.

last_name = input("Enter your last name: ").strip().upper()
if not last_name:
    last_name = "CABALAN"

capacity = len(last_name)
array = [""] * capacity
size = 0

# ADD
print("\n--- Adding letters ---")
for letter in last_name:
    array[size] = letter
    size = size + 1
    print(f"Added {letter} at index {size - 1} -> {array}")

# REMOVE
print("\n--- Removing letters ---")
while size > 0:
    size = size - 1
    removed = array[size]
    array[size] = ""
    print(f"Removed {removed} from index {size} -> {array}")

print("\nArray is empty." if size == 0 else "")