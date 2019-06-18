"""Fibonacci series is a series of numbers following a simple pattern where each number is a sum of
two preceding numbers

0 1 1 2 3 5 8 13 21

The series is a common pattern observed in nature, ex: Arrangement of sunflower seeds in the flower
"""
from typing import Dict
from functools import lru_cache

# custom exception to not compute fib series for less than 0


class NegativeNumberError(Exception):
    pass


def fib_recursion(n: int) -> int:
    """Calculatin fib using plain recursion"""

    # base case
    if n in {0, 1}:
        return n
    elif n < 0:
        raise NegativeNumberError
    else:
        # its the sum of prev two results
        return fib_recursion(n-1) + fib_recursion(n-2)


fib_table: Dict[int, int] = {0: 0, 1: 1}


def fib_from_table(n: int) -> int:
    """Calculating fib series using memoization"""
    if n in fib_table:
        return n
    else:
        fib_table[n] = fib_from_table(n-1) + fib_from_table(n-2)
        return fib_table[n]


@lru_cache(maxsize=None)
def fib_memozation(n: int) -> int:
    """Calculate fib series using builtin python memoization function"""
    if n in {0, 1}:
        return n
    elif n < 0:
        raise NegativeNumberError
    else:
        return fib_memozation(n-1) + fib_memozation(n-2)


def fib_iteration(n: int) -> int:
    """Calculate fib using iterative method
    Any problem that can be solved with recursion can be solved with iterative methods
    """
    pass


def fib_generator(n: int) -> int:
    """Calculate fib using python generators"""
    pass
