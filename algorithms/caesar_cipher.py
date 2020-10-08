"""
Notes:
    - Simple encryption algorithm based on rotation of alphabets.

TODO:
    - Optimization possible, you don't need to generate the key map and caclulate the encrypted
    char just in time.
    - Add tests.
"""

def gen_key_map(key):
    """Generates a key map with original to encrypted chars"""

    # generate alphabet codes from a to z
    alphabet_codes = range(ord('a'), ord('z') + 1)

    char_orig = [ ascii_code from ascii_code in range(ord('a'), ord('z') + 1) ]

    # rotate the list until key length
    # Use a queue so that pop & append operations are optimized
    for _ in range(key):
        popped_char = char_key.pop()
        char_key.append(popped_char)

    return { chr(key): chr(value) for (key, value) in zip(char_orig, char_key) }

def encrypt(string, key):
    """Encrypt the string using a given key"""
    
    max_key_possible = 26
    key_map = gen_key_map(key % max_key_possible)

    encrypted = [ key_map[a_char] for a_char in string ]
    
    return "".join(encrypted)


