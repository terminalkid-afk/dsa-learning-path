# Linked List Traversal

## 💡 Concept
**Traversal** is the process of visiting every node in a linked list exactly once. Since linked lists are not stored in contiguous memory (like arrays), you cannot jump to a specific index. You must start at the **Head** and follow the `next` pointers until you reach the end.

**Imagine this:** A treasure hunt. You find the first clue. That clue gives you the map to the second clue. You go to the second clue, which tells you where the third one is. You cannot skip to the fifth clue because you don't know where it is until you've found the fourth.

### How it works:
**📺 See it in Action**: [Visualize Linked List Traversal here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

1. Start a temporary pointer (`current`) at the **Head**.
2. While `current` is not `None`:
   - Process the data in the `current` node (e.g., print it).
   - Move the `current` pointer to the next node: `current = current.next`.
3. When `current` becomes `None`, you have reached the end of the list.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Traversal** | $O(n)$ | $O(1)$ |

Since you must visit every single node to finish the traversal, the time taken grows linearly with the number of elements.

## 💻 Implementation

Check out the [traversal.py](./traversal.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Print Linked List](https://www.geeksforgeeks.org/print-a-linked-list/)
- [LeetCode: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Uses a special traversal called "Fast and Slow Pointers").
