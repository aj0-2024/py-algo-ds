"""
Notes:
    - Quick sort is a simple algorithm that runs on average O(nlogn)
        1. Divide collection into roughly two equal parts using a pivot
        2. Elements larger than pivot move to the right of pivot and elements smaller than pivot
            move to the left.
        3. Repeat until the whole sequence is sorted

    - Unstable algorithm (Does not guarantee the positions of items stay the same.

References:
    - https://stackabuse.com/quicksort-in-python/
"""
import unittest

def partition(sequence, start, end):
    """Divide the list into two and move elements around pivot"""

    pivot = sequence[start]
    low = start + 1
    high = end

    # arrage in such a way that lowest are below pivot
    # and highest are above pivot
    while True:
        while low <= high and sequence[high] >= pivot:
            high = high - 1

        while low <= high and sequence[low] <= pivot:
            low = low + 1

        if low <= high:
            sequence[low], sequence[high] = sequence[high], sequence[low]
        else:
            break

    # since the pivot is at the start, swap [start] & [high]
    # switch this if you want to change the pivot
    sequence[start], sequence[high] = sequence[high], sequence[start]

    return high

def quick_sort(sequence, start, end):
    """Perform quick sort on the sequence in place"""
    
    if start >= end:
        return sequence

    mid = partition(sequence, start, end)
    quick_sort(sequence, start, mid - 1)
    quick_sort(sequence, mid + 1, end)

    return sequence

class TestQuickSort(unittest.TestCase):

    def test_empty(self):
        sequence = []
        self.assertEqual(quick_sort(sequence, 0, 0), [])

    def test_basic_case(self):
        sequence = [ 5, 4, 3, 2, 1 ]
        self.assertEqual(quick_sort(sequence, 0, len(sequence) - 1), [ 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()


