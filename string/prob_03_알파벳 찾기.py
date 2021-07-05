import sys

S = sys.stdin.readline().split()[0]
alphabet_index = str()
for ascii_num in range(97, 123):
    alphabet = chr(ascii_num)
    if alphabet in S: alphabet_index += ' ' + str(S.index(alphabet))
    else: alphabet_index += ' -1'
print(alphabet_index.strip())