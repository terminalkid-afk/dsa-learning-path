# IsFull Operation

## 💡 Concept
The **IsFull** operation checks whether a stack has reached its maximum predefined capacity.

### When is this used?
In many modern languages like Python, lists are dynamic, meaning they grow automatically as you add more elements. In such cases, a stack is almost never "full" until the computer runs out of physical memory.

However, **IsFull** is critical in:
- **Low-level languages (C/C++)**: Where stacks are often implemented using fixed-size arrays.
- **Embedded Systems**: Where memory is extremely limited and you must define a strict cap on how much data a stack can hold.
- **Fixed-size Buffers**: When you want to prevent a stack from consuming too much memory and crashing the system.

If you try to `Push` an element onto a stack that `IsFull` returns `True` for, you encounter a **Stack Overflow**.

**Imagine this:** A Pringles can. Once the can is filled to the brim with chips, you cannot fit another chip inside without crushing the others or removing some. The can has reached its "IsFull" state.

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **IsFull** | $O(1)$ | $O(1)$ |

The time complexity is constant because it simply compares the current number of elements with the maximum capacity limit.

## 💻 Implementation

In our Python implementation, we can simulate this by adding a `max_size` parameter to our Stack class.

```python
def is_full(self):
    return len(self.items) == self.max_size
```

See the implementation in the [Implementation Section](../Implementation/Array-Implementation/README.md).

## 🚀 Practice Problems
- [GeeksforGeeks: Stack Overflow and Underflow](https://www.geeksforgeeks.org/stack-overflow-and-underflow/)
