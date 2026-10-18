# Linked List Deletion

## 💡 Concept
**Deletion** is the process of removing a node from a linked list. Because linked lists are not contiguous, deleting a node doesn't require shifting elements (unlike arrays). Instead, you simply "bypass" the node you want to remove by changing the pointer of the previous node.

Depending on the location of the node, the logic varies:

### 1. Deletion at the Beginning (Head)
This is the simplest operation. You simply move the head pointer to the next node in the list. The old head is then left for the garbage collector to clean up.

### 2. Deletion at the End (Tail)
To remove the last node, you must traverse the entire list to find the node **immediately before** the tail. You then set that node's `next` pointer to `None`.

### 3. Deletion from the Middle
You traverse to the node just *before* the one you want to delete. You then update its `next` pointer to skip over the target node and point directly to the node that follows it.

**Imagine this:** A line of people holding hands.
- **At the start**: The first person lets go and leaves; the second person is now the new leader.
- **At the end**: The second-to-last person lets go of the last person's hand.
- **In the middle**: Person A is holding Person B's hand, and Person B is holding Person C's hand. To remove Person B, Person A simply lets go of B and reaches over to hold Person C's hand instead.

## ⏱️ Complexity Analysis
**📺 See it in Action**: [Visualize Linked List Deletion here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

| Position | Time Complexity | Why? |
| :--- | :--- | :--- |
| **At Head** | $O(1)$ | Just update the head pointer. |
| **At Tail** | $O(n)$ | Must traverse to find the second-to-last node. |
| **At Middle**| $O(n)$ | Must traverse to find the node before the target. |

**Space Complexity:** $O(1)$ as no extra memory is required.

## 💻 Implementation

Check out the [deletion.py](./deletion.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
- [LeetCode: Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)
- [GeeksforGeeks: Deletion in a Linked List](https://www.geeksforgeeks.org/deletion-in-a-linked-list/)
