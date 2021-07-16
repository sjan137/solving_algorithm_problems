import sys

def minChange(m, n, board):
    # 기준 생성
    ref = [str()] * 2
    for _ in range(n):
        if _ % 2 == 0:
            ref[0] += 'W'
            ref[1] += 'B'
        else:
            ref[0] += 'B'
            ref[1] += 'W'
    
    m_start = 0
    n_start = 0
    total_result = list()
    while m_start + 8 <= m:
        while n_start + 8 <= n:
            result1 = list()
            result2 = list()
            for i in range(m_start, m_start+8):
                row = board[i]
                for j in range(n_start, n_start+8):
                    if i % 2 == 0:
                        result1.append(row[j] == ref[0][j])
                        result2.append(row[j] == ref[1][j])
                    else:
                        result1.append(row[j] == ref[1][j])
                        result2.append(row[j] == ref[0][j])
            total_result.append(result1.count(False))
            total_result.append(result2.count(False))
            n_start += 1
        m_start += 1
    print(min(total_result))

M, N = map(int, sys.stdin.readline().split())
board = list()
for _ in range(M):
    board_tile = str(sys.stdin.readline().strip())
    board.append(board_tile)
minChange(M, N, board)