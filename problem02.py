"""Project Euler Problem 2

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

below = 4000000
n1 = 0
n2 = 1
n = n1 + n2
result = 0

while n <= below:
    # print n,
    if n % 2 == 0:
        result += n
        # print "*",
    n1 = n2
    n2 = n
    n = n1 + n2

print "Sum of even Fibonacci numbers below %d is %d" % (below, result)
