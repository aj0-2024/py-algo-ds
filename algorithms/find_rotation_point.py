"""
Given a sequence of numbers in ascending to descending/descending to ascending order find the 
rotation point.
"""

def find_rotation_point(sequence):
    """Returns the index of the rotation"""

    if not sequence:
        return None

    left_index = 0
    right_index = len(sequence) - 1

    first_element = sequence[0]

    while left_index <= right_index:

        mid_index = (left_index + right_index) // 2

        if first_element <= sequence[mid_index]:
            left_index = mid_index
        else:
            right_index = mid_index

        # when indexes are next to each other, we have a rotation point
        if left_index + 1 == right_index:
            return left_index

    return None
            
    
