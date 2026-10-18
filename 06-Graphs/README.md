# Graph Introduction

## 💡 Concept
A **Graph** is a non-linear data structure consisting of a set of **Vertices** (or nodes) and **Edges** that connect these vertices. While a Tree is a special kind of graph, a general Graph can have cycles and no specific root.

**Imagine this:** A Social Network.
- Each person is a **Vertex**.
- A friendship between two people is an **Edge**.
- If the friendship is mutual, it's an **Undirected Graph**.
- If one person follows another (like on X/Twitter), it's a **Directed Graph**.

### Key Terminology
- **Vertex (Node)**: An individual data point in the graph.
- **Edge**: The connection between two vertices.
- **Weight**: A value assigned to an edge (e.g., distance between two cities in a map).
- **Degree**: The number of edges connected to a vertex.
- **Path**: A sequence of edges that allows you to travel from one vertex to another.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected Graph**: A graph where there is a path between every pair of vertices.

### Graph Types
1. **Undirected Graph**: Edges have no direction. If A is connected to B, B is also connected to A.
2. **Directed Graph (Digraph)**: Edges have a direction. A $\rightarrow$ B does not imply B $\rightarrow$ A.
3. **Weighted Graph**: Edges have weights (costs, distances).
4. **Unweighted Graph**: All edges are considered equal.

## ⏱️ Complexity Analysis (General)

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Add Vertex** | $O(1)$ | Adding a node to the list. |
| **Add Edge** | $O(1)$ | Linking two existing nodes. |
| **Search/Visit**| $O(V + E)$ | In worst case, we visit every vertex $V$ and edge $E$. |

---

## 🚀 Learning Path for Graphs
In this section, we will cover:
1. **Representation**: Adjacency Matrix vs. Adjacency List.
2. **Traversal**: Breadth-First Search (BFS) and Depth-First Search (DFS).
3. **Algorithms**: 
   - **Dijkstra's**: Shortest path in weighted graphs.
   - **Prim's & Kruskal's**: Minimum Spanning Trees (MST).
   - **Topological Sort**: Ordering tasks with dependencies.
