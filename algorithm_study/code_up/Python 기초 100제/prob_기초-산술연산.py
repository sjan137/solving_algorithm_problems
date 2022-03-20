#---------- 6032 정수 1개 입력받아 부호 바꾸기 ----------
import sys

n = int(sys.stdin.readline())
print(-n)

#---------- 6033 문자 1개 입력받아 다음 문자 출력하기 ----------
import sys

n = ord(sys.stdin.readline().strip())
print(chr(n+1))

#---------- 6034 정수 2개 입력받아 차 계산하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(a-b)

#---------- 6035 실수 2개 입력받아 곱 계산하기 ----------
import sys

a, b = map(float, sys.stdin.readline().split())
print(a*b)

#---------- 6036 단어 여러 번 출력하기 ----------
import sys

w, n = sys.stdin.readline().split()
print(w*int(n))

#---------- 6037 문장 여러 번 출력하기 ----------
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
print(s*n)

#---------- 6038 정수 2개 입력받아 거듭제곱 계산하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(a**b)

#---------- 6039 실수 2개 입력받아 거듭제곱 계산하기 ----------
import sys

a, b = map(float, sys.stdin.readline().split())
print(a**b)

#---------- 6040 정수 2개 입력받아 나눈 몫 계산하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(a//b)

#---------- 6041 정수 2개 입력받아 나눈 나머지 계산하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(a%b)

#---------- 6043 실수 2개 입력받아 나눈 결과 계산하기 ----------
import sys

f1, f2 = map(float, sys.stdin.readline().split())
print(f"{f1/f2:.3f}")

#---------- 6044 정수 2개 입력받아 자동 계산하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(f"{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}\n{a/b:.2f}")

#---------- 6045 정수 3개 입력받아 합과 평균 출력하기 ----------
import sys

a, b, c = map(int, sys.stdin.readline().split())
n_sum = a + b + c
print(n_sum, f"{n_sum/3:.2f}")

