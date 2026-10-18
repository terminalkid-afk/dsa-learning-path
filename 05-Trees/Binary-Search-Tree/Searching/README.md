# BST Searching

## 💡 Concept
Searching in a **Binary Search Tree (BST)** is where the power of this data structure really shines. Because of the **BST Property** (Left < Root < Right), we don't have to look at every node. Instead, we can eliminate half of the remaining tree at every single step.

### The Logic
To search for a target value:
1. Start at the **Root**.
2. If the root's value is the target $\rightarrow$ **Found it!**
3. If the target is **smaller** than the root $\rightarrow$ move to the **Left Subtree** and repeat.
4. If the target is **larger** than the root $\rightarrow$ move to the **Right Subtree** and repeat.
5. If you reach a `None` pointer $\rightarrow$ the target is **not in the tree**.

**Imagine this:** You are playing a "Number Guessing Game." I think of a number between 1 and 100. You guess `50`. I tell you "Higher." You now know the number is between 51 and 100. You've just eliminated 50% of the possibilities in one go! That is exactly how BST searching works.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize BST Search here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Average Case** | $O(\log n)$ | In a balanced tree, the search space is halved each time. |
| **Worst Case** | $O(n)$ | In a skewed tree (linked list shape), you might visit every node. |

**Space Complexity:** $O(h)$ for recursive implementation (stack space) or $O(1)$ for iterative.

## 💻 Implementation

Check out the [searching.py](./searching.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- [GeeksforGeeks: Search a key in BST](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/)
