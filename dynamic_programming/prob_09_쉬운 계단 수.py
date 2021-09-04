import sys


def solve(n):
    stair_dict = {'0': [1], '9': [8]}
    for i in range(1, 9):
        stair_dict[str(i)] = [i-1, i+1]
    count = [[0] * 10 for _ in range(n)]

    for i in range(n):
        if i == 0:
            for j in range(1, 10):
                count[i][j] += 1
        else:
            for j in range(10):
                pre_count = count[i-1][j]
                to_plus = stair_dict[str(j)]
                for k in to_plus:
                    count[i][k] += pre_count
    return sum(count[-1])

N = int(sys.stdin.readline())
to_div = 10 ** 9
print(solve(N) % to_div)