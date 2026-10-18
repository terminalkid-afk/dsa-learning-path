# Dijkstra's Algorithm in Python

"""
Goal: Find the shortest path from a source node to all other nodes in a weighted graph.
Algorithm: Use a Priority Queue (min-heap) to always expand the closest unvisited node.
"""
import heapq

class WeightedGraph:
    def __init__(self):
        # Adjacency List: { vertex: [(neighbor, weight), ...] }
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        """Add a weighted edge between u and v (undirected)."""
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def dijkstra(self, start_node):
        """
        Compute shortest paths from start_node to all others.
        Time Complexity: O((V + E) log V)
        Space Complexity: O(V)
        """
        # Distances dictionary: { node: distance }
        # Initialize all distances as infinity, start_node as 0
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start_node] = 0

        # Priority Queue stores tuples: (distance, node)
        # We use distance as the first element so heapq sorts by it (min-heap)
        pq = [(0, start_node)]

        visited = set()

        while pq:
            # Pop the node with the smallest known distance
            current_dist, current_node = heapq.heappop(pq)

            # If we've already processed this node with a shorter path, skip it
            if current_node in visited:
                continue
            visited.add(current_node)

            # Explore neighbors
            for neighbor, weight in self.adj_list.get(current_node, []):
                distance = current_dist + weight

                # If a shorter path to the neighbor is found, update and push to PQ
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

# --- Usage Example ---
if __name__ == "__main__":
    graph = WeightedGraph()

    # Creating a weighted graph
    # A --(4)-- B --(8)-- D
    # |        /|        /
    # (8)    (11)(7)    (2)
    # |    /    |    /
    # C --(1)-- E --(6)-- D
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 8)
    graph.add_edge("B", "C", 11)
    graph.add_edge("B", "D", 8)
    graph.add_edge("B", "E", 7)
    graph.add_edge("C", "E", 1)
    graph.add_edge("E", "D", 6)

    start = "A"
    shortest_paths = graph.dijkstra(start)

    print(f"Shortest distances from {start}:")
    for node, dist in shortest_paths.items():
        print(f"To {node}: {dist}")

    # Verification:
    # A to B: 4
    # A to C: 8 (or A->B->C = 15) -> 8
    # A to E: A->C->E = 8+1 = 9
    # A to D: A->B->D = 4+8 = 12 (or A->C->E->D = 8+1+6 = 15) -> 12
