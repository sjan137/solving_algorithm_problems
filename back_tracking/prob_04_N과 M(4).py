import sys

def notDescSeq(n, m):
    if len(row) == m:
        print(' '.join(map(str, row)))
        return
    else:
        for i in range(n):
            if check[i]: continue
            check[:i] = [True] * i
            row.append(i+1)
            notDescSeq(n, m)
            check[:i] = [False] * i
            row.pop()

N, M = map(int, sys.stdin.readline().split())
check = [False] * N
row = list()
notDescSeq(N, M)