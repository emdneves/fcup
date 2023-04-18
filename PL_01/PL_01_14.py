import math


def convert(t):
    temp = (5/9) * (t - 32)
    return(temp)

t = float(input("insert temp "))

temp = convert(t)
print(temp)



