import math

def radianos(graus, mins, segs):
    # Converter graus, minutos e segundos para graus decimais
    angulo = graus + (mins/60) + (segs/3600)
    # Converter para radianos
    rad = angulo * (math.pi / 180)
    return rad