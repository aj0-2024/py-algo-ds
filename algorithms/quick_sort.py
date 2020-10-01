"""
Quick sort is a simple algorithm that runs on average O(nlogn)
1. Divide collection into roughly two equal parts using a pivot
2. Elements larger than pivot move to the right of pivot and elements smaller than pivot
move to the left.
3. Repeat until the whole array is sorted

https://stackabuse.com/quicksort-in-python/
"""

def partition(sequence, start, end):
    """Divide the list into two and move elements around pivot"""

    pivot = sequence[end]
    low = start + 1
    high = end

    while True:
        while low <= high and sequence[high] >= pivot:
            high = high - 1

        while low <= high and sequence[low] <= pivot:
            low = low + 1

        if low <= high:
            sequence[low], sequence[high] = sequence[high], sequence[low]
        else:
            break

    array[start], array[end] = array[end], array[start]

    return high

def quick_sort(sequence, start, end, comparator):
    """Perform quick sort on the sequence in place"""
    
    if start >= end:
        return sequence

    high = partition(sequence, start, end, comparato)
    quick_sort(sequence, start, high - 1, comparator)
    quick_sort(sequence, high + 1, end, comparator)

    return sequence


