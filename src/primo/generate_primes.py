"""
Sieve of Eratosthenes to generate primes.
"""
from typing import List


def generate_primes(max_prime: int) -> List[int]:
    """
    Generate all primes less than max_prime

    This is a straightforward implementation of the Sieve of Eratosthenes.

    The list of numbers is for playing Primel:
    https://converged.yt/primel/
    """
    pbool = [True for _ in range(max_prime)]
    pbool[0] = False
    pbool[1] = False
    p = 2
    while p * p < max_prime:
        if pbool[p]:
            # Only mark things we still think are primes
            for i in range(p * p, max_prime, p):
                # Mark its multiples as non-prime
                pbool[i] = False
        p += 1
    return [x for x in range(2, max_prime) if pbool[x]]
