# Single Ended Queue

## 💡 Concept
A **Single Ended Queue** is the standard, classic queue we've discussed. It strictly follows the **FIFO (First-In-First-Out)** principle.

In a single ended queue:
- Insertion happens **only at one end** (the Rear).
- Deletion happens **only at the other end** (the Front).

This is a "one-way street" for data. Once an element is enqueued, it must wait for every element in front of it to be dequeued before it can leave.

**Imagine this:** A simple tunnel. Cars enter from one side (Rear) and leave from the other (Front). No car can turn around or jump the line; they must exit in the exact order they entered.

### Why do we use it?
- It's the simplest form of a queue.
- Perfect for tasks that must be handled in strict arrival order (e.g., a printer queue).

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Enqueue** | $O(1)$ | $O(1)$ |
| **Dequeue** | $O(1)$ | $O(1)$ |

## 💻 Implementation

This is the default implementation used in our core queue class. See the [enqueue_dequeue.py](../Operations/Enqueue-Dequeue/enqueue_dequeue.py) file.

## 🚀 Practice Problems
- [LeetCode: First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (Can be solved using a queue to keep track of order).
