"""Project Euler Problem 7

What is the 10 001st prime number?
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
        if is_prime_optimized(i):
            yield i
        """Skip multiples of 2 and 3"""
        i += 2 if flag else 4
        flag = not flag


number = 10001
result = 0

i = 1
for p in get_primes():
    if i == number:
        result = p
        break
    i += 1

print "The prime number #%d is %d." % (number, result)
