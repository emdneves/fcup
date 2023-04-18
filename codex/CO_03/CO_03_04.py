# O método de Newton pode ser usado para aproximar o valor da raiz quadrada de um número positivo q . 
# Para primeira aproximação tomamos x 0 = q / 2 ; para as aproximações seguintes usamos a recorrência: x n + 1 = 1 2 ( x n + q x n ) 
#Defina uma função raiz(q, epsilon) que aproxima a raiz de q fazendo iterações até que a diferença em valor absoluto entre aproximações sucessivas seja inferior a ϵ , 
# isto é, terminando na primeira iteração n tal que | x n − x n − 1 | < ϵ . Submissões: always

def raiz(q, epsilon):
    x = q/2  # valor inicial
    diff = float('inf')

    while diff >= epsilon:
        xn = (x + q/x) / 2
        diff = abs(xn - x)
        x = xn  

    return x