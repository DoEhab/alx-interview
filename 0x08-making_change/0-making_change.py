#!/usr/bin/python3
"""
method makeChange
"""


def makeChange(coins, total):
    """
    function
    :param coins: list of numbers
    :param total: target
    :return:
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    if total != 0:
        return -1
    return count
