"""Project Euler Problem 6

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(number):
    """Return the sum of squares of numbers 1 to number.
    """
    res = 0
    for i in range(number + 1):
        res += i*i
    return res


def square_of_sum(number):
    """Return the square of the sum of numbers 1 to number.
    """
    just_sum = 0.5 * number * (number + 1)
    return just_sum * just_sum


number = 100

result = square_of_sum(number) - sum_of_squares(number)

print "The difference between the sum of the squares of the first \
%d natural numbers and the square of the sum is %d" % (number, result)
