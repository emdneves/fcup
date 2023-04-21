# 5.10 O triângulo de Pascal é constituido pelos valores (n k ) das combinações de n em k em que n é a linha e k é a coluna. As primeiras cinco linhas do triângulo são:
# 1 (n = 0)
# 1 1 (n = 1)
# 1 2 1 (n = 2)
# 1 3 3 1 (n = 3)
# 1 4 6 4 1 (n = 4)

# Escreva uma função pascal(n) cujo resultado é uma lista com os coeficientes
# da n-ésima linha do triângulo de Pascal.
# Por exemplo:
# >>> pascaln(4)
# [1, 4, 6, 4, 1]
# Nota: Os valores devem estar no formato inteiro.

def pascal_triangle(n):
    # Cria uma lista vazia para armazenar as linhas do triângulo de Pascal
    pascal = []
    
    # Loop para gerar cada linha do triângulo
    for i in range(n):
        # Cria uma lista vazia para armazenar os elementos da linha atual
        row = []
        
        # Loop para calcular cada elemento da linha atual
        for j in range(i + 1):
            # Se o elemento estiver na borda do triângulo (primeiro ou último),
            # seu valor é 1. Caso contrário, é a soma dos dois elementos acima
            # dele na linha anterior.
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
        
        # Adiciona a linha atual à lista do triângulo de Pascal
        pascal.append(row)
    
    # Loop para imprimir o triângulo de Pascal
    for row in pascal:
        print(' '.join(str(x) for x in row).center(n*2))
