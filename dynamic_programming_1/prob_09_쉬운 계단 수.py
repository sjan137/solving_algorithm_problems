import sys


def solve(n):
    if len(stair_num) == n:
        result.append(1)
        return None

    for i in range(10):
        if not stair_num:
            if i == 0: continue
            stair_num.append(i)
            solve(n)
            stair_num.pop()
        elif abs(stair_num[-1] - i) == 1:
            stair_num.append(i)
            solve(n)
            stair_num.pop()
    return None

N = int(sys.stdin.readline())
stair_num = []
result = []
solve(N)
print(len(result))