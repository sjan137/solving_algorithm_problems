import sys

def drawStar(n):
    if n == 3:
        star_list = ['***', '* *', '***']
        return star_list
    else:
        star_list = drawStar(n//3) * 3
        for i in range(n):
            if i in range(n//3, 2*(n//3)):
                star_list[i] += (' ' * (n//3) + star_list[i])
            else: star_list[i] += (star_list[i] * 2)
        return star_list

N = int(sys.stdin.readline())
for row in drawStar(N):
    print(row)