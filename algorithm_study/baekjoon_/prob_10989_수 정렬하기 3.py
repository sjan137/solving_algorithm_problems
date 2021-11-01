import sys

N = int(sys.stdin.readline())
nums = [0] * 10001
idx = 0

for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

while idx < 10001:
    if nums[idx]:
        print(idx)
        nums[idx] -= 1
    else: idx += 1