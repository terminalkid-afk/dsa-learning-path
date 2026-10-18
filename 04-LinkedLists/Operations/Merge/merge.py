# Merge Sorted Linked Lists in Python

"""
Goal: Merge two sorted singly linked lists into one single sorted linked list.
Algorithm: Use two pointers to compare elements from both lists and link them in ascending order.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Helper to add elements to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Print the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

def merge_sorted_lists(head1, head2):
    """
    Merges two sorted linked lists into one sorted linked list.
    Time Complexity: O(n + m)
    Space Complexity: O(1) - we reuse the existing nodes.
    """
    # Create a dummy node to act as the starting point of the merged list
    dummy = Node(0)
    tail = dummy

    # Traverse both lists until one of them is exhausted
    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # If any nodes remain in either list, attach them to the end
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    # The merged list starts after the dummy node
    return dummy.next

# --- Usage Example ---
if __name__ == "__main__":
    # List 1: 1 -> 3 -> 5
    list1 = LinkedList()
    for val in [1, 3, 5]:
        list1.insert(val)

    # List 2: 2 -> 4 -> 6
    list2 = LinkedList()
    for val in [2, 4, 6]:
        list2.insert(val)

    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()

    print("\nMerging lists...")
    merged_head = merge_sorted_lists(list1.head, list2.head)

    # Wrap the merged head back into a LinkedList object for easy display
    result_list = LinkedList()
    result_list.head = merged_head
    print("Merged Sorted List:")
    result_list.display() # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
