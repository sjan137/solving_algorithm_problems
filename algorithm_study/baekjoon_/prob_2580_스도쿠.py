import sys

def isPossible(x, y, num, board):
    for i in range(9):
        if board[i][x] == num: return False
        if board[y][i] == num: return False
    
    a, b = x//3, y//3
    for three_rows in board[3*b:3*b+3]:
        if num in three_rows[3*a:3*a+3]: return False
    
    return True

def solveSudoku(nums, blanks, solved):
    global flag
    if flag: return

    if solved == len(blanks):
        flag = True
        for row in nums:
            print(*row)
        return
    
    y, x = blanks[solved]
    for num in range(1, 10):
        if not isPossible(x, y, num, nums): continue
        nums[y][x] = num
        solveSudoku(nums, blanks, solved+1)
        nums[y][x] = 0
    
    return

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
flag = False
solveSudoku(board, zeros, 0)