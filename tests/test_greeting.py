"""test_greeting.py - Unit Tests for Greeting Module.

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

from src.greeting import (
    greet,
    get_time_based_greeting,
    format_multiline_banner,
)


class TestGreetingStyles(unittest.TestCase):
    """Test suite for greeting generation and formatting styles."""

    def test_default_standard_greeting(self):
        """Verify default style is standard greeting."""
        result = greet("Anant")
        self.assertEqual(result, "Hello, Anant!")

    def test_formal_greeting_with_and_without_title(self):
        """Verify formal greeting formatting."""
        without_title = greet("Sarah", style="formal")
        self.assertEqual(without_title, "Good day, Sarah.")

        with_title = greet("Sarah", style="formal", title="Dr.")
        self.assertEqual(with_title, "Good day, Dr. Sarah.")

        with_empty_title = greet("Sarah", style="formal", title="   ")
        self.assertEqual(with_empty_title, "Good day, Sarah.")

    def test_casual_greeting(self):
        """Verify casual greeting format."""
        result = greet("Alex", style="casual")
        self.assertEqual(result, "Hey Alex, what's up?")

    def test_robotics_greeting(self):
        """Verify robotics operator greeting format."""
        result = greet("Anant", style="robotics", title="Commander")
        self.assertEqual(
            result,
            "System online: Welcome operator Commander Anant. Telemetry active."
        )

        result_no_title = greet("Anant", style="robotics")
        self.assertEqual(
            result_no_title,
            "System online: Welcome operator Anant. Telemetry active."
        )

    def test_developer_greeting(self):
        """Verify developer debug session greeting format."""
        result = greet("Linus", style="developer")
        self.assertEqual(result, "[DEBUG] User session initialized for: Linus.")

    def test_case_insensitivity_of_style(self):
        """Ensure style names are case-insensitive and stripped."""
        self.assertEqual(greet("Anant", style="  STANDARD  "), "Hello, Anant!")
        self.assertEqual(greet("Anant", style="Robotics"), "System online: Welcome operator Anant. Telemetry active.")


class TestTimeBasedGreeting(unittest.TestCase):
    """Test suite for time-aware greetings."""

    def test_morning_greeting(self):
        """Hours 5 to 11 should yield Good morning."""
        self.assertEqual(get_time_based_greeting("Anant", current_hour=8), "Good morning, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=5), "Good morning, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=11), "Good morning, Anant!")

    def test_afternoon_greeting(self):
        """Hours 12 to 16 should yield Good afternoon."""
        self.assertEqual(get_time_based_greeting("Anant", current_hour=12), "Good afternoon, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=14), "Good afternoon, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=16), "Good afternoon, Anant!")

    def test_evening_greeting(self):
        """Hours 17 to 21 should yield Good evening."""
        self.assertEqual(get_time_based_greeting("Anant", current_hour=17), "Good evening, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=19), "Good evening, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=21), "Good evening, Anant!")

    def test_night_greeting(self):
        """Hours 22 to 4 should yield Hello, night owl."""
        self.assertEqual(get_time_based_greeting("Anant", current_hour=22), "Hello, night owl, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=23), "Hello, night owl, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=0), "Hello, night owl, Anant!")
        self.assertEqual(get_time_based_greeting("Anant", current_hour=4), "Hello, night owl, Anant!")

    def test_default_current_hour(self):
        """Calling without current_hour uses system datetime cleanly."""
        res = get_time_based_greeting("Anant")
        self.assertTrue(res.endswith(", Anant!"))


class TestBannerAndValidation(unittest.TestCase):
    """Test banner creation and error handling."""

    def test_format_multiline_banner(self):
        """Ensure banner contains project name and operator name."""
        banner = format_multiline_banner("Anant", "ROS2 Autonomous Rover")
        self.assertIn("ROS2 AUTONOMOUS ROVER", banner)
        self.assertIn("OPERATOR: Anant", banner)
        self.assertIn("STATUS: READY", banner)

    def test_empty_or_whitespace_name_raises_value_error(self):
        """Blank names should raise ValueError."""
        with self.assertRaises(ValueError):
            greet("")
        with self.assertRaises(ValueError):
            greet("   ")
        with self.assertRaises(ValueError):
            get_time_based_greeting("   \t  ")
        with self.assertRaises(ValueError):
            format_multiline_banner("   ", "Valid Project")

    def test_empty_or_whitespace_project_name_raises_value_error(self):
        """Blank project name in banner should raise ValueError."""
        with self.assertRaises(ValueError):
            format_multiline_banner("Anant", "")
        with self.assertRaises(ValueError):
            format_multiline_banner("Anant", "   ")

    def test_invalid_type_name_raises_type_error(self):
        """Non-string names should raise TypeError."""
        with self.assertRaises(TypeError):
            greet(12345)  # type: ignore
        with self.assertRaises(TypeError):
            greet(None)  # type: ignore
        with self.assertRaises(TypeError):
            format_multiline_banner(123, "Project")  # type: ignore
        with self.assertRaises(TypeError):
            format_multiline_banner("Anant", 456)  # type: ignore

    def test_invalid_title_type_raises_type_error(self):
        """Non-string, non-None title should raise TypeError."""
        with self.assertRaises(TypeError):
            greet("Anant", style="formal", title=123)  # type: ignore

    def test_invalid_style_raises_value_error(self):
        """Unknown styles should raise descriptive ValueError."""
        with self.assertRaises(ValueError) as ctx:
            greet("Anant", style="nonexistent_style")
        self.assertIn("Unknown style", str(ctx.exception))

    def test_invalid_hour_bounds_and_types(self):
        """Hours < 0 or > 23 or invalid type should raise errors."""
        with self.assertRaises(ValueError):
            get_time_based_greeting("Anant", current_hour=-1)
        with self.assertRaises(ValueError):
            get_time_based_greeting("Anant", current_hour=24)
        with self.assertRaises(TypeError):
            get_time_based_greeting("Anant", current_hour="12")  # type: ignore
        with self.assertRaises(TypeError):
            get_time_based_greeting("Anant", current_hour=12.5)  # type: ignore
        with self.assertRaises(TypeError):
            get_time_based_greeting("Anant", current_hour=True)  # type: ignore


if __name__ == "__main__":
    unittest.main()
