import sys

rest_set = set()
for i in range(10):
    num = int(sys.stdin.readline())
    rest_set.add(num%42)
print(len(rest_set))