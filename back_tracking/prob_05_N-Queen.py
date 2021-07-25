import sys

def nQueen(x, y, n):
    for i in range(y):
        if x == x_check[i]: return 0
        if y == y_check[i]: return 0
        if abs(x - x_check[i]) == abs(y - y_check[i]): return 0
    
    if y == n-1: return 1
    
    x_check[y] = x
    y_check[y] = y
    
    count = 0
    for i in range(n):
        count += nQueen(i, y+1, n)

    return count

N, count = int(sys.stdin.readline()), 0
x_check = [None] * N
y_check = [None] * N
for i in range(N):
    count += nQueen(i, 0, N)
print(count)