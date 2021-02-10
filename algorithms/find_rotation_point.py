"""
Given a sequence of numbers in ascending to descending/descending to ascending order find the 
rotation point.
"""
import unittest

def find_rotation_point(sequence):
    """Returns the index of the rotation"""

    if not sequence:
        return sequence

    left = 0
    right = len(sequence) - 1

    while left <= right:

        mid = (left + right) // 2
        
        if sequence[left] >= sequence[mid]: 
            left = mid + 1
        else:
            right = mid - 1


    return right 
            
class TestFindRotationPoint(unittest.TestCase):

    def test_increasing_and_then_decreasing(self):
        self.assertEqual(
            find_rotation_point([5, 4, 3, 2, 1, 2, 3, 4]),
            4
        )

    def test_strictly_decreasing(self):
        self.assertEqual(
            find_rotation_point([5, 4, 3, 2, 1]),
            4
        )

    def test_strictly_increasing(self):
        self.assertEqual(
            find_rotation_point([1, 2, 3, 4, 5]),
            0
        )

if __name__ == "__main__":
    unittest.main()
