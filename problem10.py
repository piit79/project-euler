"""Project Euler Problem 10

Find the sum of all the primes below two million.
"""

import math


def is_prime_optimized(number):
    """Return True if number is prime.
    """
    mid = math.sqrt(number) + 1
    i = 5
    flag = True
    while i < mid:
        if number % i == 0:
            return False
        """Skip all multiples of 2 and 3 as they were handled before"""
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
        if is_prime_optimized(i):
            yield i
        i += 2 if flag else 4
        flag = not flag


below = 2000000
result = 0

i = 1
for p in get_primes():
    if p >= below:
        break
    result += p

print "The sum of all the primes below %d is %d." % (below, result)
