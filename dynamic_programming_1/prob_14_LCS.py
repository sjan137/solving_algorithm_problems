import sys


def getLCS(str1, str2):
    # 두 단어의 길이를 각각 x축, y축으로 하며, 누적하여 공통 부분 숫자를 더하는 배열 생성
    x = len(str1)
    y = len(str2)
    acc_arr = [[0] * x for _ in range(y)]

    if str1[0] == str2[0]: acc_arr[0][0] = 1  # [0][0] 값 설정

    for i in range(y):
        for j in range(x):
            if j == 0:  # 1열은 위의 값을 가져옴. 만약 문자가 같다면, 1을 넘지 않는 선에서 +1
                if i == 0: continue  # 1열 1행 값은 이미 정했으므로 패스
                acc_arr[i][j] = acc_arr[i-1][j]
                if str1[j] == str2[i] and acc_arr[i][j] < i+1 and acc_arr[i][j] < j+1:
                    acc_arr[i][j] += 1
            else:  # 1열 외의 다른 열은 바로 직전 행의 값과 직전 열의 값 중 큰 값을 가져옴.
                if i == 0: acc_arr[i][j] = acc_arr[i][j-1]  # 단, 직전 행이 없으므로 1행은 직전 열의 값을 가져옴.
                else: acc_arr[i][j] = max(acc_arr[i-1][j], acc_arr[i][j-1])
                if str1[j] == str2[i] and acc_arr[i][j] < i+1 and acc_arr[i][j] < j+1:
                    acc_arr[i][j] = acc_arr[i-1][j-1] + 1
    return acc_arr

string_1 = sys.stdin.readline().strip()
string_2 = sys.stdin.readline().strip()
print(getLCS(string_1, string_2))