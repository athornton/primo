"""
Test our prime calculator
"""

from primo.primo import Primo


def test_prime_count() -> None:
    """
    Does it actually get the primes less than 100000?
    """
    p = Primo()
    # pretty much anywhere, but ... https://primes.utm.edu/howmany.html
    assert len(p.prime_list) == 9592


def test_generation() -> None:
    """
    Do we get the right primes?
    """
    p = Primo(maximum=50, prime_length=2, base=7)
    # primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
    assert p.prime_list == [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
    ]


def test_conversion() -> None:
    """
    Do we convert to base-7 strings?
    """
    p = Primo(maximum=50, prime_length=2, base=7)
    # in base 7: 2, 3, 5, 10, 14, 16, 23, 25, 32, 41, 43, 52, 56, 61, 65
    p.generate_representations()
    assert p.prime_strs == [
        "2",
        "3",
        "5",
        "10",
        "14",
        "16",
        "23",
        "25",
        "32",
        "41",
        "43",
        "52",
        "56",
        "61",
        "65",
    ]


def test_length_categorization() -> None:
    """
    Primes less than 50 in base 7.
    """
    p = Primo(maximum=50, prime_length=2, base=7)
    # two-digit (base 7): 10, 14, 16, 23, 25, 32, 41, 43, 52, 56, 61, 65
    p.generate_representations()
    assert p.get_primes_of_length() == [
        "10",
        "14",
        "16",
        "23",
        "25",
        "32",
        "41",
        "43",
        "52",
        "56",
        "61",
        "65",
    ]


def test_frequency() -> None:
    """
    Do we get the right count for each character?
    """
    p = Primo(maximum=50, prime_length=2, base=7)
    # 1: 10, 14, 16, 41, 61      -> 5
    # 2: 23, 25, 32, 52          -> 4
    # 3: 23, 32, 43              -> 3
    # 4: 14, 41, 43              -> 3
    # 5: 25, 52, 56, 65          -> 4
    # 6: 16, 56, 61, 65          -> 4
    # 0: 10                      -> 1
    p.generate_digit_freq()
    assert p.digit_freq == {
        "1": 5,
        "2": 4,
        "3": 3,
        "4": 3,
        "5": 4,
        "6": 4,
        "0": 1,
    }


def test_frequency_str() -> None:
    """
    Test string representation: sorted by character frequency.
    """
    p = Primo(maximum=50, prime_length=2, base=7)
    assert p.generate_freqs() == (
        "{'1': 5, '6': 4, '2': 4, '5': 4, " + "'4': 3, '3': 3, '0': 1}"
    )
