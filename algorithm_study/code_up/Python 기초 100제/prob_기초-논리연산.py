#---------- 6052 정수 입력받아 참 거짓 평가하기 ----------
import sys

n = int(sys.stdin.readline())
print(bool(n))

#---------- 6053 참 거짓 바꾸기 ----------
import sys

n = int(sys.stdin.readline())
print(not bool(n))

#---------- 6054 둘 다 참일 경우만 참 출력하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(bool(a) and bool(b))

#---------- 6055 하나라도 참이면 출력하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(bool(a) or bool(b))

#---------- 6056 참/거짓이 서로 다를 때에만 참 출력하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
a, b = bool(a), bool(b)
print(((not a) and b) or (a and (not b)))

#---------- 6057 참/거짓이 서로 같을 때에만 참 출력하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
a, b = bool(a), bool(b)
print(((not a) and (not b)) or (a and b))

#---------- 6058 둘 다 거짓일 경우만 참 출력하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
a, b = bool(a), bool(b)
print(not(a or b))