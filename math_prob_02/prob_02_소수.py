import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
if (M > 2) and (M % 2 == 0): M += 1
n_list = list(range(M, N+1))
if 1 in n_list: n_list.remove(1)
temp_list = n_list[:]
for n in n_list:
    start = 2
    while start <= (n // 2):
        if n % start == 0:
            temp_list.remove(n)
            break
        start += 1
if len(temp_list) == 0: print(-1)
else:
    print(sum(temp_list))
    print(min(temp_list))