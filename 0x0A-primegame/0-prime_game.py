#!/usr/bin/python3
""" Module for solving prime game problem using the eratosthenes algorithm.
"""


def isWinner(x, nums):
    """Determine the winner in the prime game.
    x: An integer representing the number of rounds in the prime game.
    nums: A list of integers representing the upper bounds for each round.
    """
    Maria = 0
    Ben = 0


    for round in range(x):
        """his loop iterates through each round of the game (from 0 to x-1).
        """
        List_playing_numbers = [num for num in range(2, nums[round] + 1)]
        index = 0
        # Implements the Sieve of Eratosthenes algorithm
        while (index < len(List_playing_numbers)):
            currentPrime = List_playing_numbers[index]
            sieveIndex = index + currentPrime
            while(sieveIndex < len(List_playing_numbers)):
                List_playing_numbers.pop(sieveIndex)
                sieveIndex += currentPrime - 1
            index += 1
        # Determining the Winner:
        # -If the count is even, Maria wins (increment Maria),
        # Otherwise, Ben wins (increment Ben).
        # -If Maria and Ben have the same score, the function returns None.
        # Otherwise, it returns the name of the winner either ‘Ben’ or ‘Maria’
        primeCount = (len(List_playing_numbers))
        if primeCount and primeCount % 2:
            Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None
    return 'Ben' if Ben > Maria else 'Maria'
