# Postfix Evaluation in Python

"""
Goal: Evaluate a mathematical expression given in Postfix (Reverse Polish Notation).
Algorithm: Use a stack to store operands and apply operators to the top two elements.
"""

def evaluate_postfix(expression):
    # Stack to hold the operands
    stack = []

    # Split the expression into tokens (numbers and operators)
    tokens = expression.split()

    for token in tokens:
        # If the token is a digit, push it to the stack
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(int(token))
        else:
            # The token is an operator. Pop two operands from the stack.
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression: not enough operands.")

            # The first pop is the second operand (Right side)
            val2 = stack.pop()
            # The second pop is the first operand (Left side)
            val1 = stack.pop()

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
        raise ValueError("Invalid postfix expression: too many operands.")

    return stack.pop()

# --- Usage Example ---
if __name__ == "__main__":
    # Test Case 1: Simple expression (3 4 +) -> 7
    expr1 = "3 4 +"
    print(f"Expression: {expr1} | Result: {evaluate_postfix(expr1)}")

    # Test Case 2: More complex (5 3 2 * +) -> 5 + (3*2) = 11
    expr2 = "5 3 2 * +"
    print(f"Expression: {expr2} | Result: {evaluate_postfix(expr2)}")

    # Test Case 3: With subtraction and division (10 2 / 3 +) -> (10/2) + 3 = 8
    expr3 = "10 2 / 3 +"
    print(f"Expression: {expr3} | Result: {evaluate_postfix(expr3)}")

    # Test Case 4: Complex nested (100 200 + 2 * 10 /) -> ((100+200)*2)/10 = 60
    expr4 = "100 200 + 2 * 10 /"
    print(f"Expression: {expr4} | Result: {evaluate_postfix(expr4)}")
