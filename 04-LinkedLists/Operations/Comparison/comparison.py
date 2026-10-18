# Comparing Linked Lists in Python

"""
Goal: Determine if two singly linked lists are identical.
Algorithm: Parallel traversal of both lists and comparing data at each node.
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

    def display(self):
        """Print the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

def are_identical(head1, head2):
    """
    Compares two linked lists for identity.
    Returns True if they have the same length and same elements in the same order.
    Time: O(min(n, m))
    Space: O(1)
    """
    curr1 = head1
    curr2 = head2

    # Traverse both lists simultaneously
    while curr1 and curr2:
        # If data differs, they are not identical
        if curr1.data != curr2.data:
            return False

        curr1 = curr1.next
        curr2 = curr2.next

    # If both pointers reached None, they are the same length and identical
    return curr1 is None and curr2 is None

# --- Usage Example ---
if __name__ == "__main__":
    # List 1: 10 -> 20 -> 30
    l1 = LinkedList()
    for val in [10, 20, 30]: l1.insert(val)

    # List 2: 10 -> 20 -> 30 (Identical to l1)
    l2 = LinkedList()
    for val in [10, 20, 30]: l2.insert(val)

    # List 3: 10 -> 20 (Shorter)
    l3 = LinkedList()
    for val in [10, 20]: l3.insert(val)

    # List 4: 10 -> 25 -> 30 (Different value)
    l4 = LinkedList()
    for val in [10, 25, 30]: l4.insert(val)

    print("List 1:")
    l1.display()
    print("List 2:")
    l2.display()
    print(f"Are L1 and L2 identical? {are_identical(l1.head, l2.head)}") # Expected: True

    print("\nList 1:")
    l1.display()
    print("List 3:")
    l3.display()
    print(f"Are L1 and L3 identical? {are_identical(l1.head, l3.head)}") # Expected: False

    print("\nList 1:")
    l1.display()
    print("List 4:")
    l4.display()
    print(f"Are L1 and L4 identical? {are_identical(l1.head, l4.head)}") # Expected: False
