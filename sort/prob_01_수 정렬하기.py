import sys

N = int(sys.stdin.readline())
num_list = list()
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
for _ in num_list:
    print(_)