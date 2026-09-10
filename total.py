def total(numbers: list[int]) -> int:
    """Return the sum of the integers in numbers."""
    if any(type(number) is not int for number in numbers):
        raise TypeError("numbers must contain only integers")
    return sum(numbers)
