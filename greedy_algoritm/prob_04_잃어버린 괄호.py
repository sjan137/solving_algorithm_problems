import sys


def main():
    # 한 번 마이너스가 나온 뒤에는 괄호를 통해 다 마이너스 연산이 되도록 할 수 있음.
    line_to_cal = sys.stdin.readline().split('-')
    result = sum(map(int, line_to_cal[0].split('+')))

    for line in line_to_cal[1:]:
        result -= sum(map(int, line.split('+')))
    
    print(result)
    return None

if __name__ == "__main__":
    main()