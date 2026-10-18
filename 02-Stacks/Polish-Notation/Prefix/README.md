# Prefix Notation Evaluation

## 💡 Concept
**Prefix notation**, also known as **Polish Notation**, is a mathematical notation in which every operator precedes its operands.

**Example:**
- Standard (Infix): `3 + 4`
- Postfix: `3 4 +`
- Prefix: `+ 3 4`

Like Postfix, Prefix notation eliminates the need for parentheses because the operator's position explicitly defines the order of operations. While humans find Infix intuitive, computers prefer Prefix or Postfix because they can be evaluated in a single pass using a **Stack**.

### Why do we use Prefix?
It is primarily used in certain compiler designs and functional programming languages (like Lisp), where functions (operators) are called before their arguments (operands).

## ⚙️ Visual Logic: How the Stack Evaluates Prefix
Evaluating Prefix is almost exactly like Postfix, but with two key differences:
1. We scan the expression from **Right to Left** (backwards).
2. When we pop operands, the **first pop is the first operand** (left side) and the **second pop is the second operand** (right side).

Suppose we have the prefix expression: `+ 5 * 3 2`

1. **Scan Right to Left**:
2. **Read `2`**: It's a number $\rightarrow$ **Push** to stack. Stack: `[2]`
3. **Read `3`**: It's a number $\rightarrow$ **Push** to stack. Stack: `[2, 3]`
4. **Read `*`**: It's an operator!
   - **Pop** `3` (operand 1)
   - **Pop** `2` (operand 2)
   - Calculate `3 * 2 = 6`
   - **Push** `6` back. Stack: `[6]`
5. **Read `5`**: It's a number $\rightarrow$ **Push** to stack. Stack: `[6, 5]`
6. **Read `+`**: It's an operator!
   - **Pop** `5` (operand 1)
   - **Pop** `6` (operand 2)
   - Calculate `5 + 6 = 11`
   - **Push** `11` back. Stack: `[11]`

**Final Result:** `11`

## ⏱️ Complexity Analysis

| Aspect | Complexity | Why? |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We scan the expression exactly once (backwards). |
| **Space Complexity** | $O(n)$ | In the worst case, we store all operands on the stack. |

## 💻 Implementation

Check out the [prefix.py](./prefix.py) file for the clean Python implementation.

## 🚀 Practice Problems
- [GeeksforGeeks: Evaluation of Prefix Expression](https://www.geeksforgeeks.org/stack-set-2-evaluation-of-prefix-expression/)
- [LeetCode: Basic Calculator](https://leetcode.com/problems/basic-calculator/) (A challenging problem that involves parsing and stack-based evaluation).
