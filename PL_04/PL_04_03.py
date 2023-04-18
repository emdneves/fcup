# 4.3 Escreva uma definição da função filtra_letras(txt) que, dada uma cadeia
# de caracteres txt, retorna uma cadeia de caracteres com apenas as letras
# maiúsculas ou minúsculas da cadeia txt.
# Exemplo:
# >>> filtra_letras(’Ola!, -- disse ele...’)
# ’Oladisseele’


def filtra_letras(txt):
    filtrado = ""
    for char in txt:
        if char.isalpha():
            filtrado += char
    return filtrado

# Exemplo de uso da função
txt = "Ola!, -- disse ele..."
filtrado = filtra_letras(txt)
print(filtrado) # Oladisseele