import sys

def solveSudoku(sudoku_arr, empty_list, empty_count):
    # 전역 변수 flag를 통해 답이 나온 상태면, 다른 경우는 모두 리턴
    global flag
    if flag: return

    if empty_count == len(empty_list):
        for row in sudoku_arr:
            print(*row)
        # 첫 번째 답이 나오면 flag는 True로 설정
        flag = True
        return
    
    # 0인 경우는 필요 없지만, 각 칸의 숫자를 바로 인덱스로 활용하기 위해 True인 상태로 추가
    check = [True] + [False] * 9
    # 빈 칸(0) 리스트 중 'empty_count' 번째 좌표를 y, x에 저장
    y, x = empty_list[empty_count]
    # 해당 좌표의 가로, 세로에 겹치는 숫자 체크
    for i in range(9):
        if not check[sudoku_arr[y][i]]:
            check[sudoku_arr[y][i]] = True
        if not check[sudoku_arr[i][x]]:
            check[sudoku_arr[i][x]] = True
    
    # 빈 칸 좌표가 포함된 3X3 박스 체크
    b = y // 3
    a = x // 3
    for i in range(3*b, 3*b+3):
        for j in range(3*a, 3*a+3):
            if check[sudoku_arr[i][j]]: continue
            check[sudoku_arr[i][j]] = True

    for i in range(1, 10):    # check[0]은 무의미
        if check[i]: continue
        sudoku_arr[y][x] = i
        solveSudoku(sudoku_arr, empty_list, empty_count+1)
        sudoku_arr[y][x] = 0
    return

sudoku_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
empty_list = [(i, j) for i in range(9) for j in range(9) if sudoku_arr[i][j] == 0]
flag = False
solveSudoku(sudoku_arr, empty_list, 0)