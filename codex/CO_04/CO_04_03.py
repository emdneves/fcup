#Defina uma função forte(palavra) que verifica se uma palavra-passe (dada como cadeia de carateres) tem 8 carateres ou mais de comprimento e pelo menos uma letra maiúscula, uma letra minúscula e um algarismo.
# O resultado deve ser um valor lógico (True ou False).

def forte(palavra):
    mai = False
    min = False
    alg = False

    if len(palavra) < 8:
        return False

    for char in palavra:
        if 65 <= ord(char) <= 90:
            mai = True
        elif 97 <= ord(char) <= 122:
            min = True
        elif char.isdigit():
            alg = True

    return mai and min and alg