import unittest
from project4.project4 import isPalindrome, computeLargestPalindromeOfTwoThreeDigitNumbers

class testComputeLargestPalindromeOfTwoThreeDigitNumbers(unittest.TestCase):

    def testIsPalindrome(self):
        self.assertTrue(isPalindrome(101))
        self.assertTrue(isPalindrome(123454321))
        self.assertFalse(isPalindrome(100))
        self.assertFalse(isPalindrome(1234567876543210))

    def testComputeLargestPalindromeOfFactor(self):
        self.assertEqual(computeLargestPalindromeOfTwoThreeDigitNumbers(99, 99), 9009)
        self.assertEqual(computeLargestPalindromeOfTwoThreeDigitNumbers(9, 20), 171)
