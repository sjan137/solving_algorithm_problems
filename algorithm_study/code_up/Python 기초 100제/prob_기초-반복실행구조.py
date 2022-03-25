#---------- 6071 0 입력될 때까지 무한 출력하기 ----------
import sys

n = int(sys.stdin.readline())
while n != 0:
    print(n)
    n = int(sys.stdin.readline())

#---------- 6072 정수 1개 입력받아 카운트다운 출력하기1 ----------
import sys

n = int(sys.stdin.readline())
while n != 0:
    print(n)
    n -= 1

#---------- 6073 정수 1개 입력받아 카운트다운 출력하기2 ----------
import sys

n = int(sys.stdin.readline())
while n != 0:
    n -= 1
    print(n)

#---------- 6074 문자 1개 입력받아 알파벳 출력하기 ----------
import sys

e = ord(sys.stdin.readline().strip())
s = ord('a')
while s <= e:
    print(chr(s), end=' ')
    s += 1

#---------- 6075 정수 1개 입력받아 그 수까지 출력하기1 ----------
import sys

n = int(sys.stdin.readline())
s = 0
while s <= n:
    print(s)
    s += 1

#---------- 6076 정수 1개 입력받아 그 수까지 출력하기2 ----------
import sys

n = int(sys.stdin.readline())
for i in range(n+1):
    print(i)