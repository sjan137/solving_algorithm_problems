import sys

result = 0

for i in range(8):
    row = list(sys.stdin.readline().strip())
    if i % 2 == 0:
        for j in range(8):
            if (j % 2 == 0) and (row[j] == 'F'): result += 1
    else:
        for j in range(8):
            if (j % 2 == 1) and (row[j] == 'F'): result += 1

print(result)