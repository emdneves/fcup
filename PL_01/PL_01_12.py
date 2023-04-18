import math

x = input("quantos km foram percorridos? ")
x = float(x)
y = input("quantos litros foram gastos? ")
y = float(y)

consumo = (y * 100) / x

print(consumo, "l/100")

