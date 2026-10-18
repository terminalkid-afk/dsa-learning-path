# Introduction to Trees

## 💡 Concept
A **Tree** is a non-linear data structure used to represent hierarchical relationships. Unlike Arrays, Stacks, or Queues, which are linear (one element follows another), a Tree organizes data in a parent-child relationship.

**Imagine this:** A family tree. 
- You have a grandparent (the **Root**).
- The grandparent has children (the **Parents**).
- The parents have children (the **Children**).
- Some people have no children; they are the "leaves" of the family tree.

### Key Terminology
To understand trees, you need to know these terms:
- **Root**: The topmost node of the tree. Every tree has exactly one root.
- **Node**: A structure containing a value and pointers to its children.
- **Edge**: The link connecting two nodes.
- **Leaf**: A node that has no children.
- **Parent**: A node that has a link to another node (its child).
- **Child**: A node that is a descendant of another node.
- **Subtree**: A tree consisting of a node and all its descendants.
- **Height**: The number of edges on the longest path from the root to a leaf.
- **Depth**: The number of edges from the root to a specific node.

### Why do we need Trees?
Trees are used everywhere in computer science because they allow for extremely efficient searching and organization:
- **File Systems**: Your computer's folders and subfolders are a tree.
- **HTML DOM**: The structure of a webpage is a tree of elements.
- **Databases**: B-Trees and AVL trees are used to make database indexing lightning fast.
- **Decision Making**: AI uses decision trees to arrive at a conclusion.

## ⏱️ Complexity Analysis (General)

| Operation | Average Complexity | Worst Case |
| :--- | :--- | :--- |
| **Search** | $O(\log n)$ | $O(n)$ |
| **Insertion** | $O(\log n)$ | $O(n)$ |
| **Deletion** | $O(\log n)$ | $O(n)$ |

*Note: The $O(\log n)$ performance is typical for balanced trees (like BSTs), while $O(n)$ happens if the tree becomes "skewed" (looks like a linked list).*

---

## 🚀 Learning Path for Trees
In this section, we will cover:
1. **Binary Tree**: Basics, properties, and types.
2. **Binary Search Tree (BST)**: Efficient searching, insertion, and balancing (AVL).
3. **Traversal**: How to visit every node (Pre-order, In-order, Post-order, BFS).
4. **Advanced Trees**: Tries, Segment Trees, and Red-Black Trees.
5. **Algorithms & Applications**: LCA, Heap Sort, and Huffman Coding.
