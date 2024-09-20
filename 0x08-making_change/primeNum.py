#!/usr/bin/python3
"""
Get the prime numbers
"""
prime_count  = 0

for n in range(1, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        prime_count += 1

print(f'There are {prime_count} prime numbers between 1 and 10')