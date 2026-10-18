# BST Searching in Python

"""
Goal: Implement an efficient search for a target value in a Binary Search Tree (BST).
Algorithm: Use the BST property (Left < Root < Right) to eliminate half the tree at each step.
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

    def search(self, target):
        """
        Search for a target value in the BST.
        Returns the Node if found, otherwise None.
        Time Complexity: O(log n) average, O(n) worst case.
        Space Complexity: O(1) for iterative approach.
        """
        current = self.root

        while current:
            if target == current.data:
                return current  # Found it!
            elif target < current.data:
                current = current.left  # Search the left subtree
            else:
                current = current.right # Search the right subtree

        return None # Target not found

# --- Usage Example ---
if __name__ == "__main__":
    bst = BST()
    # Creating a BST:
    #        50
    #       /  \
    #      30   70
    #     /  \  /  \
    #    20   40 60  80
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)

    # Test Case 1: Target exists
    target = 40
    result = bst.search(target)
    if result:
        print(f"✅ Value {target} found in the BST!")
    else:
        print(f"❌ Value {target} not found.")

    # Test Case 2: Target does not exist
    target_missing = 100
    result_missing = bst.search(target_missing)
    if result_missing:
        print(f"✅ Value {target_missing} found!")
    else:
        print(f"❌ Value {target_missing} not found in the BST.")
