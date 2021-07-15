import sys

def getMaxUnderM(m, num_list):
    sum_list = list()
    for num1 in num_list:
        for num2 in num_list:
            if num1 == num2: continue
            else:
                for num3 in num_list:
                    if (num1 == num3) or (num2 == num3): continue
                    else: sum_list.append(num1 + num2 + num3)
    sum_list.sort()
    print(sum_list)
    while sum_list[-1] > m: sum_list.pop()
    print(sum_list.pop())

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
getMaxUnderM(M, num_list)