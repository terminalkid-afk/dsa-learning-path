# Kruskal's Algorithm

## 💡 Concept
**Kruskal's Algorithm** is another greedy approach to find the **Minimum Spanning Tree (MST)** of a connected, weighted, undirected graph. While Prim's algorithm grows the MST from a single starting node, Kruskal's algorithm treats every node as an individual tree and merges them together.

The core logic is: **Always pick the absolute cheapest edge available in the entire graph**, as long as adding that edge doesn't create a cycle.

To efficiently detect and prevent cycles, Kruskal's uses a data structure called **Union-Find (Disjoint Set Union)**.

**Imagine this:** You are connecting several small islands with bridges. You look at a list of all possible bridges and their costs. You build the cheapest bridge first, regardless of where it is. Then you build the next cheapest. If a bridge would connect two islands that are already connected (via some other path), you skip it to avoid wasting money on a redundant bridge.

### The Logic
1. Sort all edges in the graph by weight in ascending order.
2. Initialize a Union-Find structure where every vertex is its own parent.
3. Iterate through the sorted edges:
   - If the two vertices of the edge belong to different sets (different components), add the edge to the MST and **Union** the two sets.
   - If they are already in the same set, skip the edge (it would form a cycle).
4. Repeat until you have $V-1$ edges in your MST.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Kruskal's Algorithm here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Aspect | Complexity | Why? |
| :--- | :--- | :--- |
| **Sorting Edges** | $O(E \log E)$ | Sorting all edges by weight. |
| **Union-Find** | $O(E \cdot \alpha(V))$ | $\alpha$ is the inverse Ackermann function (nearly $O(1)$). |
| **Total** | $O(E \log E)$ or $O(E \log V)$ | Dominated by the sorting step. |

## 💻 Implementation

Check out the [kruskal.py](./kruskal.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [GeeksforGeeks: Kruskal's Minimum Spanning Tree](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-mst-greedy-algo-2/)
- [LeetCode: Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
