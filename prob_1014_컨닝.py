import sys

# 1. 현재 위치(0, 0)에서 좌(-1, 0), 우(1, 0), 좌측 대각선 위(-1, -1), 우측 대각선 위(1, -1)에 자리가 있으면서(.) 사람이 없다면(0), 현재 위치 1
# 2. 모든 칸을 탐색하며 가능한 학생 수를 누적
# 3. M이 2 이상이라면 시작 위치를 (0, 1)에서도 탐색
def scan(board, n, m):
    direction = [(-1, 0), (1, 0), (-1, -1), (1, -1)]
    check = [[0] * M for _ in range(N)]
    result1 = 0
    result2 = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'x': continue
            flag = 0
            for xx, yy in direction:
                x, y = xx+j, yy+i
                if (0 <= x < m) and (0 <= y < n): flag += check[y][x]
            if flag == 0:
                check[i][j] = 1
                result1 += 1
    print(check)
    
    if m > 1:
        check2 = [[0] * M for _ in range(N)]
        for i in range(n):
            for j in range(m):
                if i == j == 0: continue
                if board[i][j] == 'x': continue
                flag = 0
                for xx, yy in direction:
                    x, y = xx+j, yy+i
                    if (0 <= x < m) and (0 <= y < n): flag += check2[y][x]
                if flag == 0:
                    check2[i][j] = 1
                    result2 += 1
        print(check2)
    
    return max(result1, result2)

C = int(sys.stdin.readline())
for _ in range(C):
    N, M = map(int, sys.stdin.readline().split())
    rows = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print('sol: ', scan(rows, N, M))