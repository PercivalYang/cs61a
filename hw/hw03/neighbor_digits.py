def neighbor_digits(num, prev_digits=-1):
    """
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    if num < 10:
        return num == prev_digits
    last = num%10
    rest = num//10
    return int(prev_digits==last or rest%10==last) + neighbor_digits(rest,last)
