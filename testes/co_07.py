

def triangular(n):
    soma = 0
    aux = 1
    while soma < n:
        soma = soma + aux
        aux = aux + 1
    return soma == n
