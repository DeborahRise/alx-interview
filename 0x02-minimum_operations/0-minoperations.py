#!/usr/bin/python3
"""
given a single character H
my text editor only does 'copy all' and 'paste'
given a number n?
a method that calculates the fewest number of operations
for the output n H character in the file
e.g: character A, number 5
what is the minimum number of operations that can
result in 5 A, knowing I can only use
copy all and paste
A
after the first Copy All and paste = AA
if i copy all and paste again => AAAA
meaning it will exceed 5 in the end,
so i will need to copy all just and paste 1st time and paste again 3 times

Algorithm:
if n = 5
cp = hh
p = hhh
p = hhhh
p = hhhhh
tmp = 5

if n = 6
c p = hh
c p = hhhh
p = hhhhhh
tmp = 5

if n = 12
cp = hh
cp = hhhh
cp = hhhhhhhh
p = hhhhhhhhhhhh
tmp = 7

if n = 9
c p = hh
p = hhh
c p = hhhhhh
p = hhhhhhhhh
tmp = 6

if n = 14
c p = hh
c p = hhhh
p = hhhhhh
p = hhhhhhhh
p = hhhhhhhhhh
p = hhhhhhhhhhhh
p = hhhhhhhhhhhhhh
tmp = 9

minimum of 2 operations the first time if n > 1
initialize and increament a counter after every operation
after an operation,
    if the length of character(loc) in file is = n
    return counter
    else if n / loc

    from this pattern, we noticed that if the current length of characters
    can divide n without a reminder, then you can 'copyall and paste'
    else just paste
"""


def minOperations(n):
    """
    from the pattern above, we noticed that if the current length of characters
    can divide n without a reminder, then you can 'copyall and paste'
    else just paste
    """
    if not isinstance(n, int):
        return 0
    file = 'H'
    loc = len(file)
    counter = 0
    copy_all = ''
    while loc < n:
        if n % loc == 0:
            copy_all = file
            file = file + copy_all
            counter += 2
            loc = len(file)
        else:
            file += copy_all
            counter += 1
            loc = len(file)
    return counter
