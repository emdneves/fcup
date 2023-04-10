import math

hor = int(input("insert hours: "))
min = int(input("insert minutes: "))
sec = int(input("insert seconds: "))


def segundos(hor, min, sec):
    conv = ((hor * 3600) + (min * 60) + sec)
    return(conv)

total = segundos(hor, min, sec)
print(total,"segundos")    