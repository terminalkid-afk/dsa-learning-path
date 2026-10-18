# Merging Linked Lists

## 💡 Concept
**Merging** two linked lists involves combining them into a single, unified list. The most common and useful form of this is **Merging two Sorted Lists**, where the resulting list must also be sorted.

To achieve this, we use a "Two-Pointer" technique. We compare the head nodes of both lists and pick the smaller one to be the next node in our new merged list. We then move the pointer forward in the list we picked from and repeat the process.

**Imagine this:** Two lines of students sorted by height. You want to merge them into one single line that is also sorted by height. You look at the person at the front of Line A and the person at the front of Line B. Whoever is shorter joins your new line first. You repeat this until one of the lines is empty, then you simply attach the remainder of the other line to the end.

### Why do we need Merging?
- It is the core "Merge" step in the **Merge Sort** algorithm.
- Used in combining sorted data streams or logs from different sources.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Linked List Merging here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Merge** | $O(n + m)$ | $O(1)$ or $O(n+m)$ |

- **Time**: We visit every node in both lists exactly once.
- **Space**: If we rearrange the existing nodes (in-place), it's $O(1)$. If we create a brand new list, it's $O(n+m)$.

## 💻 Implementation

Check out the [merge.py](./merge.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [LeetCode: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [GeeksforGeeks: Merge two sorted linked lists](https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/)
