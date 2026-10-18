# Array-Based Stack Implementation

## 💡 Concept
An **Array-based Stack** is a stack implemented using a fixed-size array (or a dynamic list in Python). This is the most common way to implement a stack when the maximum number of elements is known or when you want fast, contiguous memory access.

In this implementation:
- The **bottom** of the stack is index `0`.
- The **top** of the stack is the last element currently in the array.

### How it works:
- **Push**: We simply add an element to the end of the array.
- **Pop**: We remove the element from the end of the array.
- **Peek**: We look at the element at the very last index.

**Imagine this:** A stack of trays in a cafeteria. The array is the physical space on the table. As you add trays, the stack grows "upwards" (to higher indices in the array). When you take one, you always take the one that was added last.

### Pros and Cons
| Pros | Cons |
| :--- | :--- |
| **Speed**: $O(1)$ for all basic operations. | **Fixed Size**: In low-level languages, you must define the size upfront. |
| **Memory**: Very efficient as it uses contiguous memory. | **Resizing Cost**: If the array fills up, resizing it to a larger array takes $O(n)$ time. |

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Push** | $O(1)$ | $O(1)$ |
| **Pop** | $O(1)$ | $O(1)$ |
| **Peek** | $O(1)$ | $O(1)$ |

**Overall Space Complexity**: $O(n)$ to store $n$ elements.

## 💻 Implementation

Check out the [stack_array.py](./stack_array.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [GeeksforGeeks: Stack using Array](https://www.geeksforgeeks.org/stack-using-array/)
