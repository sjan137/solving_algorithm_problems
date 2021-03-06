import sys

# DFS, 재귀
def permutation(n, m):
    if len(row) == m:
        print(' '.join(map(str, row)))
        return
    else:
        for i in range(n):
            if check[i]: continue
            row.append(i+1)
            check[i] = True
            permutation(n, m)
            row.pop()
            check[i] = False

# 1<=M<=N<=8
N, M = map(int, sys.stdin.readline().split())
check = [False] * N
row = list()
permutation(N, M)