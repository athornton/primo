# Primo

Writing a
[Wordle solver](https://github.com/athornton/wordle-solver.git) that
could also do [Primel](https://converged.yt/primel/) made me curious
about the distribution of digits in prime numbers represented in
different integral bases.

## Interactive use

Run `show_frequency` to get a list of digit distributions for primes up
to 100000 in bases from 2 to 36 inclusive.  Digits for each base are 0-9
and then A-Z--hence 2 to 36.

`show-frequency --primes-only` will just show you the distributions for
prime bases, and you can change 100000 to whatever you like with the
`--maximum` option.  Prime generation is the good old Sieve of
Eratosthenes, so you probably shouldn't use this for very large primes.

There's also `--unary` if you have a thing for base 1.  This, obviously,
creates some very large string representations, and really doesn't have
any point for digit distributions, since there's only one digit, but
it's there if you want it.

## Developing

If you want to play around with this yourself, ``make init`` will set up
the pre-commit hooks for you.  The Primo class itself has no external
requirements: everything in it is in the Python 3.8 standard library;
however, the test suite and pre-commit hooks have some external packages
they require.
