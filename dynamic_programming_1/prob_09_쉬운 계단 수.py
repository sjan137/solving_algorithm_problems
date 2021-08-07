import sys


def solve(n):
    count = [[0] * 10 for _ in range(n)]
    for i in range(n):
        if i == 0:
            for j in range(1, 10):
                count[i][j] += 1
        else:
            for j in range(10):
                a = count[i-1][j]
                b = stair_dict[str(j)]
                for k in b:
                    count[i][k] += a
    return sum(count[-1])

N = int(sys.stdin.readline())
stair_dict = {'0': [1], '9': [8]}
for i in range(1, 9):
    stair_dict[str(i)] = [i-1, i+1]
to_div = 10 ** 9
print(solve(N) % to_div)