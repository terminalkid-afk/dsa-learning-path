# Lowest Common Ancestor (LCA) in Python

"""
Goal: Find the Lowest Common Ancestor of two nodes in a Binary Search Tree (BST).
Algorithm: Use the BST property to determine when the two target nodes split into different subtrees.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Helper to build the tree."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def find_lca(self, n1, n2):
        """
        Find the Lowest Common Ancestor of two values in the BST.
        Time Complexity: O(h) where h is the height of the tree.
        Space Complexity: O(1) for the iterative approach.
        """
        current = self.root

        while current:
            # If both nodes are smaller than current, LCA must be in the left subtree
            if n1 < current.data and n2 < current.data:
                current = current.left
            # If both nodes are larger than current, LCA must be in the right subtree
            elif n1 > current.data and n2 > current.data:
                current = current.right
            else:
                # We have found the split point!
                # Either one node is on the left and one on the right,
                # or the current node is one of the target nodes.
                return current.data

        return None

# --- Usage Example ---
if __name__ == "__main__":
    bst = BST()
    # Constructing a BST:
    #        20
    #       /  \
    #      8    22
    #     / \     \
    #    4   12    25
    #       /  \
    #      10   14
    values = [20, 8, 22, 4, 12, 25, 10, 14]
    for val in values:
        bst.insert(val)

    # Test Case 1: LCA of 10 and 14
    # Path: 20 -> 8 -> 12. LCA is 12.
    n1, n2 = 10, 14
    print(f"LCA of {n1} and {n2}: {bst.find_lca(n1, n2)}") # Expected: 12

    # Test Case 2: LCA of 4 and 14
    # Path: 20 -> 8. LCA is 8.
    n1, n2 = 4, 14
    print(f"LCA of {n1} and {n2}: {bst.find_lca(n1, n2)}") # Expected: 8

    # Test Case 3: LCA of 8 and 22
    # Root is 20. One is left, one is right. LCA is 20.
    n1, n2 = 8, 22
    print(f"LCA of {n1} and {n2}: {bst.find_lca(n1, n2)}") # Expected: 20
