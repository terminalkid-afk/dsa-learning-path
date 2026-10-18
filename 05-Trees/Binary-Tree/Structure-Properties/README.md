# Binary Tree: Structure & Properties

## 💡 Concept
A **Binary Tree** is a tree data structure in which each node has **at most two children**, referred to as the **left child** and the **right child**.

This simple constraint—limiting children to two—is what makes binary trees so powerful for computation, as it allows us to split the search space in half at every step.

### Core Properties
1. **Root**: The topmost node.
2. **Leaf Node**: A node with no children.
3. **Internal Node**: A node with at least one child.
4. **Subtree**: Any node can be viewed as the root of its own smaller binary tree.

### Common Types of Binary Trees
- **Full Binary Tree**: Every node has either 0 or 2 children. No node has only one child.
- **Complete Binary Tree**: All levels are completely filled except possibly the last level, which is filled from left to right.
- **Perfect Binary Tree**: All internal nodes have two children, and all leaf nodes are at the same level.
- **Balanced Binary Tree**: The height of the left and right subtrees of every node differs by no more than 1. (Critical for performance!)
- **Degenerate (Skewed) Tree**: Every node has only one child. It effectively becomes a Linked List, and performance drops from $O(\log n)$ to $O(n)$.

**Imagine this:** A decision flow chart. At every step, you have a "Yes" or "No" choice. "Yes" takes you to the left branch, and "No" takes you to the right branch. By the time you reach a leaf node, you've arrived at a final decision.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Binary Trees here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Operation | Average Case | Worst Case (Skewed) |
| :--- | :--- | :--- |
| **Search** | $O(\log n)$ | $O(n)$ |
| **Insertion** | $O(\log n)$ | $O(n)$ |
| **Deletion** | $O(\log n)$ | $O(n)$ |

**Space Complexity:** $O(n)$ to store $n$ nodes.

## 💻 Implementation

The basic structure of a Binary Tree node is:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Detailed implementation can be found in the [Binary Search Tree section](../Binary-Search-Tree/Searching/README.md).

## 🚀 Practice Problems
- [LeetCode: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [GeeksforGeeks: Binary Tree Data Structure](https://www.geeksforgeeks.org/binary-tree-data-structure/)
