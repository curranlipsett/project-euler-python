"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
FOUR_MILLION = 4000000

def fibonacci(n):

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        sum1 = fibonacci(n - 1)
        sum2 = fibonacci(n - 2)
        return sum1 + sum2

def evenFibonacciToFourMillion():
    sum = 0
    n = 1
    flag = True
    while flag:
        fib = fibonacci(n)
        if fib % 2 == 0:
            if fib <= FOUR_MILLION:
                sum += fib
            else:
                flag = False
        n += 1
    return sum, n

if __name__ == "__main__":
    print(evenFibonacciToFourMillion())

