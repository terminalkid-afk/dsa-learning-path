# Circular Queue

## 💡 Concept
A **Circular Queue** is an advanced version of a linear queue that solves a major problem: **Memory Wastage**.

In a standard array-based linear queue, once you dequeue an element, that space at the front becomes empty. Even if you have space at the front, you cannot use it to enqueue new elements because the "Rear" pointer only moves forward. Eventually, you reach the end of the array and get a "Queue Overflow" error, even though there are empty slots at the beginning!

A **Circular Queue** solves this by "wrapping around." When the Rear pointer reaches the end of the array, it jumps back to the first index (`0`) if that space has been freed by a dequeue operation.

**Imagine this:** A circular track in a stadium. Runners (data) enter the track and move forward. When the leader leaves the track, a new runner can enter the track and follow the path, eventually looping back to where the first runner started.

### Why do we need Circular Queues?
- **Memory Efficiency**: They reuse empty slots, making them ideal for systems with fixed memory.
- **Buffering**: Used in CPU scheduling, traffic management in networks, and audio/video buffering (where old data is replaced by new data in a loop).

## ⚙️ Visual Logic
Suppose we have a Circular Queue of size `5`.

1. **Enqueue(10, 20, 30, 40, 50)**: Queue is full: `[10, 20, 30, 40, 50]`. Front=0, Rear=4.
2. **Dequeue()**: Removes `10`. Queue: `[_, 20, 30, 40, 50]`. Front=1, Rear=4.
3. **Dequeue()**: Removes `20`. Queue: `[_, _, 30, 40, 50]`. Front=2, Rear=4.
4. **Enqueue(60)**: Rear was at 4 (the end). It wraps around to index 0!
   Queue: `[60, _, 30, 40, 50]`. Front=2, Rear=0.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Enqueue** | $O(1)$ | $O(1)$ |
| **Dequeue** | $O(1)$ | $O(1)$ |

The "wrap around" is handled by a simple modulo operator: `rear = (rear + 1) % size`.

## 💻 Implementation

Check out the [circular_queue.py](./circular_queue.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [GeeksforGeeks: Circular Queue](https://www.geeksforgeeks.org/circular-queue/)
- [LeetCode: Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)
