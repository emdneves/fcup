
import math



def dist(x1, y1, x2, y2):
    d =math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return d

print(dist(1, 2, 3, 4))