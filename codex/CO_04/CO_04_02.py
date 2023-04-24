# Escreva uma função palindromo(txt) para testar se uma cadeia txt é um palíndromo neste sentido mais geral. O resultado deve ser um valor lógico (True ou False).

def palindromo(txt):
    start = 0
    end = len(txt) - 1

    while start < end:
        if txt[start].lower() != txt[end].lower():
            return False
        start += 1
        end -= 1

    return True


    
