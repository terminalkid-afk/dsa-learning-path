# Prefix Evaluation in Python

"""
Goal: Evaluate a mathematical expression given in Prefix (Polish Notation).
Algorithm: Scan the expression from right to left, using a stack to store operands.
"""

def evaluate_prefix(expression):
    # Stack to hold the operands
    stack = []

    # Split the expression into tokens and reverse them to scan Right-to-Left
    tokens = expression.split()
    tokens.reverse()

    for token in tokens:
        # If the token is a digit, push it to the stack
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(int(token))
        else:
            # The token is an operator. Pop two operands from the stack.
            if len(stack) < 2:
                raise ValueError("Invalid prefix expression: not enough operands.")

            # In Prefix evaluation (Right-to-Left scan):
            # The first pop is the FIRST operand (Left side)
            # The second pop is the SECOND operand (Right side)
            val1 = stack.pop()
            val2 = stack.pop()

            # Apply the operator
            if token == '+':
                stack.append(val1 + val2)
            elif token == '-':
                stack.append(val1 - val2)
            elif token == '*':
                stack.append(val1 * val2)
            elif token == '/':
                # Using integer division for simplicity
                stack.append(int(val1 / val2))
            else:
                raise ValueError(f"Unsupported operator: {token}")

    # The final result should be the only element left in the stack
    if len(stack) != 1:
        raise ValueError("Invalid prefix expression: too many operands.")

    return stack.pop()

# --- Usage Example ---
if __name__ == "__main__":
    # Test Case 1: Simple expression (+ 3 4) -> 7
    expr1 = "+ 3 4"
    print(f"Expression: {expr1} | Result: {evaluate_prefix(expr1)}")

    # Test Case 2: More complex (+ 5 * 3 2) -> 5 + (3*2) = 11
    expr2 = "+ 5 * 3 2"
    print(f"Expression: {expr2} | Result: {evaluate_prefix(expr2)}")

    # Test Case 3: With subtraction and division (- 10 / 4 2) -> 10 - (4/2) = 8
    expr3 = "- 10 / 4 2"
    print(f"Expression: {expr3} | Result: {evaluate_prefix(expr3)}")

    # Test Case 4: Complex nested (/ * + 100 200 2 10) -> ((100+200)*2)/10 = 60
    expr4 = "/ * + 100 200 2 10"
    print(f"Expression: {expr4} | Result: {evaluate_prefix(expr4)}")
