import sys

def solveSudoku(y, x, sudoku_arr):
    if sudoku_arr[y][x] != 0: return
    
    result = list()
    sudoku_col = list()
    sudoku_sqr = list()
    count = 0
    for row in sudoku_arr:
        sudoku_col.append(row[x])
        if (count//3) == (y//3):
            sudoku_sqr = sudoku_sqr + row[x//3:x//3+3]
        count += 1
    for i in range(9):
        if (i+1) in sudoku_arr[y]: check[i] = True
        if (i+1) in sudoku_col[x]: check[i] = True
        if (i+1) in sudoku_sqr: check[i] = True
    
    for i in range(9):
        if check[i]: continue
        result.append(i+1)
    return

sudoku_arr = list()
check = [False] * 9
check_index = list(range(9))
check_num = list(range(1, 10))
for _ in range(9):
    sudoku_arr.append(list(map(int, sys.stdin.readline().split())))
for i in range(9):
    solveSudoku(i, 0, sudoku_arr)