"""
Compute prime factors for a few numbers and find the largest of those factors
"""

# Largest prime factor of 12 is 3
# Largest rime factor of 27 is 3
# Prime factors of 13195 are 5, 7, 13 and 29 with 29 being the largest
import unittest
from project3.project3 import computeLargestPrimeFactor, isPrime

class project1test(unittest.TestCase):
    def testComputeLargestPrimeFactor(self):
        self.assertEqual(computeLargestPrimeFactor(12), 3)
        self.assertEqual(computeLargestPrimeFactor(27), 3)
        self.assertEqual(computeLargestPrimeFactor(13195), 29)

    def testIsPrime(self):
        self.assertTrue(isPrime(19))
        self.assertFalse(isPrime(100))
        self.assertTrue(isPrime(139))
        self.assertFalse(isPrime(4000))