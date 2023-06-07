#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 11:00 AM
# @Author  : Nguyen Le

def max_pairwise_product_loop(numbers):
    max_product = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                product = numbers[i] * numbers[j]
                if product > max_product:
                    max_product = product
    return max_product

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
    #P# write quick tests to check the correctness of your code
    # 1. Create a list of 10 positive random integers
    # 2. Call the function max_pairwise_product_loop to get the max pairwise product
    # 3. Call the function max_pairwise_product to get the max pairwise product
    # 4. Compare the results from 2 and 3
    # 5. If the results are different, print out the list of 10 positive random integers
    #P# and raise an exception
    #P# loop for 10 times
    #P# run the test if TEST_CASE is True
    TEST_CASE = True
    if TEST_CASE:
        import random
        for i in range(10):
            # create a list of 10 positive random integers
            numbers = [random.randint(1, 1000) for i in range(10)]
            # call the function max_pairwise_product_loop to get the max pairwise product
            result1 = max_pairwise_product_loop(numbers)
            # call the function max_pairwise_product to get the max pairwise product
            result2 = max_pairwise_product(numbers)
            # compare the results from 2 and 3
            # if the results are different, print out the list of 10 positive random integers
            # and raise an exception
            if result1 != result2:
                print(numbers)
                raise Exception('Wrong answer: {} {}'.format(result1, result2))
            else:
                print('OK i = ', i)
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
