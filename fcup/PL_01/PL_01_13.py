import math


def circle_area(r):
    area = math.pi * (r **2)
    return(area)

r = float(input("qual o raio do circulo? "))

area_ = circle_area(r)
print(area_)



