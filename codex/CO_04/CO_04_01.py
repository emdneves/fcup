# Escreva uma definição da função apenas_letras(txt) que testa se uma cadeia de caracteres contém apenas letras maiúsculas ou minúsculas (sem acentos). 
# O resultado deve ser True ou False.

def apenas_letras(txt):
    for c in txt:
        ascii = ord(c)
        if not (65 <= ascii <= 90 or 97 <= ascii <= 122):
            return False
    return True