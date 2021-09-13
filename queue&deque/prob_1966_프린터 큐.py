import sys
from collections import deque

def main():
    T = int(sys.stdin.readline())
    result = []

    for _ in range(T):
        N, idx = map(int, sys.stdin.readline().split())
        nums = deque(map(int, sys.stdin.readline().split()))
        idx_list = deque(range(N))
        cnt = 0

        while True:
            if nums[0] == max(nums):
                cnt += 1
                if idx_list[0] == idx: break
                else:
                    nums.popleft()
                    idx_list.popleft()
            else:
                nums.append(nums.popleft())
                idx_list.append(idx_list.popleft())
        
        result.append(cnt)

    return result

if __name__ == "__main__":
    print('\n'.join(map(str, main())))