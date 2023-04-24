


def algarismos(n):
    contador = 0
    while (n != 0):
        n = n // 10
        contador = contador + 1
    return contador

print(algarismos(123456))