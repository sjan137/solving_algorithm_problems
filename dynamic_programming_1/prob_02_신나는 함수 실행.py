import sys

# dynamic programming W
def dpW(a, b, c):
    if a <= 0 or b <= 0 or c<= 0:
        a = b = c = 0
        val[a][b][c] = 1
    elif a > 20 or b > 20 or c> 20:
        a = b = c = 20
    
    if val[a][b][c]: return val[a][b][c]
    else:
        if a < b and b < c:
            val[a][b][c] = dpW(a, b, c-1) + dpW(a, b-1, c-1) - dpW(a, b-1, c)
            return val[a][b][c]
        else:
            val[a][b][c] = dpW(a-1, b, c) + dpW(a-1, b-1, c) + dpW(a-1, b, c-1) - dpW(a-1, b-1, c-1)
            return val[a][b][c]

max_num = 21
val = [[[0] * max_num for _ in range(max_num)] for _ in range(max_num)]
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1: break
    print('w(%d, %d, %d) = %d' % (a, b, c, dpW(a, b, c)))