# Graph Representation in Python

"""
Goal: Implement Graph representations using both Adjacency Matrix and Adjacency List.
Algorithm: Use a 2D list for the Matrix and a Dictionary for the List.
"""

class GraphMatrix:
    def __init__(self, num_vertices):
        self.v = num_vertices
        # Initialize a V x V matrix with 0s
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1, directed=False):
        """Add an edge between vertex u and v."""
        self.adj_matrix[u][v] = weight
        if not directed:
            self.adj_matrix[v][u] = weight
        print(f"Edge added between {u} and {v} (weight: {weight})")

    def remove_edge(self, u, v):
        """Remove the edge between u and v."""
        self.adj_matrix[u][v] = 0
        # We don't know if it's directed here, but typically we'd check the graph type
        # For this simple impl, we assume undirected if we want to remove both
        self.adj_matrix[v][u] = 0
        print(f"Edge removed between {u} and {v}")

    def display(self):
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

class GraphList:
    def __init__(self):
        # Dictionary: { vertex: [list of neighbors] }
        self.adj_list = {}

    def add_vertex(self, v):
        """Add a new vertex to the graph."""
        if v not in self.adj_list:
            self.adj_list[v] = []
            print(f"Vertex {v} added.")

    def add_edge(self, u, v, directed=False):
        """Add an edge between vertex u and v."""
        # Ensure vertices exist first
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)
        print(f"Edge added: {u} <-> {v}")

    def get_neighbors(self, v):
        """Return the list of neighbors for a vertex."""
        return self.adj_list.get(v, [])

    def display(self):
        print("\nAdjacency List:")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {', '.join(map(str, neighbors))}")

# --- Usage Example ---
if __name__ == "__main__":
    print("--- Testing Adjacency Matrix ---")
    gm = GraphMatrix(4)
    gm.add_edge(0, 1)
    gm.add_edge(0, 2)
    gm.add_edge(1, 2)
    gm.add_edge(2, 3)
    gm.display()

    print("\n--- Testing Adjacency List ---")
    gl = GraphList()
    gl.add_edge("A", "B")
    gl.add_edge("A", "C")
    gl.add_edge("B", "C")
    gl.add_edge("C", "D")
    gl.display()
