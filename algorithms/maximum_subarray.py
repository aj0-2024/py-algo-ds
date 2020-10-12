"""
Notes:
    - Divide and conquer method.
    - Recursive & Iterative.
    - Kadane's algorithm is an improvement and more efficient way to solve this problem.

Applications:
    - Stock problem where maximum profit has to be calculated. 
"""

def find_max_cross_subarray(sequence: List[int], low: int, mid: int, high: int):
    """Find max with a crossover point at mid"""

    # calculate the max_left, left_sum
    left_sum = float("-inf")
    curr_sum = 0
    # TODO: None check
    max_left = None
    for left_index in range(mid, low):
        curr_sum += sequence[left_index]
        if curr_sum > left_sum:
            left_sum = curr_sum
            max_left = left_index

    # cacluclate the right sum
    right_sum = float("-inf")
    curr_sum = 0
    for right_index in range(mid+1, high):
        curr_sum += sequence[right_index]
        if curr_sum > right_sum:
            right_sum = curr_sum
            max_right = right_index

    return (max_left, max_right, left_sum + right_sum)

def recursive_find_max_subarray(sequence: List[int], low: int, high: int) -> (int, int, int):
    """Using recursive method to solve the maximum subarray"""

    # base case
    if high == low:
        return (low, high, sequence[low])

    mid = (low + high) // 2

    left_low, left_high, left_sum = recursive_find_max_subarray(sequence, low, mid)
    right_low, right_high, right_sum = recursive_find_max_subarray(sequence, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_cross_subarray(sequence, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)
    

def iterative_find_max_subarray():
    pass
