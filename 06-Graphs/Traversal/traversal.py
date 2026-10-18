# Graph Traversal in Python

"""
Goal: Implement Breadth-First Search (BFS) and Depth-First Search (DFS) for a graph.
Algorithm:
- BFS: Uses a Queue to visit nodes level by level.
- DFS: Uses Recursion (Stack) to visit nodes as deeply as possible.
"""
from collections import deque

class Graph:
    def __init__(self):
        # Adjacency List: { vertex: [neighbors] }
        self.adj_list = {}

    def add_edge(self, u, v, directed=False):
        """Add an edge between u and v."""
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []

        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)

    def bfs(self, start_node):
        """
        Breadth-First Search.
        Time: O(V + E), Space: O(V)
        """
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)

        result = []
        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_node, visited=None):
        """
        Depth-First Search.
        Time: O(V + E), Space: O(V)
        """
        if visited is None:
            visited = set()

        visited.add(start_node)
        result = [start_node]

        for neighbor in self.adj_list.get(start_node, []):
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))

        return result

# --- Usage Example ---
if __name__ == "__main__":
    g = Graph()
    # Constructing a graph:
    # A -- B -- D
    # |    |
    # C -- E
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "E")

    print("Graph Structure: A connected to B,C; B connected to A,D,E; C connected to A,E; etc.")

    print(f"BFS starting from 'A': {g.bfs('A')}")
    # Expected: ['A', 'B', 'C', 'D', 'E'] (Order may vary slightly based on edge insertion)

    print(f"DFS starting from 'A': {g.dfs('A')}")
    # Expected: ['A', 'B', 'D', 'E', 'C'] (Order depends on traversal)
