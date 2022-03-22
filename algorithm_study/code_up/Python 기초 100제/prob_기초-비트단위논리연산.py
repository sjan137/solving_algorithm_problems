#---------- 6059 비트단위로 NOT 하여 출력하기 ----------
import sys

n = int(sys.stdin.readline())
print(~n)

#---------- 6060 비트단위로 AND 하여 출력하기 ----------
import sys

a, b = map(int, sys.stdin.readline().split())
print(a&b)