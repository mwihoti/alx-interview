#!/usr/bin/python3

"""Prime Game"""


def isWinner(x, nums):
    """Determine the winner of the game"""
    def sieve_of_eratosthenes(n):
        """Generate all prime numbers up to n"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        return primes

    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_set = set(range(1, n + 1))
        prime_set = set(primes).intersection(current_set)
        maria_turn = True

        while prime_set:
            prime = min(prime_set)
            multiples = {i for i in current_set if i % prime == 0}
            current_set -= multiples
            prime_set -= multiples
            maria_turn = not maria_turn

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
