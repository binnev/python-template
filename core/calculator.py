# A simple calculator library with basic arithmetic operations


def add(a: float, b: float) -> float:
    """
    Return the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Return the difference of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of the two numbers.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Return the product of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the division of two numbers. Raise an error if dividing by zero.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
