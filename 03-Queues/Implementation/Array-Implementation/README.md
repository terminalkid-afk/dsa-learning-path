# Array-Based Queue Implementation

## 💡 Concept
An **Array-based Queue** implements the FIFO (First-In-First-Out) logic using a fixed-size array. This is the most basic way to build a queue, where elements are added at one end and removed from the other.

In a simple linear array implementation:
- The **Front** pointer tracks the first element to be dequeued.
- The **Rear** pointer tracks the position where the next element will be enqueued.

### The "Drifting" Problem
In a basic linear array queue, as you dequeue elements, the `Front` pointer moves forward. Eventually, the `Rear` pointer reaches the end of the array, and you can no longer add elements—even if there is empty space at the beginning!

**Solution:** This is why **Circular Queues** are preferred over simple linear array queues.

**Imagine this:** A row of parking spots. Cars enter at spot 0 and leave from spot 0. As cars leave, the "first available" spot moves forward. If we don't "wrap around" back to spot 0, we'll eventually run out of parking spots even if the first few are empty.

### Pros and Cons
| Pros | Cons |
| :--- | :--- |
| **Speed**: $O(1)$ for Enqueue and Dequeue (if using a circular buffer). | **Fixed Size**: You must define the capacity upfront. |
| **Memory**: Very efficient contiguous memory access. | **Overhead**: Managing two pointers (`front` and `rear`) adds slight complexity. |

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Enqueue** | $O(1)$ | $O(1)$ |
| **Dequeue** | $O(1)$ | $O(1)$ |
| **Peek** | $O(1)$ | $O(1)$ |

**Overall Space Complexity**: $O(n)$ to store $n$ elements.

## 💻 Implementation

Check out the [circular_queue.py](../Types/Circular/circular_queue.py) file for the most efficient array-based implementation.

## 🚀 Practice Problems
- [GeeksforGeeks: Queue using Array](https://www.geeksforgeeks.org/queue-implementation-using-array/)
- [LeetCode: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
