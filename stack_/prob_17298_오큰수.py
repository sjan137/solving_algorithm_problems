import sys

# 첫 번째 숫자에 대해 [1]부터 찾다가 큰 숫자를 발견하면 스택(st) 저장
# 발견 못하면 -1 저장
# 두 번째 숫자부터
# 스택의 마지막 숫자(st[-1]) > 현재 숫자인 경우 스택의 마지막 숫자 또 저장
# 아닌 경우 다시 자신 이후부터 숫자 탐색
# 탐색 후 없으면 -1 저장
def search(num_list):
    for num in num_list[1:]:
        if num > num_list[0]: return num
    return -1

def main():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    st = []

    for i in range(N):
        if st and st[-1] > nums[i]: st.append(st[-1])
        elif i == N-1: st.append(-1)
        else: st.append(search(nums[i:]))
    
    return st

if __name__ == "__main__":
    print(" ".join(map(str, main())))