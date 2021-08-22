import sys


def gcd(a, b):
    return gcd(b%a, a) if b%a else a

def solve(n_list):
    result = []
    n_list.sort()
    if len(n_list) == 2:
        gcd_num = n_list[1] - n_list[0]
        for i in range(2, min(n_list)+1):
            if gcd_num % i == 0: result.append(i)
    else:
        gcd_num = gcd(n_list[1]-n_list[0], n_list[2]-n_list[0])
        for i in range(2, gcd_num+1):
            if gcd_num % i == 0: result.append(i)
    print(*result)
    return None

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
solve(numbers)