import unittest
from math import isclose
from fonctions.angleToFunction import angleToFunction


class AngleToFx_Test(unittest.TestCase):
    def test_angleZero(self):
        # a tend vers l'infini et b = 0
        a, b = angleToFunction(0, (0, 0))
        self.assertGreater(a, 10e10)
        self.assertEqual(b, 0)

    def test_angle180(self):
        # a tend vers -∞ et b = 0
        a, b = angleToFunction(180, (0, 0))
        self.assertLess(a, -10e10)
        self.assertEqual(b, 0)

    def test_pointEgaux45(self):
        # a doit etre 1 et b = 0 dans tous les cas
        for i in range(0, 10):
            a, b = angleToFunction(45, (i, i))
            self.assertTrue(isclose(1.0, a, rel_tol=1e-8))
            self.assertTrue(isclose(0.0, b, abs_tol=1e-8))

    def test_12Angle45(self):
        # a doit etre 1 et b=-1
        a, b = angleToFunction(45, (2, 1))
        self.assertTrue(isclose(1.0, a, rel_tol=1e-8))
        self.assertTrue(isclose(-1.0, b, abs_tol=1e-8))



if __name__ == '__main__':
    unittest.main()
