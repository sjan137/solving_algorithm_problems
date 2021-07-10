import sys

T = int(sys.stdin.readline())
for t in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    digit_num = 0
    acc_num = 0
    while acc_num < distance:
        digit_num += 1
        acc_num += (2 * digit_num + 1)
    if distance == (acc_num - 2 * digit_num): print(2 * digit_num - 1)
    elif distance <= (acc_num - digit_num): print(2 * digit_num)
    else: print(2 * digit_num + 1)