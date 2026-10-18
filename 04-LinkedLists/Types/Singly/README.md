# Singly Linked List

## 💡 Concept
A **Singly Linked List** is the simplest type of linked list. In this version, each node only has **one pointer**, which points to the **next** node in the sequence. The movement is strictly one-way: from the head towards the tail.

### Structure of a Node:
- **Data**: The value stored in the node.
- **Next**: A reference to the next node. If it is the last node, this pointer is `None`.

**Imagine this:** A one-way street. You can go from house #1 to house #2, and from #2 to #3, but there are no U-turns allowed. If you are at house #3 and realize you forgot something at house #1, you have to go back to the start of the street and walk all the way forward again.

### Key Characteristics:
- **Head**: The starting point of the list. If you lose the head, you lose the entire list.
- **Tail**: The final node whose `next` pointer is `None`.
- **Unidirectional**: You can only traverse in one direction.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Access/Search** | $O(n)$ | Must traverse from the head. |
| **Insertion (Head)** | $O(1)$ | Just update the head pointer. |
| **Insertion (Tail)** | $O(n)$ | Must traverse to the end first. |
| **Deletion (Head)** | $O(1)$ | Move head to `head.next`. |
| **Deletion (Tail)** | $O(n)$ | Must find the node *before* the tail to update its pointer. |

## 💻 Implementation

The core logic for Singly Linked Lists is implemented in the [traversal.py](../Operations/Traversal/traversal.py) and other operation files.

## 🚀 Practice Problems
- [LeetCode: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [LeetCode: Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [GeeksforGeeks: Singly Linked List](https://www.geeksforgeeks.org/singly-linked-list/)
