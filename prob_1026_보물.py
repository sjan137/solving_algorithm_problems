import sys

N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))
B_list = list(map(int, sys.stdin.readline().split()))

A_list.sort()
B_list.sort(reverse=True)

result = 0
for i in range(N):
    result += A_list[i] * B_list[i]

print(result)