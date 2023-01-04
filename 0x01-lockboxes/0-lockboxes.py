#!/usr/bin/python3
''' A Module for working with lockboxes
'''


def canUnlockAll(boxes):
    ''' Checks if all the boxes in a list of boxes containing the keys
    to other boxes can be unlocked given that the first box is unlocked.
    '''
    n = len(boxes)
    visited = set()
    visited.add(0)
    keys_to_check = boxes[0]
    while keys_to_check:
        key = keys_to_check.pop()
        if key not in visited:
            visited.add(key)
            keys_to_check.extend(boxes[key])
    return len(visited) == n
