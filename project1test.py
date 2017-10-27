from project1 import isMultipleOf5, isMultipleOf3
import unittest

class project1test(unittest.TestCase):
    def testMultipleOf3Correct(self):

        # Test a few known multiples of 3 to make sure we are calculating correctly
        # Also test a few known non multiples of 3

        # 3 is a multiple of 3
        # 6 is a multiple of 3
        # 27 is a multiple of 3
        # 300 is a multiple of 3
        self.assertTrue(isMultipleOf3(3))
        self.assertTrue(isMultipleOf3(6))
        self.assertTrue(isMultipleOf3(27))
        self.assertTrue(isMultipleOf3(300))

        # 4 is not a multiple of 3
        # 13 is not a multiple of 3
        # 998 is not a multiple of 3
        self.assertFalse(isMultipleOf3(4))
        self.assertFalse(isMultipleOf3(13))
        self.assertFalse(isMultipleOf3(998))

    def testMultipleOf5Correct(self):

        # Test a few known multiples of 5 to make sure we are calculating correctly
        # Also test a few known non multiples of 5

        # 5 is a multiple of 5
        # 10 is a multiple of 5
        # 55 is a multiple of 5
        # 555 is a multiple of 5
        self.assertTrue(isMultipleOf5(5))
        self.assertTrue(isMultipleOf5(10))
        self.assertTrue(isMultipleOf5(55))
        self.assertTrue(isMultipleOf5(555))

        # 6 is not a multiple of 5
        # 17 is not a multiple of 5
        # 998 is not a multiple of 5
        self.assertFalse(isMultipleOf5(6))
        self.assertFalse(isMultipleOf5(17))
        self.assertFalse(isMultipleOf5(998))