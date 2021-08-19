import sys


def main():
    n = int(sys.stdin.readline())
    road_list = list(map(int, sys.stdin.readline().split()))
    city_price_list = list(map(int, sys.stdin.readline().split()))
    
    price = 10 ** 9
    greedy_sum = 0
    for i in range(n-1):
        price = city_price_list[i] if city_price_list[i] < price else price
        greedy_sum += price * road_list[i]
    
    print(greedy_sum)
    return None

if __name__ == '__main__':
    main()