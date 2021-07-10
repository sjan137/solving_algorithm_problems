import sys

T = int(sys.stdin.readline())
for t in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    w, h = map(str, divmod(N, H))
    if h == '0': h = str(H)
    else: w = str(int(w) + 1)
    if len(w) < 2: w = '0' + str(w)
    print(h+w)