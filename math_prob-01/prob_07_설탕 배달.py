N = int(input())
a_5, b_5 = divmod(N, 5)
if b_5 == 0:
    print(a_5)
else:
    if (b_5 % 3) == 0:
        print(a_5 + (b_5 // 3))
    elif N % 3 == 0:
        print(N // 3)
    else:
        a_8, b_8 = divmod(N, 8)
        if b_8 == 0: print(a_8 * 2)
        elif (b_8 == 3) or (b_8 == 5): print(a_8 * 2 + 1)
        elif b_8 == 6: print((a_8 + 1) * 2)
        else: print(-1)