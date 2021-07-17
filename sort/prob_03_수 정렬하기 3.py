import sys

N = int(sys.stdin.readline())
num_list = list()
for i in range(N):
    num_list.append(int(sys.stdin.readline()))
num_counts = [0]
for i in range(1, max(num_list)+1):
    num_counts.append(num_counts[i-1] + num_list.count(i))
result = [0] * N
while len(num_list):
    last = num_list.pop()
    result[num_counts[last]-1] = last
    num_counts[last] = num_counts[last] - 1
for i in result:
    print(i)