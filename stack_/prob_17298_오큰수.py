import sys

# 1. 인덱스를 저장하는 스택 생성(초기값 [0])
# 2. 스택이 남아있고, 현재 선택한 인덱스[i] 숫자가 스택의 [-1]보다 크면,
#    [-1]의 원소가 [i]보다 크지 않을 때까지 pop하고,
#    pop한 인덱스의 result 원소는 [i]에 해당하는 숫자로 저장
# 3. 2번 과정이 다 끝난 후에는 i를 스택에 저장
# 4. 모든 숫자를 다 체크한 후에 인덱스 스택에 남은 인덱스에 해당하는 result 원소는 모두 -1로 저장
# 4번 과정은 처음에 result = [-1] * n으로 생성하면 수행할 필요 없음.
def main():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    idxStack = [0]
    result = [-1] * N

    for i in range(1, N):
        while idxStack and nums[i] > nums[idxStack[-1]]:
            idx = idxStack.pop()
            result[idx] = nums[i]
        idxStack.append(i)
    
    return result

if __name__ == "__main__":
    print(*main())