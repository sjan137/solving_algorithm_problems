import sys
from collections import deque

def BFS(baked, starts, n, m):
    flag = False  # 익을 수 있는 모든 토마토가 익은 후, 0이 남아있다면 True
    max_cnt = 0  # 가장 오래 걸리는 일수 저장
    q = deque(starts)
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        i, j = q.popleft()
        for di, dj in dr:
            if 0 <= i+di < n and 0 <= j+dj < m and not baked[i+di][j+dj]:
                baked[i+di][j+dj] = baked[i][j] + 1
                q.append((i+di, j+dj))
                max_cnt = max(max_cnt, baked[i+di][j+dj])

    for i in range(N):
        for j in range(M):
            if not baked[i][j]:
                flag = True
                break
    
    return -1 if flag else (max_cnt-1 if max_cnt > 0 else 0)

M, N = map(int, sys.stdin.readline().split())
tomato_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
start_positions = []
for i in range(N):
    for j in range(M):
        if tomato_info[i][j] == 1: start_positions.append((i, j))

print(BFS(tomato_info, start_positions, N, M))