"""calculator.py - Modular Arithmetic and Scientific Calculation Module.

Week 3 Demonstration Codebase for Git & GitHub Practice.
Designed for Robotics & AI B.Tech Curriculum.
"""

from typing import Union, List
import math

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the arithmetic sum of two numbers.

    Args:
        a: First numeric operand.
        b: Second numeric operand.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If either operand is not an int or float.
    """
    _validate_numeric(a, "First operand 'a'")
    _validate_numeric(b, "Second operand 'b'")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the arithmetic difference of two numbers (a - b).

    Args:
        a: Minuend.
        b: Subtrahend.

    Returns:
        The difference of a and b.

    Raises:
        TypeError: If either operand is not an int or float.
    """
    _validate_numeric(a, "First operand 'a'")
    _validate_numeric(b, "Second operand 'b'")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the arithmetic product of two numbers.

    Args:
        a: Multiplicand.
        b: Multiplier.

    Returns:
        The product of a and b.

    Raises:
        TypeError: If either operand is not an int or float.
    """
    _validate_numeric(a, "First operand 'a'")
    _validate_numeric(b, "Second operand 'b'")
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return the quotient of dividing a by b (a / b).

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        The floating-point quotient.

    Raises:
        TypeError: If either operand is not an int or float.
        ZeroDivisionError: If divisor b is equal to zero.
    """
    _validate_numeric(a, "Dividend 'a'")
    _validate_numeric(b, "Divisor 'b'")
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """Raise a base to the specified exponent.

    Args:
        base: The base value.
        exponent: The power to which base is raised.

    Returns:
        base ** exponent.

    Raises:
        TypeError: If either base or exponent is not numeric.
    """
    _validate_numeric(base, "Base")
    _validate_numeric(exponent, "Exponent")
    return math.pow(base, exponent)


def square_root(x: Number) -> float:
    """Calculate the square root of a non-negative number.

    Args:
        x: Non-negative number.

    Returns:
        The square root of x.

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is strictly negative.
    """
    _validate_numeric(x, "Value 'x'")
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number in real domain.")
    return math.sqrt(x)


def calculate_mean(values: List[Number]) -> float:
    """Calculate the arithmetic mean of a sequence of numeric values.

    Useful for robotic sensor readings and telemetry data smoothing.

    Args:
        values: List of numeric values.

    Returns:
        Floating-point mean.

    Raises:
        TypeError: If values is not a list or contains non-numeric elements.
        ValueError: If values list is empty.
    """
    if not isinstance(values, list):
        raise TypeError("Input 'values' must be a list.")
    if len(values) == 0:
        raise ValueError("Cannot calculate mean of an empty list.")
    for idx, item in enumerate(values):
        _validate_numeric(item, f"Element at index {idx}")
    return sum(values) / len(values)


def _validate_numeric(val: object, param_name: str) -> None:
    """Internal helper to validate numeric types (int, float, but not bool)."""
    # In Python, bool is a subclass of int, so we explicitly disallow booleans.
    if isinstance(val, bool) or not isinstance(val, (int, float)):
        raise TypeError(f"{param_name} must be an integer or float, got {type(val).__name__}.")


if __name__ == "__main__":
    print("=== Calculator Demo ===")
    print(f"10 + 5  = {add(10, 5)}")
    print(f"10 - 5  = {subtract(10, 5)}")
    print(f"10 * 5  = {multiply(10, 5)}")
    print(f"10 / 5  = {divide(10, 5)}")
    print(f"2 ^ 8   = {power(2, 8)}")
    print(f"sqrt(81)= {square_root(81)}")
    print(f"Mean sensor data [12.4, 12.6, 12.5, 12.9] = {calculate_mean([12.4, 12.6, 12.5, 12.9]):.2f}")

