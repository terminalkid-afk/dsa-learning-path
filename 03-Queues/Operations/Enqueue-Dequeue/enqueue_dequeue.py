# Enqueue & Dequeue in Python

"""
Goal: Implement basic Queue operations (Enqueue and Dequeue).
Algorithm: Using a Python list (deque) for efficient O(1) pops from the front.
"""
from collections import deque

class Queue:
    def __init__(self):
        # We use collections.deque because popping from the front of a
        # standard Python list is O(n). deque allows O(1) for both ends.
        self.items = deque()

    def enqueue(self, item):
        """Add an element to the rear of the queue."""
        self.items.append(item)
        print(f"Enqueued {item} to the rear.")

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            print("❌ Queue Underflow! Cannot dequeue from an empty queue.")
            return None

        item = self.items.popleft()
        print(f"Dequeued {item} from the front.")
        return item

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def peek(self):
        """Look at the front element without removing it."""
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the queue."""
        return f"Queue (front to rear): {list(self.items)}"

# --- Usage Example ---
if __name__ == "__main__":
    # Create a new queue instance
    my_queue = Queue()

    # Test Enqueue operations
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    print(my_queue) # Expected: [10, 20, 30]

    # Test Peek
    print(f"Front element is: {my_queue.peek()}") # Expected: 10

    # Test Dequeue operations
    my_queue.dequeue() # Dequeues 10
    my_queue.dequeue() # Dequeues 20
    print(my_queue) # Expected: [30]

    # Test dequeuing until empty
    my_queue.dequeue() # Dequeues 30
    my_queue.dequeue() # Should trigger Queue Underflow
