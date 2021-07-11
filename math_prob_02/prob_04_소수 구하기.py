import sys

M, N = map(int, sys.stdin.readline().split())

# 초기 설정
sosu_list = list()
if (M <= 2) and (N >= 2):
    sosu_list.append(2)
    M = 3
if M % 2 == 0: M += 1

mn_list = list(range(M, N+1, 2))
temp_list = mn_list[:]
for mn in mn_list:
    start = 2
    while start <= (mn//2):
        if mn % start == 0: break
        start += 1
    if start == (mn//2)+1: sosu_list.append(mn)

for sosu in sosu_list:
    print(sosu)