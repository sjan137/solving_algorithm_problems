import sys
import math


def whereIsRyu(dist_list):
    x1 = dist_list[0]
    y1 = dist_list[1]
    r1 = dist_list[2]
    x2 = dist_list[3]
    y2 = dist_list[4]
    r2 = dist_list[5]
    circle_dist = math.sqrt((y2-y1)**2 + (x2-x1)**2)
    r_sum = r1 + r2
    if (circle_dist == 0) & (r1 == r2): print(-1)
    elif (circle_dist == 0) & (r1 != r2): print(0)
    elif circle_dist < r_sum: print(2)
    elif circle_dist == r_sum: print(1)
    else: print(0)

T = int(sys.stdin.readline())
for t in range(T):
    dist_list = list(map(int, sys.stdin.readline().split()))
    whereIsRyu(dist_list)