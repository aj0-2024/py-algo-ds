"""
Merge sort is an important sorting algorithm which works by repeatedy diving the input
and merging them again after sorting the smaller sequences.

O(nlogn)
"""

def merge(seq1, seq2):
    """Merge two sorted arrays into a single array"""
    
    merged_size = len(seq1) + len(seq2)
    merged_seq = [None] * merged_size

    seq1_index = 0
    seq2_index = 0
    merged_index = 0

    while merged_index < merged_size:

        is_first_seq_exhausted = seq1_index >= len(seq1)
        is_second_seq_exhausted = seq2_index >= len(seq2)

        if (not is_first_seq_exhausted) and (
                is_second_seq_exhausted or seq1[seq1_index] <= seq2[seq2_index]
            ):
            merged_seq[merged_index] = seq1[seq1_index]
            seq1_index += 1
            merged_index += 1
        else:
            merged_seq[merged_index] = seq2[seq2_index]
            seq2_index += 1
            merged_index += 1

    return merged_seq
