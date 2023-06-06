#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

#P# implement a faster fibonacci  % m before current assignment
def get_fibonacci_fast(n, m):
    #P# if n <= 1, return n
    if n <= 1:
        return n
    #P# initialize the previous fibonacci number to 0
    prev = 0
    #"""  """ initialize the current fibonacci number to 1
    current = 1
    #P# loop from 2 to n
    for i in range(2, n + 1):
        # save the previous fibonacci number and update current fibonacci number
        # by adding the previous fibonacci number and take % m to reduce
        # the number of digits
        prev, current = current, (prev + current) % m
    # return the current fibonacci number
    return current


#P# find the Pisano period of m
def pisano_period(m):
    # initialize the pisano period to 0
    pisano_period = 0
    # initialize the previous fibonacci number to 0
    prev = 0
    #"""  """ initialize the current fibonacci number to 1
    current = 1
    #P# loop from 2 to m * m + 3
    for i in range(2, m * m + 4):
        # save the previous fibonacci number and update current fibonacci number
        # by adding the previous fibonacci number and take % m to reduce
        # the number of digits
        prev, current = current, (prev + current) % m
        # if the previous fibonacci number is 0 and the current fibonacci number is 1
        # then we find the pisano period
        if prev == 0 and current == 1:
            # set the pisano period to i - 1
            pisano_period = i - 1
            # break out of the loop
            break
    # return the pisano period
    return pisano_period

#P# implement a faster fibonacci  % m using Pisano period
def get_fibonacci_huge(n, m):
    #P# if m <= 2 return get_fibonacci_fast(n, m)
    if m <= 2:
        return get_fibonacci_fast(n, m)
    
    #P# find Pisano period of m mPisano
    mPisano = pisano_period(m)
    # return the get_fibonacci_huge_naive(n % mPisano, m)
    return get_fibonacci_fast(n % mPisano, m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge(n, m))
