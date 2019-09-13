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
       @version: 0.2
       """
    # test du cas 0/360° et 180°
    if angle == 0 or angle == 360:
        pass
    # correction du repère
    angle = 90 - angle
    startPoint_X, startPoint_Y = point
    # calcul de la pente
    a = tan(radians(angle))
    print(a)
    # calcul du coef de la droite affine
    b = startPoint_Y - (a * startPoint_X)
    print(b)
    return a, b


angleToFunction(45, (1, 1))
