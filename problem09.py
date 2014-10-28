"""Project Euler Problem 9

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def is_pythagorean(a, b, c):
    """Return True if a^2 + b ^2 == c^2.
    """
    return c * c == a * a + b * b


num = 1000
a = b = c = 0

for c in range(num - 2, num // 3, -1):
    for b in range(1, (num - c) // 2 + 1):
        a = num - c - b
        if is_pythagorean(a, b, c):
            break
    else:
        continue
    break

print "The product is %d * %d * %d = %d" % (a, b, c, a * b * c)
