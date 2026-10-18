# Linked List Deletion in Python

"""
Goal: Implement deletion operations for a Singly Linked List.
Algorithm: Bypass the target node by updating the 'next' pointer of the previous node.
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

    def delete_at_beginning(self):
        """Remove the first node. Time: O(1)"""
        if not self.head:
            print("❌ List is empty! Nothing to delete.")
            return None

        popped_data = self.head.data
        self.head = self.head.next
        print(f"Deleted {popped_data} from the beginning.")
        return popped_data

    def delete_at_end(self):
        """Remove the last node. Time: O(n)"""
        if not self.head:
            print("❌ List is empty! Nothing to delete.")
            return None

        # Special case: Only one node in the list
        if not self.head.next:
            popped_data = self.head.data
            self.head = None
            print(f"Deleted {popped_data} (the only node).")
            return popped_data

        # Traverse to the second-to-last node
        current = self.head
        while current.next.next:
            current = current.next

        popped_data = current.next.data
        current.next = None
        print(f"Deleted {popped_data} from the end.")
        return popped_data

    def delete_by_value(self, value):
        """Remove the first node that matches the given value. Time: O(n)"""
        if not self.head:
            print("❌ List is empty!")
            return False

        # If the head itself holds the value
        if self.head.data == value:
            self.delete_at_beginning()
            return True

        current = self.head
        while current.next:
            if current.next.data == value:
                # Bypass the target node
                current.next = current.next.next
                print(f"Deleted node with value {value}.")
                return True
            current = current.next

        print(f"❌ Value {value} not found in the list.")
        return False

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
    ll.display() # [10, 20, 30, 40, 50]

    # Test 1: Delete at beginning
    ll.delete_at_beginning()
    ll.display() # [20, 30, 40, 50]

    # Test 2: Delete at end
    ll.delete_at_end()
    ll.display() # [20, 30, 40]

    # Test 3: Delete by value
    ll.delete_by_value(30)
    ll.display() # [20, 40]

    # Test 4: Delete non-existent value
    ll.delete_by_value(100)
