def han_num(num):
    if num < 100:
        count = num
        return count
    else:
        count = 99
        for i_num in range(100, num+1):
            a, b = divmod(i_num, 100)
            b, c = divmod(b, 10)
            if (a - b) == (b - c): count += 1
        return count

num = int(input())
print(han_num(num))