#---------- 6092 이상한 출석 번호 부르기1 ----------
import sys

n = int(sys.stdin.readline())
called = list(map(int, sys.stdin.readline().split()))
result = [0 for _ in range(24)]

for i in called:
    result[i] += 1

for i in range(1, 24):
    print(result[i], end=' ')

#---------- 6093 이상한 출석 번호 부르기2 ----------
import sys

n = int(sys.stdin.readline())
called = list(map(int, sys.stdin.readline().split()))
called.reverse()
print(*called)

#---------- 6094 이상한 출석 번호 부르기3 ----------
import sys

n = int(sys.stdin.readline())
called = list(map(int, sys.stdin.readline().split()))
print(min(called))

#---------- 6095 바둑판에 흰 돌 놓기 ----------
import sys

board = [[0 for _ in range(19)] for _ in range(19)]
n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

for row in board:
    print(*row)

#---------- 6096 바둑알 십자 뒤집기 ----------
import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(19):
        board[x-1][i] ^= 1
        board[i][y-1] ^= 1

for row in board:
    print(*row)

#---------- 6097 설탕과자 뽑기 ----------
import sys

h, w = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(w)] for _ in range(h)]
n = int(sys.stdin.readline())

for _ in range(n):
    l, garosero, y, x = map(int, sys.stdin.readline().split())
    for i in range(l):
        if garosero == 0:
            if y<=h and x+i<=w: board[y-1][x-1+i] = 1
        else:
            if y+i<=h and x<=w: board[y-1+i][x-1] = 1

for row in board:
    print(*row)

#---------- 6098 성실한 개미 ----------
import sys

maze = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
yx = (1, 1)
maze[1][1] = 9

while True:
    y, x = yx[0], yx[1]
    if maze[y][x+1] != 1:
        x += 1
    elif maze[y+1][x] != 1:
        y += 1
    else: break

    if maze[y][x] == 2:
        maze[y][x] = 9
        break
    else: maze[y][x] = 9

    yx = (y, x)

for row in maze:
    print(*row)