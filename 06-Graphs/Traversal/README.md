# Graph Traversal (BFS & DFS)

## 💡 Concept
Unlike linear data structures, graphs can have cycles and multiple paths to the same node. To visit every node without getting stuck in an infinite loop, we must keep track of which nodes have already been **visited**.

### 1. Breadth-First Search (BFS)
BFS explores the graph **level by level**. It visits all the immediate neighbors of the starting node first, then all the neighbors of those neighbors, and so on.

**Implementation**: Uses a **Queue** (FIFO).
**Imagine this:** A ripple in a pond. When you drop a stone, the ripple expands outward in a perfect circle, hitting everything at distance 1, then everything at distance 2, and so on.

### 2. Depth-First Search (DFS)
DFS explores as **deeply as possible** along one branch before backtracking to the last fork in the road to try a different path.

**Implementation**: Uses a **Stack** (LIFO) or **Recursion**.
**Imagine this:** Exploring a maze. You follow one path until you hit a dead end, then you backtrack to the last junction and try the other direction.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Graph Traversals here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Traversal | Time Complexity | Space Complexity | Why? |
| :--- | :--- | :--- | :--- |
| **BFS** | $O(V + E)$ | $O(V)$ | Visit every vertex $V$ and edge $E$; queue can hold $V$ nodes. |
| **DFS** | $O(V + E)$ | $O(V)$ | Visit every vertex $V$ and edge $E$; recursion stack can reach $V$ depth. |

## 💻 Implementation

Check out the [traversal.py](./traversal.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Number of Islands](https://leetcode.com/problems/number-of-islands/) (Classic BFS/DFS problem!)
- [LeetCode: Clone Graph](https://leetcode.com/problems/clone-graph/)
- [GeeksforGeeks: BFS for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
