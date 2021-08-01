import sys

def padovan(n):
    for i in range(n):
        if padovan_list[i]: continue
        padovan_list[i] = padovan_list[i-2] + padovan_list[i-3]
    return padovan_list[n-1]

T = int(sys.stdin.readline())
padovan_list = [1, 1, 1] + [0] * 97
for _ in range(T):
    print(padovan(int(sys.stdin.readline())))