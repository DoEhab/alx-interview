#!/usr/bin/python3
"""
function minOperations
"""


def minOperations(n):
    """
    This function calculates the prime factorization
    :param n: target number of H char
    :return: number of ops
    """
    if n < 2:
        return 0
    i = 2
    ops = 0
    while i * i <= n:
        while n % i == 0:
            ops += i
            n //= i
        i += 1
    if n > 1:
        ops += n
    return ops
