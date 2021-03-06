def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        50
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total
if __name__ == '__main__':
    sum_naturals(10)
    from doctest import run_docstring_examples
    run_docstring_examples(sum_naturals, globals(), True)
