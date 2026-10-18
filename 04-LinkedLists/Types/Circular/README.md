# Circular Linked List

## 💡 Concept
A **Circular Linked List** is a variation of a linked list where the last node does not point to `None`. Instead, the **last node points back to the first node**, creating a closed loop.

This can be either a Singly Circular Linked List (last node points to head) or a Doubly Circular Linked List (last node points to head, and head points to last node).

**Imagine this:** A game of "Pass the Parcel." The music starts, and the parcel goes around the circle. The last person in the circle passes the parcel back to the first person, and the loop continues indefinitely until the music stops. There is no "end" to the line.

### Why do we need Circular Linked Lists?
- **Continuous Loop**: Useful for applications that need to cycle through a list of items repeatedly (e.g., switching between open windows in an OS using `Alt+Tab`).
- **Efficient Tail Access**: In a singly circular list, if you keep a pointer to the **Tail**, you can access both the Tail AND the Head (Tail.next) in $O(1)$ time.
- **Round Robin Scheduling**: Used by Operating Systems to give each process a small slice of CPU time in a repeating cycle.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Traversal** | $O(n)$ | Must stop when you reach the starting node again. |
| **Insert (Head)** | $O(1)$ | If tail pointer is kept, just update tail.next. |
| **Insert (Tail)** | $O(1)$ | If tail pointer is kept, add after tail and update tail. |
| **Search** | $O(n)$ | Must traverse the loop. |

**Space Complexity:** $O(n)$ for storing $n$ nodes.

## 💻 Implementation

Check out the [traversal.py](../Operations/Traversal/traversal.py) and operation files for logic on handling circular pointers.

## 🚀 Practice Problems
- [GeeksforGeeks: Circular Linked List](https://www.geeksforgeeks.org/circular-linked-list/)
- [LeetCode: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (The most famous problem involving circular references!)
