import sys

def drawStar(n):
    if n == 1:
        return '*', ' '
    else:
        element1, element2 = drawStar(n//3)
        for i in range(n):
            if i // (n//3) == 1:
                a = (element1 + element2 + element1)
                print(a)
            else:
                b = (element1 * 3)
                print(b)
        return a, b


drawStar(9)