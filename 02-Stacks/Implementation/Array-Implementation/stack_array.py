# Array-Based Stack in Python

"""
Goal: Implement a Stack using a fixed-size array simulation.
Algorithm: Use a Python list but enforce a maximum capacity to simulate
          how stacks work in low-level languages like C or Java.
"""

class ArrayStack:
    def __init__(self, capacity=10):
        # Define the maximum capacity of the stack
        self.capacity = capacity
        # Initialize the stack as a list with None values to simulate a fixed-size array
        self.stack = [None] * capacity
        # 'top' points to the index of the last added element
        self.top = -1

    def push(self, item):
        """Add an element to the top of the stack."""
        if self.is_full():
            print(f"❌ Stack Overflow! Cannot push {item}. Capacity {self.capacity} reached.")
            return False

        self.top += 1
        self.stack[self.top] = item
        print(f"Pushed {item} onto the stack.")
        return True

    def pop(self):
        """Remove and return the element from the top of the stack."""
        if self.is_empty():
            print("❌ Stack Underflow! Cannot pop from an empty stack.")
            return None

        item = self.stack[self.top]
        self.stack[self.top] = None  # Clear the slot
        self.top -= 1
        print(f"Popped {item} from the stack.")
        return item

    def peek(self):
        """Look at the top element without removing it."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[self.top]

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top == -1

    def is_full(self):
        """Check if the stack is full."""
        return self.top == self.capacity - 1

    def __str__(self):
        """Return a string representation of the current stack state."""
        # Only return the parts of the array that are actually filled
        return f"Stack: {self.stack[:self.top + 1]} | Top Index: {self.top}"

# --- Usage Example ---
if __name__ == "__main__":
    # Create a stack with a small capacity to test overflow
    my_stack = ArrayStack(capacity=3)

    # Test Push operations
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    print(my_stack) # Expected: [10, 20, 30]

    # Test Stack Overflow
    my_stack.push(40) # Should trigger Overflow

    # Test Peek
    print(f"Top element is: {my_stack.peek()}") # Expected: 30

    # Test Pop operations
    my_stack.pop() # Pops 30
    print(my_stack) # Expected: [10, 20]

    # Test popping until empty
    my_stack.pop() # Pops 20
    my_stack.pop() # Pops 10
    my_stack.pop() # Should trigger Underflow
