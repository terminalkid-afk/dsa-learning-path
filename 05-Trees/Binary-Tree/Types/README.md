# Types of Binary Trees

## 💡 Concept
While all binary trees limit each node to two children, they can take many different shapes. The "shape" of the tree determines its efficiency. If a tree is well-balanced, operations are fast; if it is skewed, it becomes as slow as a linked list.

### 1. Full Binary Tree
A binary tree is **Full** if every node has either **0 or 2 children**. No node in a full binary tree has only one child.

### 2. Complete Binary Tree
A binary tree is **Complete** if:
- All levels are completely filled except possibly the last level.
- The last level is filled from **left to right**.
This structure is critical for implementing **Heaps**.

### 3. Perfect Binary Tree
A binary tree is **Perfect** if:
- All internal nodes have exactly two children.
- All leaf nodes are at the exact same level.
A perfect binary tree of height $h$ has exactly $2^{h+1} - 1$ nodes.

### 4. Balanced Binary Tree
A binary tree is **Balanced** if the height of the left and right subtrees of every node differs by **no more than 1**. 
- **Why it matters**: Balanced trees guarantee $O(\log n)$ time for search, insert, and delete operations.
- **Examples**: AVL Trees, Red-Black Trees.

### 5. Degenerate (Skewed) Binary Tree
A tree where every parent node has only one child. 
- **Left-Skewed**: Every node only has a left child.
- **Right-Skewed**: Every node only has a right child.
**Warning**: In a skewed tree, the time complexity for searching becomes $O(n)$.

**Imagine this:** 
- **Perfect Tree**: A perfectly symmetrical pyramid.
- **Complete Tree**: A pyramid that is finished except for a few blocks missing on the far right of the bottom row.
- **Skewed Tree**: A single long line of blocks leaning to one side.

## ⏱️ Comparison Table
**📺 See it in Action**: [Visualize Binary Tree Types here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Tree Type | Max Nodes at Height $h$ | Search Efficiency | Common Use Case |
| :--- | :--- | :--- | :--- |
| **Perfect** | $2^{h+1}-1$ | Optimal $O(\log n)$ | Theoretical models |
| **Complete** | $\approx 2^{h+1}-1$ | Optimal $O(\log n)$ | Binary Heaps / Priority Queues |
| **Balanced** | Variable | Guaranteed $O(\log n)$ | Database Indexing |
| **Skewed** | $h+1$ | Poor $O(n)$ | Basically a Linked List |

## 🚀 Practice Problems
- [LeetCode: Check if a Binary Tree is Balanced](https://leetcode.com/problems/balanced-binary-tree/)
- [GeeksforGeeks: Types of Binary Trees](https://www.geeksforgeeks.org/types-of-binary-tree/)
