#Podemos contar algarismos decimais na representação de um número fazendo divisões inteiras por dez. 
#Por exemplo: 9733 tem 4 algarismos porque podemos fazer quatro divisões inteiras sucessivas por 10 até obter quociente zero.
#Defina uma função algarismos(n) que retorna o número de algarismos decimais de um inteiro positivo n. Sugestão: utilize um ciclo while.

def algarismos(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count