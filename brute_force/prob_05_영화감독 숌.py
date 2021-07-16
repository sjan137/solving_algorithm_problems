import sys

def numberOfEnd(n):
    num_init = 665
    count = 1
    while count <= n:
        num_init += 1
        if '666' in str(num_init): count += 1
    print(num_init)

N = int(sys.stdin.readline())
numberOfEnd(N)