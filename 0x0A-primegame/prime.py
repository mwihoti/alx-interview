#!/usr/bin/python3

"""Prime Game"""

def isWinner(x, nums):
    """
    Determines the winner of a set of prime numbers
    """
    if x <0 or nums is None:
        return None
    if x != len(nums):
        return None
    
    # Initialize scores and array of possible prime numbers
    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] +1)]

    a[0], a[1] = 0, 0

    for i in range(2, len(a)):
        prime_multiples(a, i)
        # play each round of game
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determine winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
def prime_multiples(ls, x):
    for i in range(2, len(ls)):
        try:
            ls[i*x] = 0
        except (ValueError, IndexError):
            break