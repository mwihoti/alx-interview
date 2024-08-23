#!/usr/bin/python3
"""
method to determine if a given data set represents a valid utf-8 encoding
"""


def validUTF8(data):
    """
    method validUTF8
    """
    num_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7

        if num_bytes == 0:
            while mask_byte & i:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (1 & mask_2)):
                return False

        num_bytes -= 1
    if num_bytes == 0:
        return True

    return False
