# 3.2 Utilizando a função range, escreva um programa que imprime os valores 10, 13, 16,..., 55.

for i in range(10, 55, 3):
    print("number:", i)


# (a) Usando a instrução break, modifique-o para terminar o ciclo quando encontrarum múltiplo de 7.

for i in range(10, 55, 3):
    if i % 7 == 0:
        break
    print("number:", i)
print("end")


# (b) Usando a instrução continue, modifique-o para não imprimir valores múltiplos de 7.

for i in range(10, 55, 3):
    if i % 7 != 0:
        print("number:", i)
print("end")