#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

#P# implement a faster fibonacci algorithm iteratively using 
#P# 2 variables to store the 2 previous fibonacci numbers
def calc_fib_iter(n):
    #P# if n <= 1, return n
    if (n <= 1):
        return n
    #P# if n > 1, use 2 variables to store the 2 previous fibonacci numbers
    #P# initialize the 2 variables to 0 and 1
    prev1 = 0
    prev2 = 1
    #P# loop from 2 to n
    for i in range(2, n + 1):
        #P# calculate the current fibonacci number by adding the 2 previous fibonacci numbers
        current = prev1 + prev2
        #P# update the 2 previous fibonacci numbers
        prev1 = prev2
        prev2 = current
    #P# return the current fibonacci number
    return current

n = int(input())

#P# write a quick test to compare the 2 fibonacci algorithms up to 12
#P# if TEST_FIB is True, run the comparison test
TEST_FIB = False
MAX_FIB = 12
if TEST_FIB:
    #P# loop from 0 to MAX_FIB
    for i in range(MAX_FIB + 1):
        #P# calculate the fibonacci number using the 2 algorithms
        fib1 = calc_fib(i)
        fib2 = calc_fib_iter(i)
        #P# check if the 2 fibonacci numbers are the same
        #P# print pass and i, calc_fib(i), calc_fib_iter(i)
        #P# else print fail and break
        if fib1 == fib2:
            print('pass', i, fib1, fib2)
        else:
            print('fail', i, fib1, fib2)
            break

print(calc_fib_iter(n))
