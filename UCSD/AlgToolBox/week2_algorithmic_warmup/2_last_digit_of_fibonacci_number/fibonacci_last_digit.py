#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

#P# implement a faster fibonacci to find the last digit 
#P# of the nth fibonacci number by taking % 10 every time
def get_fibonacci_last_digit(n):
    #P# if n <= 1, return n
    if n <= 1:
        return n
    #P# if n > 1, use 1 variables to store the previous fibonacci numbers
    #P# initialize the variable to 0 and 1
    prev = 0
    current = 1
    #P# loop from 2 to n
    for i in range(2, n + 1):
        #P# save the previous fibonacci number and update current fibonacci number
        #P# by adding the previous fibonacci number and take % 10 to reduce
        #P# the number of digits
        prev, current = current, (prev + current) % 10
    #P# return the current fibonacci number
    return current

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)

    #P# test get_fibonacci_last_digit and get_fibonacci_last_digit_naive
    #P# for i in range 0 to NUM_TESTS
    #P# print pass if the 2 functions return the same result
    #P# else print fail and break
    TEST_FIB = False
    NUM_TESTS = 12
    if TEST_FIB:
        for i in range(NUM_TESTS + 1):
            fib1 = get_fibonacci_last_digit(i)
            fib2 = get_fibonacci_last_digit_naive(i)
            if fib1 == fib2:
                print('pass', i, fib1, fib2)
            else:
                print('fail', i, fib1, fib2)
                break
    
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit(n))
