# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
# find 2 max numbers in the array
max1 = max(a)
a.remove(max1)
max2 = max(a)
result = max1 * max2
print(result)
