import sys
from collections import deque

def bfs(board, n, position):
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    area = 0
    q = deque([position])

    while q:
        x, y = q.popleft()
        if board[x][y] == '1':
            board[x][y] = '0'
            area += 1
        for xx, yy in dr:
            if 0 <= x+xx < n and 0 <= y+yy < n and board[x+xx][y+yy] == '1': q.append([x+xx, y+yy])
    
    return area

def main():
    N = int(sys.stdin.readline())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    result = []
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == '0': continue
            area = bfs(board, N, [i, j])
            result.append(area)

    return [len(result)] + sorted(result)

if __name__ == "__main__":
    for i in main():
        print(i)