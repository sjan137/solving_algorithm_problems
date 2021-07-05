import sys

T = int(sys.stdin.readline())
for t in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    new_S = str()
    for s_str in S:
        new_S += s_str * R
    print(new_S)