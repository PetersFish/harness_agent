"""Side-effect-free learning tools for smolagents.

These tools do not access the network, filesystem, or shell. They exist
to practice tool selection and parameter passing with a ToolCallingAgent.
"""

from __future__ import annotations

from smolagents import tool


@tool
def fibonacci_number(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed).

    Args:
        n: A non-negative integer index into the Fibonacci sequence.
            fibonacci_number(0) == 0, fibonacci_number(1) == 1.

    Returns:
        The n-th Fibonacci number.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a