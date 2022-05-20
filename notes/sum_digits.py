def sum_digits(n):
    """
    >>> sum_digits(9)
    9
    >>> sum_digits(19)
    10
    >>> sum_digits(2019)
    12
    """
    if n // 10:
        return sum_digits(n//10) + n%10
    return n
