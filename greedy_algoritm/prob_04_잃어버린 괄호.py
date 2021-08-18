import sys


def main():
    # 한 번 마이너스가 나온 뒤에는 괄호를 통해 다 마이너스 연산이 되도록 할 수 있음.
    line = sys.stdin.readline()
    flag = False
    plus_count = 0
    for digit in line:
        if not flag:
            if digit == '+': plus_count += 1
            elif digit == '-': flag = True
    
    new_line = list(map(int, line.replace('+', ' ').replace('-', ' ').split()))
    result = 0
    plus_count += 1
    for num in new_line:
        if plus_count:
            result += num
            plus_count -= 1
        else: result -= num
    
    print(result)
    return None

if __name__ == "__main__":
    main()