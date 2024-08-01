#!/usr/bin/python3
"""
method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    """
    visited = {0}
    queue = [boxes[0]]
    while queue:
        box = queue.pop(0)
        for key in box:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(boxes[key])
    return len(visited) == len(boxes)
