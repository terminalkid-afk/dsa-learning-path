# Reversing a Linked List

## 💡 Concept
**Reversing a Linked List** is a classic problem that tests your understanding of how pointers work. The goal is to flip the direction of every pointer in the list so that the original tail becomes the new head, and the original head becomes the new tail.

### The Logic
To reverse a singly linked list, we need to keep track of three different nodes at each step:
1. **Previous**: The node that will become the `next` of the current node.
2. **Current**: The node we are currently processing.
3. **Next**: A temporary pointer to store the rest of the list before we overwrite the current node's pointer.

**Imagine this:** A line of people where each person is pointing to the person in front of them. To reverse the line, each person must turn around and point to the person who was previously *behind* them. But before you turn around, you must first remember who was in front of you so you don't lose the rest of the line!

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Linked List Reversal here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Suppose we have: `10 -> 20 -> 30 -> None`

1. **Start**: `prev = None`, `curr = 10`.
2. **Step 1**: 
   - Save `next` as `20`.
   - Change `10.next` to `None` (prev).
   - Move `prev` to `10`, `curr` to `20`.
   - List: `None <- 10`  (Remaining: `20 -> 30 -> None`)
3. **Step 2**:
   - Save `next` as `30`.
   - Change `20.next` to `10` (prev).
   - Move `prev` to `20`, `curr` to `30`.
   - List: `None <- 10 <- 20` (Remaining: `30 -> None`)
4. **Step 3**:
   - Save `next` as `None`.
   - Change `30.next` to `20` (prev).
   - Move `prev` to `30`, `curr` to `None`.
   - List: `None <- 10 <- 20 <- 30`

**Final Result**: The new head is `30`. The list is `30 -> 20 -> 10 -> None`.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Reverse** | $O(n)$ | $O(1)$ |

We visit each node exactly once and only use a few extra pointers regardless of the list size.

## 💻 Implementation

Check out the [reverse.py](./reverse.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [LeetCode: Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [GeeksforGeeks: Reverse a Linked List](https://www.geeksforgeeks.org/reverse-a-linked-list/)
