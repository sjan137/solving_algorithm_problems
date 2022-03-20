#---------- 6025 정수 2개 입력받아 합 계산하기 ----------
import sys

n1, n2 = map(int, sys.stdin.readline().split())
print(n1+n2)

#---------- 6026 실수 2개 입력받아 합 계산하기 ----------
import sys

n1 = float(sys.stdin.readline())
n2 = float(sys.stdin.readline())
print(n1+n2)

#---------- 6029 16진 정수 입력받아 8진수로 출력하기 ----------
import sys

n = int(sys.stdin.readline(), 16)
print('%o'%n)

#---------- 6030 영문자 1개 입력받아 10진수로 변환하기 ----------
import sys

n = ord(sys.stdin.readline().strip())
print(n)

#---------- 6031 정수 입력받아 유니코드 문자로 변환하기 ----------
import sys

c = int(sys.stdin.readline())
print(chr(c))

#---------- 6042 실수 1개 입력받아 소숫점 이하 자리 변환하기 ----------
import sys

a = float(sys.stdin.readline())
print(f"{a:0.2f}")

