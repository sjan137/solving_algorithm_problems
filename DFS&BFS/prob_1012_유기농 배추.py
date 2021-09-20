import sys

def dfs(board, location, m, n):
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    y, x = location
    board[y][x] = 0
    
    for yy, xx in dr:
        if 0 <= x+xx < M and 0 <= y+yy < N and board[y+yy][x+xx]: dfs(board, [y+yy, x+xx], m, n)

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0] * M for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: continue
            cnt += 1
            dfs(board, [i, j], M, N)
    
    print(cnt)