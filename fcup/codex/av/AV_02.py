def listas_iguais(xs, ys):
  for i in range(len(xs)):
    if xs[i] != ys[i]:
      return i
  return -1