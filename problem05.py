"""Project Euler Problem 5

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

import math


def is_prime(number):
    """Return True if number is prime.
    """
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    mid = math.sqrt(number) + 1
    i = 3
    while i < mid:
        if number % i == 0:
            return False
        i += 2  # we can skip all even numbers since number is odd
    return True


def get_prime(over=2):
    """Return a prime greater than over.
    """
    p = over + 1
    while not is_prime(p):
        p += 1
    return p


def product(factorization):
    """Return the product of the numbers in the list.
    """
    res = 1
    for p, n in factorization.iteritems():
        res *= p ** n
    return res


def factorize(number):
    """Return a prime factorization of a number in a dictionary.

    Result is in the form { prime1: power1, prime2: power2 ... }
    """
    factors = {}
    p = 2
    while number != 1:
        while number % p == 0:
            if p not in factors:
                factors[p] = 1
            else:
                factors[p] += 1
            number /= p
        p = get_prime(p)
    return factors


divisors = range(2, 21)
factorized = []

"""Factorize all the divisors"""
for d in divisors:
    factorized.append(factorize(d))

"""This will hold the factorization of the least common multiple of all the
divisors"""
lcm = {}

"""Compute the least common multiple of all divisors"""
for fd in factorized:
    for p in fd.keys():
        """If the prime is not in the factorization"""
        if p not in lcm or lcm[p] < fd[p]:
            """Prime factor is not in the factorization or has a lower power"""
            lcm[p] = fd[p]

result = product(lcm)

print "The smallest positive number that is evenly divisible by \
all of the numbers from 1 to 20 is %d" % result
