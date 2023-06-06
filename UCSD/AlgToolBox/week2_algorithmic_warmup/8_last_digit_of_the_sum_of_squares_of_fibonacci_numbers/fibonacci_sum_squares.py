# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

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
    #P# loop from 2 to 7 * m
    for i in range(2, 7 * m + 1):
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

    #P# find Pisano period of m mPisano
    mPisano = pisano_period(m)
    # return the get_fibonacci_huge_naive(n % mPisano, m)
    return get_fibonacci_fast(n % mPisano, m)

#P# def fibonacci_sum_squares_fast(n):
def fibonacci_sum_squares_fast(n):
    #P# return (get_fibonacci_huge(n, 10) * get_fibonacci_huge(n + 1, 10)) % 10
    result = (get_fibonacci_huge(n, 10) * get_fibonacci_huge(n + 1, 10)) % 10
    #P# if result < 0, return result + 10
    if result < 0:
        result += 10
    #P# return result
    return result

if __name__ == '__main__':
    n = int(stdin.read())
    # print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares_fast(n))
