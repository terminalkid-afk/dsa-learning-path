# Double Ended Queue (Deque)

## 💡 Concept
A **Double Ended Queue**, commonly called a **Deque** (pronounced "deck"), is a more flexible version of a queue. While a standard queue only allows adding at the back and removing from the front, a Deque allows you to:
- Add elements to the **Front** AND the **Rear**.
- Remove elements from the **Front** AND the **Rear**.

Essentially, a Deque is a hybrid between a **Stack** and a **Queue**. You can use it as a stack (LIFO) or a queue (FIFO) depending on which operations you call.

**Imagine this:** A deck of cards. You can slide a card into the top or the bottom. You can also pull a card off the top or the bottom. You have full control over both ends of the "line."

### Why do we need Deques?
- **Undo/Redo buffers**: Where you might need to add/remove from both ends.
- **Sliding Window Problems**: Extremely useful in competitive programming for finding the maximum/minimum in a sliding window of an array.
- **Palindrome Checking**: You can pop elements from both ends and compare them to see if they match.

## ⚙️ Visual Logic
Let's trace a Deque:

1. **AddRear(10)**: Deque $\rightarrow$ `[10]`
2. **AddFront(20)**: Deque $\rightarrow$ `[20, 10]`
3. **AddRear(30)**: Deque $\rightarrow$ `[20, 10, 30]`
4. **RemoveFront()**: Removes `20`. Deque $\rightarrow$ `[10, 30]`
5. **RemoveRear()**: Removes `30`. Deque $\rightarrow$ `[10]`

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Add Front** | $O(1)$ | $O(1)$ |
| **Add Rear** | $O(1)$ | $O(1)$ |
| **Remove Front** | $O(1)$ | $O(1)$ |
| **Remove Rear** | $O(1)$ | $O(1)$ |

## 💻 Implementation

In Python, the `collections.deque` class is the industry standard for implementing this. Check out the [enqueue_dequeue.py](../Operations/Enqueue-Dequeue/enqueue_dequeue.py) for how `deque` is used.

## 🚀 Practice Problems
- [LeetCode: Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Classic Deque problem!)
- [LeetCode: Palindrome Game](https://leetcode.com/problems/valid-palindrome/)
