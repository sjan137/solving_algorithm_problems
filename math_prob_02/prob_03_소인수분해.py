N = int(input())
odd_list = list(range(3, N//2+1, 2))
sosu_list = odd_list[:]
result = list()

for odd in odd_list:
    start = 2
    while start <= (odd // 2):
        if odd % start == 0:
            sosu_list.remove(odd)
            break
        start += 1
sosu_list.insert(0, 2)

while N != 1:
    for sosu in sosu_list:
        if N % sosu == 0:
            result.append(sosu)
            N = N // sosu
            continue
        else: sosu_list.remove(sosu)
    if len(sosu_list) == 0: break

if len(result) == 0: print(N)
else:
    result.sort()
    for i in result:
        print(i)