import sys

def streetRGB(n, rgb_arr, start, acc_sum):
    global rgb_price
    if acc_sum >= rgb_price: return

    if start == n:
        rgb_price = acc_sum
        return

    for i in range(3):
        if not result:
            result.append(i)
            streetRGB(n, rgb_arr, start+1, acc_sum+rgb_arr[start][i])
            result.pop()
        else:
            if result[-1] == i: continue
            result.append(i)
            streetRGB(n, rgb_arr, start+1, acc_sum+rgb_arr[start][i])
            result.pop()
    return

N = int(sys.stdin.readline())
rgb_array = []
rgb_price = 1000 * 1000
result = []
for _ in range(N):
    rgb_array.append(list(map(int, sys.stdin.readline().split())))
streetRGB(N, rgb_array, 0, 0)
print(rgb_price)