import sys
import heapq

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    heapq.heappush(nums, int(sys.stdin.readline()))

while nums:
    print(heapq.heappop(nums))