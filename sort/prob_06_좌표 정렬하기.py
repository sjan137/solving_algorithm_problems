import sys

def xySort(x_list, y_list):
    result = list()
    for ref in range(-100000, 100001):
        temp_y = list()
        while ref in x_list:
            index_num = x_list.index(ref)
            x_list.remove(ref)
            temp_y.append(y_list.pop(index_num))
        temp_y.sort()
        if temp_y:
            for y in temp_y:
                result.append([ref, y])

    for xy in result:
        print(xy[0], xy[1])

N = int(sys.stdin.readline())
x_list = list()
y_list = list()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)
xySort(x_list, y_list)