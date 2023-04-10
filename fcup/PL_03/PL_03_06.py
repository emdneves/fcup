# 3.6 Teste a função do exercício anterior (3.5) fazendo um programa que escreve uma tabela dos anos bissextos entre 2000 e 2020. Verifique os resultados usando o calendário do computador.


# 3.7 Escreva uma definição da função fatorial(n) que, dado um inteiro positivo n, calcula e retorna o seu fatorial. Relembre que n! = n * (n-1) * _ * 1.

def bissexto(n):
    if n % 4 == 0 or n % 100 == 0:
        n = 0
        return True
    else: 
        n = False
        return n

for n in range(2000, 2021, 1):
    anos = bissexto(n)
    if anos == True:
        print(n,"bissexto")
    else:
        print(n,"não é bissexto")
