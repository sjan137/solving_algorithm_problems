import sys

M, N = map(int, sys.stdin.readline().split())

isSosu = [False] * 2 + [True] * (N - 1)
for i in range(2, int(N**0.5)+1):
    if isSosu[i]:
        for j in range(2*i, N+1, i):
            isSosu[j] = False

for i in range(M, N+1):
    if isSosu[i]: print(i)