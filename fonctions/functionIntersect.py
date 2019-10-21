def functionIntersect(a, b, c, d):
    """
          Renvoie le point d'intersection de deux fonctions
          f1(x)=ax+b et f2(x)=cx+d

          @type  a: float
          @param a: coef directeur de la droite f1(x)
          @type  b: float
          @param b: coef de la droite f1(x)
          @type c: float
          @param c: coef directeur de la droite f2(x)
          @type d: float
          @param d: coef de la droite f2(x)
          @rtype: tuple
          @return: coord du point d'intersection (x,y)

          @author: Maxime Favier
          @version: 0.3
          """
    # test droites paralleles
    if a == c:
        raise Exception("droites paralleles")

    # calcul de l'intersection x
    x = (-b + d) / (a - c)
    y = a * x + b
    return x, y


print(functionIntersect(1, 1, 2, 0))
