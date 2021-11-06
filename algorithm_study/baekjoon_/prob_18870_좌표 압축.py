import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums_sorted = sorted(list((set(nums))))
nums_dict = {}

for i in range(len(nums_sorted)):
    nums_dict[nums_sorted[i]] = i

for i in nums:
    print(nums_dict[i], end=' ')