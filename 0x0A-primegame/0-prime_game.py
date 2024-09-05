#!/usr/bin/python3
"""
choosing a prime number from the set
and removing that number and its multiples from the set
 """


def generatePrimeNumbers(limit):
    """The player that cannot make a move loses the game"""
    primeNums = []
    checkList = [True] * (limit + 1)
    for isPrime in range(2, limit + 1):
        if checkList[isPrime]:
            primeNums.append(isPrime)
            for multiple in range(isPrime, limit + 1, isPrime):
                checkList[multiple] = False
    return primeNums


def isWinner(numberOfRounds, valueOfRounds):
    """
     determine who the winner of each game is.
    """
    if not numberOfRounds or not valueOfRounds:
        return None
    mariaScore = benScore = 0
    for i in range(numberOfRounds):
        primes = generatePrimeNumbers(valueOfRounds[i])
        if len(primes) % 2 == 0:
            benScore += 1
        else:
            mariaScore += 1
    if mariaScore > benScore:
        return "Maria"
    elif benScore > mariaScore:
        return "Ben"
    return None
