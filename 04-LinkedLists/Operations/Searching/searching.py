# Linked List Searching in Python

"""
Goal: Implement search operations for a Singly Linked List.
Algorithm: Use Linear Search to traverse the list and find a target value or index.
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

    def search_by_value(self, target):
        """
        Search for a node containing the target value.
        Returns the index (0-indexed) if found, otherwise -1.
        Time: O(n)
        """
        current = self.head
        index = 0

        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1

        return -1

    def search_by_position(self, position):
        """
        Find the data at a specific index.
        Returns the data if the position exists, otherwise None.
        Time: O(n)
        """
        if position < 0:
            return None

        current = self.head
        count = 0

        while current:
            if count == position:
                return current.data
            current = current.next
            count += 1

        return None

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

    print("Current List:")
    ll.display()

    # Test 1: Search for value that exists
    target_val = 30
    res_val = ll.search_by_value(target_val)
    print(f"Searching for value {target_val}: Found at index {res_val}")

    # Test 2: Search for value that does not exist
    target_missing = 100
    res_missing = ll.search_by_value(target_missing)
    print(f"Searching for value {target_missing}: {'Not found' if res_missing == -1 else res_missing}")

    # Test 3: Search by position
    pos = 2
    res_pos = ll.search_by_position(pos)
    print(f"Value at position {pos}: {res_pos}")

    # Test 4: Search by position out of bounds
    pos_out = 10
    res_out = ll.search_by_position(pos_out)
    print(f"Value at position {pos_out}: {res_out}")
