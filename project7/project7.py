"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math
def isPrime(x):
    prime = True
    stop = math.ceil(math.sqrt(x))
    if x % 2 == 0:
        return False
    for i in range(2, stop + 1):
        if x % i == 0:
            prime = False
    return prime

def find10001stPrime():
    target = 10001
    primesComputed = 0
    count = 1
    while primesComputed != target:
        if isPrime(count):
            primesComputed += 1
        count += 1
    # Count will have incremented by 1 by the time we make this check, so subtract 1
    # to get the actual answer
    return count - 1

print(find10001stPrime())


