# Um número n diz-se triangular se n = 1 + 2 + ⋯ + k para algum natural k . 
# Os primeiros cinco números triangulares são 1 , 3 , 6 , 10 e 15 . 
# Escreva uma função triangular(n) que retorna True ou False conforme n é triangular ou não.

def triangular(n):
    soma = 0
    aux = 1
    while soma < n:
        soma = soma + aux
        aux = aux + 1
    return soma == n
