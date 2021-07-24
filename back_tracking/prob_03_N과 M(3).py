import sys

def allCase(n, m):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    else:
        for i in range(n):
            result.append(i+1)
            allCase(n, m)
            result.pop()

N, M = map(int, sys.stdin.readline().split())
result = list()
allCase(N, M)