#!/usr/bin/env python3
"""
CLI for showing prime character frequency.
"""

import argparse
from math import log

from .generate_primes import generate_primes
from .primo import Primo


def show_prime_char_freq(
    n: int = 100000,
    primes: bool = False,
    unary: bool = False,
    base: int = 0,
) -> None:
    """
    Show the character frequency of primes represented in all bases in range
    (optionally: only prime bases) up to some maximum.
    """
    least = 2
    greatest = 37  # defaults
    if base:
        least = base
        greatest = base + 1
    else:
        if unary:
            least = 1
    if primes:
        plist = generate_primes(greatest)
    p = Primo(maximum=n, prime_length=2)
    print(f"Primes <= {n} (n={len(p.prime_list)}):")
    for b in range(least, greatest):
        if primes:
            if b not in plist:
                print(f"{b} is not prime; skipping.")
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
                f"Base: {b}; prime length: {d}; primes: {len(ps)}\n "
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
        "-b",
        "--base",
        help="Only try this base (0 means all bases in range 2-36)",
        type=int,
        default=0,
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
    show_prime_char_freq(
        n=args.max, primes=args.primes_only, unary=args.unary, base=args.base
    )


if __name__ == "__main__":
    main()
