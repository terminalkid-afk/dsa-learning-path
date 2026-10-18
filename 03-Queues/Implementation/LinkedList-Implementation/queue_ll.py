# Linked List-Based Queue in Python

"""
Goal: Implement a Queue using a Singly Linked List.
Algorithm: Maintain both 'front' and 'rear' pointers to ensure O(1)
          enqueue and dequeue operations.
"""

class Node:
    """A single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        # 'front' is where we dequeue (remove)
        self.front = None
        # 'rear' is where we enqueue (add)
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        """Add an element to the rear of the queue."""
        new_node = Node(item)

        # If the queue is empty, both front and rear are the new node
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            # Link the current rear to the new node and update rear
            self.rear.next = new_node
            self.rear = new_node

        self._size += 1
        print(f"Enqueued {item} to the rear.")

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            print("❌ Queue Underflow! Cannot dequeue from an empty queue.")
            return None

        # Store the data from the front node
        dequeued_item = self.front.data
        # Move the front pointer to the next node
        self.front = self.front.next

        # If the queue becomes empty after dequeue, reset rear to None
        if self.front is None:
            self.rear = None

        self._size -= 1
        print(f"Dequeued {dequeued_item} from the front.")
        return dequeued_item

    def peek(self):
        """Look at the front element without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def size(self):
        """Return the current number of elements in the queue."""
        return self._size

    def __str__(self):
        """Return a string representation of the queue."""
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"

# --- Usage Example ---
if __name__ == "__main__":
    # Create a new linked queue
    my_queue = LinkedQueue()

    # Test Enqueue operations
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    print(f"Current Queue: {my_queue}") # Expected: 10 -> 20 -> 30 -> None

    # Test Peek
    print(f"Front element is: {my_queue.peek()}") # Expected: 10

    # Test Dequeue operations
    my_queue.dequeue() # Dequeues 10
    my_queue.dequeue() # Dequeues 20
    print(f"Current Queue: {my_queue}") # Expected: 30 -> None

    # Test dequeuing until empty
    my_queue.dequeue() # Dequeues 30
    my_queue.dequeue() # Should trigger Queue Underflow
