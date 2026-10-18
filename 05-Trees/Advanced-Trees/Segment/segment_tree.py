# Segment Tree in Python

"""
Goal: Implement a Segment Tree for efficient Range Sum Queries and Point Updates.
Algorithm: Use a binary tree where each node stores the sum of a specific range of the array.
"""

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n) # Allocate 4n space to avoid index out of bounds
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, start, end):
        """
        Recursively build the segment tree.
        """
        if start == end:
            # Leaf node: stores the actual element from the array
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            # Recursively build left and right children
            self._build(data, 2 * node, start, mid)
            self._build(data, 2 * node + 1, mid + 1, end)
            # Internal node stores the sum of its children
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, idx, val):
        """
        Update the value at a specific index.
        Time Complexity: O(log n)
        """
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            # Found the leaf node to update
            self.tree[node] = val
            return

        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)

        # Update internal node after child update
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, L, R):
        """
        Query the sum of elements in range [L, R].
        Time Complexity: O(log n)
        """
        return self._query(1, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        # Case 1: Range of node is completely outside query range [L, R]
        if R < start or end < L:
            return 0

        # Case 2: Range of node is completely inside query range [L, R]
        if L <= start and end <= R:
            return self.tree[node]

        # Case 3: Range of node partially overlaps query range
        mid = (start + end) // 2
        sum_left = self._query(2 * node, start, mid, L, R)
        sum_right = self._query(2 * node + 1, mid + 1, end, L, R)
        return sum_left + sum_right

# --- Usage Example ---
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(data)

    print(f"Original array: {data}")
    print(f"Sum of range [1, 3] (3+5+7): {st.query(1, 3)}") # Expected: 15

    print("\nUpdating index 1 to 10...")
    st.update(1, 10)
    # New array: [1, 10, 5, 7, 9, 11]
    print(f"Sum of range [1, 3] (10+5+7): {st.query(1, 3)}") # Expected: 22

    print(f"Sum of range [0, 5] (all elements): {st.query(0, 5)}") # Expected: 43
