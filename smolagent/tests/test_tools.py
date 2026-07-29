import pytest

from smolagent.tools import fibonacci_number


def test_fibonacci_base_cases():
    assert fibonacci_number(0) == 0
    assert fibonacci_number(1) == 1


def test_fibonacci_small_indices():
    assert fibonacci_number(10) == 55
    assert fibonacci_number(20) == 6765


def test_fibonacci_negative_index_raises():
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci_number(-1)


def test_fibonacci_non_integer_raises():
    with pytest.raises(TypeError):
        fibonacci_number(1.5)