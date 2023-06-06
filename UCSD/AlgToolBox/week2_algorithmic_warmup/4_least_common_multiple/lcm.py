#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

#P# implement a faster gcd algorithm
def gcd(a, b):
    #P# if b == 0, return a
    if b == 0:
        return a
    #P# else, return gcd(b, a % b)
    return gcd(b, a % b)

#P# implement a faster lcm algorithm
def lcm(a, b):
    # return a * b / gcd(a, b)
    return a * b // gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm(a, b))

