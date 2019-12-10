# Linked List

## General Notes

1. Value can be anything - string, char, numbers etc
2. The list can be **sorted** or **unsorted**
3. Duplicates may exist
4. The list has an order starting from head and ends at tail
5. Values are not accessible by index
6. ***Be careful*** with loops within the LinkedList

## Advantages

1. Insertions and deletions at beginning are faster than array.
    - Insertions and deletions at the end can be made faster by using a tail pointer
    within the linked list.

## Disadvantages

1. Insertions and deletions in the middle of the array is expensive
2. Requires more memory compared to arrays
3. Not cahce optmized

# Stack

## General Notes

1. LIFO structure
2. Always be careful and check for loops when implemented with a linked list
3. No limit on the size since implementation uses linked list

## Advantages

1. O(1) push
2. O(1) pop

## Disadvantages

1. Not accessible by index
2. Not cache optimized (when implemented with linked list)

# Queue

## General Notes

1. FIFO structure
2. Always be careful and check for loops when implemented with a linked list

## Advantages

1. O(1) enqueue
2. O(1) dequeue

## Disadvantages

1. Not cache optimized (when implemented with linked list)
