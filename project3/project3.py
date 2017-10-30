"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def computeLargestPrimeFactor(n):

    # To find the largest factor of a number, we need to check up to the square root of that number
    # To know if a number is prime, it should only be evenly divisible by 1 and itself

    # Use the ceiling of the square root in case it's not an integer
    checkUpTo = math.ceil(math.sqrt(n))

    largestPrimeFactor = 1

    for i in range(3, checkUpTo + 1):
        if isPrime(i) and i > largestPrimeFactor and n % i == 0:
            largestPrimeFactor = i

    return largestPrimeFactor

# Compute if a number is prime
def isPrime(n):

    isNumberPrime = True

    checkUpTo = math.ceil(math.sqrt(n))

    if checkUpTo <= 2:
        checkUpTo = n

    for i in range(2, checkUpTo + 1):
        if n % i == 0 and n != i:
            isNumberPrime = False
            break

    return isNumberPrime

if __name__ == "__main__":
    print(computeLargestPrimeFactor(600851475143))