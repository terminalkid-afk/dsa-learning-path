# Tree Traversals in Python

"""
Goal: Implement the 4 major ways to traverse a Binary Tree.
Algorithm:
- DFS (Pre, In, Post) uses Recursion.
- BFS (Level-order) uses a Queue.
"""
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeTraversals:
    # --- Depth-First Search (DFS) ---

    def preorder(self, root):
        """Root -> Left -> Right"""
        if not root:
            return []
        return [root.data] + self.preorder(root.left) + self.preorder(root.right)

    def inorder(self, root):
        """Left -> Root -> Right (Sorted for BSTs)"""
        if not root:
            return []
        return self.inorder(root.left) + [root.data] + self.inorder(root.right)

    def postorder(self, root):
        """Left -> Right -> Root"""
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.data]

    # --- Breadth-First Search (BFS) ---

    def level_order(self, root):
        """Visit nodes level by level from top to bottom."""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

# --- Usage Example ---
if __name__ == "__main__":
    # Constructing a sample Binary Tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    traverser = TreeTraversals()

    print("Tree Structure: 1 is root, 2&3 children, 4&5 children of 2, 6 child of 3")
    print(f"Pre-order (Root, L, R):   {traverser.preorder(root)}")
    # Expected: [1, 2, 4, 5, 3, 6]

    print(f"In-order (L, Root, R):    {traverser.inorder(root)}")
    # Expected: [4, 2, 5, 1, 3, 6]

    print(f"Post-order (L, R, Root):  {traverser.postorder(root)}")
    # Expected: [4, 5, 2, 6, 3, 1]

    print(f"Level-order (BFS):       {traverser.level_order(root)}")
    # Expected: [1, 2, 3, 4, 5, 6]
