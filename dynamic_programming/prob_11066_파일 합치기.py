import sys

# 결국 마지막 비용은 costs의 모든 원소의 합이다.
# 그리고 그 이전에는 costs 중 가장 큰 값 하나를 제외한 나머지의 합이다.
# 
def calCost(n, costs):
    result = []
    costs.sort()
    for i in range(2, n+1):
        result.append(sum(costs[:i]))
    return sum(result)

def main():
    T = int(sys.stdin.readline())
    result = []
    for _ in range(T):
        N = int(sys.stdin.readline())
        cost_list = list(map(int, sys.stdin.readline().split()))
        result.append(calCost(N, cost_list))
    return result

if __name__ == "__main__":
    print(main())