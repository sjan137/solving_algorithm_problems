import sys

def zipCoordinates(x_list):
    # 입력된 x값 목록을 세트-리스트로 변환하면서 겹치는 x값 제거
    x_unique = list(set(x_list))
    count_hash = {}
    # 각 x값마다 중복 제거한 x값 목록의 모든 값과 일일이 비교
    for x_ref in x_unique:
        count = 0
        for x in x_unique:
            if x_ref > x: count += 1
        count_hash[x_ref] = count
    
    for x in x_list:
        print(count_hash[x], end=' ')

N = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().split()))
zipCoordinates(x_list)