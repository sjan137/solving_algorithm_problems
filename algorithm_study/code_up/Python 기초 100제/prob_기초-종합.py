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

#---------- 6084 소리 파일 저장용량 계산하기 ----------
import sys

h, b, c, s = map(int, sys.stdin.readline().split())
print(f"{h*b*c*s/(8*1024*1024):.1f} MB")

#---------- 6085 그림 파일 저장용량 계산하기 ----------
import sys

w, h, b = map(int, sys.stdin.readline().split())
print(f"{w*h*b/(8*1024*1024):.2f} MB")

#---------- 6086 거기까지! 이제 그만~ ----------
import sys

n = int(sys.stdin.readline())
s, result = 1, 0
while 1:
    result += s
    s += 1
    if result >= n:
        break

print(result)

#---------- 6087 3의 배수는 통과 ----------
import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    if i%3 == 0: continue
    print(i, end=' ')

#---------- 6088 수 나열하기1 ----------
import sys

a, d, n = map(int, sys.stdin.readline().split())
print(a+d*(n-1))

#---------- 6089 수 나열하기2 ----------
import sys

a, r, n = map(int, sys.stdin.readline().split())
print(a*(r**(n-1)))

#---------- 6090 수 나열하기3 ----------
import sys

a, m, d, n = map(int, sys.stdin.readline().split())
print(a*(m**(n-1))+d*sum([m**i for i in range(n-1)]))
# a
# a*m+d=am+d
# (a*m+d)*m+d=amm+d(m+1)
# ammm+dm(m+1)+d=ammm+d(mm+m+1)