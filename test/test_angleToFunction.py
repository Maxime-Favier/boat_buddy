#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fonctions.angleToFunction import angleToFunction


class AngleToFx_Test(unittest.TestCase):
    """tests automatiques de angleToFunction qui renvoie l'equation affine d'une droite à partir de l'angle par rapport au nord et la position d'un point
    """
    def test_angle0(self):
        """teste que quand l'angle est 0, a tend vers l'infini"""
        # a tend vers l'infini et b = 0
        a, b = angleToFunction(0, (0, 0))
        self.assertGreater(a, 10e10)
        self.assertEqual(b, 0)

    def test_angle180(self):
        """teste quand l'angle est 180, a tend vers moins l'infini"""
        # a tend vers -∞ et b = 0
        a, b = angleToFunction(180, (0, 0))
        self.assertLess(a, -10e10)
        self.assertEqual(b, 0)

    def test_angle45(self):
        """teste quand l'angle est 45, a=1"""
        # a = 1 quand angle = 45
        a, b = angleToFunction(45, (0, 0))
        # a= 0.9999999999 a cause des arrondis de python
        self.assertEqual(round(a), 1.0)
        self.assertEqual(b, 0.0)

    def test_angle225(self):
        """teste quand l'angle est 255 au point (1,1), a=1 et b=2 """
        # a= 1 et b=2.0
        a, b = angleToFunction(225, (1, 1))
        self.assertEqual(round(a), 1.0)
        self.assertEqual(b, 2.0)
        # print(a, b)

    def test_angle315(self):
        """teste quand l'angle est 315 au point (1,0), a=-1 et b=-1"""
        # a=-1 et b=-1
        a, b = angleToFunction(315, (1, 0))
        self.assertEqual(round(a), -1.0)
        self.assertEqual(round(b), -1.0)


if __name__ == '__main__':
    unittest.main()
