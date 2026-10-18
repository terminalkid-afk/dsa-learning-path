# BST Insertion in Python

"""
Goal: Implement the insertion of a value into a Binary Search Tree (BST).
Algorithm: Recursively navigate left or right based on the BST property
          until an empty spot is found.
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
        """Public method to insert a value into the BST."""
        if self.root is None:
            self.root = Node(data)
            print(f"Inserted {data} as the root.")
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        """Helper method to find the correct spot recursively."""
        if data < current.data:
            # Go left
            if current.left is None:
                current.left = Node(data)
                print(f"Inserted {data} to the left of {current.data}.")
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            # Go right
            if current.right is None:
                current.right = Node(data)
                print(f"Inserted {data} to the right of {current.data}.")
            else:
                self._insert_recursive(current.right, data)
        else:
            print(f"Value {data} already exists in the BST. No duplicates allowed.")

    def inorder_traversal(self, node, result=None):
        """Helper to verify the BST is sorted (In-order traversal of BST is always sorted)."""
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result

# --- Usage Example ---
if __name__ == "__main__":
    bst = BST()

    # Insert elements
    # Root: 50
    # Left child: 30, Right child: 70
    # 30's children: 20, 40
    # 70's child: 60
    values = [50, 30, 70, 20, 40, 60]
    for val in values:
        bst.insert(val)

    print("\nVerification: In-order traversal of the BST:")
    print(bst.inorder_traversal(bst.root))
    # Expected: [20, 30, 40, 50, 60, 70] (Should be perfectly sorted)

    # Test duplicate
    bst.insert(30)
