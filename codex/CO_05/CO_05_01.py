def pascal(n):
    linha_atual = [1]
    print (' ' * (n + 1)  , linha_atual)
    for i in range(0, n):
        linha_atual = [1] + [linha_atual[j] + linha_atual[j+1]                  
            for j in range(len(linha_atual)-1)] + [1]
        print (' ' * (n - i), linha_atual)
pascal(4)

