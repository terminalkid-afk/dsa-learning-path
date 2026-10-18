# Linked List-Based Queue Implementation

## 💡 Concept
A **Linked List-based Queue** implements the FIFO (First-In-First-Out) logic using a singly linked list. Unlike an array, a linked list does not have a fixed size, allowing the queue to grow and shrink dynamically as needed.

To keep both Enqueue and Dequeue operations efficient ($O(1)$), we maintain **two pointers**:
1. **Front**: Points to the first node of the list (used for Dequeue).
2. **Rear**: Points to the last node of the list (used for Enqueue).

### How it works:
- **Enqueue**: We create a new node and attach it to the `next` pointer of the current `Rear` node. Then, we update the `Rear` pointer to this new node.
- **Dequeue**: We simply remove the `Front` node and move the `Front` pointer to the next node in the list.

**Imagine this:** A train. 
- To **Enqueue**, a new train car is attached to the very back of the train.
- To **Dequeue**, the locomotive at the very front is detached and leaves the station.
- The train can grow as long as there are more cars available, and you always know exactly where the front and back are.

### Pros and Cons
| Pros | Cons |
| :--- | :--- |
| **Dynamic Size**: No capacity limits; it only stops when the system runs out of memory. | **Extra Memory**: Each element requires extra space for the `next` pointer. |
| **Constant Time**: No need for the "wrap-around" logic required by circular arrays. | **Cache Locality**: Nodes are scattered in memory, making it slightly slower than arrays for the CPU to access. |

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Enqueue** | $O(1)$ | $O(1)$ |
| **Dequeue** | $O(1)$ | $O(1)$ |
| **Peek** | $O(1)$ | $O(1)$ |

**Overall Space Complexity**: $O(n)$ to store $n$ nodes.

## 💻 Implementation

Check out the [queue_ll.py](./queue_ll.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- [GeeksforGeeks: Queue using Linked List](https://www.geeksforgeeks.org/queue-implementation-using-linked-list/)
