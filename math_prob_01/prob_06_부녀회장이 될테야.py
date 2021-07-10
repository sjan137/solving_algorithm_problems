import sys

T = int(sys.stdin.readline())
for t in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    n_list = list()
    temp_list = [0] * N
    for n in range(N):
        n_list.append(n+1)
    for k in range(1, K+1):
        for n in range(N):
            temp_list[n] = sum(n_list[:n+1])
        n_list = temp_list[:]
    print(n_list[n])