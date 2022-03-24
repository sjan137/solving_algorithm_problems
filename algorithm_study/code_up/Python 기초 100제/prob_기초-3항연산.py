#---------- 6063 정수 2개 입력받아 큰 값 출력하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(a if a>b else b)

#---------- 6064 정수 3개 입력받아 가장 작은 값 출력하기 ----------
import sys

a, b, c = map(int, sys.stdin.readline().split())
res = b if b < c else c
print(a if a < res else res)