import sys


def getLCS(str1, str2):
    # 두 단어의 길이를 각각 x축, y축으로 하며, 누적하여 공통 부분 숫자를 더하는 배열 생성
    x = len(str1)
    y = len(str2)
    acc_arr = [[0] * x for _ in range(y)]

    if str1[0] == str2[0]: acc_arr[0][0] = 1  # [0][0] 값 설정

    for i in range(y):
        flag = False
        for j in range(x):
            if j == 0:  # 1열일 때는 위의 값을 가져옴. 같다면 +1. 단, 이미 1이면 그냥 패스
                if i == 0:
                    if acc_arr[0][0]: flag = True
                    continue  # 이미 [0][0] 값은 구해서 할당함.
                acc_arr[i][j] = acc_arr[i-1][j]
                if acc_arr[i][j]: continue  # 1열의 값은 이미 1이라면 같은 문자여도 통과
                elif str1[j] == str2[i] and not flag:
                    flag = True
                    acc_arr[i][j] += 1
            else:  # 아닐 때는 위쪽과 왼쪽 중 큰 값을 가져옴. 같다면 +1 하면서 
                acc_arr[i][j] = max(acc_arr[i][j-1], acc_arr[i-1][j])
                if str1[j] == str2[i] and not flag:
                    flag = True
                    acc_arr[i][j] += 1
    return acc_arr

string_1 = sys.stdin.readline().strip()
string_2 = sys.stdin.readline().strip()
print(getLCS(string_1, string_2))