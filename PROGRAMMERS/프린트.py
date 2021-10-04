from collections import deque

def solution(priorities, location):
    answer = 0
    N = len(priorities)
    nums = deque(priorities)
    idx_list = deque(range(N))

    while True:
        if nums[0] == max(nums):
            answer += 1
            if idx_list[0] == location: break
            else:
                nums.popleft()
                idx_list.popleft()
        else:
            nums.append(nums.popleft())
            idx_list.append(idx_list.popleft())

    return answer