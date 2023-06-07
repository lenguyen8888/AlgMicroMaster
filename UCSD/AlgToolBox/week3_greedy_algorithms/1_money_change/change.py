#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Problem Description
# Task. The goal in this problem is to find the minimum number of coins 
# needed to change the input value
# (an integer) into coins with denominations 1, 5, and 10.
# Input Format. The input consists of a single integer 𝑚.
# Constraints. 1 ≤𝑚 ≤103.
# Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
# Sample 1.
# Input:
# 2
# Output:
# 2
# 2 = 1 + 1.
# Sample 2.
# Input:
# 28
# Output:
# 6
# 28 = 10 + 10 + 5 + 1 + 1 + 1.
# Need Help?
# Ask a question or see the questions asked by other learners at this forum thread.
# 3

import sys

#P# 1. Divide the amount by 10, 5 and 1
#P# 2. Get the remainder
#P# 3. Repeat the process with the remainder
#P# 4. Add the number of times the amount was divided by 10, 5 and 1

def get_change(m):
    #write your code here
    coins = [10, 5, 1]
    count = 0
    for coin in coins:
        count += m // coin
        m %= coin
    return count



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
