# IsEmpty Operation

## 💡 Concept
The **IsEmpty** operation is a safety check that returns a boolean value (`True` or `False`) indicating whether the queue contains any elements.

### Why is it so important?
If you attempt to perform a `Dequeue` or `Peek Front` operation on a queue that has no elements, the program will encounter an error or crash. This is known as **Queue Underflow**.

By checking `IsEmpty()` first, you can ensure your program handles empty states gracefully:
```python
if not queue.is_empty():
    queue.dequeue()
else:
    print("The queue is already empty!")
```

**Imagine this:** You are checking a mailbox. Before you reach in to grab the mail, you look to see if there is actually anything inside. Checking for the presence of mail is exactly what `IsEmpty` does for a queue.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **IsEmpty** | $O(1)$ | $O(1)$ |

The time complexity is constant because the queue typically tracks its current size or maintains a pointer. Checking if that size is `0` takes the same amount of time regardless of the queue's capacity.

## 💻 Implementation

This logic is implemented as a method within the Queue class. See the [enqueue_dequeue.py](../Enqueue-Dequeue/enqueue_dequeue.py) file.

## 🚀 Practice Problems
- [LeetCode: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) (Essential for knowing when to stop popping from a queue during the stack simulation).
