import sys

N = int(sys.stdin.readline())
acc_sum = 0
nums_cnt = [0] * 8001
nums_list = []

for _ in range(N):
    num = int(sys.stdin.readline())
    acc_sum += num
    nums_cnt[num+4000] += 1
    nums_list.append(num)

nums_list.sort()

# 산술평균
print(int(round(acc_sum/N, 0)))

# 중앙값
print(nums_list[N//2])

# 최빈값
max_cnt = max(nums_cnt)
idx = nums_cnt.index(max_cnt)
if nums_cnt.count(max_cnt) == 1:
    print(idx-4000)
else:
    nums_cnt[idx] = 0
    new_idx = nums_cnt.index(max_cnt)
    print(new_idx-4000)

# 범위
print(nums_list[N-1]-nums_list[0])