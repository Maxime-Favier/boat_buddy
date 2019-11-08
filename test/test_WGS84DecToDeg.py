#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fonctions.WGS84DecToDeg import WGS84DecToDeg


class WGS84_Test(unittest.TestCase):
    """
    Tests automatiques pour la fonction WGS84DecToDeg qui convertit les degrés WGS84 decimal en sexadécimal
    """

    def test_1(self):
        """38.8897 = 38 53' 23'' """
        D, M, S = WGS84DecToDeg(38.8897)
        self.assertEqual((D, M, round(S)), (38, 53, 23))

    def test_2(self):
        """-77.0089 = -77 00' 32'' """
        D, M, S = WGS84DecToDeg(-77.0089)
        self.assertEqual((D, M, round(S)), (-77, 00, 32))

    def test_3(self):
        """47.494128 = 47 29' 39''"""
        D, M, S = WGS84DecToDeg(47.494128)
        self.assertEqual((D, M, round(S)), (47, 29, 39))

    def test_4(self):
        """3.043041 = 3 2' 35''"""
        D, M, S = WGS84DecToDeg(3.043041)
        self.assertEqual((D, M, round(S)), (3, 2, 35))


if __name__ == '__main__':
    unittest.main()
