"""
Sieve of Eratosthenes to generate primes.
"""
from typing import List


def generate_primes(max_n: int) -> List[int]:
    """
    Generate all primes less than or equal to max_n

    This is a straightforward implementation of the Sieve of Eratosthenes.

    The list of numbers is for playing Primel:
    https://converged.yt/primel/
    """
    # Python ranges are half-open, so increase the ceiling by 1
    top: int = max_n + 1
    pbool = [True for _ in range(top)]
    pbool[0] = False
    pbool[1] = False
    p: int = 2
    while p * p < (max_n + 1):
        if pbool[p]:
            # Only mark things we still think are primes
            for i in range(p * p, top, p):
                # Mark its multiples as non-prime
                pbool[i] = False
        p += 1
    return [x for x in range(2, top) if pbool[x]]
