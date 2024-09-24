#!/usr/bin/python3

from collections import defaultdict

def how_many_ways(m, coins):
    memo = defaultdict(lambda: 0)

    memo[0] = 1
    for i in range(1, m + 1):
        memo[i] = 0

        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = memo[i] + memo[subproblem]
    return memo[m]
print(how_many_ways(17, [6, 3, 4]))