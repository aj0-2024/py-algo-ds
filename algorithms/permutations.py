"""
Algorithm to find the permutations
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

def get_permutations_str(string_given):

    # base case
    if len(string_given) <= 1:
        return set([string_given])

    string_without_last_character = string_given[:1]
    last_character = string_given[-1]

    all_permutations_without_last_character = get_permutations_str(string_without_last_character)

    permutations = Set()

    for permutation_curr in all_permutations_without_last_character:
        for position in range(len(string_without_last_character) + 1):
            
            permutation_new = (
                permutation_curr[:position] + 
                last_character + 
                permutation[position:]
            )

            permutations.add(permutation_new)

    return permutations
