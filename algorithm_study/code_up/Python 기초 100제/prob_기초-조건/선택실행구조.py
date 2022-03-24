#---------- 6065 정수 3개 입력받아 짝수만 출력하기 ----------
import sys

a, b, c = map(int, sys.stdin.readline().split())
if a % 2 == 0: print(a)
if b % 2 == 0: print(b)
if c % 2 == 0: print(c)

#---------- 6066 정수 3개 입력받아 짝/홀 출력하기 ----------
import sys

a, b, c = map(int, sys.stdin.readline().split())
print('even') if a%2==0 else print('odd')
print('even') if b%2==0 else print('odd')
print('even') if c%2==0 else print('odd')

#---------- 6067 정수 1개 입력받아 분류하기 ----------
import sys

n = int(sys.stdin.readline())
if n < 0:
    if n%2==0: print("A")
    else: print("B")
else:
    if n%2==0: print("C")
    else: print("D")

#---------- 6068 점수 입력받아 평가 출력하기 ----------
import sys

n = int(sys.stdin.readline())
if n >= 90: print("A")
elif n >= 70: print("B")
elif n >= 40: print("C")
else: print("D")

#---------- 6069 평가 입력받아 다르게 출력하기 ----------
import sys

s = sys.stdin.readline().strip()
if s == "A": print("best!!!")
elif s == "B": print("good!!")
elif s == "C": print('run!')
elif s == "D": print("slowly~")
else: print("what?")

#---------- 6070 월 입력받아 계절 출력하기 ----------
import sys

m = int(sys.stdin.readline())
if m//3 == 1: print("spring")
elif m//3 == 2: print("summer")
elif m//3 == 3: print("fall")
else: print("winter")