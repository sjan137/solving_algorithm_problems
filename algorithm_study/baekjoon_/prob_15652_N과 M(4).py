import sys

def getComb(n, m, visited, result):
    if len(result) == m: print(*result)
    else:
        for i in range(n):
            if visited[i]: continue
            visited[:i] = [True] * i
            result.append(i+1)
            getComb(n, m, visited, result)
            visited[:i] = [False] * i
            result.pop()
    return None

N, M = list(map(int, sys.stdin.readline().split()))
check = [False] * N
getComb(N, M, check, [])