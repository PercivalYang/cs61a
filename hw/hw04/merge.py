def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    lst = []
    if lst1 == []:
        return lst2
    if lst2 == []:
        return lst1
    if lst1[0] < lst2[0]:
        lst.append(lst1.pop(0))
    else:
        lst.append(lst2.pop(0))
    lst.extend(merge(lst1,lst2))
    return lst
