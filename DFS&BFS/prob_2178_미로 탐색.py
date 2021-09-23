import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
positions = deque([(0, 0)])

while positions:
    ii, jj = positions.popleft()
    for di, dj in dr:
        i, j = ii+di, jj+dj
        if not(0 <= i < N and 0 <= j < M and maze[i][j] == 1): continue
        maze[i][j] = maze[ii][jj] + 1
        positions.append((i, j))

print(maze[-1][-1])