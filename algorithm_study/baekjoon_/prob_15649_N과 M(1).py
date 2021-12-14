import sys

def getComb(n, m, visited, result):
    if len(result) == m: print(*result)
    for i in range(n):
        if visited[i]: continue
        result.append(i+1)
        visited[i] = True
        getComb(n, m, visited, result)
        result.pop()
        visited[i] = False
    return None

N, M = list(map(int, sys.stdin.readline().split()))
check = [False] * N
getComb(N, M, check, [])