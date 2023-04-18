# 3.8 Um número n diz-se um quadrado perfeito se, para algum natural k, pode ser escrito como a soma dos k primeiros números ímpares, isto é, 1 + 3 + _ + k. Os primeiros cinco quadrados perfeitos são 1; 4; 9; 16 e 25. 
# Escreva uma função quadrado_perfeito(n) cujo resultado é True, se n é um quadrado perfeito. Caso contrário, o resultado deverá ser False.


xs = [2, 8, 32]

count = 0
   
aux = 1

for n in range(len(xs)):
    aux = aux * xs[n]
    count = count +1
    print ("aux",aux)
    print("count",count)
