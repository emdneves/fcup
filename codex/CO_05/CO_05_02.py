import math

def desvio_padrao(xs):
    n = len(xs)
    media = sum(xs) / n
    soma_quadrados = sum((x - media) ** 2 for x in xs)
    desvio_padrao = math.sqrt(soma_quadrados / (n - 1))
    return desvio_padrao
