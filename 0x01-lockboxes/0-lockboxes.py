#!/usr/bin/python3
"""
canUnlockAll method
"""


def canUnlockAll(boxes):
    """
    checks all available keys
    :param boxes: list of lists of keys
    :return: true or false
    """
    opened = [False] * len(boxes)
    opened[0] = True
    keys = [0]

    for key in keys:
        for new_key in boxes[key]:
            if new_key < len(boxes) and not opened[new_key]:
                opened[new_key] = True
                keys.append(new_key)

    return all(opened)
