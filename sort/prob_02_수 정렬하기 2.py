import sys

N = int(sys.stdin.readline())
num_list = list()
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

result = sorted(num_list)
for i in result:
    print(i)