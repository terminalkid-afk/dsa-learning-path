# Binary Search Tree (BST) Insertion

## 💡 Concept
**Insertion** in a Binary Search Tree (BST) is the process of adding a new value while maintaining the **BST Property**:
- For any given node, all values in its **left subtree** must be **smaller** than the node's value.
- All values in its **right subtree** must be **larger** than the node's value.

### The Logic
To insert a value, we start at the root and compare the new value with the current node:
1. If the new value is **smaller** than the current node $\rightarrow$ move to the **left** child.
2. If the new value is **larger** than the current node $\rightarrow$ move to the **right** child.
3. Repeat this until you find an **empty spot** (`None`). Place the new node there.

**Imagine this:** You are sorting a deck of cards into a system. You look at the first card (the root). If your new card is smaller, you put it in the "small" pile on the left. If it's larger, you put it in the "large" pile on the right. You repeat this process within each pile until the card finds its exact home.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize BST Insertion here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Average Case** | $O(\log n)$ | In a balanced tree, we discard half the tree at each step. |
| **Worst Case** | $O(n)$ | If the tree is skewed (like a linked list), we might visit every node. |

**Space Complexity:** $O(h)$ where $h$ is the height of the tree (due to the recursion stack).

## 💻 Implementation

Check out the [insertion.py](./insertion.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
- [GeeksforGeeks: Insertion in BST](https://www.geeksforgeeks.org/insertion-in-a-binary-search-tree/)
