# 4.4 Escreva uma função inversa(txt) que retorne a cadeia de caracteres dada por ordem inversa.
# Exemplo:
# >>> inversa(’Ola Mundo!’)
# ’!odnuM alO’


def inversa(txt):
    return txt[::-1]

# Exemplo de uso da função
txt = "Ola Mundo!"
inverso = inversa(txt)
print(inverso) # !odnuM alO