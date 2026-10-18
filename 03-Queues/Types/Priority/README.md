# Priority Queue

## 💡 Concept
A **Priority Queue** is a special type of queue where every element has a "priority" associated with it. In a standard queue, the element that arrives first is served first. In a Priority Queue, the element with the **highest priority** is served first, regardless of when it arrived.

If two elements have the same priority, they are typically served according to their order in the queue (FIFO).

**Imagine this:** An Emergency Room (ER) in a hospital.
- Patient A arrives at 10:00 AM with a sore throat.
- Patient B arrives at 10:05 AM with a broken arm.
- Patient C arrives at 10:10 AM with a heart attack.

Even though Patient A arrived first, Patient C has the **highest priority** (life-threatening) and will be treated first. Patient B follows, and finally, Patient A.

### Why do we need Priority Queues?
- **Operating Systems**: Scheduling high-priority system tasks over background tasks.
- **Dijkstra's Algorithm**: Used to find the shortest path in a graph by always expanding the node with the smallest distance.
- **Huffman Coding**: Used in data compression to build a tree based on the frequency of characters.

## ⚙️ Visual Logic
Suppose we have a Priority Queue where **smaller numbers = higher priority**.

1. **Enqueue(10, priority=2)**: Queue $\rightarrow$ `[(10, 2)]`
2. **Enqueue(20, priority=1)**: `20` has higher priority than `10`. Queue $\rightarrow$ `[(20, 1), (10, 2)]`
3. **Enqueue(30, priority=3)**: `30` has lower priority than both. Queue $\rightarrow$ `[(20, 1), (10, 2), (30, 3)]`
4. **Dequeue()**: Removes `20` because it has the highest priority (priority 1).

## ⏱️ Complexity Analysis
The complexity depends on the implementation:

| Implementation | Enqueue | Dequeue | Peek |
| :--- | :--- | :--- | :--- |
| **Unsorted Array** | $O(1)$ | $O(n)$ | $O(n)$ |
| **Sorted Array** | $O(n)$ | $O(1)$ | $O(1)$ |
| **Binary Heap** | $O(\log n)$ | $O(\log n)$ | $O(1)$ |

**Binary Heaps** are the most efficient way to implement Priority Queues and are the standard choice for production systems.

## 💻 Implementation

Check out the [priority_queue.py](./priority_queue.py) file for a clean Python implementation using the `heapq` module.

## 🚀 Practice Problems
- [LeetCode: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [LeetCode: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
