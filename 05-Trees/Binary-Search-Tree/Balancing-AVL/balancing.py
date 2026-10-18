# AVL Tree Balancing in Python

"""
Goal: Implement a self-balancing Binary Search Tree (AVL Tree).
Algorithm: Perform rotations (LL, RR, LR, RL) to maintain a balance factor of -1, 0, or 1.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # New nodes start with height 1

class AVLTree:
    def get_height(self, node):
        """Return height of node; return 0 if node is None."""
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """Calculate balance factor: height(left) - height(right)."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        """
        Perform a right rotation.
        y is the node to be rotated.
        """
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x # New root

    def left_rotate(self, x):
        """
        Perform a left rotation.
        x is the node to be rotated.
        """
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y # New root

    def insert(self, root, data):
        """Recursively insert data and balance the tree."""
        # 1. Standard BST insertion
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # 2. Update height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor to check for imbalance
        balance = self.get_balance(root)

        # Case 1: Left Left (LL) -> Right Rotate
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # Case 2: Right Right (RR) -> Left Rotate
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # Case 3: Left Right (LR) -> Left rotate child, then Right rotate root
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4: Right Left (RL) -> Right rotate child, then Left rotate root
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        """Helper to verify the tree is sorted."""
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res.extend(self.inorder(root.right))
        return res

# --- Usage Example ---
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    # Insert values that would normally cause a skewed tree (sorted)
    # This will force the AVL tree to rotate multiple times.
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        root = tree.insert(root, val)
        print(f"Inserted {val}, current root: {root.data}")

    print("\nFinal AVL Tree (In-order):", tree.inorder(root))
    # Expected: [10, 20, 25, 30, 40, 50] (Perfectly sorted)

    # Check if it's actually balanced:
    # root should be 30 (or similar) instead of 10.
    print(f"Root of balanced tree: {root.data}")
