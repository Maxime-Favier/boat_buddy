from math import *


def angleToFunction(angle, point):
    """
       Renvoie l'équation d'une droite à partir d'un point et d'un angle

       @type  angle: float
       @param angle: angle par rapport au nord. (0° - 360°)
       @type  point: tuple
       @param point: point de la droite
       @rtype: tuple
       @return: a et b de l'équation f(x)=ax+b

       @author: Maxime Favier
       @since: 0.2
       @version: 0.3
       """
    a = -tan(radians(90 - angle))
    #print("a", a)
    b = point[1] - (a * point[0])
    return a, b

print(angleToFunction(0, (0, 0)))