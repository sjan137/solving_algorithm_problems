import sys

def streetRGB(n, rgb_arr, start):
    if start == n:
        price = 0
        for i in range(n):
            price += rgb_arr[i][result[i]]
        rgb_price.append(price)
        return
    
    for i in range(3):
        if not result:
            result.append(i)
            streetRGB(n, rgb_arr, start+1)
            result.pop()
        else:
            if result[-1] == i: continue
            result.append(i)
            streetRGB(n, rgb_arr, start+1)
            result.pop()
    return

N = int(sys.stdin.readline())
rgb_array = []
rgb_price = []
result = []
for _ in range(N):
    rgb_array.append(list(map(int, sys.stdin.readline().split())))
streetRGB(N, rgb_array, 0)
print(min(rgb_price))