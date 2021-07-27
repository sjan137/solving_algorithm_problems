import sys

def listOperator(num_list, opr4, count, n):
    if count == n-1:
        for i in range(n-1):
            if i == 0:
                result = calWithOpr(num_list[0], num_list[1], opr_list[i])
            else:
                result = calWithOpr(result, num_list[i+1], opr_list[i])
        result_list.append(result)
        return
    
    # 각 연산자가 사용될 숫자가 0이면 패스
    for i in range(4):
        if not opr_count_list[i]: continue
        # 숫자가 있다면 사용(-1)하고 연산자 사용 순서 기록 리스트에 추가
        opr_count_list[i] -= 1
        opr_list.append(opr4[i])
        listOperator(num_list, opr4, count+1, n)
        # 다시 돌아오기
        opr_count_list[i] += 1
        opr_list.pop()
    return

# 입력된 숫자, 연산자 표시 리스트에 따라 계산값 반환
def calWithOpr(a, b, opr):
    if opr[0]: return a+b
    elif opr[1]: return a-b
    elif opr[2]: return a*b
    elif opr[3]:
        if a < 0 and b > 0:
            return -(abs(a) // b)
        else: return a//b

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
opr_count_list = list(map(int, sys.stdin.readline().split()))
opr4 = [[False] * i + [True] + [False] * (3-i) for i in range(4)]
opr_list = list()
result_list = list()
listOperator(num_list, opr4, 0, N)
print(max(result_list))
print(min(result_list))