import sys


def getLCS(str1, str2):
    # 다른 풀이를 참고한 풀이. 이중 반복문과 누적 개수 이용
    x = len(str1)
    y = len(str2)
    dp = [0] * 1000

    for i in range(x):
        temp = 0
        for j in range(y):
            if temp < dp[j]: temp = dp[j]
            elif str1[i] == str2[j]: dp[j] = temp + 1
    
    return max(dp)

string_1 = sys.stdin.readline().strip()
string_2 = sys.stdin.readline().strip()
print(getLCS(string_1, string_2))