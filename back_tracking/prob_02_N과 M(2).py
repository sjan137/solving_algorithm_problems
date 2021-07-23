import sys

def combination(start, n, m):
    if len(row) == m:
        print(' '.join(map(str, row)))
        return
    else:
        for i in range(start, n):
            if check[i]: continue
            check[i] = True
            row.append(i+1)
            combination(i+1, n, m)
            check[i] = False
            row.pop()

N, M = map(int, sys.stdin.readline().split())
check = [False] * N
row = list()
combination(0, N, M)