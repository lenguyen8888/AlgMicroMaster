#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 11:00 AM
# @Author  : Nguyen Le

def max_pairwise_product(numbers):
    #P# Find the 2 max values in the list numbers
    #P# 1st max value is the max value in the list in firstMax
    firstMax = max(numbers)
    #P# 2nd max value is the max value in the list in secondMax
    #P# remove the 1st max value from the list before finding the 2nd max value
    numbers.remove(firstMax)
    secondMax = max(numbers)
    #P# return the product of the 2 max values
    return firstMax * secondMax


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
