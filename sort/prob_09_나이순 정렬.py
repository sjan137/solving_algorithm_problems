import sys

def ageNameSort(age_name_hash):
    age_list = list(age_name_hash.keys())
    age_list.sort()
    for i in age_list:
        while len(age_name_hash[i]) != 0:
            print(i, age_name_hash[i].pop(0))

N = int(sys.stdin.readline())
age_name_hash = {}
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    if age in age_name_hash.keys():
        age_name_hash[age].append(name)
    else: age_name_hash[age] = [name]
ageNameSort(age_name_hash)