
# xs = (1, 2, 3)
# ys = (1, 2, 3)



def listas_iguais(xs, ys):
  for i in range(len(xs)):
    if xs[i] != ys[i]:
      return i
  return -1

# print(listas_iguais(xs, ys))