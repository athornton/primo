"""
Investigate a hypothesis about digit distribution in primes as represented
in (primarily prime) bases.
"""

import string
from typing import Dict, List, Mapping, Union

from .generate_primes import generate_primes


def to_base_n_str(n: int, base: int) -> str:
    """
    Convert an integer to a base N representation, 1 <= N <= 36.
    """
    if base < 1 or base > 36:
        raise RuntimeError("Base must be an integer in the range [1, 36]")
    digitabet = string.digits + string.ascii_uppercase
    if base == 1:
        return "." * n
    if n < base:
        return digitabet[n]
    return to_base_n_str(n // base, base) + digitabet[n % base]


class Primo:
    """
    Generate primes, and then represent them in various bases.
    """

    def __init__(
        self, maximum: int = 100000, prime_length: int = 6, base: int = 10
    ):
        self.prime_list: List[int] = []
        if maximum < 2:
            raise ValueError("C'mon, man. Maximum == {maximum}? Really?")
        self.maximum: int = maximum
        self.prime_length: int = prime_length
        if base < 1 or base > 36:
            raise ValueError("Base {base}?  Really?")
        self.base: int = base
        self.prime_strs: List[str] = []
        self.digit_freq: Dict[str, int] = {}
        self.rebuild_prime_list()

    def rebuild_prime_list(self) -> None:
        """
        Rebuild the list of primes if you've changed the max value.
        """
        self.prime_list = generate_primes(self.maximum)
        self.digit_freq = {}
        self.prime_strs = []

    def reset_base(self, base: int) -> None:
        """
        Reset the base for string representation.
        """
        if base < 1 or base > 36:
            raise ValueError("Base {base}?  Really?")
        if base != self.base:
            self.base = base
        self.digit_freq = {}
        self.prime_strs = []

    def generate_representations(self) -> None:
        """
        Generate string representations of primes in base N.
        """
        # https://stackoverflow.com/questions/28824874
        self.prime_strs = [
            to_base_n_str(x, self.base) for x in self.prime_list
        ]
        self.digit_freq = {}

    def get_primes_of_length(self) -> List[str]:
        """
        Return all primes whose representation (in whatever base) is N.
        """
        if not self.prime_strs:
            self.generate_representations()
        return [x for x in self.prime_strs if len(x) == self.prime_length]

    def generate_digit_freq(self) -> None:
        """
        Generate character frequency from the prime representation list.
        """
        cf = {}
        to_consider = self.get_primes_of_length()
        for w in to_consider:
            for c in w:
                if c not in cf:
                    cf[c] = 1
                else:
                    cf[c] += 1
        s_cf = self.sort_by_weight(cf)
        sorted_frequencies = {}
        for x in s_cf:
            sorted_frequencies[x] = cf[x]
        self.digit_freq = sorted_frequencies

    def sort_by_weight(
        self, weights: Mapping[str, Union[int, float]]
    ) -> List[str]:
        """
        Return the words with the highest weight (meaning, summed letter
        frequency, or word frequency) first.
        """
        # pylint: disable=no-self-use
        return [
            x[0]
            for x in sorted(weights.items(), key=lambda y: y[1], reverse=True)
        ]

    def generate_freqs(self) -> str:
        """
        Display the frequencies of each digit for the selected base.
        """
        if not self.prime_list:
            self.rebuild_prime_list()
        if not self.digit_freq:
            if not self.prime_strs:
                self.generate_representations()
            self.generate_digit_freq()
        return f"{self.digit_freq}"
