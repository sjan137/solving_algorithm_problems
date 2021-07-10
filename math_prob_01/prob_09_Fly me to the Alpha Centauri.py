import sys

T = int(sys.stdin.readline())
for t in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    number = 0
    start = [0]
    while distance != number:
        if str(3) in start:
            index_3 = start.index('3')
            start[index_3] = '2'
            try:
                start[index_3 + 1] = str(int(start[index_3 + 1]) + 1)
            except:
                start.append('1')
        else:
            start[0] = str(int(start[0]) + 1)
        number += 1
    start_num = [int(a) for a in start]
    print(sum(start_num))