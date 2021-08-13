import sys


def solve(n, num_list):
    max_sum = -1 * (10 ** 8)

    for i in range(1, n):
        for j in range(i, n):
            num_sum = sum(num_list[j-i:j])
            if max_sum < num_sum: max_sum = num_sum

    return max_sum

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(solve(N, nums))