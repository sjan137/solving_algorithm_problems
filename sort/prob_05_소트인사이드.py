import sys

N = [int(string) for string in str(sys.stdin.readline().strip())]
N.sort()
N_str = str()
while N:
    N_str += str(N.pop())
print(N_str)