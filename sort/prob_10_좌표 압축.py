import sys

def zipCoordinates(x_list):
    x_unique = list(set(x_list))
    x_unique.sort()
    # 각 원소별 개수를 딕셔너리로 저장
    count_hash = {}
    for x in x_unique:
        count_hash[x] = x_unique.count(x)
    
    # 원소마다 해당 원소보다 작은 원소들의 각 개수를 합해서 딕셔너리로 저장
    result_hash = {}
    for i in range(len(x_unique)):
        count = 0
        for j in range(i):
            count += count_hash[x_unique[j]]
        result_hash[x_unique[i]] = count
        
    for x in x_list:
        print(result_hash[x], end=' ')

N = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
zipCoordinates(x_list)