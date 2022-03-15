import sys

a = str(sys.stdin.readline().strip())
for i in range(3):
    print(a[2*i:2*i+2], sep=' ')