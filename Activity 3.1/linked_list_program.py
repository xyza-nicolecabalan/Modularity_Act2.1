# Linked List
# Adds every letter of a last name as a node, then removes nodes until empty.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def show(head):
    parts = []
    current = head
    while current is not None:
        parts.append(current.data)
        current = current.next
    return " -> ".join(parts + ["NULL"])


last_name = input("Enter your last name: ").strip().upper()
if not last_name:
    last_name = "CABALAN"

head = None

# ADD
print("\n--- Adding letters ---")
for letter in last_name:
    new_node = Node(letter)
    if head is None:
        head = new_node
    else:
        last = head
        while last.next is not None:
            last = last.next
        last.next = new_node
    print(f"Added {letter}: {show(head)}")

# REMOVE
print("\n--- Removing letters ---")
while head is not None:
    temp = head
    head = head.next
    print(f"Removed {temp.data}: {show(head)}")

print("\nList is empty.")