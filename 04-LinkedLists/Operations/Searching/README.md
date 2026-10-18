# Linked List Searching

## 💡 Concept
**Searching** in a linked list is the process of finding the location (or verifying the existence) of a specific value. Because linked lists are not stored in contiguous memory, we cannot use indexing (like `arr[5]`) or Binary Search.

The only way to find an element is through **Linear Search**: starting at the Head and visiting every node one by one until the target is found or we reach the end of the list.

**Imagine this:** You are walking through a train. You are looking for a passenger named "Alice." You start at the first carriage and ask the people there. If Alice isn't there, you move to the second carriage, then the third, and so on, until you either find Alice or reach the end of the train.

### Search Types
1. **Search by Value**: Looking for a node that contains a specific piece of data.
2. **Search by Position**: Looking for the node at a specific index (e.g., the 3rd node).

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Linked List Searching here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Best Case** | $O(1)$ | $O(1)$ |
| **Worst Case** | $O(n)$ | $O(1)$ |
| **Average Case** | $O(n)$ | $O(1)$ |

The **Worst Case** occurs when the element is at the very end of the list or not present at all, requiring us to visit every single node.

## 💻 Implementation

Check out the [searching.py](./searching.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) (Compare this to Linked List search!)
- [GeeksforGeeks: Search an element in a Linked List](https://www.geeksforgeeks.org/search-an-element-in-a-linked-list/)
