import sys

N = int(sys.stdin.readline())
xy_list = list()
for _ in range(N):
    xy = list(map(int, sys.stdin.readline().split()))
    xy_list.append(xy)

print(xy_list)