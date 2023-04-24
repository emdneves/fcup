


def apenas_letras(txt):
    for i in (txt):
        if (txt[i] > 'A' or txt[i] < 'Z'): # maiusculas
            print('maiuscula' + txt[i])
        elif (txt[i] > 'a' or txt[i] < 'z'): # minusculas
            print('minuscula' + txt[i])    
        else:
            print(false)

apenas_letras('abcABC')
# A = 65, Z = 98
# a = 97, z = 122