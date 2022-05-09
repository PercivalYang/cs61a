def has_subseq(n, seq):
    """
    >>> has_subseq(123,12)
    True
    >>> has_subseq(141,11)
    True
    >>> has_subseq(144,12)
    False
    >>> has_subseq(144,1441)
    False
    >>> has_subseq(1343412,134)
    True
    """
    if n==seq:
        return True
    if n<seq:
        return False
    if seq%10==n%10:
        return has_subseq(n//10,seq//10)
    return has_subseq(n//10,seq)
