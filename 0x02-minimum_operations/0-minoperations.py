#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste characters
    in the file.

    Args:
        n (int): The number of desired H characters.

    Returns:
        int: The number of minimal operations needed to get n H characters
    or 0 if it is impossible to achieve n.
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
