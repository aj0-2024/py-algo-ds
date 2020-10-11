"""
Notes:
    - Created by David Hoffman.
    - Lossless compression of data.
    - Uses a varaible length code that depends on frequency of characters.
    - High frequency chars use smallest codes & least fequently used chars use largest codes.
    - Create a huffman tree and traverse to find codes.
    - O(nlogn) for encoding each char

Applications:
    - Computer Networks as data can be compressed.

References:
    - https://www.programiz.com/dsa/huffman-coding
"""
