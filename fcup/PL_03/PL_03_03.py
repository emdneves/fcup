# 3.3 Escreva uma função media_arit(xs) que, dada uma lista de n valores numéricos xs, retorna a média aritmética dos seus valores, isto é:

xs = [3, 6, 9]


def media_artit(xs):
    count = 0
    aux = 0
    for n in range(len(xs)):
        aux = aux + xs[n]
        count = count +1
                
    return (aux / count)

total = media_artit(xs)
print("media =", total)




