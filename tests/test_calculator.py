"""test_calculator.py - Unit Tests for Calculator Module.

Week 3 Git & GitHub Testing Suite.
Utilizes Python's built-in unittest framework.
"""

import sys
from pathlib import Path
import unittest

# Ensure src/ is importable
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from src.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root,
    calculate_mean,
)


class TestCalculatorBasicOperations(unittest.TestCase):
    """Test suite for basic arithmetic operations in calculator."""

    def test_add_integers(self):
        """Verify addition of positive and negative integers."""
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-7, 3), -4)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(0, 42), 42)

    def test_add_floats(self):
        """Verify floating-point precision addition."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(add(3.14159, 2.71828), 5.85987, places=5)

    def test_subtract_integers_and_floats(self):
        """Verify subtraction behavior across operands."""
        self.assertEqual(subtract(20, 8), 12)
        self.assertEqual(subtract(5, 12), -7)
        self.assertEqual(subtract(-4, -6), 2)
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3, places=7)

    def test_multiply_integers_and_floats(self):
        """Verify multiplication edge cases and scaling."""
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(-3, -3), 9)
        self.assertEqual(multiply(100, 0), 0)
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0, places=7)

    def test_divide_valid(self):
        """Verify valid division results."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-15, 3), -5.0)
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=6)

    def test_divide_by_zero_raises_exception(self):
        """Ensure division by zero cleanly raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError) as context:
            divide(10, 0)
        self.assertIn("Division by zero", str(context.exception))

        with self.assertRaises(ZeroDivisionError):
            divide(-5.5, 0.0)


class TestCalculatorAdvancedOperations(unittest.TestCase):
    """Test suite for power, square root, and mean operations."""

    def test_power(self):
        """Verify exponentiation calculations."""
        self.assertEqual(power(2, 3), 8.0)
        self.assertEqual(power(5, 0), 1.0)
        self.assertEqual(power(0, 5), 0.0)
        self.assertEqual(power(4, 0.5), 2.0)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(2, -2), 0.25)

    def test_square_root_valid(self):
        """Verify positive square root outputs."""
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(0.25), 0.5)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=6)

    def test_square_root_negative_raises_value_error(self):
        """Verify negative inputs to square_root raise ValueError."""
        with self.assertRaises(ValueError) as context:
            square_root(-4)
        self.assertIn("real domain", str(context.exception))

    def test_calculate_mean_valid(self):
        """Verify mean calculation across numeric samples."""
        self.assertEqual(calculate_mean([10, 20, 30]), 20.0)
        self.assertAlmostEqual(calculate_mean([1.5, 2.5, 3.5, 4.5]), 3.0, places=7)
        self.assertEqual(calculate_mean([42]), 42.0)
        self.assertEqual(calculate_mean([-10, 10]), 0.0)

    def test_calculate_mean_empty_raises_value_error(self):
        """Verify empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_mean([])
        self.assertIn("empty list", str(context.exception))


class TestCalculatorValidation(unittest.TestCase):
    """Test suite ensuring strict type validation."""

    def test_invalid_types_raise_type_error(self):
        """Ensure non-numeric types trigger descriptive TypeErrors."""
        invalid_inputs = ["10", None, [1, 2], {"a": 1}, True, False]
        for val in invalid_inputs:
            with self.subTest(val=val):
                with self.assertRaises(TypeError):
                    add(val, 5)
                with self.assertRaises(TypeError):
                    subtract(5, val)
                with self.assertRaises(TypeError):
                    multiply(val, 2)
                with self.assertRaises(TypeError):
                    divide(10, val)
                with self.assertRaises(TypeError):
                    power(val, 2)
                with self.assertRaises(TypeError):
                    power(2, val)
                with self.assertRaises(TypeError):
                    square_root(val)

    def test_calculate_mean_invalid_container_or_element(self):
        """Verify list-level validation in calculate_mean."""
        with self.assertRaises(TypeError):
            calculate_mean("not a list")  # type: ignore

        with self.assertRaises(TypeError):
            calculate_mean((1, 2, 3))  # type: ignore

        with self.assertRaises(TypeError):
            calculate_mean([1, 2, "three", 4])  # type: ignore

        # Booleans inside list must be rejected
        with self.assertRaises(TypeError):
            calculate_mean([1, True, 3])  # type: ignore


if __name__ == "__main__":
    unittest.main()
