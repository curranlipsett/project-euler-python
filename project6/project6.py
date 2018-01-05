"""
The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the
sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# Brute force to square each number and add to a running total
def computeSumOfFirst100Squares():
    total = 0
    for i in range(1, 101):
        total += i*i
    return total

# It's known that 1 + 2 + 3 ... + 98 + 99 + 100 is the same as 101 * 50, so that's a shortcut in this situation
def computeSquareOfSumOfFirst100NaturalNumbers():
    return (101 * 50) * (101 * 50)

def computeDifference(squareOfSums, sumOfSquares):
    return squareOfSums - sumOfSquares

print(computeDifference(computeSquareOfSumOfFirst100NaturalNumbers(), computeSumOfFirst100Squares()))