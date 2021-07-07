import sys

N = int(sys.stdin.readline().strip())
ref = 0
count = 0
acc_count = 0
while ref < N:
    ref = 6 * acc_count + 1
    count += 1
    acc_count += count
print(count)