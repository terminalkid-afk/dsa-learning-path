# Introduction to Stacks

## 💡 Concept
A **Stack** is a linear data structure that follows a particular order in which operations are performed. The order is **LIFO (Last-In-First-Out)**.

**Think of it like this:** Imagine a stack of plates in a cafeteria. 
- You place the first plate on the table.
- You place the second plate on top of the first.
- When you want a plate, you **must** take the one from the top first (the last one you put there).

You cannot magically pull a plate from the bottom without removing everything on top of it first.

### Why do we need Stacks?
Stacks are fundamental to how computers actually work. They are used in:
- **Function Calls**: When a function calls another, the current state is "pushed" onto the call stack.
- **Undo/Redo Mechanisms**: Your text editor stores your changes in a stack. When you hit `Ctrl+Z`, it "pops" the last action.
- **Browser History**: The "Back" button pops the last visited URL from the history stack.
- **Expression Evaluation**: Used to convert and solve mathematical expressions (like Postfix notation).

## ⚙️ Core Operations
A stack primarily supports these operations:
1. **Push**: Adding an element to the top of the stack.
2. **Pop**: Removing the element from the top of the stack.
3. **Peek (or Top)**: Looking at the top element without removing it.
4. **IsEmpty**: Checking if the stack has any elements.
5. **IsFull**: Checking if the stack has reached its maximum capacity (relevant for array-based stacks).

## ⏱️ Complexity Analysis

| Operation | Time Complexity | Why? |
| :--- | :--- | :--- |
| **Push** | $O(1)$ | We only add to the top; no shifting required. |
| **Pop** | $O(1)$ | We only remove from the top. |
| **Peek** | $O(1)$ | Immediate access to the top element. |
| **Search** | $O(n)$ | In the worst case, we must pop everything to find an item. |

**Space Complexity:** $O(n)$ to store $n$ elements.

---

## 🚀 Learning Path for Stacks
In this section, we will cover:
1. **Operations**: Detailed look at Push, Pop, and Peek.
2. **Polish Notation**: How stacks evaluate Prefix and Postfix expressions.
3. **Implementation**: How to build a stack using Arrays vs. Linked Lists.
