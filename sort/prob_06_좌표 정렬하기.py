import sys

def xySort(xy_hash):
    result = list()
    key_list = list(xy_hash.keys())
    key_list.sort()
    for key in key_list:
        y_value = xy_hash[key]
        if len(y_value) > 1:
            y_value.sort()
            for y in y_value:
                result.append([key, y])
        else: result.append([key, y_value[0]])

    for xy in result:
        print(xy[0], xy[1])

N = int(sys.stdin.readline())
xy_hash = {}
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x in xy_hash.keys():
        xy_hash[x].append(y)
    else: xy_hash[x] = [y]
xySort(xy_hash)