import sys
from collections import deque

def bfs(board, visited, n, m, position):
    q = deque([position])
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        print(q)
        y, x = q.popleft()
        if 0 <= y < n and 0 <= x < m and board[y][x] and not visited[y][x]: visited[y][x] = True
        for dy, dx in dr:
            i, j = y+dy, x+dx
            if 0 <= i < n and 0 <= j < m and board[i][j] and not visited[i][j]:
                visited[i][j] = True
                q.append([i, j])

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    ones = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        ones[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if not ones[i][j] or visited[i][j]: continue
            cnt += 1
            bfs(ones, visited, N, M, [i, j])
    
    print(cnt)