# BST Deletion

## 💡 Concept
**Deletion** in a Binary Search Tree (BST) is the most complex of the basic BST operations because we must remove a node while ensuring the **BST Property** (Left < Root < Right) is preserved.

Depending on the node we want to delete, there are three different scenarios:

### 1. Case 1: The Node is a Leaf (No Children)
This is the easiest case. We simply remove the node by setting the pointer from its parent to `None`.

### 2. Case 2: The Node has One Child
We "bypass" the node. The child of the node to be deleted is linked directly to the parent of the deleted node.

### 3. Case 3: The Node has Two Children
We cannot just remove the node, or the tree would split. Instead, we replace the node's value with the value of its **In-order Successor** (the smallest value in the right subtree) or its **In-order Predecessor** (the largest value in the left subtree). Then, we delete that successor/predecessor node.

**Imagine this:** A corporate hierarchy. 
- **Leaf**: A junior employee with no reports leaves. No one is affected.
- **One Child**: A manager with one report leaves. The report now reports directly to the manager's boss.
- **Two Children**: A CEO leaves. To keep the company stable, the most qualified person from the right-hand department (the In-order Successor) is promoted to CEO, and their previous spot is filled by their own subordinates.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize BST Deletion here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Case | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Average Case** | $O(\log n)$ | We traverse the height of the tree to find the node. |
| **Worst Case** | $O(n)$ | If the tree is skewed, we may visit every node. |

**Space Complexity:** $O(h)$ for the recursion stack, where $h$ is the height of the tree.

## 💻 Implementation

Check out the [deletion.py](./deletion.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
- [GeeksforGeeks: Deletion in BST](https://www.geeksforgeeks.org/deletion-in-binary-search-tree/)
