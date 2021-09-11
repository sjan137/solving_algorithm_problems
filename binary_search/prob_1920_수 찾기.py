import sys

def binarySearch(nums_list, num):
    n = len(nums_list)
    if n == 1: return "Yes" if nums_list[0] == num else "No"
    mid = n // 2
    return binarySearch(nums_list[:mid], num) if nums_list[mid] > num else binarySearch(nums_list[mid:], num)

def main():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    toCheck = list(map(int, sys.stdin.readline().split()))
    result = []
    nums.sort()

    for num in toCheck:
        result.append(binarySearch(nums, num))
    
    return result

if __name__ == "__main__":
    print(*main())