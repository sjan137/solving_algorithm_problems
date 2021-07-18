import sys

def xySort(xy_list):
    change_count = 1
    while change_count != 0:
        change_count = 0
        i = 0
        while i < (len(xy_list) - 1):
            if xy_list[i][0] > xy_list[i+1][0]:
                xy_list[i], xy_list[i+1] = xy_list[i+1], xy_list[i]
                change_count += 1
            elif (xy_list[i][0] == xy_list[i+1][0]) & (xy_list[i][1] > xy_list[i+1][1]):
                xy_list[i], xy_list[i+1] = xy_list[i+1], xy_list[i]    
                change_count += 1
            i += 1
    
    for xy in xy_list:
        print(xy[0], xy[1])

N = int(sys.stdin.readline())
xy_list = list()
for _ in range(N):
    xy = list(map(int, sys.stdin.readline().split()))
    xy_list.append(xy)
xySort(xy_list)