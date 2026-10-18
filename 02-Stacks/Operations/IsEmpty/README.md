# IsEmpty Operation

## 💡 Concept
The **IsEmpty** operation is a simple but vital safety check for any stack. It returns a boolean value (`True` or `False`) based on whether the stack contains any elements.

### Why is it so important?
If you attempt to perform a `Pop` or `Peek` operation on a stack that has no elements, the program will crash or throw an error. This is known as **Stack Underflow**. 

By checking `IsEmpty()` first, you can gracefully handle the situation:
```python
if not stack.is_empty():
    stack.pop()
else:
    print("The stack is already empty!")
```

**Imagine this:** You are trying to take a cookie from a cookie jar. Before you reach in, you glance inside to see if it's empty. Checking for the presence of cookies is exactly what `IsEmpty` does for a stack.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **IsEmpty** | $O(1)$ | $O(1)$ |

The time complexity is constant because the stack usually keeps track of its current size or top index. Checking if that number is `0` takes the same amount of time regardless of how large the stack could potentially be.

## 💻 Implementation

This logic is implemented as a method within the Stack class. See the [push_pop.py](../Push-Pop/push_pop.py) file.

## 🚀 Practice Problems
- [LeetCode: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (You must check if the stack is empty at the end to ensure all parentheses were closed).
