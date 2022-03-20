#---------- 6009 문자 1개 입력받아 그대로 출력하기 ----------
import sys

a = sys.stdin.readline()
print(a)

#---------- 6010 정수 1개 입력받아 int로 변환하여 출력하기 ----------
import sys

n = int(sys.stdin.readline())
print(n)

#---------- 6011 실수 1개를 입력받아 변환하여 출력하기 ----------
import sys

f = float(sys.stdin.readline())
print(f)

#---------- 6012 정수 2개 입력받아 그대로 출력하기1 ----------
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(f"{a}\n{b}")

#---------- 6013 문자 2개 입력받아 순서 바꿔 출력하기 ----------
import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
print(f"{b}\n{a}")

#---------- 6014 실수 1개 입력받아 3번 출력하기 ----------
import sys

a = float(sys.stdin.readline())
print(f"{a}\n{a}\n{a}")

#---------- 6015 정수 2개 입력받아 그대로 출력하기2 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(f'{a}\n{b}')

#---------- 6016 문자 2개 입력받아 순서 바꿔 출력하기2 ----------
import sys

a, b = map(str, sys.stdin.readline().split())
print(f'{b} {a}')

#---------- 6017 문장 1개 입력받아 3번 출력하기 ----------
import sys

a = str(sys.stdin.readline().strip())
print(a, a, a)

#---------- 6018 시간 입력받아 그대로 출력하기 ----------
import sys

a = str(sys.stdin.readline().strip())
print(a)

#---------- 6019 연원일 입력받아 순서 바꿔 출력하기 ----------
import sys

y, m, d = map(int, sys.stdin.readline().split('.'))
print(d, m, y, sep='-')

#---------- 6020 주민번호 입력받아 형태 바꿔 출력하기 ----------
import sys

f, b = map(str, sys.stdin.readline().split('-'))
print(f+b)

#---------- 6021 단어 1개 입력받아 나누어 출력하기 ----------
import sys

a = str(sys.stdin.readline().strip())
for i in range(len(a)):
    print(a[i])

#---------- 6022 연월일 입력받아 나누어 출력하기 ----------
import sys

a = str(sys.stdin.readline().strip())
for i in range(3):
    print(a[2*i:2*i+2], sep=' ')

#---------- 6023 시분초 입력받아 분만 출력하기 ----------
import sys

h, m, s = map(str, sys.stdin.readline().split(':'))
print(m)

#---------- 6024 단어 2개 입력받아 이어 붙이기 ----------
import sys

w1, w2 = sys.stdin.readline().split()
print(w1+w2)

