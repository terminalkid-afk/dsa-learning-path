# Circular Queue in Python

"""
Goal: Implement a Circular Queue using a fixed-size array.
Algorithm: Use the modulo operator (%) to wrap the rear and front pointers
          around the array when they reach the end.
"""

class CircularQueue:
    def __init__(self, k):
        """
        Initialize the queue with a fixed capacity k.
        """
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enqueue(self, value):
        """
        Insert an element into the circular queue.
        Returns True if the operation is successful.
        """
        if self.is_full():
            print(f"❌ Queue Overflow! Cannot enqueue {value}.")
            return False

        # If queue is empty, initialize head to 0
        if self.head == -1:
            self.head = 0

        # Move tail forward circularly: (tail + 1) % capacity
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        print(f"Enqueued {value} at index {self.tail}.")
        return True

    def dequeue(self):
        """
        Remove an element from the circular queue.
        Returns the removed element or None if empty.
        """
        if self.is_empty():
            print("❌ Queue Underflow! Cannot dequeue.")
            return None

        item = self.queue[self.head]
        self.queue[self.head] = None # Clear for visualization

        # If there was only one element, reset the queue to empty state
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            # Move head forward circularly: (head + 1) % capacity
            self.head = (self.head + 1) % self.k

        print(f"Dequeued {item}.")
        return item

    def peek(self):
        """Get the front element."""
        if self.is_empty():
            return None
        return self.queue[self.head]

    def is_empty(self):
        """Check if the queue is empty."""
        return self.head == -1

    def is_full(self):
        """Check if the queue is full."""
        return (self.tail + 1) % self.k == self.head

    def __str__(self):
        """Return a string representing the current state of the queue."""
        return f"Queue: {self.queue} | Head: {self.head} | Tail: {self.tail}"

# --- Usage Example ---
if __name__ == "__main__":
    # Create a circular queue of capacity 5
    cq = CircularQueue(5)

    # 1. Fill the queue
    for i in [10, 20, 30, 40, 50]:
        cq.enqueue(i)
    print(cq) # Expected: [10, 20, 30, 40, 50]

    # 2. Test Overflow
    cq.enqueue(60) # Should trigger Overflow

    # 3. Dequeue some elements to create space at the front
    cq.dequeue() # Removes 10
    cq.dequeue() # Removes 20
    print(cq) # Expected: [None, None, 30, 40, 50]

    # 4. Test Circularity: Enqueue again to see wrap-around
    cq.enqueue(60)
    cq.enqueue(70)
    print(cq) # Expected: [60, 70, 30, 40, 50]

    # 5. Final check
    print(f"Front element: {cq.peek()}") # Expected: 30
