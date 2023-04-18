## 4.1 Escreva uma definição da função conta_letras(txt) que retorna o número
# de letras (maiúsculas ou minúsculas) sem acentos da cadeia de caracteres txt.
# Exemplo:
# >>> conta_letras(’Ola, mundo!’)
# >>>8 

txt = "banana"

def conta_letras(txt):
    for i in range(len(txt)):
        i = i + 1
    return i

d = conta_letras(txt)
print(" o número de letras em", txt, " é " , d)