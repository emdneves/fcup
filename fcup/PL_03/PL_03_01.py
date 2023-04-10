# 3.1 Considere um programa que começa com a atribuição de uma lista de valores de temperatura em graus Celsius à variável tempC: tempC = [-5,0,5,10,15,20,25]

# (a) Escreva um ciclo for que imprime cada um dos valores de temperatura da lista tempC numa linha separada.

tempC = [-5,0,5,10,15,20,25]
for x in  tempC:
    print(x) 

# (b) Escreva um outro ciclo for que imprima os mesmos valores da lista tempC, mas gerados à custa da função range.
tempC = [-5,0,5,10,15,20,25]
for i in range(len(tempC)):
    print(tempC) 

# (c) Escreva um ciclo while que produza o mesmo resultado da alínea anterior.

tempC = [-5,0,5,10,15,20,25]
i = 0
while i < len(tempC):
    valores_lista = tempC[i]
    print(valores_lista)
    i = i + 1

# (d) Escreva um ciclo em que para os valores de temperatura acima, em cada linha, imprime o valor em graus Celsius e o valor correspondente em graus Fahrenheit. 
# function to convert from farenheit to celsius
def convert(t):
    temp = (5/9) * (t - 32)
    return temp

tempC = [-5,0,5,10,15,20,25]

for i in range(len(tempC)):
    valores_lista = tempC[i]
    farenheit = convert(valores_lista)
    print(farenheit)

# Nota: Pode (e deve) utilizar a função celsius(F) implementada no exercício 1.14.