import math


def hipotenusa(a, b):
    h = a**2 + b**2
    return(h)

a = float(input("insert a "))
b = float(input("insert b "))

total = hipotenusa(a, b)
print(total)