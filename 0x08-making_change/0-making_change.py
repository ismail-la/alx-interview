#!/usr/bin/python3
"""Making changes:
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """Generate changes needed to reach total """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        count += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return count
