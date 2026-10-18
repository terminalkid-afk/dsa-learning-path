# Push & Pop in Python

"""
Goal: Implement basic Stack operations (Push and Pop).
Algorithm: Using a Python list as the underlying storage.
"""

class Stack:
    def __init__(self):
        # We use a list to store our stack elements.
        # The end of the list will represent the 'top' of the stack.
        self.items = []

    def push(self, item):
        """Add an element to the top of the stack."""
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Remove and return the element from the top of the stack."""
        if self.is_empty():
            print("❌ Stack Underflow! Cannot pop from an empty stack.")
            return None

        item = self.items.pop()
        print(f"Popped {item} from the stack.")
        return item

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def peek(self):
        """Look at the top element without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the stack for easy printing."""
        return f"Stack (bottom to top): {self.items}"

# --- Usage Example ---
if __name__ == "__main__":
    # Create a new stack instance
    my_stack = Stack()

    # Test Push operations
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    print(my_stack) # Expected: [10, 20, 30]

    # Test Peek
    print(f"Top element is: {my_stack.peek()}") # Expected: 30

    # Test Pop operations
    my_stack.pop() # Pops 30
    my_stack.pop() # Pops 20
    print(my_stack) # Expected: [10]

    # Test popping until empty
    my_stack.pop() # Pops 10
    my_stack.pop() # Should trigger Stack Underflow
