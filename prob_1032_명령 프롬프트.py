import sys

N = int(sys.stdin.readline())
files = [sys.stdin.readline().strip() for _ in range(N)]
result = ''

for i in range(len(files[0])):
    flag = False
    for j in range(N-1):
        if flag: continue
        elif files[j][i] != files[j+1][i]: flag = True
    if flag: result += '?'
    else: result += files[0][i]

print(result)