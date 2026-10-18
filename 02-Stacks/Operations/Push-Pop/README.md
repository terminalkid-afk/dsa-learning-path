# Push & Pop Operations

## 💡 Concept
The heart of a stack is the **Push** and **Pop** operations. These are the only ways to add or remove data from a stack, ensuring the **LIFO (Last-In-First-Out)** property.

### 1. Push
**Push** means adding a new element to the top of the stack. If the stack has a fixed size and is already full, trying to push a new element results in a **Stack Overflow**.

### 2. Pop
**Pop** means removing the element that is currently at the top. If you try to pop from an empty stack, it results in a **Stack Underflow**.

**Imagine this:** A Pez dispenser. 
- When you load candy into the dispenser, you are **Pushing**.
- When you tilt your head back and a candy comes out, you are **Popping**.
- The last candy you put in is always the first one to come out.

## ⚙️ Visual Logic
**📺 See it in Action**: [Visualize Stack Operations here](https://www.dsavisualizer.in/visualizer) (Interactive Animation)

Let's trace a stack:

1. **Push(10)**: Stack $\rightarrow$ `[10]` (Top is 10)
2. **Push(20)**: Stack $\rightarrow$ `[10, 20]` (Top is 20)
3. **Push(30)**: Stack $\rightarrow$ `[10, 20, 30]` (Top is 30)
4. **Pop()**: Removes `30`. Stack $\rightarrow$ `[10, 20]` (Top is 20)
5. **Pop()**: Removes `20`. Stack $\rightarrow$ `[10]` (Top is 10)

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Push** | $O(1)$ | $O(1)$ |
| **Pop** | $O(1)$ | $O(1)$ |

Neither operation requires looping or searching; they both happen instantly at the "Top" pointer.

## 💻 Implementation

Check out the [push_pop.py](./push_pop.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [LeetCode: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (The most classic Stack problem!)
