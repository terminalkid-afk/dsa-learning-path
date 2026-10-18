# Linked List-Based Stack Implementation

## 💡 Concept
A **Linked List-based Stack** implements the stack logic using a singly linked list. Unlike an array, where elements are stored in a contiguous block of memory, a linked list stores elements in separate "nodes" that point to the next element.

In this implementation:
- Each node contains the **data** and a **pointer (next)** to the node below it.
- The **top** of the stack is simply the head of the linked list.

### How it works:
- **Push**: We create a new node and make it the new head of the list. The new node's `next` pointer points to the previous head.
- **Pop**: We remove the head node and update the head pointer to the next node in the list.
- **Peek**: We simply return the data stored in the head node.

**Imagine this:** A chain of people holding hands. 
- To **Push**, a new person joins the front of the line and holds the hand of the person who was previously first.
- To **Pop**, the person at the front of the line simply lets go and leaves. The person they were holding onto becomes the new leader.

### Pros and Cons
| Pros | Cons |
| :--- | :--- |
| **Dynamic Size**: No need to define a capacity upfront. It grows as long as there is system memory. | **Extra Memory**: Each element requires extra space to store the pointer to the next node. |
| **No Resizing Cost**: Pushing an element always takes $O(1)$ time; no expensive array copying. | **Slower Access**: While top operations are fast, you cannot access elements by index like in an array. |

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Push** | $O(1)$ | $O(1)$ |
| **Pop** | $O(1)$ | $O(1)$ |
| **Peek** | $O(1)$ | $O(1)$ |

**Overall Space Complexity**: $O(n)$ to store $n$ nodes.

## 💻 Implementation

Check out the [stack_ll.py](./stack_ll.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [GeeksforGeeks: Stack using Linked List](https://www.geeksforgeeks.org/stack-using-linked-list/)
