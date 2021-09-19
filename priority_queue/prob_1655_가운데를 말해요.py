import sys, heapq

# 0. 중간값은 숫자를 나열했을 때(예시: 1, 2, 3, 4, 5), 반을 기준(홀수일 경우 최대 힙에 +1)으로 최대 힙과 최소 힙으로 분리하고,
# 최대 힙(3, 2, 1)의 [0]번째 값을 중간값으로 정의한다.
# 1. 최대 힙, 최소 힙을 생성
# 2-1. 숫자 하나를 입력 받았을 때, 최대 힙이 비어있거나, 최대 힙의 [0]번째보다 작으면 최대 힙에 push, 
#      push 후에 '최대 힙의 길이 > 최소 힙의 길이 + 1'이면 최대 힙에서 pop한 값을 최소 힙에 push
# 2-2. 아닌 경우에는 최소 힙에 push
#      push 후에 '최대 힙의 길이 < 최소 힙의 길이'라면 최소 힙에서 pop한 값을 최대 힙에 push
N = int(sys.stdin.readline())
max_hq, min_hq = [], []

for _ in range(N):
    num = int(sys.stdin.readline())
    if not max_hq or num < -max_hq[0]:
        heapq.heappush(max_hq, -num)
        if len(max_hq) > len(min_hq) + 1: heapq.heappush(min_hq, -heapq.heappop(max_hq))
    else:
        heapq.heappush(min_hq, num)
        if len(max_hq) < len(min_hq): heapq.heappush(max_hq, -heapq.heappop(min_hq))
    print(-max_hq[0])