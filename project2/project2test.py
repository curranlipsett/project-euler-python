from project2.project2 import fibonacci
import unittest

class project1test(unittest.TestCase):
    def testFibonacci(self):

        """
        Fibonacci num iterations / fibonacci value
        1 : 1
        2 : 2
        3 : 3
        4 : 5
        5 : 8
        10 : 89
        """
        
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 2)
        self.assertEqual(fibonacci(3), 3)
        self.assertEqual(fibonacci(4), 5)
        self.assertEqual(fibonacci(5), 8)
        self.assertEqual(fibonacci(10), 89)