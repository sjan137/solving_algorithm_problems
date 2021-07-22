import sys

def permutation(n, m):
    num_list = list(range(1, n+1))
    limit_count = 1
    for i in range(n-m+1, n+1):
        if i == 0: continue
        limit_count *= i
    print(limit_count)

# 1<=M<=N<=8
N, M = map(int, sys.stdin.readline().split())
permutation(N, M)