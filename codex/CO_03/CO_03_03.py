#Dois inteiros são co-primos se e só se o seu maior divisor comum for 1. 
# Por exemplo: 4 e 15 são co-primos, mas não o são 4 e 14 (porque 2 é um divisor comum). 
# Defina uma função coprimos(n) cujo resultado é a lista de inteiros entre 1 e n que são co-primos com n .

def coprimos(n):
    resultado = []
    for i in range(1, n+1):
        is_coprimo = True
        for j in range(2, min(i, n)+1):
            if i % j == 0 and n % j == 0:
                is_coprimo = False
                break
        if is_coprimo:
            resultado += [i]
    return resultado
