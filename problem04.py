"""Project Euler Problem 4

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(number):
    num_str = str(number)
    l = len(num_str)
    m = l // 2   # the 'midpoint'
    """Compare the first half of the string with the reversed second half"""
    return num_str[0:m] == num_str[l:l-m-1:-1]


largest = 999
smallest = 101  # we can skip 100 as numbers ending in 0 can't be palindromes
result = 0
k = l = 0

i = largest
while i > smallest:
    j = i - 1
    while j > smallest:
        n = i * j
        if n < result:
            break
        if is_palindrome(n):
            result = n
            k = i
            l = j
            break
        j -= 1
    i -= 1

print "The largest palindrome made from the product of \
two 3-digit numbers is %d = %d x %d" % (result, k, l)
