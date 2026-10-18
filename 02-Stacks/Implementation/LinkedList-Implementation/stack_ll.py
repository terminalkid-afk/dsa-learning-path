# Linked List-Based Stack in Python

"""
Goal: Implement a Stack using a Singly Linked List.
Algorithm: Every Push adds a node to the head, and every Pop removes the head.
"""

class Node:
    """A single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        # The 'top' pointer always points to the head of the linked list
        self.top = None
        self._size = 0

    def push(self, item):
        """Add an element to the top of the stack."""
        new_node = Node(item)
        # The new node points to the current top
        new_node.next = self.top
        # The new node becomes the new top
        self.top = new_node
        self._size += 1
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Remove and return the element from the top of the stack."""
        if self.is_empty():
            print("❌ Stack Underflow! Cannot pop from an empty stack.")
            return None

        # Store the data to return
        popped_item = self.top.data
        # Move the top pointer to the next node in the list
        self.top = self.top.next
        self._size -= 1
        print(f"Popped {popped_item} from the stack.")
        return popped_item

    def peek(self):
        """Look at the top element without removing it."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def size(self):
        """Return the current number of elements in the stack."""
        return self._size

    def __str__(self):
        """Return a string representation of the stack."""
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None (Bottom)"

# --- Usage Example ---
if __name__ == "__main__":
    # Create a new linked stack
    my_stack = LinkedStack()

    # Test Push operations
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    print(f"Current Stack: {my_stack}") # Expected: 30 -> 20 -> 10 -> None

    # Test Peek
    print(f"Top element is: {my_stack.peek()}") # Expected: 30

    # Test Pop operations
    my_stack.pop() # Pops 30
    my_stack.pop() # Pops 20
    print(f"Current Stack: {my_stack}") # Expected: 10 -> None

    # Test popping until empty
    my_stack.pop() # Pops 10
    my_stack.pop() # Should trigger Stack Underflow
