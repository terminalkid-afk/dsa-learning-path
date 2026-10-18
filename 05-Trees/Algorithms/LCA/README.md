# Lowest Common Ancestor (LCA)

## 💡 Concept
The **Lowest Common Ancestor (LCA)** of two nodes $u$ and $v$ in a tree is the lowest (deepest) node that has both $u$ and $v$ as descendants.

Every node is considered a descendant of itself. Therefore, if node $u$ is an ancestor of node $v$, then $u$ is the LCA of $u$ and $v$.

**Imagine this:** You are looking at your family tree. You and your sibling's LCA is your Parent. You and your cousin's LCA is your Grandparent. The LCA is the "closest" relative that you both share in your lineage.

### Logic for Binary Search Tree (BST)
In a BST, finding the LCA is incredibly efficient because of the sorted property:
1. Start at the **Root**.
2. If both target values are **smaller** than the current node $\rightarrow$ move to the **Left**.
3. If both target values are **larger** than the current node $\rightarrow$ move to the **Right**.
4. If one is smaller and one is larger (or the current node is one of the targets) $\rightarrow$ **You've found the LCA!**

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize LCA here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Case | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Average Case** | $O(\log n)$ | $O(1)$ (Iterative) |
| **Worst Case** | $O(n)$ | $O(h)$ (Recursive) |

## 💻 Implementation

Check out the [lca.py](./lca.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [LeetCode: Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
