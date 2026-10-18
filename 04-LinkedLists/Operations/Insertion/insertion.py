# Linked List Insertion in Python

"""
Goal: Implement insertion operations for a Singly Linked List.
Algorithm: Update pointers to integrate a new node at the head, tail, or middle.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the start of the list. Time: O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        """Insert a new node at the end of the list. Time: O(n)"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} as the first node.")
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end.")

    def insert_at_position(self, data, position):
        """Insert a new node at a specific index (0-indexed). Time: O(n)"""
        if position < 0:
            print("Position cannot be negative.")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        # Traverse to the node just before the insertion point
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current:
            print(f"Position {position} is out of bounds.")
            return

        # Link the new node
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at position {position}.")

    def display(self):
        """Print the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# --- Usage Example ---
if __name__ == "__main__":
    ll = LinkedList()

    # Test 1: Insertion at beginning
    ll.insert_at_beginning(10) # [10]
    ll.insert_at_beginning(5)   # [5, 10]
    ll.display()

    # Test 2: Insertion at end
    ll.insert_at_end(20)       # [5, 10, 20]
    ll.display()

    # Test 3: Insertion in middle
    ll.insert_at_position(15, 2) # [5, 10, 15, 20]
    ll.display()

    # Test 4: Out of bounds
    ll.insert_at_position(100, 10)
