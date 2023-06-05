#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 11:00 AM
# @Author  : Nguyen Le

#P# write a program that takes 2 single digit numbers from input() and
#P# print out the sum of the 2 numbers

#P# input: 2 single digit numbers
#P# output: sum of the 2 numbers
#P# run if this is the main program
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(a + b)
