# Primo

Writing a
[Wordle solver](https://github.com/athornton/wordle-solver.git) that
could also do [Primel](https://converged.yt/primel/) made me curious
about the distribution of digits in prime numbers represented in
different integral bases.

## Interactive use

Run `show_frequency` to get a list of digit distributions for primes up
to 100000 in bases from 2 to 36 inclusive.

`show-frequency --primes-only` will just show you the distributions for
prime bases, and you can change 100000 to whatever you like with the
`--maximum` option.  Prime generation is the good old Sieve of
Eratosthenes, so you probably shouldn't use this for very large primes.

## Developing

If you want to play around with this yourself, ``make init`` will set up
the pre-commit hooks for you.  The Primo class itself has no external
requirements: everything in it is in the Python 3.8 standard library;
however, the test suite and pre-commit hooks have some external packages
they require.
