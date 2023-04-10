# Escreva uma definição da função conta_vogais(txt) que retorna o número de vogais (maiúsculas ou minúsculas) sem acentos da cadeia de carateres txt.


def conta_vogais(txt):
    num_vogais = 0
    for c in txt:
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            if c in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                num_vogais += 1
    return num_vogais