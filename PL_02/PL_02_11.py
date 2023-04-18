

from turtle import *

numero = int(input("insert number of figures "))
size = int(input("insert size of figures "))


def friso(size, numero):
    for x in range(numero):
        forward(size)
        left(90)
        forward(size)
        right(90)
        forward(size)
        right(90)
        forward(size)
        left(90)
friso(size, numero)
done()