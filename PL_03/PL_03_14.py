# As espirais da figura ao lado foram desenhadas usando o módulo turtle apenas mudando o ângulo de rotação entre cada lado. Escreva uma função espiral(...) para desenhar espirais deste tipo.

from turtle import *

i = range(0, 100)

speed (10)
for x in i:
    color('red')
    forward(1 - x)
    color('blue')
    left(90 - 1)
done()

e = range(0, 100)

speed (10)
for y in e:
    color('red')
    forward(1 - y)
    color('blue')
    left(90 - 1)

