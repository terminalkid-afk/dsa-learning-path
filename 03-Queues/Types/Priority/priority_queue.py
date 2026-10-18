# Priority Queue in Python

"""
Goal: Implement a Priority Queue.
Algorithm: Use a Binary Heap via Python's 'heapq' module for O(log n) efficiency.
"""
import heapq

class PriorityQueue:
    def __init__(self):
        # Python's heapq implements a MIN-HEAP by default.
        # This means the smallest number always has the highest priority.
        self.elements = []

    def enqueue(self, item, priority):
        """
        Add an item with a given priority.
        Lower priority number = Higher priority.
        """
        # heapq.heappush stores tuples; it sorts by the first element of the tuple.
        heapq.heappush(self.elements, (priority, item))
        print(f"Enqueued '{item}' with priority {priority}.")

    def dequeue(self):
        """Remove and return the item with the highest priority (lowest priority number)."""
        if self.is_empty():
            print("❌ Priority Queue Underflow!")
            return None

        # heapq.heappop always removes the smallest element from the heap.
        priority, item = heapq.heappop(self.elements)
        print(f"Dequeued '{item}' (Priority: {priority}).")
        return item

    def peek(self):
        """Return the highest priority item without removing it."""
        if self.is_empty():
            return None
        # The root of the heap [0] is always the smallest element.
        return self.elements[0][1]

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.elements) == 0

    def __str__(self):
        """Return a string representation of the heap."""
        return f"Priority Queue (heap): {self.elements}"

# --- Usage Example ---
if __name__ == "__main__":
    # Create a priority queue
    pq = PriorityQueue()

    # Test Enqueue: Add patients to an ER
    # (Priority: 1 = Critical, 2 = Urgent, 3 = Stable)
    pq.enqueue("Patient A (Sore Throat)", 3)
    pq.enqueue("Patient B (Broken Arm)", 2)
    pq.enqueue("Patient C (Heart Attack)", 1)
    pq.enqueue("Patient D (Flu)", 3)

    print(f"\nCurrent state: {pq}")

    # Test Peek
    print(f"Next patient to treat: {pq.peek()}") # Expected: Patient C

    # Test Dequeue: See who gets treated first
    print("\nStarting Treatment:")
    while not pq.is_empty():
        pq.dequeue()
