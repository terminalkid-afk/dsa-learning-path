# Topological Sort in Python

"""
Goal: Perform a Topological Sort on a Directed Acyclic Graph (DAG).
Algorithm: Kahn's Algorithm (BFS-based approach using in-degrees).
"""
from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}
        self.in_degree = [0] * num_vertices

    def add_edge(self, u, v):
        """Add a directed edge from u to v."""
        self.adj_list[u].append(v)
        self.in_degree[v] += 1
        print(f"Edge added: {u} -> {v}")

    def topological_sort(self):
        """
        Perform Topological Sort using Kahn's Algorithm.
        Returns a list of vertices in topological order.
        Returns None if a cycle is detected (not a DAG).
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        # 1. Find all vertices with in-degree 0 (no dependencies)
        queue = deque([i for i in range(self.v) if self.in_degree[i] == 0])

        topo_order = []

        while queue:
            # Pop a node with no dependencies
            u = queue.popleft()
            topo_order.append(u)

            # Visit all neighbors and reduce their in-degree
            for v in self.adj_list[u]:
                self.in_degree[v] -= 1
                # If in-degree becomes 0, it's now ready to be processed
                if self.in_degree[v] == 0:
                    queue.append(v)

        # If topo_order doesn't contain all vertices, there is a cycle
        if len(topo_order) != self.v:
            print("❌ Cycle detected! Graph is not a DAG.")
            return None

        return topo_order

# --- Usage Example ---
if __name__ == "__main__":
    # Scenario: Course Prerequisites
    # Course 0: Intro to CS
    # Course 1: Data Structures (needs 0)
    # Course 2: Algorithms (needs 1)
    # Course 3: OS (needs 1)
    # Course 4: Database (needs 2 and 3)
    # Course 5: AI (needs 4)

    num_courses = 6
    g = Graph(num_courses)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print("\nCalculating course sequence...")
    order = g.topological_sort()

    if order:
        print(f"Correct course sequence: {' -> '.join(map(str, order))}")
    else:
        print("Error: Courses have circular dependencies!")

    # Test Case 2: Graph with a cycle
    print("\n--- Testing Cycle Detection ---")
    cycle_g = Graph(3)
    cycle_g.add_edge(0, 1)
    cycle_g.add_edge(1, 2)
    cycle_g.add_edge(2, 0) # Cycle!
    cycle_g.topological_sort()
