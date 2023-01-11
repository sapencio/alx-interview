#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    numOp = 0
    while n != 0: 
        if n % 2 == 0: 
            numOp += 1 
            n /= 2 
        else: 
            numOp += 1 
        n -= 1 
    return numOp
