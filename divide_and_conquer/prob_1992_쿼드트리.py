import sys

# 배열과 시작 좌표(x, y), 총 길이 n를 입력으로 받음.
# 각각의 숫자를 문자열로 변환하고 괄호를 씌운 상태로 반환
def zipArray(arr, x, y, n):
    zipped_str = ""
    if n == 1: return f"{arr[y][x]}"
    
    pivot = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if pivot != arr[i][j]:
                for xx, yy in [[x, y], [x+n//2, y], [x, y+n//2], [x+n//2, y+n//2]]:
                    zipped_str += zipArray(arr, xx, yy, n//2)
                return f"({zipped_str})"
    return str(pivot)

def main():
    N = int(sys.stdin.readline())
    array = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    return zipArray(array, 0, 0, N)

if __name__ == "__main__":
    print(main())