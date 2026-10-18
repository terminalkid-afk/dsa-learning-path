# Postfix Notation Evaluation

## 💡 Concept
**Postfix notation**, also known as **Reverse Polish Notation (RPN)**, is a mathematical notation in which every operator follows all of its operands. 

**Example:** 
- Standard (Infix): `3 + 4`
- Postfix: `3 4 +`

In standard math (Infix), we use parentheses to define the order of operations (e.g., `(3 + 4) * 2`). In Postfix, **parentheses are never needed**. The position of the operator naturally determines the order of evaluation.

### Why do we use Postfix?
Computers struggle with Infix notation because they have to "look ahead" to check for operator precedence (like doing multiplication before addition). Postfix is perfect for computers because it can be solved in a single linear pass using a **Stack**.

## ⚙️ Visual Logic: How the Stack Evaluates Postfix
Suppose we have the postfix expression: `5 3 2 * +`

1. **Read `5`**: It's a number $\rightarrow$ **Push** to stack. Stack: `[5]`
2. **Read `3`**: It's a number $\rightarrow$ **Push** to stack. Stack: `[5, 3]`
3. **Read `2`**: It's a number $\rightarrow$ **Push** to stack. Stack: `[5, 3, 2]`
4. **Read `*`**: It's an operator!
   - **Pop** `2` (operand 2)
   - **Pop** `3` (operand 1)
   - Calculate `3 * 2 = 6`
   - **Push** `6` back. Stack: `[5, 6]`
5. **Read `+`**: It's an operator!
   - **Pop** `6` (operand 2)
   - **Pop** `5` (operand 1)
   - Calculate `5 + 6 = 11`
   - **Push** `11` back. Stack: `[11]`

**Final Result:** `11`

## ⏱️ Complexity Analysis

| Aspect | Complexity | Why? |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We scan the expression exactly once. |
| **Space Complexity** | $O(n)$ | In the worst case, we store all operands on the stack. |

## 💻 Implementation

Check out the [postfix.py](./postfix.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [LeetCode: Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- [GeeksforGeeks: Evaluation of Postfix Expression](https://www.geeksforgeeks.org/stack-set-2-evaluation-of-postfix-expression/)
