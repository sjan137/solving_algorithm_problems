import sys


def solve(n, num_list):
    result = [[-1 * (10 ** 8)] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == j: result[i][i] = num_list[j]
            else:
                result[i][j] = result[i][j-1] + num_list[j]

    max_sum = -1 * (10 ** 8)
    for row in result:
        if max(row) > max_sum: max_sum = max(row)
    return max_sum

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(solve(N, nums))