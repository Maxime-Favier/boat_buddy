#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fonctions.functionIntersect import functionIntersect


class Intersection(unittest.TestCase):
    """tests automatiques de la fonction d'intersection qui calcule le point d'intersection avec de deux fonctions affines"""

    def test_droitesParalleles(self):
        """teste que la fonction retourne une erreur lorsque les deux droites sont parralles"""
        # Exeptions droites parallèles
        with self.assertRaises(Exception):
            functionIntersect(1, 0, 1, 5)

    def test_intersection00(self):
        """teste que la fonction retourne (0,0) comme point d'intersection pour les fonctions y=x et y=-4x """
        # intersection en 0, 0 quand b et c =0
        pt = functionIntersect(1, 0, -4, 0)
        self.assertTupleEqual(pt, (0, 0))

    def test_intersection12(self):
        """teste que la fonction retourne (1,2) comme point d'intersection pour les fonctions y=-2x+4 et y=3x-1 """
        # intersection en 1, 2
        pt = functionIntersect(-2, 4, 3, -1)
        self.assertTupleEqual(pt, (1, 2))

    def test_intersection52(self):
        """teste que la fonction retourne (5,-2) comme point d'intersection pour les fonctions y=-5/7x+11/7 et y=3/5x-5 """
        pt = functionIntersect(-5 / 7, 11 / 7, 3 / 5, -5)
        self.assertTupleEqual(pt, (5, -2))


if __name__ == '__main__':
    unittest.main()
