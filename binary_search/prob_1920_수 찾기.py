import sys

def binarySearch(nums_list, num, start, end):
    if start > end: return 0
    mid = (start + end) // 2
    return 1 if nums_list[mid] == num else (binarySearch(nums_list, num, start, mid-1) if nums_list[mid] > num  else binarySearch(nums_list, num, mid+1, end))

def main():
    N = int(sys.stdin.readline())
    nums = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    toCheck = list(map(int, sys.stdin.readline().split()))
    result = []

    for num in toCheck:
        result.append(1) if num in nums else result.append(0)
    
    return result

if __name__ == "__main__":
    print('\n'.join(map(str, main())))