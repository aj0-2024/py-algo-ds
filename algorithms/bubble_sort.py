"""
Bubble sort is a basic sorting algorithm that sorts elements of a list in-place

1. Track the sorting status with a boolean
2. While the list is not sorted, start from first index and keep swapping elements not in order
3. If elements are swapped, update the sorting status as false
4. Continue until all the elements are swapped
"""
import unittest


def bubble_sort(input_list):
    """Implementation of the bubble sort algorithm, employs an enhancement where the inner loops
    keep track of the last sorted element as described in the video below.

    (https://www.youtube.com/watch?v=6Gv8vg0kcHc)

    The input_list is sorted in-place, this is dangerous to do
    """

    is_sorted = False
    last_unsorted_index = len(input_list) - 1

    while not is_sorted:
        is_sorted = True

        for curr_index in range(0, last_unsorted_index):
            curr_element = input_list[curr_index]

            # be sure to not go out of bounds in the loop since we are accessing
            # the next element, happens at the edge of the list
            next_index = curr_index + 1
            next_element = input_list[next_index]

            # swap the elements that are not in order
            if curr_element > next_element:
                input_list[curr_index], input_list[next_index] =\
                    input_list[next_index], input_list[curr_index]
                is_sorted = False

        # as we loop everytime, the last elements of the list will be in order
        # this is explained in the video in the docstring above
        last_unsorted_index -= 1

    return input_list


class TestBubbleSort(unittest.TestCase):

    def test_case_simple(self):
        input_list = [5, 3, 2, 3, 4]
        expected_output = [2, 3, 3, 4, 5]

        bubble_sort(input_list)

        self.assertEqual(input_list, expected_output)


if __name__ == "__main__":
    unittest.main()
