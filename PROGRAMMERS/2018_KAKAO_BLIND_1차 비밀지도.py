def toBinary(num, n):
    result = [0] * n
    idx = n-1
    while num:
        num, m = divmod(num, 2)
        result[idx] = m
        idx -= 1
    return ''.join(map(str, result))

def solution(n, arr1, arr2):
    answer = []
    N = len(arr1)
    binaryArr1 = [toBinary(num, N) for num in arr1]
    binaryArr2 = [toBinary(num, N) for num in arr2]
    for i in range(n):
        temp_map = ''
        for j in range(n):
            if int(binaryArr1[i][j]) + int(binaryArr2[i][j]): temp_map += '#'
            else: temp_map += ' '
        answer.append(temp_map)
    return answer