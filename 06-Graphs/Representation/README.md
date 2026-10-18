# Graph Representation

## 💡 Concept
A graph is a collection of vertices (nodes) and edges. To implement a graph in code, we need a way to store which vertices are connected to which. There are two primary ways to do this: the **Adjacency Matrix** and the **Adjacency List**.

### 1. Adjacency Matrix
An Adjacency Matrix is a 2D array of size $V \times V$ (where $V$ is the number of vertices).
- If `matrix[i][j] == 1`, there is an edge from vertex $i$ to vertex $j$.
- If `matrix[i][j] == 0`, there is no edge.
- For weighted graphs, the `1` is replaced by the weight of the edge.

**Imagine this:** A grid of cities. Every city has a row and a column. If city A and city B are connected by a road, you put a checkmark in the cell where row A and column B meet.

### 2. Adjacency List
An Adjacency List is a collection of lists. Each vertex has its own list containing all the other vertices it is connected to. In Python, this is typically implemented as a **Dictionary** where keys are vertices and values are lists/sets of neighbors.

**Imagine this:** A contact list on your phone. Each person (vertex) has a list of "friends" (neighbors). To find who Person A is connected to, you just look at Person A's specific friend list.

### Comparison Table

| Feature | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Space Complexity** | $O(V^2)$ | $O(V + E)$ |
| **Check if Edge Exists**| $O(1)$ (Instant) | $O(\text{degree of node})$ |
| **Find all neighbors** | $O(V)$ | $O(\text{degree of node})$ |
| **Best for...** | Dense Graphs (many edges) | Sparse Graphs (few edges) |

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Graph Representations here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Operation | Matrix | List |
| :--- | :--- | :--- |
| **Add Vertex** | $O(V^2)$ (Must resize matrix) | $O(1)$ |
| **Add Edge** | $O(1)$ | $O(1)$ |
| **Remove Edge** | $O(1)$ | $O(E)$ (Search and remove) |

## 💻 Implementation

Check out the [representation.py](./representation.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)
- [GeeksforGeeks: Graph and its Representations](https://www.geeksforgeeks.org/graph-and-its-representations/)
