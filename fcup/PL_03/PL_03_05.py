# 3.5 Um ano é bissexto se for divisível por 4, exceto se for múltiplo de 100 e não for divisível por 400. Escreva a função bissexto(n) que resulta em True se n for um ano bissexto e False no caso contrário.


def bissexto(n):
    if n % 4 == 0 or n % 100 == 0:
        n = 0
        return True
    else: 
        n = False
        return n