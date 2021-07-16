import sys

def minChange(m, n, board):
    # 기준 생성
    ref = ['WB', 'BW']
    
    m_start = 0
    total_result = list()
    while m_start + 8 <= m:
        n_start = 0
        while n_start + 8 <= n:
            result1 = list()
            result2 = list()
            for i in range(m_start, m_start+8):
                row = board[i]
                for j in range(n_start, n_start+8):
                    if i % 2 == 0:
                        result1.append(row[j] == ref[0][j%2])
                        result2.append(row[j] == ref[1][j%2])
                    else:
                        result1.append(row[j] == ref[1][j%2])
                        result2.append(row[j] == ref[0][j%2])
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