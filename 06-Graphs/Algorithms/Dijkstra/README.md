# Dijkstra's Algorithm

## 💡 Concept
**Dijkstra's Algorithm** is used to find the **shortest path** from a single source vertex to all other vertices in a weighted graph. It is a "greedy" algorithm, meaning it always chooses the closest unvisited node to process next.

**Imagine this:** You are using Google Maps to find the quickest route from your house to the airport. Google Maps doesn't look at every possible path in the city (that would take forever). Instead, it starts at your house and gradually expands outward, always following the shortest known road, until it finally reaches the airport.

### The Logic
1. Assign a distance of **infinity** to all nodes, and **0** to the start node.
2. Mark all nodes as **unvisited**.
3. While there are unvisited nodes:
   - Pick the unvisited node with the **smallest current distance** (use a Priority Queue!).
   - For each neighbor of this node, calculate the distance from the start via the current node.
   - If this new distance is smaller than the previously known distance, **update it**.
   - Mark the current node as **visited**.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Dijkstra's Algorithm here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Aspect | Complexity | Why? |
| :--- | :--- | :--- |
| **Time Complexity** | $O((V + E) \log V)$ | We visit every edge and use a Priority Queue for vertices. |
| **Space Complexity** | $O(V)$ | To store distances and the visited set. |

**Crucial Note**: Dijkstra's algorithm only works for graphs with **non-negative edge weights**. For graphs with negative weights, you must use the Bellman-Ford algorithm.

## 💻 Implementation

Check out the [dijkstra.py](./dijkstra.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- [GeeksforGeeks: Dijkstra's Shortest Path Algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-//)
