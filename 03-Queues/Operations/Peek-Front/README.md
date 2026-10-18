# Peek Front Operation

## 💡 Concept
The **Peek Front** operation (also known as `Front`) allows you to look at the element currently at the front of the queue without removing it.

Unlike `Dequeue`, which removes the element, `Peek` is a non-destructive operation. It is extremely useful when you need to inspect the next item to be processed before actually deciding to process it.

**Imagine this:** You are in a line at a coffee shop. The barista looks at the first person in line to see what their order is before calling them forward. The barista is "peeking" at the front of the queue.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Peek Front** | $O(1)$ | $O(1)$ |

Since the queue maintains a reference to the front element, accessing it takes constant time regardless of the queue's size.

## 💻 Implementation

This logic is integrated into the main Queue class. See the [enqueue_dequeue.py](../Enqueue-Dequeue/enqueue_dequeue.py) file.

## 🚀 Practice Problems
- [LeetCode: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) (You'll need to peek at the last element added to simulate a stack top).
