"""Project Euler Problem 10

Find the sum of all the primes below two million.

Dump algorith that checks divisibility by all numbers below sqrt(n) except
multiples of 2 and 3 that aren't even considered as candidates (reduces number
of checks by 50 + 16 = 66%)
"""

import math


def is_prime(number):
    """Return True if number is prime.
    """
    mid = math.sqrt(number) + 1
    i = 5
    flag = True
    while i < mid:
        if number % i == 0:
            return False
        """Skip multiples of 2 and 3 as they were handled before"""
        i += 2 if flag else 4
        flag = not flag
    return True


def get_primes():
    """Return all prime numbers.
    """
    yield 2
    yield 3
    i = 5
    flag = True
    while True:
        if is_prime(i):
            yield i
        """Skip multiples of 2 and 3"""
        i += 2 if flag else 4
        flag = not flag


below = 2000000
result = 0

for p in get_primes():
    if p >= below:
        break
    result += p

print "The sum of all the primes below %d is %d." % (below, result)
