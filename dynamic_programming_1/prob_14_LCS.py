import sys


def getLCS(str1, str2):
    # str1을 기준으로 할 때
    len_1 = len(str1)
    len_2 = len(str2)
    for i in range(len_1):
        list_1 = []
        list_2 = []
        for j in range(len_2):
            if str1[i] == str2[j]:
                if not list_1:
                    list_1.append(i)
                    list_2.append(j)
                elif j > list_2[-1]:
                    list_1.append(i)
                    list_2.append(j)
        print(list_1, list_2)
    return

string_1 = sys.stdin.readline().strip()
string_2 = sys.stdin.readline().strip()
print(string_1, string_2)
print(getLCS(string_1, string_2))