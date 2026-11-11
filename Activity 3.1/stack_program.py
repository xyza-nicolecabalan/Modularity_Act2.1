# Stack (Last In, First Out)
# Pushes every letter of a last name, then pops them until empty.

last_name = input("Enter your last name: ").strip().upper()
if not last_name:
    last_name = "CABALAN"

stack = []

# PUSH
print("\n--- Pushing letters ---")
for letter in last_name:
    stack.append(letter)
    print(f"Pushed {letter}: bottom -> top {stack}")

# POP
print("\n--- Popping letters ---")
while len(stack) > 0:
    removed = stack.pop()
    print(f"Popped {removed}: bottom -> top {stack}")

print("\nStack is empty.")