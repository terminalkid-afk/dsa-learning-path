# Prim's Algorithm

## 💡 Concept
**Prim's Algorithm** is a greedy algorithm used to find the **Minimum Spanning Tree (MST)** of a connected, weighted, undirected graph. 

A **Minimum Spanning Tree** is a subset of the edges that connects all the vertices together, without any cycles, and with the minimum possible total edge weight.

**Imagine this:** You are a city planner wanting to connect 5 neighborhoods with fiber-optic cables. You want every neighborhood to be connected to the network, but cables are expensive. You start at one neighborhood and always pick the cheapest available cable that connects a "connected" neighborhood to an "unconnected" one. By the end, you've connected everyone using the least amount of cable possible.

### The Logic
1. Start with an arbitrary node and mark it as visited.
2. Look at all edges connecting visited nodes to unvisited nodes.
3. Pick the edge with the **minimum weight**.
4. Add the new node to the visited set and the edge to the MST.
5. Repeat until all nodes are visited.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Prim's Algorithm here](https://www.//www.dsavisualizer.in/visualizer) (Interactive Animation)

| Implementation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Adjacency Matrix** | $O(V^2)$ | Scanning all vertices to find the min edge. |
| **Binary Heap** | $O(E \log V)$ | Using a priority queue to find the min edge. |

**Space Complexity:** $O(V + E)$ to store the graph and the MST.

## 💻 Implementation

Check out the [prim.py](./prim.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [GeeksforGeeks: Prim's Algorithm](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst/)
- [LeetCode: Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
