import sys

def zipCoordinates(x_list):
    x_unique = list(set(x_list))
    x_unique.sort()
    # 중복 제거한 x값 목록의 index는 해당 x보다 작은 숫자임을 의미
    count_hash = {}
    for i in range(len(x_unique)):
        count_hash[x_unique[i]] = i
    
    for x in x_list:
        print(count_hash[x], end=' ')

N = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
zipCoordinates(x_list)