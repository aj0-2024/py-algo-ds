"""
Notes:
    - Find the nonempty, contiguous subarray of sequence whose values have the largest sum.
    - Divide and conquer method.
    - Recursive & Iterative.
    - Kadane's algorithm is an improvement and more efficient way to solve this problem.

Applications:
    - Stock problem where maximum profit has to be calculated. 

TODO:
    - The implementations are incomplete.

Links:
    - https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""
import unittest
from typing import List


def bruteforce_max_subarray(sequence: List[int]):
    """Brute force implementation of the maximum subarray problem"""
    max_sum = float("-inf")

    for left_index in range(len(sequence)):

        curr_sum = 0
        for right_index in range(left_index, len(sequence)):
            curr_sum += sequence[right_index]
            max_sum = max(max_sum, curr_sum)

    return max_sum


def kadane_algorithm(sequence: List[int]):
    """Greedy algorithm to track max sum so far - O(n) time and O(1) space"""

    if len(sequence) < 1:
        return 0

    max_sum = sequence[0]
    curr_sum = sequence[0]

    for curr_index in range(1, len(sequence)):
        curr_sum = max(sequence[curr_index], curr_sum + sequence[curr_index])
        max_sum = max(curr_sum, max_sum)

    return max_sum


def find_max_cross_subarray(sequence: List[int], low: int, mid: int, high: int):
    """Find max with a crossover point at mid"""

    # calculate the max_left, left_sum
    left_sum = float("-inf")
    curr_sum = 0

    # TODO: None check
    max_left = None

    for left_index in range(mid, low):
        curr_sum += sequence[left_index]
        print(curr_sum, left_sum)
        if curr_sum > left_sum:
            left_sum = curr_sum
            curr_sum = sequence[left_index]
            max_left = left_index

    # calculate the right sum
    right_sum = float("-inf")
    curr_sum = 0

    # TODO: None check
    max_right = None

    for right_index in range(mid+1, high):
        curr_sum += sequence[right_index]
        if curr_sum > right_sum:
            right_sum = curr_sum
            curr_sum = sequence[right_index]
            max_right = right_index

    print(max_left, max_right, left_sum + right_sum)

    return (max_left, max_right, left_sum + right_sum)


def recursive_find_max_subarray(sequence: List[int], low: int, high: int) -> (int, int, int):
    """Using recursive method to solve the maximum subarray"""

    # base case
    if high == low:
        return (low, high, sequence[low])

    mid = (low + high) // 2

    left_low, left_high, left_sum = recursive_find_max_subarray(
        sequence, low, mid)
    right_low, right_high, right_sum = recursive_find_max_subarray(
        sequence, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_cross_subarray(
        sequence, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)


def init_recursive_find_max_subarray(sequence: List[int]):
    low, high, result = recursive_find_max_subarray(
        sequence, 0, len(sequence) - 1)
    return result


def iterative_find_max_subarray():
    pass


class TestMaxSubarray(unittest.TestCase):

    def test_all_positive(self):
        input = [10, 11, 21]
        output = 42
        self.assertEqual(kadane_algorithm(input), output)
        self.assertEqual(bruteforce_max_subarray(input), output)

    def test_with_positive_at_start(self):
        input = [10, 11, -7, -10, 6]
        output = 21
        self.assertEqual(kadane_algorithm(input), output)
        self.assertEqual(bruteforce_max_subarray(input), output)

    def test_with_positive_at_middle(self):
        input = [-2, 5, 3, -1, 2]
        output = 9
        self.assertEqual(kadane_algorithm(input), output)
        self.assertEqual(bruteforce_max_subarray(input), output)

    def test_wih_positive_at_end(self):
        input = [-2, -5, -4, -3, 1, 2]
        output = 3
        self.assertEqual(kadane_algorithm(input), output)
        self.assertEqual(bruteforce_max_subarray(input), output)
        
    def test_with_mixed_numbers(self):
        input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6
        self.assertEqual(kadane_algorithm(input), output)
        self.assertEqual(bruteforce_max_subarray(input), output)


if __name__ == "__main__":
    unittest.main()
