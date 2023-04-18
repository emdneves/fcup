import math

x1 = int(input("x ponto 1: "))
x2 = int(input("y ponto 1: "))
y1 = int(input("x ponto 2: "))
y2 = int(input("y ponto 2: "))

def dist(x1, y1, x2, y2):
    d = math.sqrt ((x2- x1)**2 + (y2 - y1)**2)
    return(d)

total = dist(x1, y1, x2, y2)
print(total)    