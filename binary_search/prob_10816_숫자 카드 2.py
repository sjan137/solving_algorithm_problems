import sys

def binarySearch(num, numbers, start, end):
    if start > end: return 0
    mid = (start + end) // 2
    if numbers[mid] < num: return binarySearch(num, numbers, mid+1, end)
    elif numbers[mid] > num: return binarySearch(num, numbers, start, mid-1)
    else:
        cnt = 1
        left_idx, right_idx = mid-1, mid+1
        while True:
            if start <= left_idx and numbers[left_idx] == num: left_idx -= 1
            elif right_idx <= end and numbers[right_idx] == num: right_idx += 1
            else: break
            cnt += 1
        return cnt

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
M = int(sys.stdin.readline())
toFind = list(map(int, sys.stdin.readline().split()))
result = []

for num in toFind:
    result.append(binarySearch(num, nums, 0, N-1))

print(*result)