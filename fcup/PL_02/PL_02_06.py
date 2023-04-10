import math

## a
xs =[5, 0, 42, 10, 24, 30, 81]

for x in xs:
    print(x)

## b

for x in xs:
    print( x, " | ", x**2, " | ", math.sqrt(x))

## c

# print sum of xs
# print sum of xs untill position of the list


xs = [5, 0, 42, 10, 24, 30, 81]
soma = 0

for x in range(len(xs)):
    soma = soma + xs[x]
    print(x+1, ":", soma, xs[x])

    xs = [5, 0, 42, 10, 24, 30, 81]
total = 0





