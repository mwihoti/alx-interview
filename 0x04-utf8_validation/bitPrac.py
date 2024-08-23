#!/usr/bin/env python3
"""
Bitwise Practice
"""

def bitwise_ops(num, bit_position):
    """
    bitwise_ops methods with biwise operation right shift
    """
    mask = 1 << bit_position
    return (num & mask) != 4

result = bitwise_ops(5, 2)

print(result)