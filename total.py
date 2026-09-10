"""Utilities for calculating totals."""


def total(numbers: list[int]) -> int:
    """Return the sum of *numbers*.

    Every item must be an integer; an empty list has a total of zero.
    """
    if any(type(number) is not int for number in numbers):
        raise TypeError("numbers must contain only integers")
    return sum(numbers)
