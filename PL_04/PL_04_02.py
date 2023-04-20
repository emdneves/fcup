# 4.2 Escreva uma definição da função apenas_letras(txt) que testa se uma
# cadeia de caracteres contém apenas letras maiúsculas ou minúsculas (sem acentos).
# O resultado deve ser True ou False.
# Exemplos:
# >>> apenas_letras("Abracadabra")
# True
# >>> apenas_letras("Ola, mundo!")
# False


txt = "BAnANA"

def apenas_letras(txt):
    for i in range(len(txt)):
        if txt[i] >= 'A' and txt[i] <= 'Z':
            i = i +1
            if i == len(txt):
                return True   
    
print(len(txt))
d = apenas_letras(txt)
print(d)


def apenas_letras(txt):
    for i in range(len(txt)):
        if not(txt[i].isalpha() and (txt[i].islower() or txt[i].isupper())):
            return False
    return True

# Exemplo de uso da função
txt = "Abracadabra"
print(apenas_letras(txt)) # True

txt = "Ola, mundo!"
print(apenas_letras(txt)) # False