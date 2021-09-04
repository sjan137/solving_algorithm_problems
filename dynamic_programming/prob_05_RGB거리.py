import sys


def street_rgb(n, rgb_price, check):
    for i in range(n):
        for j in range(3):
            if i == 0:
                check[i][j] = rgb_price[i][j]
            else:
                check[i][j] = min(check[i-1][(j+1)%3], check[i-1][(j+2)%3]) + rgb_price[i][j]
    return min(check[n-1])

N = int(sys.stdin.readline())
rgb_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr_check = [[0] * 3 for _ in range(N)]
print(street_rgb(N, rgb_arr, arr_check))