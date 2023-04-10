numero = int(input("Digite limite de numeros "))

n = 1
for n in range(1, numero):
    quadrado = (n**2)
    print(str(n) + " | " + str(quadrado))