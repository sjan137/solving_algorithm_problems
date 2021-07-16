import sys

def getMinConstructor(n):
    n_digit_list = [int(i) for i in str(n)]
    n_start = n - (9 * (len(n_digit_list) - 1) + n_digit_list[0])
    while n_start < n:
        n_start_digit_sum = n_start + sum([int(i) for i in str(n_start)])
        if n_start_digit_sum == n:
            print(n_start)
            break
        n_start += 1
    if n_start == n: print(0)

N = int(sys.stdin.readline())
getMinConstructor(N)