import sys

def getComb(n, m, visited, result, start):
    if len(result) == m: print(*result)
    for i in range(start, n+1):
        if visited[i-1]: continue
        result.append(i)
        visited[i-1] = True
        getComb(n, m, visited, result, i+1)
        result.pop()
        visited[i-1] = False
    return None

N, M = list(map(int, sys.stdin.readline().split()))
check = [False] * N
getComb(N, M, check, [], 1)