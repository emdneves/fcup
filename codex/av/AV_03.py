
# lista = (1, 2, 3)
# n = 0

def soma_parcial(lista, n):
    i = 0
    soma = 0
    while (i <= n):
        soma += lista[i]
        i = i + 1
    return soma
# print(soma_parcial(lista, n))