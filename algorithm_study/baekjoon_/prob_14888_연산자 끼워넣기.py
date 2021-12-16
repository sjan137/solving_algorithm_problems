import sys


def getResultList(nums, oprs):
    res = []
    if sum(oprs) == 0: return [nums[0]]

    for i in range(4):
        if not oprs[i]: continue
        oprs[i] -= 1
        a = nums.pop()
        b = nums.pop()
        res += getResultList(nums+[calWithOpr(a, b, i)], oprs)
        oprs[i] += 1
        nums.append(b)
        nums.append(a)
    
    return res


def calWithOpr(first, second, opr_num):
    if opr_num == 0: return first + second
    elif opr_num == 1: return first - second
    elif opr_num == 2: return first * second
    elif opr_num == 3:
        if first < 0 and second > 0: return -((-first) // second)
        else: return first // second


N = int(sys.stdin.readline())
nums_list = list(map(int, sys.stdin.readline().split()))
operators_cnt = list(map(int, sys.stdin.readline().split()))
nums_list.reverse()
result_list = getResultList(nums_list, operators_cnt)
print(max(result_list))
print(min(result_list))