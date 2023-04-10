# 4.5 Uma cadeia de carateres é um palíndromo se as sequências obtidas lida da
# esquerda para a direita e vice-versa são iguais, independentemente das letras
# serem maiúsculas ou minúsculas. Exemplo: "reviveR" é um palíndromo.
# Escreva uma definição da função palindromo(txt) que verifica se uma cadeia
# de caracteres é um palindromo; o resultado deve ser True ou False.


def palindromo(txt):
    txt = txt.lower()
    return txt == inversa(txt.lower())

# Exemplo de uso da função
txt = "reviveR"
print(palindromo(txt)) # True