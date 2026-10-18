# Prim's Algorithm in Python

"""
Goal: Find the Minimum Spanning Tree (MST) of a weighted undirected graph.
Algorithm: Greedy approach using a Priority Queue to always pick the cheapest edge
          connecting a visited node to an unvisited node.
"""
import heapq

class Graph:
    def __init__(self):
        # Adjacency List: { vertex: [(neighbor, weight), ...] }
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        """Add a weighted undirected edge."""
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def prims_mst(self, start_node):
        """
        Compute the MST using Prim's Algorithm.
        Time Complexity: O(E log V)
        Space Complexity: O(V + E)
        """
        mst_edges = []
        visited = set()
        # Priority Queue stores (weight, current_node, parent_node)
        pq = [(0, start_node, None)]

        total_cost = 0

        while pq:
            weight, u, parent = heapq.heappop(pq)

            if u in visited:
                continue

            visited.add(u)
            total_cost += weight
            if parent is not None:
                mst_edges.append((parent, u, weight))

            for v, w in self.adj_list.get(u, []):
                if v not in visited:
                    heapq.heappush(pq, (w, v, u))

        return mst_edges, total_cost

# --- Usage Example ---
if __name__ == "__main__":
    g = Graph()
    # Sample Graph
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 1, 4) # This was a typo in logic, fixing to just weights
    # Fixing edges to be cleaner
    g.adj_list = {} # Reset
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 1)
    g.add_edge("C", "D", 4)

    start_node = "A"
    mst, cost = g.prims_mst(start_node)

    print(f"MST starting from {start_node}:")
    for u, v, w in mst:
        print(f"{u} --({w})-- {v}")
    print(f"Total MST Cost: {cost}")
