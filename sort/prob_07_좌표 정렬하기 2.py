import sys

def yx_sort(yx_hash):
    y_keys = list(yx_hash.keys())
    y_keys.sort()
    for y in y_keys:
        yx_hash[y].sort(reverse=True)
        while len(yx_hash[y]) != 0:
            print(yx_hash[y].pop(), y)

N = int(sys.stdin.readline())
yx_hash = {}
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y in yx_hash.keys():
        yx_hash[y].append(x)
    else: yx_hash[y] = [x]
yx_sort(yx_hash)