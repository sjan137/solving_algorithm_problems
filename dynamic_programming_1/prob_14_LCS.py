import sys


def getLCS(str1, str2):
    max_length = 0
    print(str1, str2)

    for i in range(len(str1)):
        for j in range(len(str2)):
            # print(i, j)
            a, b = i, j
            if str1[a] == str2[b]:
                print(str1[a], str2[b])
                temp = 0
                while str1[a] == str2[b]:
                    temp += 1
                    a += 1
                    b += 1
                    # print(a, len(str1))
                    if a >= len(str1) or b >= len(str2): break
                if temp > max_length: max_length = temp
                print(temp)
    return max_length

string_1 = sys.stdin.readline().split()
string_2 = sys.stdin.readline().split()
print(getLCS(string_1[0], string_2[0]))