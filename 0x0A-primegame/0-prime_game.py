#!/usr/bin/python3
""" Module for solving prime game problem using the eratosthenes algorithm.
"""


def isWinner(x, nums):
    """Determine the winner in the prime game.
    x: An integer representing the number of rounds in the prime game.
    nums: A list of integers representing the upper bounds for each round.
    """
    if not nums or x < 1:
        return None
    numMax = max(nums)

    # Implements the Sieve of Eratosthenes algorithm
    list_filter = [True for _ in range(max(numMax + 1, 2))]
    for i in range(2, int(pow(numMax, 0.5)) + 1):
        if not list_filter[i]:
            continue
        for j in range(i * i, numMax + 1, i):
            list_filter[j] = False
    list_filter[0] = list_filter[1] = False
    y = 0
    for i in range(len(list_filter)):
        if list_filter[i]:
            y += 1
        list_filter[i] = y
    firstPlayer = 0
    # Winner Determination:
    # -If firstPlayer wins exactly half the rounds, the function returns None.
    # -If firstPlayer wins more than half the rounds, it returns "Maria".
    # Otherwise, it returns "Ben".
    for x in nums:
        firstPlayer += list_filter[x] % 2 == 1
    if firstPlayer * 2 == len(nums):
        return None
    if firstPlayer * 2 > len(nums):
        return "Maria"
    return "Ben"
