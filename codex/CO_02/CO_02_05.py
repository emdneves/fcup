def classifica(p: int):
    if ((p < 0) or (p > 100)):
        return "inválido"
    elif (p < 50):
        return "insuficiente"
    elif ((p >= 50) and (p < 70)):
        return "suficiente"
    elif ((p >= 70) and (p < 80)):
        return "bom"
    elif ((p >= 80) and (p < 90)):
        return "muito bom"
    else:
        return "excelente"