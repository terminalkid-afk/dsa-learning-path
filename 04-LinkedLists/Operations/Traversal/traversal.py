# Linked List Traversal in Python

"""
Goal: Implement and demonstrate traversal for Singly, Doubly, and Circular Linked Lists.
Algorithm: Use a pointer to visit each node sequentially until the end is reached.
"""

class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedListTraversal:
    @staticmethod
    def traverse_singly(head):
        """Traverse a Singly Linked List from head to tail."""
        if not head:
            print("List is empty.")
            return

        print("Singly Linked List Traversal: ", end="")
        current = head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    @staticmethod
    def traverse_doubly_forward(head):
        """Traverse a Doubly Linked List forward."""
        if not head:
            print("List is empty.")
            return

        print("Doubly Linked List (Forward): ", end="")
        current = head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    @staticmethod
    def traverse_doubly_backward(tail):
        """Traverse a Doubly Linked List backward from tail."""
        if not tail:
            print("List is empty.")
            return

        print("Doubly Linked List (Backward): ", end="")
        current = tail
        while current:
            print(f"{current.data} -> ", end="")
            current = current.prev
        print("None")

    @staticmethod
    def traverse_circular(head):
        """Traverse a Circular Linked List until we hit the head again."""
        if not head:
            print("List is empty.")
            return

        print("Circular Linked List Traversal: ", end="")
        current = head
        while True:
            print(f"{current.data} -> ", end="")
            current = current.next
            if current == head:
                break
        print("(Back to Head)")

# --- Usage Example ---
if __name__ == "__main__":
    # 1. Setup Singly Linked List: 10 -> 20 -> 30 -> None
    s1 = SinglyNode(10)
    s2 = SinglyNode(20)
    s3 = SinglyNode(30)
    s1.next = s2
    s2.next = s3

    # 2. Setup Doubly Linked List: None <- 10 <-> 20 <-> 30 -> None
    d1 = DoublyNode(10)
    d2 = DoublyNode(20)
    d3 = DoublyNode(30)
    d1.next = d2
    d2.prev = d1
    d2.next = d3
    d3.prev = d2

    # 3. Setup Circular Linked List: 10 -> 20 -> 30 -> (back to 10)
    c1 = SinglyNode(10)
    c2 = SinglyNode(20)
    c3 = SinglyNode(30)
    c1.next = c2
    c2.next = c3
    c3.next = c1

    traverser = LinkedListTraversal()
    traverser.traverse_singly(s1)
    traverser.traverse_doubly_forward(d1)
    traverser.traverse_doubly_backward(d3)
    traverser.traverse_circular(c1)
