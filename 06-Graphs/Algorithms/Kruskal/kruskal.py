# Kruskal's Algorithm in Python

"""
Goal: Find the Minimum Spanning Tree (MST) of a weighted undirected graph.
Algorithm: Sort all edges by weight and use Union-Find to avoid cycles.
"""

class UnionFind:
    """Disjoint Set Union (DSU) with Path Compression and Union by Rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        """Find the root of the set containing i, with path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """Union of two sets based on rank."""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True # Union successful
        return False # Already in the same set (cycle detected)

def kruskal_mst(num_vertices, edges):
    """
    Computes the MST using Kruskal's Algorithm.
    Edges should be a list of tuples: (u, v, weight)
    Time Complexity: O(E log E) due to sorting edges.
    Space Complexity: O(V) for Union-Find structure.
    """
    # 1. Sort all edges by weight in ascending order
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(num_vertices)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        # 2. If adding the edge doesn't form a cycle, add it to MST
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight
            # Optimization: Stop when we have V-1 edges
            if len(mst) == num_vertices - 1:
                break

    return mst, total_cost

# --- Usage Example ---
if __name__ == "__main__":
    # Graph defined as: (node1, node2, weight)
    # Vertices are 0, 1, 2, 3
    num_v = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst, cost = kruskal_mst(num_v, edges)

    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} --({w})-- {v}")
    print(f"Total MST Cost: {cost}")
    # Expected: (0,3,5), (2,3,4), (0,1,10) -> Total 19
