import sys

def main():
    T = int(sys.stdin.readline())
    result = []

    for _ in range(T):
        N, idx = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        idx_list = list(range(N))
        cnt = 1
        max_idx = nums.index(max(nums))
        
        while idx != idx_list[max_idx]:
            nums = nums[max_idx+1:] + nums[:max_idx]
            idx_list = idx_list[max_idx+1:] + idx_list[:max_idx]
            max_idx = nums.index(max(nums))
            cnt += 1
        result.append(cnt)

    return result

if __name__ == "__main__":
    print('\n'.join(map(str, main())))