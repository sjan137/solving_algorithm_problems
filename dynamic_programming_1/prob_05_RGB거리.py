import sys

def streetRGB(n, rgb_arr, start, acc_sum):
    global rgb_price
    if acc_sum >= rgb_price: return

    if start == n:
        rgb_price = acc_sum
        print(rgb_price, result)
        return

    for i in range(3):
        if check[i]:
            check[i] = False
            continue
        check[i] = True
        result.append(i)
        streetRGB(n, rgb_arr, start+1, acc_sum+rgb_arr[start][i])
        result.pop()
        check[i] = False
    return

N = int(sys.stdin.readline())
rgb_price = 1000 * 1000
check = [False] * 3
result = []
rgb_array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
streetRGB(N, rgb_array, 0, 0)
print(rgb_price)