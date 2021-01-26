"""
Algorithm to find the permutations of a given array
"""

def get_permutations(sequence, permutation_curr = [], permutation_all = []):
    """
    Returns all the possible permutations of the given sequence

    O(n^2 * n!) time
    O(n * n!) space
    """

    # base case, when sequence is empty current permutation is the only one possible
    if not len(sequence) and len(permutation_curr):
        permutations.append(curr_permutation)
        return

    for index_curr in range(len(sequence)):

        sequence_without_current_element = sequence[:index_curr] + sequence[index_curr + 1:]
        permutation_with_current_element = permutation_curr + [sequence[index_curr]]

        get_permutations(
            sequence_without_current_element, 
            permutation_with_current_element, 
            permutations
        )
    
    return permutation_all
    
