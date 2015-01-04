"""Project Euler Problem 10

Find the sum of all the primes below two million.

Optimized using a list of primes - for each consecutive number n we only check
divisibility by all the primes below sqrt(n) (found previously)
"""

import math

primes = [2, 3]


def is_prime(number):
    """Return True if number is prime.
    """
    mid = math.sqrt(number)
    for p in primes:
        if number % p == 0:
            return False
        if p > mid:
            # number is a prime, add it to the list
            primes.append(number)
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
        i += 2 if flag else 4
        flag = not flag


below = 2000000
result = 0

for p in get_primes():
    if p >= below:
        break
    result += p

print "The sum of all the primes below %d is %d." % (below, result)
