# Enqueue & Dequeue Operations

## 💡 Concept
The primary purpose of a queue is to manage data in a **First-In-First-Out (FIFO)** manner. This is achieved through two main operations: **Enqueue** and **Dequeue**.

### 1. Enqueue
**Enqueue** means adding a new element to the **Rear** (back) of the queue. If the queue has a fixed size and is already full, attempting to enqueue a new element results in a **Queue Overflow**.

### 2. Dequeue
**Dequeue** means removing the element from the **Front** (head) of the queue. If you try to dequeue from an empty queue, it results in a **Queue Underflow**.

**Imagine this:** A checkout line at a grocery store. 
- When a new customer arrives and joins the end of the line, they are being **Enqueued**.
- When the cashier finishes helping the person at the front and they leave, that person is being **Dequeued**.

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Queue Operations here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Let's trace a queue:

1. **Enqueue(10)**: Queue $\rightarrow$ `[10]` (Front: 10, Rear: 10)
2. **Enqueue(20)**: Queue $\rightarrow$ `[10, 20]` (Front: 10, Rear: 20)
3. **Enqueue(30)**: Queue $\rightarrow$ `[10, 20, 30]` (Front: 10, Rear: 30)
4. **Dequeue()**: Removes `10`. Queue $\rightarrow$ `[20, 30]` (Front: 20, Rear: 30)
5. **Dequeue()**: Removes `20`. Queue $\rightarrow$ `[30]` (Front: 30, Rear: 30)

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Enqueue** | $O(1)$ | $O(1)$ |
| **Dequeue** | $O(1)$ | $O(1)$ |

Both operations happen instantly at the respective ends of the queue, regardless of the total number of elements.

## 💻 Implementation

Check out the [enqueue_dequeue.py](./enqueue_dequeue.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [LeetCode: Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)
