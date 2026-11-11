# Queue (First In, First Out)
# Enqueues every letter of a last name, then dequeues them until empty.

from collections import deque

last_name = input("Enter your last name: ").strip().upper()
if not last_name:
    last_name = "CABALAN"

queue = deque()

# ENQUEUE
print("\n--- Enqueuing letters ---")
for letter in last_name:
    queue.append(letter)
    print(f"Enqueued {letter}: front -> rear {list(queue)}")

# DEQUEUE
print("\n--- Dequeuing letters ---")
while len(queue) > 0:
    removed = queue.popleft()
    print(f"Dequeued {removed}: front -> rear {list(queue)}")

print("\nQueue is empty.")