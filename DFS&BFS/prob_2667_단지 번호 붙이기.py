import sys
from collections import deque

# BFS 이용한 코드(deque) - 32108KB, 96ms
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

# DFS 이용한 코드(재귀 호출) - 29304KB, 76ms
def dfs(board, n, position, visited):
    dr = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    area = 0
    x, y = position
    
    for dx, dy in dr:
        if 0 <= x+dx < n and 0 <= y+dy < n and board[x+dx][y+dy] and not visited[x+dx][y+dy]:
            visited[x+dx][y+dy] = True
            area += 1
            area += dfs(board, n, [x+dx, y+dy], visited)
    
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
            # result.append(bfs(board, N, [i, j], visited))  # BFS - 32108KB, 96ms
            result.append(dfs(board, N, [i, j], visited))  # DFS - 29304KB, 76ms
            cnt += 1

    return [cnt] + sorted(result)

if __name__ == "__main__":
    for i in main():
        print(i)