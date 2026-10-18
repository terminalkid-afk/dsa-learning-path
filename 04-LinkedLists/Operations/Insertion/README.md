# Linked List Insertion

## 💡 Concept
**Insertion** is the process of adding a new node to a linked list. Unlike arrays, where inserting in the middle requires shifting all subsequent elements, inserting into a linked list only requires updating a few pointers.

Depending on where you want to add the node, the logic changes slightly:

### 1. Insertion at the Beginning (Head)
This is the fastest operation. You create a new node, point it to the current head, and then update the head pointer to be this new node.

### 2. Insertion at the End (Tail)
You must first traverse the entire list to find the last node (where `next` is `None`), then point that last node's `next` to your new node.

### 3. Insertion in the Middle (At a specific position)
You traverse to the node just *before* the desired position. You point the new node to the next node, and the previous node to the new node.

**Imagine this:** You are adding a new link to a physical chain.
- **At the start**: You just attach a new link to the front.
- **At the end**: You walk to the end of the chain and attach a new link.
- **In the middle**: You unclip two existing links, insert your new link between them, and clip it to both.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Linked List Insertion here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Position | Time Complexity | Why? |
| :--- | :--- | :--- |
| **At Head** | $O(1)$ | No traversal needed. |
| **At Tail** | $O(n)$ | Must traverse to the end (unless a Tail pointer is kept). |
| **At Middle**| $O(n)$ | Must traverse to the insertion point. |

**Space Complexity:** $O(1)$ as we only create one new node.

## 💻 Implementation

Check out the [insertion.py](./insertion.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Design Linked List](https://leetcode.com/problems/design-linked-list/)
- [GeeksforGeeks: Insertion in a Linked List](https://www.geeksforgeeks.org/insertion-in-a-linked-list/)
