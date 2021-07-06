import sys

words = sys.stdin.readline().strip()
temp_words = words
croa_alphas = ['c=', 'c-', 'dz=', 'd-', 'lj', 's=', 'z=', 'nj']
for croa_alpha in croa_alphas:
    temp_words = temp_words.replace(croa_alpha, 'a')
print(len(temp_words))