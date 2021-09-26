import sys
from collections import deque

def BFS(baked, starts, m, n, h):
    q = deque(starts)
    dr = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    max_days = 0

    # 익는 일수 계산 및 max_days에 최대 일수 저장
    while q:
        i, j, k = q.popleft()
        for di, dj, dk in dr:
            ii, jj, kk = i+di, j+dj, k+dk
            if 0 <= ii < h and 0 <= jj < n and 0 <= kk < m and not baked[ii][jj][kk]:
                baked[ii][jj][kk] = baked[i][j][k] + 1
                max_days = max(max_days, baked[ii][jj][kk])
                q.append((ii, jj, kk))
    
    # 구울 수 있는 토마토는 모두 구운 후, 못 굽는 토마토가 있다면 -1 반환
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if not baked[i][j][k]: return -1
    
    # 최대 걸리는 일수는 max_days-1이다. 1로 시작하기  때문.
    return max_days-1 if max_days != 0 else 0

M, N, H = map(int, sys.stdin.readline().split())
tomato_box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
init_baked = []

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato_box[i][j][k] == 1: init_baked.append((i, j, k))

print(BFS(tomato_box, init_baked, M, N, H))