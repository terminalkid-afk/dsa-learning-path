# Tree Traversals

## 💡 Concept
**Traversal** is the process of visiting every node in a tree exactly once. Unlike linear data structures (Arrays, Linked Lists), there are multiple ways to traverse a tree.

Traversals are divided into two main categories:
1. **Depth-First Search (DFS)**: Explore as far as possible along each branch before backtracking.
2. **Breadth-First Search (BFS)**: Explore all nodes at the current depth (level) before moving to the next level.

### Depth-First Search (DFS) Variations
DFS is typically implemented using **Recursion** (which uses the system call stack).

1. **Pre-order (Root $\rightarrow$ Left $\rightarrow$ Right)**: Visit the root first, then the left subtree, then the right. (Useful for cloning a tree).
2. **In-order (Left $\rightarrow$ Root $\rightarrow$ Right)**: Visit the left subtree, then the root, then the right. (**Crucial**: In-order traversal of a BST always yields values in sorted order).
3. **Post-order (Left $\rightarrow$ Right $\rightarrow$ Root)**: Visit children first, then the root. (Useful for deleting a tree or calculating directory sizes).

### Breadth-First Search (BFS)
Also called **Level-Order Traversal**. It visits nodes level by level from top to bottom and left to right.
- **Implementation**: Uses a **Queue** instead of recursion.

**Imagine this:** 
- **DFS**: Exploring a maze by following one path until you hit a wall, then backtracking to the last fork in the road.
- **BFS**: Exploring a maze by taking one step in every possible direction, then two steps in every possible direction, and so on.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Tree Traversals here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Traversal | Time Complexity | Space Complexity | Why? |
| :--- | :--- | :--- | :--- |
| **DFS (All)** | $O(n)$ | $O(h)$ | Visit each node once; stack depth is tree height $h$. |
| **BFS** | $O(n)$ | $O(w)$ | Visit each node once; queue size is max width $w$. |

## 💻 Implementation

Check out the [traversal.py](./traversal.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [LeetCode: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [GeeksforGeeks: Tree Traversals](https://www.geeksforgeeks.org/tree-traversals-in-order-pre-order-post-order/)
