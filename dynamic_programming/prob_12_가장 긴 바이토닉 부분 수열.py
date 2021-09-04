import sys


def solve(n, n_list):
    asc_list = [0] * n
    desc_list = [0] * n
    for i in range(n):
        for j in range(i):
            if n_list[i] > n_list[j]:
                if asc_list[i] < asc_list[j]: asc_list[i] = asc_list[j]
            if n_list[-i-1] > n_list[-j-1]:
                if desc_list[-i-1] < desc_list[-j-1]: desc_list[-i-1] = desc_list[-j-1]
        asc_list[i] += 1
        desc_list[-i-1] += 1

    result = [asc_list[i]+desc_list[i]-1 for i in range(n)]
    return max(result)

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
print(solve(N, num_list))