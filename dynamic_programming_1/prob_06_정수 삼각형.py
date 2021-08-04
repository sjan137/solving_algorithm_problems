import sys


def int_triangle(n, num_arr, check):
    for i in range(n):
        for j in range(i+1):
            if i == 0: check[i][j] = num_arr[i][j]
            else:
                if j == 0: check[i][j] = check[i-1][j] + num_arr[i][j]
                elif j == i: check[i][j] = check[i-1][j-1] + num_arr[i][j]
                else:
                    check[i][j] = max(check[i-1][j-1], check[i-1][j]) + num_arr[i][j]
    return max(check[n-1])

N = int(sys.stdin.readline())
num_piramid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check_piramid = [[0] * (i+1) for i in range(N)]
print(int_triangle(N, num_piramid, check_piramid))