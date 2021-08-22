import sys


def solve(n_list):
    result = []
    for i in range(2, min(n_list)+1):
        if not check(n_list, i): result.append(i)
    print(*result)
    return None

def check(n_list, m):
    start = n_list[0] % m
    flag = False
    for i in range(1, len(n_list)):
        if start != (n_list[i] % m): flag = True
    return flag

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
solve(numbers)