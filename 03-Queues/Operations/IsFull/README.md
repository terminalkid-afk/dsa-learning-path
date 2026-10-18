# IsFull Operation

## 💡 Concept
The **IsFull** operation checks whether a queue has reached its maximum predefined capacity.

### When is this used?
In high-level languages like Python, lists and `deques` are dynamic, meaning they grow as you add elements. Therefore, a queue is rarely "full" until the computer's RAM is exhausted.

However, **IsFull** is critical in:
- **Low-level languages (C/C++)**: Where queues are often implemented using fixed-size arrays.
- **Embedded Systems**: Where memory is strictly limited, and you must prevent a queue from consuming too much memory.
- **Hardware Buffers**: In networking or OS kernels, where buffers have a hard limit on how many packets/requests they can hold.

If you try to `Enqueue` an element into a queue that `IsFull` returns `True` for, you encounter a **Queue Overflow**.

**Imagine this:** A waiting room with exactly 10 chairs. Once all 10 chairs are taken, the room is "Full". Any new person arriving cannot enter until someone else leaves (is dequeued).

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **IsFull** | $O(1)$ | $O(1)$ |

The time complexity is constant because it simply compares the current number of elements with the maximum capacity.

## 💻 Implementation

In our Python implementation, we can simulate this by adding a `max_size` attribute to our Queue class.

```python
def is_full(self):
    return len(self.items) == self.max_size
```

See the implementation in the [Implementation Section](../Implementation/Array-Implementation/README.md).

## 🚀 Practice Problems
- [GeeksforGeeks: Queue Overflow and Underflow](https://www.geeksforgeeks.org/queue-overflow-and-underflow/)
