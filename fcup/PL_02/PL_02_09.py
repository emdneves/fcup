from turtle import *

n = int(input("insert sides: "))
length = int(input("insert length: "))

def poligono_reg(n, length):
    i = range(0, n)
    for x in i:
        forward(length)
        right(360 /n)

poligono_reg(n, length)
done()