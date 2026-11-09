"""greeting.py - Configurable Greeting and Message Formatter.

Week 3 Demonstration Codebase for Git & GitHub Practice.
Designed for Robotics & AI B.Tech Curriculum.
"""

from typing import Optional
from datetime import datetime


def greet(
    name: str,
    style: str = "standard",
    title: Optional[str] = None
) -> str:
    """Generate a formatted greeting based on specified style and options.

    Supported styles:
        - 'standard': "Hello, <Name>!"
        - 'formal': "Good day, [Title] <Name>."
        - 'casual': "Hey <Name>, what's up?"
        - 'robotics': "System online: Welcome operator <Name>. Telemetry active."
        - 'developer': "[DEBUG] User session initialized for: <Name>."

    Args:
        name: Name of the person or operator.
        style: Style key from supported styles (default: 'standard').
        title: Optional honorific/title (e.g., 'Dr.', 'Prof.', 'Engineer').

    Returns:
        Formatted greeting string.

    Raises:
        TypeError: If name, style, or title is not a string.
        ValueError: If name is empty/whitespace or style is unrecognized.
    """
    clean_name = _validate_name(name)
    clean_style = _validate_style(style)
    clean_title = _validate_optional_title(title)

    if clean_style == "standard":
        return f"Hello, {clean_name}!"

    if clean_style == "formal":
        prefix = f"{clean_title} " if clean_title else ""
        return f"Good day, {prefix}{clean_name}."

    if clean_style == "casual":
        return f"Hey {clean_name}, what's up?"

    if clean_style == "robotics":
        prefix = f"{clean_title} " if clean_title else ""
        return f"System online: Welcome operator {prefix}{clean_name}. Telemetry active."

    if clean_style == "developer":
        return f"[DEBUG] User session initialized for: {clean_name}."

    raise ValueError(f"Unsupported greeting style: '{style}'")


def get_time_based_greeting(name: str, current_hour: Optional[int] = None) -> str:
    """Generate a time-aware greeting (Morning, Afternoon, Evening, Night Owl).

    Args:
        name: Name of the person to greet.
        current_hour: Hour of the day (0-23). If None, uses local system hour.

    Returns:
        Time-appropriate greeting string.

    Raises:
        TypeError: If name is not a string or current_hour is not an integer.
        ValueError: If name is empty or current_hour is outside 0-23.
    """
    clean_name = _validate_name(name)

    if current_hour is None:
        current_hour = datetime.now().hour
    elif not isinstance(current_hour, int) or isinstance(current_hour, bool):
        raise TypeError("current_hour must be an integer between 0 and 23.")
    elif not (0 <= current_hour <= 23):
        raise ValueError(f"current_hour must be between 0 and 23, got {current_hour}.")

    if 5 <= current_hour < 12:
        period = "Good morning"
    elif 12 <= current_hour < 17:
        period = "Good afternoon"
    elif 17 <= current_hour < 22:
        period = "Good evening"
    else:
        period = "Hello, night owl"

    return f"{period}, {clean_name}!"


def format_multiline_banner(name: str, project_name: str = "Robotics & AI Lab") -> str:
    """Generate a formatted terminal banner greeting.

    Args:
        name: Name of the operator.
        project_name: Project or lab identifier.

    Returns:
        Multi-line banner string.

    Raises:
        TypeError: If name or project_name is not a string.
        ValueError: If name or project_name is empty or whitespace.
    """
    clean_name = _validate_name(name)
    if not isinstance(project_name, str):
        raise TypeError(f"Project name must be a string, got {type(project_name).__name__}.")
    clean_project = project_name.strip()
    if not clean_project:
        raise ValueError("Project name cannot be empty or solely whitespace.")

    line = "=" * 48
    return (
        f"{line}\n"
        f"  PROJECT: {clean_project.upper()}\n"
        f"  OPERATOR: {clean_name}\n"
        f"  STATUS: READY FOR VERSION CONTROL EXERCISE\n"
        f"{line}"
    )


def _validate_name(name: object) -> str:
    """Validate that name is a non-empty string."""
    if not isinstance(name, str):
        raise TypeError(f"Name must be a string, got {type(name).__name__}.")
    trimmed = name.strip()
    if not trimmed:
        raise ValueError("Name cannot be empty or solely whitespace.")
    return trimmed


def _validate_style(style: object) -> str:
    """Validate style argument."""
    if not isinstance(style, str):
        raise TypeError(f"Style must be a string, got {type(style).__name__}.")
    lower = style.strip().lower()
    valid_styles = {"standard", "formal", "casual", "robotics", "developer"}
    if lower not in valid_styles:
        raise ValueError(f"Unknown style '{style}'. Allowed styles: {sorted(list(valid_styles))}")
    return lower


def _validate_optional_title(title: object) -> Optional[str]:
    """Validate optional title parameter."""
    if title is None:
        return None
    if not isinstance(title, str):
        raise TypeError(f"Title must be a string or None, got {type(title).__name__}.")
    trimmed = title.strip()
    return trimmed if trimmed else None


if __name__ == "__main__":
    print("=== Greeting Demo ===")
    print(greet("Anant"))
    print(greet("Anant", style="formal", title="Engineer"))
    print(greet("Anant", style="casual"))
    print(greet("Anant", style="robotics"))
    print(greet("Anant", style="developer"))
    print(get_time_based_greeting("Anant"))
    print(format_multiline_banner("Anant", "Git & GitHub Week 3 Lab"))
