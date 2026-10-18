# BST Deletion in Python

"""
Goal: Implement the deletion of a value from a Binary Search Tree (BST).
Algorithm: Handle three cases (leaf, one child, two children) to maintain the BST property.
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

    def delete(self, data):
        """Public method to delete a value from the BST."""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, root, data):
        # Base Case: The tree is empty or the value is not found
        if root is None:
            print(f"❌ Value {data} not found in the BST.")
            return root

        # Navigate the tree
        if data < root.data:
            root.left = self._delete_recursive(root.left, data)
        elif data > root.data:
            root.right = self._delete_recursive(root.right, data)
        else:
            # We found the node to delete!
            print(f"Deleting node {data}...")

            # Case 1 & 2: Node has no child or only one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node has two children
            # Find the in-order successor (smallest in the right subtree)
            successor = self._find_min(root.right)
            # Replace the current node's data with the successor's data
            root.data = successor.data
            # Delete the successor node from the right subtree
            root.right = self._delete_recursive(root.right, successor.data)

        return root

    def _find_min(self, node):
        """Helper to find the node with the minimum value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, node, result=None):
        """Helper to verify the BST state."""
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
    # Constructing a BST:
    #        50
    #       /  \
    #      30   70
    #     /  \  /  \
    #    20   40 60  80
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)

    print("Original BST (In-order):", bst.inorder_traversal(bst.root))

    # Test 1: Delete a leaf node (20)
    bst.delete(20)
    print("After deleting 20:", bst.inorder_traversal(bst.root))

    # Test 2: Delete a node with one child (30 now has only one child 40)
    bst.delete(30)
    print("After deleting 30:", bst.inorder_traversal(bst.root))

    # Test 3: Delete a node with two children (50 - the root)
    bst.delete(50)
    print("After deleting root 50:", bst.inorder_traversal(bst.root))
