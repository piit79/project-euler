"""Project Euler Problem 3

What is the largest prime factor of the number 600851475143?
"""

import math

n = 600851475143
result = 0


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


i = math.ceil(math.sqrt(n))
"""Make sure i is odd"""
i -= 0 if i % 2 else 1
while True:
    if n % i == 0 and is_prime(i):
        result = i
        break
    i -= 2  # keep i odd - no use trying even numbers

print "The largest prime factor of %d is %d" % (n, result)
