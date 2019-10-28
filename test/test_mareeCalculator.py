#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fonctions.mareeCalculator import marreCalculator


class MyTestCase(unittest.TestCase):
    def test_marree1(self):
        """les exercices p17-18"""
        # BM 4h57 3.45m PM 11h03 7.05m hauteur de l'eau a 7h45 est -+5.03m
        x = marreCalculator(663, 7.05, 297, 3.45, 465)
        self.assertEqual(round(x, 1), 5.0)

    def test_marree2(self):
        """les exercices p19-20"""
        # BM 13h18 2.25m PM 19h06 5.85m hauteur de l'eau a 16h20 est +-4.18m
        x = marreCalculator(1146, 5.85, 798, 2.25, 980)
        self.assertEqual(round(x, 1), round(4.18, 1))

    def test_marree3(self):
        """les exercices p23-24"""
        # PM 18h14 5.70m BM 12h08 1.85m hauteur de l'eau a 15h est +- 3.60m
        x = marreCalculator(1094, 5.7, 728, 1.85, 900)
        self.assertEqual(round(x, 1), 3.6)

    def test_marree4(self):
        """les exercices p25-26"""
        # PM 12h04 7.3m BM 17h52 1.6m hauteur de l'eau a 16h10 est +-2.81
        x = marreCalculator(724, 7.3, 1072, 1.6, 970)
        self.assertEqual(round(x,1), 2.8)

if __name__ == '__main__':
    unittest.main()
