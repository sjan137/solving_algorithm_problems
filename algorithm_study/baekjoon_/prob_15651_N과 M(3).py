import sys

def getComb(n, m, result):
    if len(result) == m: print(*result)
    else:
        for i in range(n):
            result.append(i+1)
            getComb(n, m, result)
            result.pop()
    return None

N, M = list(map(int, sys.stdin.readline().split()))
getComb(N, M, [])