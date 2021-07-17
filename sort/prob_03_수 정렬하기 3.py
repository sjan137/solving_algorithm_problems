import sys

N = int(sys.stdin.readline())
num_counts = [0] * 10001
for _ in range(N):
    num_counts[int(sys.stdin.readline())] += 1
for num in range(1, len(num_counts)):
    if num_counts[num] == 0: continue
    else:
        while num_counts[num] != 0:
            print(num)
            num_counts[num] -= 1