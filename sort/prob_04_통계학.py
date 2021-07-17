import sys

def getFourStaticValues(n, num_list, num_count, acc_num):
    # 산술평균 출력
    print('%0.0f' % (acc_num/n))

    # 중앙값 출력
    num_list.sort()
    print(num_list[n//2])

    # 최빈값 출력
    max_count = max(num_count)
    if num_count.count(max_count) == 1:
        print(num_count.index(max_count) - 4000)
    elif num_count.count(max_count) > 1:
        num_count[num_count.index(max_count)] = 0
        print(num_count.index(max_count) - 4000)

    # 범위 출력
    print(num_list[n-1] - num_list[0])

N = int(sys.stdin.readline())
num_list = list()
num_count = [0] * 8001
acc_sum = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)
    num_count[num+4000] += 1
    acc_sum += num
getFourStaticValues(N, num_list, num_count, acc_sum)