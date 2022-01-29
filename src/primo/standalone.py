#!/usr/bin/env python3
"""
CLI for showing prime character frequency.
"""

import argparse
from math import log

from .generate_primes import generate_primes
from .primo import Primo


def show_prime_char_freq(
    n: int = 100000, primes: bool = False, unary: bool = False
) -> None:
    """
    Show the character frequency of primes represented in all bases
    (optionally: only prime bases) up to some maximum.
    """
    max_base = 37
    if primes:
        plist = generate_primes(max_base)
    p = Primo(maximum=n, prime_length=2)
    p.rebuild_prime_list()
    print(f"Primes <= {n} (n={len(p.prime_list)}):")
    least = 2
    if unary:
        least = 1
    for b in range(least, max_base):
        if primes:
            if b not in plist:
                continue
        p.reset_base(b)
        if b > 1:
            max_digits = int(log(p.prime_list[-1], b))
        else:
            max_digits = p.prime_list[-1]
        for d in range(1, max_digits + 1):
            p.prime_length = d
            p.generate_representations()
            ps = p.get_primes_of_length()
            outstr = p.generate_freqs()
            print(
                f"Base: {b}; prime length: {d}; primes: {len(ps)}: "
                + f"character frequencies {outstr}"
            )


def get_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Look at primes in various bases"
    )
    parser.add_argument(
        "-m",
        "--max",
        "--maximum",
        help="Maximum number to consider",
        default=100000,
        type=int,
    )
    parser.add_argument(
        "-p",
        "--primes-only",
        help="only consider prime bases",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-u",
        "--unary",
        help="include base one",
        action="store_true",
        default=False,
    )
    return parser.parse_args()


def main() -> None:
    """
    Primary entry point
    """
    args = get_args()
    show_prime_char_freq(n=args.max, primes=args.primes_only, unary=args.unary)


if __name__ == "__main__":
    main()
