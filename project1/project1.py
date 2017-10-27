"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def findMultiplesOf3And5Below1000():

    # Figure out how to know if something is a multiple of 3 or 5 (evenly divisible)

    sum = 0
    for number in range(1000):
        if (isMultipleOf3(number)):
            sum += number
        elif (isMultipleOf5(number)):
            sum += number

    return sum

def isMultipleOf3(number):
    return number % 3 == 0

def isMultipleOf5(number):
    return number % 5 == 0

if __name__ == "__main__":
    print(findMultiplesOf3And5Below1000())