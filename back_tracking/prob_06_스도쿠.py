import sys

def solveSudoku(sudoku_arr, empty_list, start):
    if start == len(empty_list):
        # count2 = 0
#         for empty_index in empty_list:
            # a = empty_index[0]
            # b = empty_index[1]
            # sudoku_arr[a][b] = result[count2]
            # count2 += 1
        for row in sudoku_arr:
            print(*row)
        return
    
    check = [False] * 9
    check_point = empty_list[start]
    y = check_point[0]
    x = check_point[1]
    sudoku_col = list()
    sudoku_sqr = list()
    count = 0
    for row in sudoku_arr:
        sudoku_col.append(row[x])
        if (count//3) == (y//3):
            sudoku_sqr = sudoku_sqr + row[3*(x//3):3*(x//3)+3]
        count += 1
    for i in range(9):
        if (i+1) in sudoku_arr[y]: check[i] = True
        elif (i+1) in sudoku_col: check[i] = True
        elif (i+1) in sudoku_sqr: check[i] = True
    
    for i in range(9):
        if check[i]: continue
        sudoku_arr[y][x] = i+1
        solveSudoku(sudoku_arr, empty_list, start+1)
        sudoku_arr[y][x] = 0
    return

sudoku_arr = list()
empty_list = list()
result = list()
for _ in range(9):
    sudoku_arr.append(list(map(int, sys.stdin.readline().split())))
for i in range(9):
    for j in range(9):
        if sudoku_arr[i][j] == 0: empty_list.append([i, j])
solveSudoku(sudoku_arr, empty_list, 0)