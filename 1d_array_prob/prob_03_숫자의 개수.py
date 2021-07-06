import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
abc = list(str(a * b * c))
abc.sort()

for i in range(10):
    count = abc.count(str(i))
    print(count)