import sys
from collections import deque

def bfs(board, n, position, visited):
    dr = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    area = 0
    q = deque([position])

    while q:
        x, y = q.popleft()
        for xx, yy in dr:
            if 0 <= x+xx < n and 0 <= y+yy < n and board[x+xx][y+yy] and not visited[x+xx][y+yy]:
                q.append([x+xx, y+yy])
                visited[x+xx][y+yy] = True
                area += 1
    
    return area

def main():
    N = int(sys.stdin.readline())
    board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = []
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if not board[i][j] or visited[i][j]: continue
            result.append(bfs(board, N, [i, j], visited))
            cnt += 1

    return [cnt] + sorted(result)

if __name__ == "__main__":
    for i in main():
        print(i)