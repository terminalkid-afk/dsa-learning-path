# Comparing Linked Lists

## 💡 Concept
**Comparing Linked Lists** involves determining if two lists are identical. Two linked lists are considered identical if they have the same number of nodes and every corresponding node contains the same value in the same order.

### The Logic
To compare two lists, we use a simultaneous traversal:
1. Start two pointers, one at the head of List A and one at the head of List B.
2. While both pointers are not `None`:
   - Compare the data in the current nodes.
   - If the data is different, the lists are **not identical**.
   - If the data is the same, move both pointers to their respective `next` nodes.
3. After the loop, check if both pointers reached the end (`None`) at the same time. If one list is longer than the other, they are **not identical**.

**Imagine this:** You and a friend both have a list of shopping items. To see if your lists are exactly the same, you both read the first item. If they match, you both move to the second item. If you reach the end of your lists at the exact same time and every single item matched, the lists are identical.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Linked List Comparison here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Comparison** | $O(\min(n, m))$ | $O(1)$ |

The time complexity is proportional to the length of the shorter list, as the process stops as soon as a mismatch is found or the shorter list ends.

## 💻 Implementation

Check out the [comparison.py](./comparison.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [GeeksforGeeks: Check if two linked lists are identical](https://www.geeksforgeeks.org/check-if-two-linked-lists-are-identical/)
- [LeetCode: Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (A related problem about comparing list structures).
