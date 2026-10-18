# Reverse Linked List in Python

"""
Goal: Reverse a singly linked list so that the tail becomes the head.
Algorithm: Iteratively flip the 'next' pointers of every node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Helper to add elements to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        """
        Reverses the linked list in-place.
        Time: O(n)
        Space: O(1)
        """
        prev = None
        current = self.head

        while current:
            # 1. Store the next node before we overwrite the current pointer
            next_node = current.next

            # 2. Flip the pointer: current node now points to the previous one
            current.next = prev

            # 3. Move pointers forward for the next iteration
            prev = current
            current = next_node

        # 4. Update the head to the last non-null node we processed
        self.head = prev

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
    for val in [10, 20, 30, 40, 50]:
        ll.insert(val)

    print("Original List:")
    ll.display() # 10 -> 20 -> 30 -> 40 -> 50 -> None

    print("\nReversing the list...")
    ll.reverse()

    print("Reversed List:")
    ll.display() # 50 -> 40 -> 30 -> 20 -> 10 -> None
