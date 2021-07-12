import sys

M, N = map(int, sys.stdin.readline().split())

if M <= 2:
    M = 2

sosu_list = list(range(2, N+1))
start = 0
while sosu_list[start] <= int(N**0.5):
    for sosu in sosu_list[start+1:]:
        if sosu % sosu_list[start] == 0: sosu_list.remove(sosu)
    print(sosu_list[start])
    start += 1
    print(sosu_list)

for sosu in sosu_list:
    if sosu >= M: print(sosu)