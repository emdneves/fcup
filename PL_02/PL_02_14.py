import math

a = float(input("insert a: "))
b = float(input("insert b: "))
c = float(input("insert c: "))

def areatri(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

area = areatri(a, b, c)
print(float(area))