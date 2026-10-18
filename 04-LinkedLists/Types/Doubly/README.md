# Doubly Linked List

## 💡 Concept
A **Doubly Linked List (DLL)** is a more advanced version of a linked list where each node has **two pointers** instead of one:
1. **Next**: Points to the next node in the sequence.
2. **Prev**: Points to the previous node in the sequence.

This allows for **bidirectional traversal**, meaning you can move both forward (towards the tail) and backward (towards the head).

**Imagine this:** A train where every car is connected to the one in front and the one behind. If you are in the middle car, you can walk forward to the engine or backward to the caboose. You are never "stuck" moving in only one direction.

### Why do we need Doubly Linked Lists?
- **Easier Deletions**: If you have a pointer to a node, you can delete it in $O(1)$ time because you already know who the previous node is. In a singly linked list, you'd have to traverse from the head to find the previous node.
- **Reverse Traversal**: You can easily iterate through the list backwards.
- **More Flexible**: Useful for implementing complex structures like Deques (Double-Ended Queues).

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Access/Search** | $O(n)$ | Still must traverse from one of the ends. |
| **Insert (Head/Tail)** | $O(1)$ | Just update pointers at either end. |
| **Delete (Node)** | $O(1)$ | If the node pointer is known, we can link `prev` and `next` directly. |
| **Reverse Traversal**| $O(n)$ | Move from Tail $\rightarrow$ Head using `prev` pointers. |

**Space Complexity:** $O(n)$ but uses more memory per node than a singly linked list because of the extra `prev` pointer.

## 💻 Implementation

The logic for DLLs is integrated into the [traversal.py](../Operations/Traversal/traversal.py) and operation files.

## 🚀 Practice Problems
- [LeetCode: Design Browser History](https://leetcode.com/problems/design-browser-history/) (Perfect use case for DLL!)
- [GeeksforGeeks: Doubly Linked List](https://www.geeksforgeeks.org/doubly-linked-list/)
