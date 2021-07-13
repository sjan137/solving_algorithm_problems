import sys


def isRightAngledTriangle(x, y, z):
    seg_list = [x, y, z]
    seg_list.sort()
    c = seg_list.pop()
    b = seg_list.pop()
    a = seg_list.pop()
    a_b_power_sum = a**2 + b**2
    if a_b_power_sum == c**2: print('right')
    else: print('wrong')

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if (a + b + c) == 0: break
    isRightAngledTriangle(a, b, c)