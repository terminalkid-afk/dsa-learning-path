# Balancing AVL Trees

## 💡 Concept
A **Binary Search Tree (BST)** can become "skewed" (looking like a linked list) if elements are inserted in sorted order. This ruins the $O(\log n)$ search time and turns it into $O(n)$.

An **AVL Tree** (named after Adelson-Velsky and Landis) is a **self-balancing BST**. It ensures that for every node, the height difference between its left and right subtrees (called the **Balance Factor**) is at most **1**.

If the balance factor becomes 2 or -2, the tree performs a **Rotation** to fix itself.

### The Four Types of Rotations
1. **Left Rotation (RR)**: Used when a node is added to the right child of a right child.
2. **Right Rotation (LL)**: Used when a node is added to the left child of a left child.
3. **Left-Right Rotation (LR)**: A left rotation on the left child, followed by a right rotation on the node itself.
4. **Right-Left Rotation (RL)**: A right rotation on the right child, followed by a left rotation on the node itself.

**Imagine this:** A mobile hanging toy. If you hang too many toys on one side, the whole thing tilts. To fix it, you don't just move a toy; you shift the central support point (the pivot) to bring the structure back into balance.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize AVL Balancing here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Search** | $O(\log n)$ | Guaranteed balanced height. |
| **Insertion** | $O(\log n)$ | Search time + $O(1)$ rotation. |
| **Deletion** | $O(\log n)$ | Search time + potential rotations. |

**Space Complexity:** $O(n)$ to store the nodes.

## 💻 Implementation

Check out the [balancing.py](./balancing.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/)
- [GeeksforGeeks: AVL Tree](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/)
