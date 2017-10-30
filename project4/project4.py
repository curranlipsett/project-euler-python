"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# The smartest option in this case seems to be starting with 999 and 999 and seeing if that product is a palindrome
# and working down from there. It seems like it will be faster than starting with 111 and 111 and working up
# to check if the product is a palindrome, convert to string and see if the string reversed matches the original

def computeLargestPalindromeOfTwoThreeDigitNumbers(num1, num2):

    for i in range(num1, 0, -1):
        for j in range(num2, 0, -1):
            product = i * j
            if isPalindrome(product):
                return product


# Check if number is a palindrome
def isPalindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    print(computeLargestPalindromeOfTwoThreeDigitNumbers(999, 999))