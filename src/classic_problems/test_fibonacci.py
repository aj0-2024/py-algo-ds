from .fibonacci import (fib_recursion)


class TestFib(object):
    def test_0(self):
        assert fib_recursion(0) == 0

    def test_1(self):
        assert fib_recursion(1) == 1

    def test_2(self):
        assert fib_recursion(2) == 1
