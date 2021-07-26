# 백준에서 python3 대신 pypy3로 제출하니까 시간 초과가 뜨지 않고 성공.
import sys

def nQueen(start, n):
    # 함수 외부에서 지정한 변수 count에 계산을 실행하기 위해 전역 변수로 선언
    global count
    if start == n:
        count += 1
        return
    for i in range(n):
        if ch1[i] or ch2[n-i+start-1] or ch3[i+start]: continue
        ch1[i] = ch2[n-i+start-1] = ch3[i+start] = True
        nQueen(start+1, n)
        ch1[i] = ch2[n-i+start-1] = ch3[i+start] = False

N, count = int(sys.stdin.readline()), 0
# 세로, 대각선(\,/)에 따라 가능 유무 판단
ch1, ch2, ch3 = [False] * N, [False] * (2*N-1), [False] * (2*N-1)
nQueen(0, N)
print(count)