import sys

N = int(sys.stdin.readline())
arrA = list(map(int, sys.stdin.readline().split()))
new_arrA = sorted(arrA)
dictA = {}

for idx, a in enumerate(new_arrA):
    if a in dictA: dictA[a].append(idx)
    else: dictA[a] = [idx]

arrP = [dictA[a].pop(0) for a in arrA]

print(*arrP)