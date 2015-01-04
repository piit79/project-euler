"""Project Euler Problem 1

Find the sum of all the multiples of 3 or 5 below 1000.
"""

below = 1000
result = 0

for m in range(3, below, 3):
    result += m
for m in range(5, below, 5):
    if m % 3 > 0:  # skip multiples of 3 as they have already been added above
        result += m

print "Sum of multiples of 3 or 5 below %d is %d" % (below, result)
