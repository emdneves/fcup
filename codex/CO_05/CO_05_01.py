def pascal(n):
    linha_atual = [1]
    for i in range(n):
        linha_atual = [1] + [linha_atual[j] + linha_atual[j+1] for j in range(len(linha_atual)-1)] + [1]
    return linha_atual
