#!/usr/bin/python3
"""method that defines the minimum operation of n"""


def minOperations(n):
    """
        A function that calculates fewest numbers of
        operations to a given number of n h characters
        in a file
        args: n: numbers of characters to be displayed
        return:
                number of min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
