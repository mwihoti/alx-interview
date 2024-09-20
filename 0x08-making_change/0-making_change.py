#!/usr/bin/python3
"""
def makeChange(coins, total) determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in sorted(coins, reverse=True):
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
    return dp[total] if dp[total] != float('inf') else -1
