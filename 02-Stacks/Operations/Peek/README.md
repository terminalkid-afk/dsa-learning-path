# Peek, IsEmpty, and IsFull

## 💡 Concept
While Push and Pop change the stack, **Peek**, **IsEmpty**, and **IsFull** are "helper" operations. They provide information about the stack without modifying its contents.

### 1. Peek (or Top)
**Peek** allows you to look at the element currently at the top of the stack without removing it. This is useful when you need to make a decision based on the top element before deciding whether to pop it.

### 2. IsEmpty
**IsEmpty** returns a boolean value (`True` or `False`) indicating whether the stack contains any elements. This is critical to check before calling `Pop` or `Peek` to avoid a **Stack Underflow**.

### 3. IsFull
**IsFull** returns `True` if the stack has reached its maximum defined capacity. This is only applicable to **Array-based implementations** where the size is fixed. In dynamic lists (like Python's `list`), the stack grows as needed, so `IsFull` is rarely used unless a manual limit is set.

**Imagine this:** A stack of books.
- **Peek**: Looking at the title of the top book.
- **IsEmpty**: Checking if the table is completely clear.
- **IsFull**: Checking if the stack is so high it's about to touch the ceiling.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Peek** | $O(1)$ | $O(1)$ |
| **IsEmpty** | $O(1)$ | $O(1)$ |
| **IsFull** | $O(1)$ | $O(1)$ |

These operations are constant time because they simply check a pointer or a length property.

## 💻 Implementation

The logic for these helpers is integrated into the main Stack class. You can find the implementation in the [push_pop.py](../Push-Pop/push_pop.py) file.

## 🚀 Practice Problems
- [LeetCode: Min Stack](https://leetcode.com/problems/min-stack/) (Requires a modified Peek to track the minimum element!)
- [LeetCode: Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
