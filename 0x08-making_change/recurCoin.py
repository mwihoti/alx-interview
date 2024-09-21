#!/usr/bin/python3

def count(coins, n, sum):
    # if sum is 0 do nothing
    if (sum == 0):
        return 1
    # if sum is les than 0 no solution happens
    if (sum < 0):
        return 0
    # if there is no coins and sum is greater than 0
    if (n <= 0):
        return 0
    
    # count is sum of solutions (i)
    return count(coins, n - 1, sum) + count(coins, n, sum-coins[n-1])

coins = [1, 2, 3]
n = len(coins)
print(count(coins, n, 5))