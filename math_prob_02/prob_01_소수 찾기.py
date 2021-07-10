import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
if 1 in n_list: n_list.remove(1)
temp_list = n_list[:]
for n in n_list:
    start = 2
    while start <= (n // 2):
        if n % start == 0:
            temp_list.remove(n)
            break
        start += 1
print(len(temp_list))