"""Fibonacci series is a series of numbers following a simple pattern where each number is a sum of
two preceding numbers

0 1 1 2 3 5 8 13 21

The series is a common pattern observed in nature, ex: Arrangement of sunflower seeds in the flower
"""

# custom exception to not compute fib series for less than 0
class NegativeNumberError(Exception):
    pass

def fib_recursion(n: int) -> int:
    
    # base case
    if n in {0, 1}:
        return n
    elif n < 0:
        raise NegativeNumberError
    else:
        # its the sum of prev two results
        return fib_recursion(n-1) + fib_recursion(n-2)
