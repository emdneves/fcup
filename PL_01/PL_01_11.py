import math

a = 97 + 555
print(a) #652 type int

b = "97$+555$"
print(b) #syntax error

c = math.sqrt(2)
print(c) # 1.4142135623730951

d = "math.sqrt(-2)"
print(d) # raiz quadrada negativa

e = "2 (math.pi)"
print(e) # sem operador

f = 2 * math.pi
print(f) # 6.283185307179586

g = "srt(2 * math.pi)"
print(g) # a variável não é uma string

h = int(2 * math.pi)
print(h) # 6, e descartadas as casas decimais, uma vez que a variável é uma int

i = "97 + 555"
print(i) # não é possível somar uma string com um número inteiro

j = "97 == 97"
print(j) # não é possível igualar uma string a um número inteiro

k = "97 == int(97)"
print(k) # não é possível igualar uma string a um número inteiro

l = 102 <= 97
print(l) # false


m = 102 <= 97
print(m) # syntax error, operação entre string e int

n = 102 <= 97
print(n) # syntax error, operação entre strings

o = "valor de pi é " math.pi
print(o) # syntax error, operação entre string e float

p = "valor de pi é " + str(math.pi)
print(p)















