"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def findSmallestNumberThatIsDivisibleByAllNumbersUpTo20():
    # Start at 2520 since this is given to us by the problem
    checkNum = 2520
    # No need to check any other numbers since these numbers are multiples of the others
    divideBy = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    while (True):
        divisibleByAll = True
        for i in divideBy:
            if (checkNum % i != 0):
                divisibleByAll = False
                break
        if (divisibleByAll):
            return checkNum
        # Since the number has to be divisible by 20, add 20 each time we didn't find the number
        # to ensure it's divisible by 20 and to reduce the amount of numbers to check
        checkNum += 20


print(findSmallestNumberThatIsDivisibleByAllNumbersUpTo20())
