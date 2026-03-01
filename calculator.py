"""A simple command-line calculator application."""

import operator


OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def get_number(prompt):
    """Prompt the user for a number and return it as a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operator():
    """Prompt the user for an operator and return it."""
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in OPERATIONS:
            return op
        print("Invalid operator. Please choose +, -, *, or /.")


def calculate(a, op, b):
    """Perform a calculation and return the result.

    Args:
        a: First number.
        op: Operator string ('+', '-', '*', '/').
        b: Second number.

    Returns:
        The result of the operation.

    Raises:
        ZeroDivisionError: If dividing by zero.
        ValueError: If the operator is invalid.
    """
    if op not in OPERATIONS:
        raise ValueError(f"Unknown operator: {op}")
    if op == "/" and b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return OPERATIONS[op](a, b)


def main():
    """Run the calculator in a loop until the user quits."""
    print("=== Python Calculator ===")
    print("Type 'q' to quit.\n")

    while True:
        a = get_number("Enter first number: ")
        op = get_operator()
        b = get_number("Enter second number: ")

        try:
            result = calculate(a, op, b)
            print(f"\n  {a} {op} {b} = {result}\n")
        except ZeroDivisionError as e:
            print(f"\nError: {e}\n")

        again = input("Another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
