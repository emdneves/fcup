# 3.4 Escreva uma função media_geom(xs) que, dada uma lista de n valores numéricos xs, retorna a média geométrica dos seus valores, isto é,

import math
xs = [2, 8, 32]


def media_geom(xs):
    count = 0
   
    aux = 1
    for n in range(len(xs)):
        aux = aux * xs[n]
        count = count +1
    return ((aux)**(1/count))
    
       

total = media_geom(xs)
print("media geometrica =", total)




