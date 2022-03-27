#---------- 6077 짝수 합 구하기 ----------
import sys

n = int(sys.stdin.readline())
even_sum = 0
for i in range(2, n+1, 2):
    even_sum += i
print(even_sum)

#---------- 6078 원하는 문자가 입력될 때까지 반복 출력하기 ----------
import sys

s = sys.stdin.readline().strip()
while s != 'q':
    print(s)
    s = sys.stdin.readline().strip()
print(s)

#---------- 6079 언제까지 더해야 할까? ----------
import sys

n = int(sys.stdin.readline())
n_sum, result = 0, 0
for i in range(n):
    n_sum += i+1
    if n_sum >= n:
        result = i+1
        break
print(result)

#---------- 6080 주사위 2개 던지기 ----------
import sys

n, m = map(int, sys.stdin.readline().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

#---------- 6081 16진수 구구단 출력하기 ----------
import sys

n = int(sys.stdin.readline(), 16)
for i in range(1, 16):
    print(f'{"%X"%n}*{"%X"%i}={"%X"%(n*i)}')

#---------- 6082 3 6 9 게임의 왕이 되자 ----------
import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    if i%10 in [3, 6, 9]:
        print("X", end =' ')
    else: print(i, end=' ')

#---------- 6083 빛 섞어 색 만들기 ----------
import sys

r, g, b = map(int, sys.stdin.readline().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
print(r*g*b)