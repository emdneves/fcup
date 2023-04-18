# 3.7 Escreva uma definição da função fatorial(n) que, dado um inteiro positivo n, calcula e retorna o seu fatorial. Relembre que n! = n * (n-1) * _ * 1.



n = int(input("insert value: "))

def fatorial(n, x):
    x = n
    while n > 0:
        x = x * (n-1) 
        n -= 1 
    return(x)

fator = fatorial(n, x)
print (fator)


